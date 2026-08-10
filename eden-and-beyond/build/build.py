# -*- coding: utf-8 -*-
"""Eden & Beyond — static site generator.
Run from the eden-and-beyond/ folder:  python3 build/build.py
Header / footer / nav are defined once in _layout.py; never edit the generated
*.html at the root of eden-and-beyond/ by hand — they are overwritten."""

import datetime
import os
import re
import sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)  # eden-and-beyond/

import _layout as L

A = L.ARROW
pages = {}


def ph(label, cls="", extra=""):
    """Tonal photo placeholder (pre-photography). label shows what image goes here."""
    c = f"ph {cls}".strip()
    return f'<div class="{c}" data-label="{label}"{extra}></div>'


IMG_DIR = os.path.join(OUT, "assets", "img")


def find_img(slug):
    """Plug-and-play: if a real photo named <slug>.<ext> exists, return its path,
    else None (a placeholder is shown). Drop a file in assets/img/ and it appears."""
    for ext in (".webp", ".jpg", ".jpeg", ".png"):
        if os.path.exists(os.path.join(IMG_DIR, slug + ext)):
            return f"assets/img/{slug}{ext}"
    return None


def hero_media(slug, alt):
    """Full-bleed hero: real photo if present, else the placeholder gradient."""
    img = find_img(slug)
    if img:
        return "", f'<img src="{img}" alt="{alt}" fetchpriority="high">'
    return "hero__media--placeholder", ""


def subhero_media(slug):
    img = find_img(slug)
    if img:
        return "", f'<img src="{img}" alt="" fetchpriority="high">'
    return "subhero__media--placeholder", ""


def feat_tile(page, img_slug, title, rnd=False, meta="Limited-edition table", href=None):
    """A featured Collection tile for the home page (links to the piece page,
    or a custom href for pieces without their own page — e.g. walls)."""
    cls = "art art--round" if rnd else "art"
    src = find_img(img_slug)
    media = (f'<img src="{src}" alt="{title} — {meta} by Maija, Eden &amp; Beyond" loading="lazy">'
             if src else ph(title))
    link = href or f"{page}.html"
    return (f'<a class="{cls} reveal" href="{link}">'
            f'<div class="art__media">{media}</div>'
            f'<div class="art__cap"><span class="art__title">{title}</span>'
            f'<span class="art__meta">{meta}</span></div></a>')


def jcard(cat, title, desc):
    return f'''<article class="jcard reveal">
      <a class="jcard__img" href="journal.html"><span class="jcard__cat">{cat}</span>{ph(title)}</a>
      <div class="jcard__body">
        <span class="jcard__date">Coming soon</span>
        <h3 class="jcard__title"><a href="journal.html">{title}</a></h3>
        <p class="jcard__desc">{desc}</p>
        <a class="textlink" href="journal.html">Read Article {A}</a>
      </div>
    </article>'''


def wwd_item(title, desc):
    return f'<div class="wwd__item reveal"><h3>{title}</h3><p>{desc}</p></div>'


# ============================================================ HOME
_home_hero_cls, _home_hero_media = hero_media("hero-home", "Eden & Beyond creative studio")
home_body = f'''
{L.hero(
    eyebrow="Objects That Reveal the Invisible · Spaces That Reveal the Unexpected",
    h1_html='<span class="fbox">F<span class="fbox__stars">&#9733;&#9733;&#9733;</span> The Box</span>',
    sub=("Collectible furniture, lighting, objects and dressed walls — one-of-a-kind and limited editions.<br>"
         "Creative direction for hospitality, private living and unconventional projects."),
    actions_html=(
        f'<a class="btn btn--primary" href="collection.html">Explore the Collection</a>'
        '<a class="btn btn--light" href="studio.html">Meet the Studio</a>'),
    media_class=_home_hero_cls,
    media_html=_home_hero_media,
)}

<div class="trust"><div class="wrap trust__inner">
  <span class="trust__item"><strong>Tables</strong></span>
  <span class="trust__item"><strong>Lighting</strong></span>
  <span class="trust__item"><strong>Objects</strong></span>
  <span class="trust__item"><strong>Walls</strong></span>
  <span class="trust__item"><strong>Limited Editions</strong></span>
</div></div>

<section class="section"><div class="wrap">
  <div class="split" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow eyebrow--red">The Collection</span>
      <h2 style="margin:1rem 0 1.2rem;">Some ideas become spaces.<br>Others become objects.</h2>
      <p class="lead">Each piece is one-of-a-kind or part of a limited edition — transforming familiar forms into
      unexpected objects with character, contradiction and a life of their own.</p>
      <p style="margin-top:1rem;">Discover the collection, or commission a piece created for you.</p>
      <a class="btn btn--primary" href="collection.html" style="margin-top:1.6rem;">Explore the Collection {A}</a>
    </div>
    <div class="split__media reveal" data-delay="1">
      <a href="hubb.html">{('<img src="'+find_img('poppy-queen')+'" alt="Hubb — limited-edition table by Maija">') if find_img('poppy-queen') else ph('Hubb — table')}</a>
      <span class="tag">Hubb · Limited-edition table</span>
    </div>
  </div>
</div></section>

<section class="section section--sand" id="featured"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow eyebrow--red">Featured Pieces</span>
    <h2 style="margin-top:1rem;">Pieces that break the frame</h2>
  </div>
  <div class="artgrid">
    {feat_tile('flash', 'wondermint-camel', 'Flash')}
    {feat_tile('mona', 'mona-lisa-fez', 'Mona', rnd=True)}
    {feat_tile('divine-touch', 'creation-of-mint-tea', 'Divine Touch', rnd=True)}
    {feat_tile('babouche', 'babouche-mandala', 'Babouche')}
    {feat_tile('kenza', 'kenza', 'Kenza', meta='Lighting · mixed-media lamp')}
    {feat_tile('', 'fountain-wall', 'Fountain Wall', meta='Hand-stencilled wall', href='collection.html#walls')}
  </div>
  <div class="center reveal" style="margin-top:2.6rem;"><a class="btn btn--primary" href="collection.html">Explore the Full Collection {A}</a></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:660px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow">Two ways to work with Eden &amp; Beyond</span>
    <h2 style="margin-top:1rem;">Own a piece,<br>or commission a project.</h2>
  </div>
  <div class="duo">
    <div class="duo__card duo__card--red reveal">
      <div class="duo__body">
        <span class="eyebrow">01 — The Collection</span>
        <h3>Some pieces are meant to find you.</h3>
        <p>One-of-a-kind and limited-edition furniture, lighting, objects and dressed walls. Created to stand on their own. Made to be lived with.</p>
        <a class="btn btn--light" href="collection.html">Explore the Collection {A}</a>
      </div>
    </div>
    <div class="duo__card reveal" data-delay="1">
      <div class="duo__body">
        <span class="eyebrow">02 — The Studio</span>
        <h3>Ordinary was never the brief.</h3>
        <p>Creative direction and design for hospitality, residential and commercial projects. From a first idea to a complete world.</p>
        <a class="btn btn--light" href="{L.wa('Hi Eden &amp; Beyond, I would like to talk about a project.')}" target="_blank" rel="noopener">{L.WA_ICON} Start a Project</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section section--sand"><div class="wrap">
  <div class="center reveal" style="max-width:680px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow">The Studio · Design Services</span>
    <h2 style="margin:1.1rem 0 1.1rem;">From first idea<br>to complete world.</h2>
    <p class="lead" style="margin-inline:auto;">Hospitality, residential, bespoke pieces and creative direction —
    shaped by one vision, down to the last detail.</p>
  </div>
  <div class="disc-lite">
    <a class="disc-lite__item reveal" href="hospitality-design.html">
      <h3>Hospitality</h3>
      <p>Places people remember.</p>
      <span class="disc-lite__tags">Hotels · Restaurants · Bars · Beach Clubs · Cafés · Wellness</span>
      <span class="disc-lite__more">Explore {A}</span></a>
    <a class="disc-lite__item reveal" data-delay="1" href="residential-design.html">
      <h3>Residential</h3>
      <p>Homes with character. Never someone else's idea of beautiful.</p>
      <span class="disc-lite__tags">Private Villas · Luxury Residences · Holiday Homes</span>
      <span class="disc-lite__more">Explore {A}</span></a>
    <a class="disc-lite__item reveal" data-delay="2" href="furniture-object-design.html">
      <h3>Objects &amp; Furniture</h3>
      <p>Bespoke pieces created for a particular place and purpose.</p>
      <span class="disc-lite__tags">Furniture · Lighting · Objects · Art Curation</span>
      <span class="disc-lite__more">Explore {A}</span></a>
    <a class="disc-lite__item reveal" data-delay="3" href="creative-direction.html">
      <h3>Creative Direction</h3>
      <p>The idea behind everything.</p>
      <span class="disc-lite__tags">Concept · Storytelling · Brand Identity · Art Direction · Styling</span>
      <span class="disc-lite__more">Explore {A}</span></a>
  </div>
</div></section>

<section class="feat">{ph('Dar Mansour — Koh Phangan (featured project)', 'ph--dark')}
  <div class="wrap feat__inner reveal">
    <span class="eyebrow">Selected Project</span>
    <h2>Dar Mansour</h2>
    <p class="feat__place">Morocco's Kitchen · Koh Phangan, Thailand</p>
    <p>A contemporary interpretation of Moroccan hospitality, where architecture, craftsmanship,
    objects and storytelling come together to create an immersive dining experience.</p>
    <div style="margin-top:1.8rem;"><a class="btn btn--light" href="projects.html">Discover the Project {A}</a></div>
  </div>
</section>

<section class="section"><div class="wrap manifesto reveal">
  <span class="eyebrow" style="display:block;text-align:center;margin-bottom:1.4rem;">Our Philosophy</span>
  <p>Every object has a <span class="em">soul</span>.</p>
  <p class="lead" style="max-width:56ch;margin:1.6rem auto 0;text-align:center;">We don't believe in signature styles — we believe
  in revealing identities. In creating pieces with character, presence and a life of their own.</p>
  <p style="max-width:56ch;margin:1rem auto 0;text-align:center;font-style:italic;color:var(--ink-soft);">Because beauty was never meant to behave.</p>
</div></section>

<section class="section section--sand"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2.5rem,6vw,3.5rem);">
    <span class="eyebrow">Journal</span>
    <h2 style="margin-top:1rem;">Ideas that inspire our work</h2>
  </div>
  <div class="jgrid">
    {jcard('Design', 'Why Every Great Restaurant Begins With a Story',
           'The most memorable restaurants are not defined by their menu alone. How storytelling shapes unforgettable dining.')}
    {jcard('Hospitality', 'Designing Boutique Hotels People Return To',
           'What transforms a hotel into a destination? The principles behind memorable hospitality design.')}
    {jcard('Objects', 'Objects That Give Spaces Their Soul',
           'Why the smallest details often leave the biggest impression.')}
  </div>
  <div class="center reveal" style="margin-top:2.6rem;"><a class="textlink" href="journal.html">Explore the Journal {A}</a></div>
</div></section>

<section class="section book"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow eyebrow--red">The Collection</span>
  <h2>Bring a piece of Eden &amp; Beyond<br>into your home.</h2>
  <p class="lead">One-off and limited-edition tables, lighting, objects and dressed walls — hand-collaged by Maija.
  Message the studio for availability, editions and price.</p>
  <div class="book__actions">
    <a class="btn btn--primary" href="collection.html">Explore the Collection {A}</a>
    <a class="btn btn--ghost" href="{L.wa('Hi Eden &amp; Beyond, I would like to enquire about a piece from your collection.')}" target="_blank" rel="noopener">{L.WA_ICON} Enquire on WhatsApp</a>
  </div>
</div></section>
'''

pages["index.html"] = L.page(
    title="Eden & Beyond — Collectible Tables, Lighting & Objects by Maija",
    desc=("Collectible, hand-collaged tables, lighting, objects and dressed walls by Maija — one-off and limited "
          "edition. Plus a creative studio for hospitality, residential and commercial projects. Based in Thailand."),
    canonical="index.html",
    body=home_body,
)


# ============================================================ STUDIO (was About + Services)
about_body = f'''
{L.subhero(
    eyebrow="The Studio · Creative Services",
    h1="We don't follow trends.<br>We create stories.",
    sub=("Eden & Beyond is an independent creative studio designing places, objects and experiences for "
         "hospitality, residential and commercial projects — and a design brand with its own collection."),
)}

<section class="section"><div class="wrap">
  <div class="split">
    <div class="split__text reveal">
      <span class="eyebrow">Our Story</span>
      <h2>Design should make<br>people feel something.</h2>
      <p class="lead">Eden &amp; Beyond was born from a simple belief. After years of travelling, discovering
      cultures, meeting artisans and creating places across different worlds, Maija founded the studio to
      bring together everything she loves most.</p>
      <p style="margin-top:1.1rem;">Design. Art. Craftsmanship. Storytelling. Human connection. Today, Eden &amp; Beyond
      collaborates with homeowners, hospitality entrepreneurs and visionary brands to create spaces, objects and
      experiences that leave a lasting impression.</p>
    </div>
    <div class="split__media reveal" data-delay="1">
      {ph('Studio / Maija at work')}
      <span class="tag">The Studio</span>
    </div>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap manifesto reveal">
  <span class="eyebrow" style="display:block;text-align:center;margin-bottom:1.4rem;">Our Philosophy</span>
  <p>We don't arrive with a catalogue of styles. We arrive with <span class="em">curiosity</span>.
  We observe. We listen. We ask questions. Every place already has its own soul —
  our role is simply to reveal it.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="split split--reverse" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow">Meet Maija</span>
      <h2>Founder &amp; Creative Director</h2>
      <p class="lead" style="font-style:italic;">&ldquo;I don't create objects for people. I reveal people through objects.&rdquo;</p>
      <p style="margin-top:1.1rem;">I have always been a creator — but I spent much of my life following conventional
      paths rather than acting on it. There is a world inside me that has never been fully revealed, one that has
      relentlessly knocked at the door of my mind, asking to be released and allowed to exist. Eden &amp; Beyond is the
      key to that door.</p>
    </div>
    <div class="split__media reveal" data-delay="1">
      {('<img src="'+find_img('maija')+'" alt="Maija, founder and creative director of Eden &amp; Beyond">') if find_img('maija') else ph('Portrait — Maija')}
      <span class="tag">Maija · Founder</span>
    </div>
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap prose reveal">
  <p>I create furniture and lighting, transform objects and dress walls — through unique pieces and limited editions.
  Using paper, paint, stencils and layered collage, I take familiar forms and let them reveal the invisible life they carry within.</p>
  <p>For commissioned pieces, the process becomes deeply personal. I don't simply design something for someone. I observe,
  sense and interpret what lives beneath the surface — then reveal it through the object. Each creation becomes a mirror:
  not a literal portrait, but a material expression of the person who inspired it.</p>

  <h3>Before objects, the invisible</h3>
  <p>Before working with objects, I spent twelve years exploring the invisible dimensions of human beings — as a
  psychotherapist, hypnotherapist and family constellation practitioner. That exploration of the unconscious, of symbols,
  hidden loyalties and unseen energies, still inhabits everything I create. The language has changed. The intention has not.</p>

  <h3>Several worlds, on purpose</h3>
  <p>Born in Italy to French parents, raised within the Montessori system, shaped by thirty years in Morocco and now living
  in Thailand, I carry several worlds within me. I am not interested in choosing between them, or in making them behave.
  I let them collide, spark and come alive.</p>

  <h3>Where the name came from</h3>
  <p>Eden &amp; Beyond was born from <em>Eden</em>, Koh Phangan's iconic dance floor — the place that first made me want to
  live on this island. <em>Beyond</em> stands for everything that came after, and for the infinite possibilities that begin
  when we stop accepting the limits handed to us.</p>
  <p>I have no interest in conventional good taste. I am interested in character, contradiction, instinct and life. Some
  pieces are created freely; others are commissioned for private spaces, restaurants, hotels — places that refuse to look
  like anywhere else. All are made to provoke something: curiosity, desire, recognition, discomfort, fascination —
  sometimes all at once.</p>

  <blockquote>F*** the Box is my manifesto, my philosophy of life. Because the Box was never the problem — believing we had to live inside it was.</blockquote>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2.5rem,6vw,3.5rem);">
    <span class="eyebrow">Our Values</span>
    <h2 style="margin-top:1rem;">What drives every project</h2>
  </div>
  <div class="vals">
    <div class="val reveal"><h3>Identity</h3><p>Every project is unique. Never copied. Never repeated.</p></div>
    <div class="val reveal" data-delay="1"><h3>Curiosity</h3><p>The best ideas come from exploring beyond our own world — travel, culture, craftsmanship, art.</p></div>
    <div class="val reveal" data-delay="2"><h3>Craftsmanship</h3><p>Human hands create timeless beauty.</p></div>
    <div class="val reveal"><h3>Meaning</h3><p>Every material, every object, every detail should have a purpose.</p></div>
    <div class="val reveal" data-delay="1"><h3>Longevity</h3><p>We design for years, not for seasons.</p></div>
    <div class="val reveal" data-delay="2"><h3>Emotion</h3><p>People don't remember decoration. They remember how a place made them feel.</p></div>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;">
    <span class="eyebrow">Who We Work With</span>
    <h2 style="margin:1rem 0 2rem;">Visionaries with a story to tell</h2>
    <ul class="tags reveal">
      <li>Boutique Hotels</li><li>Restaurants &amp; Bars</li><li>Private Villas</li>
      <li>Developers</li><li>Commercial Spaces</li><li>Lifestyle Brands</li>
      <li>Visionary Entrepreneurs</li><li>Private Clients</li>
    </ul>
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2.5rem,6vw,3.5rem);">
    <span class="eyebrow">Creative Services</span>
    <h2 style="margin-top:1rem;">Four disciplines,<br>one way of thinking.</h2>
  </div>
  <div class="disc">
    <a class="disc__card reveal" href="hospitality-design.html">{ph('Hospitality design', 'ph--dark')}
      <div class="disc__body"><h3>Hospitality Design</h3>
      <p>Hotels, restaurants, cafés, bars, beach clubs and wellness spaces designed to create memorable guest experiences.</p></div></a>
    <a class="disc__card reveal" data-delay="1" href="residential-design.html">{ph('Residential design', 'ph--dark')}
      <div class="disc__body"><h3>Residential Design</h3>
      <p>Luxury villas, private residences and holiday homes designed around the people who live in them.</p></div></a>
    <a class="disc__card reveal" href="furniture-object-design.html">{ph('Furniture &amp; object design', 'ph--dark')}
      <div class="disc__body"><h3>Furniture &amp; Object Design</h3>
      <p>Bespoke furniture, lighting and custom objects — for a project, or as part of our <a href="collection.html" style="color:inherit;text-decoration:underline;">Collection</a>.</p></div></a>
    <a class="disc__card reveal" data-delay="1" href="creative-direction.html">{ph('Creative direction', 'ph--dark')}
      <div class="disc__body"><h3>Creative Direction</h3>
      <p>Concept development, storytelling, styling and creative vision for hospitality, residential and commercial projects.</p></div></a>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;margin-bottom:clamp(2.5rem,6vw,3.5rem);">
    <span class="eyebrow">Our Process</span>
    <h2 style="margin-top:1rem;">Every project follows<br>the same philosophy.</h2>
    <p class="lead" style="margin-inline:auto;margin-top:1.2rem;">No formulas. No signature style. Every project is built around its own story.</p>
  </div>
  <div class="steps">
    <div class="step reveal"><span class="step__num">01</span><h3>Discover</h3><p>Understanding people before spaces. Listening before designing.</p></div>
    <div class="step reveal" data-delay="1"><span class="step__num">02</span><h3>Define</h3><p>Finding the story before drawing the first line.</p></div>
    <div class="step reveal" data-delay="2"><span class="step__num">03</span><h3>Design</h3><p>Every material, object and light with purpose.</p></div>
    <div class="step reveal"><span class="step__num">04</span><h3>Curate</h3><p>Furniture, objects and details, chosen with intention.</p></div>
    <div class="step reveal" data-delay="1"><span class="step__num">05</span><h3>Deliver</h3><p>A finished project that feels unforgettable.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="split" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow">The Design Collection</span>
      <h2 style="margin:1rem 0 1.2rem;">Own a piece,<br>no project required.</h2>
      <p class="lead">Beyond commissioned projects, Eden &amp; Beyond is a design brand in its own right — a curated
      collection of bespoke furniture, lighting and objects you can discover, commission or acquire on their own.</p>
      <a class="btn btn--primary" href="collection.html" style="margin-top:1.6rem;">Explore the Collection {A}</a>
    </div>
    <div class="split__media reveal" data-delay="1">{ph('Collection — signature object', 'ph--dark')}<span class="tag">The Collection</span></div>
  </div>
</div></section>

{L.cta_band(
    title="Looking for more than a beautiful space?",
    text="Let's create something people will remember.",
)}
'''
pages["studio.html"] = L.page(
    title="Studio — Eden & Beyond Creative Studio & Design Brand | Maija",
    desc=("Eden & Beyond is an independent creative studio and design brand founded by Maija — hospitality, "
          "residential and commercial design, creative direction, and a collection of bespoke furniture and objects. Based in Thailand."),
    canonical="studio.html",
    body=about_body,
    extra_head=L.person_maija_schema(),
)


# ============================================================ PROJECTS
projects_body = f'''
{L.subhero(
    eyebrow="Projects",
    h1="One remarkable project says more than a hundred ordinary ones.",
    sub="Every project is an opportunity to create something entirely unique.",
)}

<section class="feat" style="min-height:70vh;">{ph('Dar Mansour — Koh Phangan', 'ph--dark')}
  <div class="wrap feat__inner reveal">
    <span class="eyebrow">Featured Project</span>
    <h2>Dar Mansour</h2>
    <p class="feat__place">Morocco's Kitchen · Koh Phangan, Thailand</p>
    <p>A contemporary interpretation of Moroccan hospitality, where architecture, craftsmanship, objects and
    storytelling come together to create an immersive dining experience.</p>
    <div style="margin-top:1.8rem;"><a class="btn btn--light" href="https://darmansour.com" target="_blank" rel="noopener">Visit darmansour.com {A}</a></div>
  </div>
</section>

<section class="section"><div class="wrap">
  <div class="split">
    <div class="split__text reveal">
      <span class="eyebrow">Our Approach</span>
      <h2>We don't build a portfolio.<br>We build lasting projects.</h2>
      <p class="lead">Rather than repeating the same style, every commission begins with a blank page and a different story.</p>
      <p style="margin-top:1.1rem;">That's why no two Eden &amp; Beyond projects will ever look the same.</p>
    </div>
    <div class="split__media reveal" data-delay="1">{ph('Dar Mansour — interior detail')}<span class="tag">Dar Mansour · Detail</span></div>
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="note reveal" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1.4rem;">
    <div>
      <span class="eyebrow" style="margin-bottom:.5rem;">Inspired by this project?</span>
      <p style="max-width:52ch;">Several furniture pieces, lighting fixtures and objects created for Dar Mansour are available as
      bespoke commissions or limited editions.</p>
    </div>
    <a class="btn btn--primary" href="collection.html">Explore the Collection {A}</a>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;">
    <span class="eyebrow">Coming Next</span>
    <h2 style="margin:1rem 0 1.4rem;">New stories, unfolding.</h2>
    <p class="lead" style="margin-inline:auto;">We're currently working on new hospitality, residential and object design projects.
    As each story unfolds, it will find its place here.</p>
  </div>
</div></section>

{L.cta_band(
    title="Every project starts with a conversation.",
    text=("Whether you're creating a boutique hotel, a restaurant, a private villa or something entirely new, "
          "we'd love to hear your vision."),
    btn_label="Start Your Story",
)}
'''
pages["projects.html"] = L.page(
    title="Projects — Eden & Beyond Creative Studio",
    desc=("Selected projects by Eden & Beyond, including Dar Mansour — Morocco's Kitchen in Koh Phangan, Thailand. "
          "Hospitality, residential and object design built around each project's own story."),
    canonical="projects.html",
    body=projects_body,
    extra_head=L.project_schema(
        "Dar Mansour — Morocco's Kitchen",
        "A contemporary interpretation of Moroccan hospitality by Eden & Beyond — architecture, craftsmanship, objects and storytelling.",
        "https://darmansour.com",
        "Koh Phangan, Thailand"),
)


# ============================================================ JOURNAL
journal_body = f'''
{L.subhero(
    eyebrow="Journal",
    h1="Ideas, stories and perspectives.",
    sub="The ideas, materials, places, people and craftsmanship that shape the way we design.",
)}

<section class="section"><div class="wrap wrap--narrow center reveal">
  <p class="lead">Our work doesn't begin with a floor plan. It begins with curiosity. The Journal is where we share
  the ideas, materials, places, people and craftsmanship that inspire every project — part editorial, part travel diary,
  part design journal.</p>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow">Featured</span>
    <h2 style="margin-top:1rem;">From the Journal</h2>
  </div>
  <div class="jgrid">
    {jcard('Design', 'Why Every Great Restaurant Begins With a Story',
           'The most memorable restaurants are not defined by their menu alone. How storytelling shapes unforgettable dining experiences.')}
    {jcard('Hospitality', 'Designing Boutique Hotels People Return To',
           'What transforms a hotel into a destination? The principles behind memorable hospitality design.')}
    {jcard('Objects', 'Objects That Give Spaces Their Soul',
           'Why the smallest details often leave the biggest impression.')}
    {jcard('Craftsmanship', 'The Beauty of Moroccan Craftsmanship',
           'Zellige, carved plaster, hand-worked brass — the human hands behind timeless materials.')}
    {jcard('Residential', 'Creating Homes With Soul',
           'How a house becomes a home — designed around the people who live in it.')}
    {jcard('Materials', 'Materials That Age Beautifully',
           'The finishes and textures that only get better with time.')}
  </div>
</div></section>

<section class="section band-dark"><div class="wrap wrap--narrow center reveal">
  <span class="eyebrow">Why We Write</span>
  <h2 style="margin:1rem 0 1.4rem;">Good design starts long<br>before construction begins.</h2>
  <p class="lead" style="margin-inline:auto;">By sharing our ideas, inspirations and process, we hope to inspire better
  conversations — and better projects.</p>
</div></section>

{L.cta_band(
    title="Have a project in mind?",
    text="Let's start the conversation.",
)}
'''
pages["journal.html"] = L.page(
    title="Journal — Design, Hospitality & Craftsmanship | Eden & Beyond",
    desc=("The Eden & Beyond Journal: editorial stories on design, hospitality, craftsmanship, materials and "
          "creative direction — the ideas that shape the way we design."),
    canonical="journal.html",
    body=journal_body,
)


# ============================================================ CONTACT
contact_body = f'''
{L.subhero(
    eyebrow="Contact",
    h1="Let's create something extraordinary.",
    sub=("Whether you're developing a boutique hotel, opening a restaurant, designing a private villa or creating "
         "something entirely new, we'd love to hear from you."),
)}

<section class="section"><div class="wrap">
  <div class="contact-grid">
    <div class="contact-info reveal">
      <span class="eyebrow">Start the Conversation</span>
      <h2 style="margin:1rem 0 1.4rem;">The best projects begin<br>with a message.</h2>
      <p style="margin-bottom:2rem;">Tell us about your vision — a project, a bespoke commission or a piece from the
      collection. WhatsApp is the fastest way to reach the studio.</p>
      <dl>
        <div><dt>WhatsApp</dt><dd><a href="{L.wa('Hi Eden &amp; Beyond, I would like to talk about a project.')}" target="_blank" rel="noopener">{L.WHATSAPP_DISPLAY}</a><span class="contact-note">Maija — the fastest response.</span></dd></div>
        <div><dt>Instagram</dt><dd><a href="{L.INSTAGRAM}" target="_blank" rel="noopener">{L.INSTAGRAM_HANDLE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{L.EMAIL}">{L.EMAIL}</a></dd></div>
        <div><dt>Location</dt><dd>Working internationally.<span class="contact-note">Based in Thailand.</span></dd></div>
      </dl>
    </div>

    <div class="enquiry reveal" data-delay="1" style="text-align:center;align-self:start;">
      <span class="eyebrow" style="margin-bottom:1rem;">Talk to the studio</span>
      <h3 style="margin-bottom:.8rem;">Message us on WhatsApp</h3>
      <p style="max-width:none;margin-bottom:1.7rem;color:var(--ink-soft);">Share your project, ask about a piece from
      the collection, or just say hello. We'll take it from there.</p>
      <a class="btn btn--primary" href="{L.wa('Hi Eden &amp; Beyond, I found you through your website and would love to talk.')}" target="_blank" rel="noopener" style="width:100%;justify-content:center;">{L.WA_ICON} Chat on WhatsApp</a>
      <p class="enquiry__note">Opens WhatsApp with a message ready to send.</p>
    </div>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:720px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow">Frequently Asked Questions</span>
    <h2 style="margin-top:1rem;">Good to know</h2>
  </div>
  <div class="faq" style="color:var(--on-dark);">
    <details class="faq__item" style="border-color:rgba(244,239,230,.18);"><summary style="color:#fff;">Where do you work?</summary>
      <div class="faq__answer" style="color:var(--on-dark-soft);"><p>We collaborate with clients worldwide. The studio is based in Thailand and works internationally.</p></div></details>
    <details class="faq__item" style="border-color:rgba(244,239,230,.18);"><summary style="color:#fff;">Can you work remotely?</summary>
      <div class="faq__answer" style="color:var(--on-dark-soft);"><p>Yes. Many projects begin remotely before moving on site.</p></div></details>
    <details class="faq__item" style="border-color:rgba(244,239,230,.18);"><summary style="color:#fff;">Do you work with architects and developers?</summary>
      <div class="faq__answer" style="color:var(--on-dark-soft);"><p>Absolutely. We regularly collaborate with architects, developers, consultants and contractors.</p></div></details>
    <details class="faq__item" style="border-color:rgba(244,239,230,.18);"><summary style="color:#fff;">Do you only work on large projects?</summary>
      <div class="faq__answer" style="color:var(--on-dark-soft);"><p>No. Whether it's a complete hospitality concept, a private villa or a bespoke furniture commission, every project receives the same attention to detail.</p></div></details>
  </div>
</div></section>
'''
CONTACT_FAQS = [
    ("Where do you work?",
     "We collaborate with clients worldwide. The studio is based in Thailand and works internationally."),
    ("Can you work remotely?",
     "Yes. Many projects begin remotely before moving on site."),
    ("Do you work with architects and developers?",
     "Absolutely. We regularly collaborate with architects, developers, consultants and contractors."),
    ("Do you only work on large projects?",
     "No. Whether it's a complete hospitality concept, a private villa or a bespoke furniture commission, "
     "every project receives the same attention to detail."),
]
pages["contact.html"] = L.page(
    title="Contact — Start a Project | Eden & Beyond Creative Studio",
    desc=("Start a project with Eden & Beyond. Boutique hotels, restaurants, private villas, bespoke furniture and "
          "creative direction. Working internationally, based in Thailand. hello@edenandbeyond.studio"),
    canonical="contact.html",
    body=contact_body,
    extra_head=L.faq_schema(CONTACT_FAQS),
)


# ============================================================ COLLECTION (design brand)
# Editorial presentation, not a shop — pieces feel collectible. Categories:
# Furniture / Lighting / Objects / Limited Editions. `img` fills in once real
# files land in assets/img/ (kebab-case, WebP, SEO alt); until then a vivid
# tinted placeholder named after the piece stands in.
def piece(slug, title, medium, shape, tint, img=None):
    cls = f"art {shape}".strip()
    # img (when given) is the image-file stem, which can differ from the display slug
    src = find_img(slug) or (find_img(img) if img else None)
    if src:
        media = f'<img src="{src}" alt="{title} — {medium}, Eden &amp; Beyond" loading="lazy">'
    else:
        media = ph(title, tint)
    # a piece with its own caption page links to it; placeholders open a WhatsApp enquiry
    href = f"{slug}.html" if slug in CAPTION_SLUGS else L.wa(
        f'Hi Eden &amp; Beyond, I would like to enquire about "{title}" from your collection.')
    return f'''<a class="{cls} reveal" href="{href}" id="{slug}">
      <div class="art__media">{media}</div>
      <div class="art__cap"><span class="art__title">{title}</span>
      <span class="art__meta">{medium}</span></div>
    </a>'''


# Slug = image filename stem (keeps the photo mapping); title = the real piece
# name from Maija's captions. The collaged tondos & panels are limited-edition
# TABLES — furniture, not wall art.
COLLECTION = [
    ("tables", "Tables",
     "Each table is a one-off — a familiar form dressed in paper, paint and layered collage until it reveals the "
     "invisible life it carries. Moroccan icons collided with Western art. Numbered, collectible, made to be lived with.", [
        ("hubb",                   "Hubb",              "Limited-edition table", "art--round", "ph--poppy",    "poppy-queen"),
        ("flash",                  "Flash",             "Limited-edition table", "",           "ph--electric", "wondermint-camel"),
        ("mona",                   "Mona",              "Limited-edition table", "art--round", "ph--teal",     "mona-lisa-fez"),
        ("babouche",               "Babouche",          "Limited-edition table", "",           "ph--magenta",  "babouche-mandala"),
        ("divine-touch",           "Divine Touch",      "Limited-edition table", "art--round", "ph--teal",     "creation-of-mint-tea"),
        ("framed",                 "Framed",            "Limited-edition table", "",           "ph--electric", "chefchaouen-framed"),
        ("qaf-in-the-oasis",       "Qaf in the Oasis",  "Limited-edition table", "art--round", "ph--magenta",  "desert-caravan-neon"),
        ("a-tea-in-the-desert",    "A Tea in the Desert","Limited-edition table","",           "ph--sun",      "teapot-camel"),
        ("ysl",                    "YSL",               "Limited-edition table", "",           "ph--teal",     "rue-yves-saint-laurent"),
     ]),
    ("lighting", "Lighting",
     "Light as atmosphere — pieces where the object matters as much as the glow. Kenza and Kenzo are a pair.", [
        ("kenza",  "Kenza",  "Lighting · mixed-media lamp",  "art--tall",  "ph--poppy"),
        ("kenzo",  "Kenzo",  "Lighting · mixed-media lamp",  "art--tall",  "ph--dark"),
     ]),
    ("objects", "Objects",
     "Transformed objects and decorative pieces — the small things that give a room its soul.", [
        ("zellige-mirror",   "Zellige Mirror",   "Object · bespoke commission", "",  "ph--teal"),
        ("sculptural-vessel","Sculptural Vessel","Object · limited edition",    "",  "ph--sun"),
     ]),
    ("walls", "Walls",
     "Hand-stencilled walls and murals — site-specific commissions that turn a surface into a story. "
     "Zellige geometry and floral damask, plastered and painted by hand onto raw earth walls.", [
        ("fountain-wall",  "Fountain Wall",  "Hand-stencilled wall · commission", "",  "ph--dark"),
        ("entrance-wall",  "Entrance Wall",  "Hand-stencilled wall · commission", "",  "ph--teal"),
        ("star-wall",      "Star Wall",      "Hand-stencilled wall · commission", "",  "ph--sun"),
        ("floral-wall",    "Floral Wall",    "Hand-stencilled wall · commission", "",  "ph--magenta"),
     ]),
]


# ---- Per-piece caption pages (Maija's texts, verbatim). Blank line = new stanza.
CAPTIONS = {
    "hubb": dict(title="Hubb", kicker="Limited-edition table", img="poppy-queen", shape="round",
        lead="She looks soft. She isn't.", text="""She looks soft.
She isn't.

Crowned in silence, wrapped in beauty — but don't get too close.

This piece lives in the tension: delicacy and danger, ritual and rebellion, a place where form becomes feeling.

Not just a table. A presence."""),
    "flash": dict(title="Flash", kicker="Limited-edition table", img="wondermint-camel", shape="",
        lead="Extra fresh. Extra cool. Not what you think.", text="""Extra fresh.
Extra cool.
Not what you think.

Minty perfection. Smooth attitude. Zero flaws. That's the promise.

Reality? A little weirder. A little louder. A lot less obedient.

Because perfection is boring. And boxes are meant to be chewed."""),
    "babouche": dict(title="Babouche", kicker="Limited-edition table", img="babouche-mandala", shape="",
        lead="Get closer. And then try to look away.", text="""Get closer.
And then try to look away.

A ritual of repetition. Colour. Pattern. Pulse.

What seems controlled starts to move. What looks playful becomes obsessive.

This is where order turns into trance — where beauty loops until it takes over.

Not decoration. A frequency."""),
    "qaf-in-the-oasis": dict(title="Qaf in the Oasis", kicker="Limited-edition table", img="desert-caravan-neon", shape="round",
        lead="Follow the line. And then — stop.", text="""Follow the line.
And then — stop.

A command in the middle of the journey. A break in the flow.

But what if stopping is just another way of moving?

Between desert and signal, tradition and interruption, this piece plays with direction — and refuses to obey it."""),
    "mona": dict(title="Mona", kicker="Limited-edition table", img="mona-lisa-fez", shape="round",
        lead="Perfect smile. Perfect pose. Perfect cage.", text="""Perfect smile.
Perfect pose.
Perfect cage.

So what happens when she decides to move?

A shift. A clash. A quiet rebellion.

Not ruined. Because timeless doesn't mean untouchable. And beauty was never meant to behave."""),
    "framed": dict(title="Framed", kicker="Limited-edition table", img="chefchaouen-framed", shape="",
        lead="Put it in a frame and suddenly it matters.", text="""Put it in a frame and suddenly it matters.

Gold edges. Perfect lines. Now you're supposed to admire it.

But what really changed? The view — or the way you were told to see it?

Because value is often just a story. And rules are just well-decorated limits."""),
    "ysl": dict(title="YSL", kicker="Limited-edition table", img="rue-yves-saint-laurent", shape="",
        lead="A real one. Rue Yves Saint Laurent.", text="""A real one. Rue Yves Saint Laurent.

But even icons who built their legacy in gardens and walls don't get to own the story forever.

Because places evolve. Meanings shift. And what was once sacred can be taken somewhere else entirely.

Not imitation. A continuation — with attitude."""),
    "divine-touch": dict(title="Divine Touch", kicker="Limited-edition table", img="creation-of-mint-tea", shape="round",
        lead="An offering. Or a command.", text="""An offering.
Or a command.

Sweetness in one hand. Freshness in the other.

Take it. Or wait to be allowed.

A quiet game of control, where desire isn't rushed — it's held.

Because the most powerful exchanges aren't given freely. They're felt, and surrendered to."""),
    "a-tea-in-the-desert": dict(title="A Tea in the Desert", kicker="Limited-edition table", img="teapot-camel", shape="",
        lead="You think you know the story. But look again.", text="""Or is it?

Wrapped in colours, dressed in codes — you think you know the story.

But look again.

Because style isn't a costume. And identity isn't a trend. It's worn."""),
    "kenza": dict(title="Kenza", kicker="Lighting · mixed-media lamp", img="kenza", shape="tall",
        lead="Handle with care.", text="""Handle with care.

She is stitched together from old stories, other people's expectations, stamps of approval, souvenirs of who she was supposed to be.

Then she switched on.

And suddenly, all that remained… was her light."""),
    "kenzo": dict(title="Kenzo", kicker="Lighting · mixed-media lamp", img="kenzo", shape="tall",
        lead="Some love stories don't need words. Just good lighting.", text="""Kenza switched on.
He stayed.

Not to save her. Not to lead. Just to burn at the same intensity.

Some love stories don't need words.
Just good lighting."""),
}
CAPTION_SLUGS = set(CAPTIONS)


def _caption_html(text):
    stanzas = text.split("\n\n")
    out = []
    for st in stanzas:
        lines = "<br>".join(st.split("\n"))
        out.append(f"<p>{lines}</p>")
    return "\n".join(out)


def _piece_wa(title, kicker):
    """Acquiring a Collection piece is a direct WhatsApp enquiry, not a project brief."""
    return L.wa(f'Hi Eden &amp; Beyond, I would like to enquire about "{title}" ({kicker}) from your '
                f'collection — availability, editions and price.')


def build_piece_pages():
    order = list(CAPTIONS.keys())
    for i, slug in enumerate(order):
        d = CAPTIONS[slug]
        src = find_img(d["img"])
        media = (f'<img src="{src}" alt="{d["title"]} — {d["kicker"]}, Eden &amp; Beyond by Maija" fetchpriority="high">'
                 if src else ph(d["title"]))
        media_cls = "piece__media" + (" piece__media--round" if d["shape"] == "round" else
                                      " piece__media--tall" if d["shape"] == "tall" else "")
        nxt = order[(i + 1) % len(order)]
        nd = CAPTIONS[nxt]
        body = f'''
{L.breadcrumb(("Collection", "collection.html"), (d["title"], None))}
<section class="section" style="padding-top:1.4rem;"><div class="wrap">
  <div class="piece">
    <div class="{media_cls} reveal">{media}</div>
    <div class="piece__body reveal" data-delay="1">
      <span class="eyebrow eyebrow--red">{d["kicker"]}</span>
      <h1>{d["title"]}</h1>
      <div class="piece__caption">{_caption_html(d["text"])}</div>
      <p class="piece__sig">F<span class="fbox__stars">&#9733;&#9733;&#9733;</span> the Box</p>
      <div class="piece__actions">
        <a class="btn btn--primary" href="{_piece_wa(d["title"], d["kicker"])}" target="_blank" rel="noopener">{L.WA_ICON} Enquire on WhatsApp</a>
        <a class="btn btn--ghost" href="collection.html">Back to the Collection</a>
      </div>
    </div>
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <a class="piece-next reveal" href="{nxt}.html">
    <span class="eyebrow eyebrow--red">Next piece</span>
    <span class="piece-next__row"><span class="piece-next__title">{nd["title"]}</span>{A}</span>
  </a>
</div></section>
'''
        pages[f"{slug}.html"] = L.page(
            title=f'{d["title"]} — {d["kicker"]} | Eden & Beyond',
            desc=f'{d["title"]} by Maija, {d["kicker"].lower()} from the Eden & Beyond collection. {d["lead"]}',
            canonical=f"{slug}.html",
            body=body,
            body_class="page-collection page-piece",
        )


def collection_section(anchor, title, blurb, pieces):
    grid = "\n    ".join(piece(*p) for p in pieces)
    return f'''
<section class="section" id="{anchor}" style="padding-top:0;"><div class="wrap">
  <div class="reveal" style="margin-bottom:clamp(1.6rem,4vw,2.4rem);">
    <span class="eyebrow">{title}</span>
    <p class="lead" style="margin-top:.6rem;max-width:60ch;">{blurb}</p>
  </div>
  <div class="artgrid">{grid}</div>
</div></section>'''


collection_nav = " · ".join(
    f'<a class="ilink" href="#{a}">{t}</a>' for a, t, _, _ in COLLECTION)
collection_sections = "\n".join(collection_section(*c) for c in COLLECTION)
_col_cls, _col_media = subhero_media("hero-collection")
_col_wa = L.wa("Hi Eden &amp; Beyond, I would like to enquire about a piece from your collection "
               "— availability, editions and price.")
collection_body = f'''
{L.breadcrumb(("Collection", None))}
{L.subhero(
    eyebrow="The Design Collection",
    h1="Bring a piece of Eden &amp; Beyond into your home.",
    sub=("Limited-edition tables, lighting, transformed objects and dressed walls — collaged by hand, designed by the "
         "studio, available on their own. Discover, commission or acquire a single piece, no project required."),
    media_class=_col_cls,
    media_html=_col_media,
)}

<section class="section"><div class="wrap wrap--narrow center reveal">
  <p class="lead">Every piece begins the way our projects do — with a story, a material, a wink. Some are born inside a
  commission and released as editions; others exist purely as objects. None are mass-produced.</p>
  <p style="margin-top:1.2rem;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);">{collection_nav}</p>
</div></section>

{collection_sections}

<section class="section" style="padding-top:0;"><div class="wrap wrap--narrow center reveal">
  <p style="color:var(--muted);font-size:.86rem;">Furniture, objects and wall pieces beyond the tables are shown on request.
  Dimensions, editions and pricing are shared over WhatsApp — <a class="ilink" href="{_col_wa}" target="_blank" rel="noopener">enquire about a piece</a>.</p>
</div></section>

<section class="section book"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow eyebrow--red">The Collection</span>
  <h2>Found a piece you love —<br>or want your own?</h2>
  <p class="lead">Every piece is one-off or limited edition. Message the studio for availability, editions and price —
  or commission something made entirely for your space.</p>
  <div class="book__actions">
    <a class="btn btn--primary" href="{_col_wa}" target="_blank" rel="noopener">{L.WA_ICON} Enquire on WhatsApp</a>
    <a class="btn btn--ghost" href="{L.wa('Hi Eden &amp; Beyond, I would like to talk about a project.')}" target="_blank" rel="noopener">Start a Full Project</a>
  </div>
</div></section>
'''
pages["collection.html"] = L.page(
    title="The Collection — Bespoke Furniture, Lighting & Objects | Eden & Beyond",
    desc=("The Eden & Beyond design collection — bespoke furniture, lighting, decorative objects and limited-edition "
          "collages by Maija. Collectible pieces available on their own, no project required. Based in Thailand."),
    canonical="collection.html",
    body=collection_body,
    body_class="page-collection",
)


# ============================================================ SEO LANDING PAGES
def landing(slug, eyebrow, h1, sub, overview, wwd_title, wwd_items, services,
            approach_title, approach, why_title=None, why=None, crumb_label=None):
    wwd_html = "".join(wwd_item(t, d) for t, d in wwd_items)
    svc_html = "".join(f'<li>{s}</li>' for s in services)
    why_block = ""
    if why:
        why_block = f'''
<section class="section band-dark"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">{why_title}</span>
  <h2 style="margin:1rem 0 1.4rem;">{why['h2']}</h2>
  <p class="lead" style="color:var(--on-dark-soft);">{why['body']}</p>
</div></section>'''
    body = f'''
{L.breadcrumb((crumb_label or h1, None))}
{L.subhero(eyebrow=eyebrow, h1=h1, sub=sub)}

<section class="section"><div class="wrap wrap--narrow prose reveal">
  <span class="eyebrow">Overview</span>
  <h2 style="margin-top:.8rem;">{overview['h2']}</h2>
  {overview['body']}
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow">What We Design</span>
    <h2 style="margin-top:1rem;">{wwd_title}</h2>
  </div>
  <div class="wwd">{wwd_html}</div>
</div></section>

<section class="section band-dark"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">Services</span>
  <h2 style="margin:1rem 0 1.4rem;">What's included</h2>
  <ul class="tags" style="justify-content:flex-start;">{svc_html}</ul>
</div></section>

<section class="section"><div class="wrap wrap--narrow prose reveal">
  <span class="eyebrow">{approach_title}</span>
  <h2 style="margin-top:.8rem;">{approach['h2']}</h2>
  {approach['body']}
</div></section>
{why_block}
{L.cta_band(title="Let's create something people will remember.",
            text="Tell us about your project — we'd love to hear your story.")}
'''
    pages[slug] = L.page(title=h1_meta[slug], desc=desc_meta[slug], canonical=slug,
                         body=body)


# Meta titles/descriptions for landing pages (SEO — geo-anchored to Thailand)
h1_meta = {
    "hospitality-design.html": "Hospitality Design Studio — Hotels, Restaurants & Bars | Eden & Beyond, Thailand",
    "restaurant-design.html": "Restaurant Design & Interior Concepts | Eden & Beyond, Thailand",
    "residential-design.html": "Villa & Residential Interior Design | Eden & Beyond, Thailand",
    "furniture-object-design.html": "Bespoke Furniture & Object Design | Eden & Beyond",
    "creative-direction.html": "Creative Direction & Brand Experience for Hospitality | Eden & Beyond",
}
desc_meta = {
    "hospitality-design.html": ("Hospitality design studio for boutique hotels, restaurants, bars, beach clubs and wellness "
                                "spaces. Eden & Beyond designs memorable guest experiences — based in Thailand, working internationally."),
    "restaurant-design.html": ("Restaurant interior design and concept development by Eden & Beyond — dining spaces built around "
                               "story, atmosphere and craft. Based in Thailand, working internationally."),
    "residential-design.html": ("Villa and residential interior design by Eden & Beyond — private homes and luxury residences "
                                "designed around the people who live in them. Based in Thailand, working internationally."),
    "furniture-object-design.html": ("Bespoke furniture, lighting and object design by Eden & Beyond — custom pieces that give each "
                                     "project its own identity."),
    "creative-direction.html": ("Creative direction, concept development, storytelling and styling for hospitality, residential and "
                                "lifestyle brands by Eden & Beyond."),
}

landing(
    "hospitality-design.html",
    eyebrow="Hospitality Design", crumb_label="Hospitality Design",
    h1="Hospitality Design",
    sub="Hotels, restaurants, bars, beach clubs, cafés and wellness spaces designed to create memorable guest experiences.",
    overview={"h2": "Design that turns a space into a destination",
              "body": ("<p>A hotel should become a destination. A restaurant should become a memory. Eden &amp; Beyond designs "
                       "hospitality spaces where architecture, interiors, objects and storytelling work together — so guests feel "
                       "something the moment they arrive, and remember it long after they leave.</p>"
                       "<p>We work internationally from our base in Thailand, with hospitality entrepreneurs, boutique hotel owners "
                       "and restaurateurs who want more than a beautiful room.</p>")},
    wwd_title="Hospitality spaces we design",
    wwd_items=[
        ("Boutique Hotels", "Immersive properties with a clear identity, from concept to guest experience."),
        ("Restaurants &amp; Cafés", "Dining rooms built around atmosphere, service flow and story."),
        ("Bars &amp; Beach Clubs", "Social spaces with energy, character and a strong sense of place."),
        ("Wellness Spaces", "Calm, considered environments designed around how people want to feel."),
    ],
    services=["Concept &amp; Storytelling", "Interior Design", "Space Planning", "Material &amp; Finish Selection",
              "Furniture &amp; Lighting", "Art &amp; Object Curation", "Styling", "Creative Direction"],
    approach_title="Approach",
    approach={"h2": "We begin with understanding, not aesthetics",
              "body": ("<p>Every hospitality project starts with the people, the place, the culture and the ambition. Only then do we "
                       "design. The result is coherent from the first impression to the smallest detail — a space with its own identity "
                       "rather than a borrowed trend.</p>"
                       '<p>See how this shaped <a href="projects.html">Dar Mansour</a>, our Moroccan hospitality project in Koh Phangan, '
                       'or read more about our <a href="studio.html">creative process</a>.</p>')},
    why_title="Why It Matters",
    why={"h2": "Memorable hospitality is designed on purpose",
         "body": "Guests don't remember decoration. They remember how a place made them feel — and that feeling is the outcome of hundreds of intentional decisions."},
)

landing(
    "restaurant-design.html",
    eyebrow="Restaurant Design", crumb_label="Restaurant Design",
    h1="Restaurant Design",
    sub="Dining spaces built around story, atmosphere and craft — from first concept to the final detail.",
    overview={"h2": "A restaurant should become a memory",
              "body": ("<p>The most memorable restaurants aren't defined by their menu alone. They're defined by how it feels to be "
                       "there. Eden &amp; Beyond designs restaurants where interiors, lighting, objects and narrative come together into "
                       "one coherent experience.</p>"
                       "<p>We work with restaurateurs and hospitality groups internationally, from our base in Thailand.</p>")},
    wwd_title="What we design for restaurants",
    wwd_items=[
        ("Concept &amp; Identity", "The story and atmosphere that make a restaurant unmistakably itself."),
        ("Interiors &amp; Layout", "Dining rooms designed around service, comfort and mood."),
        ("Lighting &amp; Materials", "The finishes and light that set the tone from day to night."),
        ("Bespoke Details", "Custom furniture, tableware direction and objects with meaning."),
    ],
    services=["Restaurant Concept", "Interior Design", "Space &amp; Seating Planning", "Lighting Design",
              "Material Selection", "Bespoke Furniture", "Styling", "Creative Direction"],
    approach_title="Philosophy",
    approach={"h2": "Every great restaurant begins with a story",
              "body": ("<p>We don't repeat a signature look from one project to the next. Each restaurant begins with a blank page and "
                       "its own story — its cuisine, its place, its people.</p>"
                       '<p>Our Moroccan project <a href="projects.html">Dar Mansour</a> in Koh Phangan is one example of this approach '
                       'in practice. Learn more about our <a href="hospitality-design.html">hospitality design</a> work.</p>')},
)

landing(
    "residential-design.html",
    eyebrow="Residential Design", crumb_label="Residential Design",
    h1="Residential Design",
    sub="Private villas, luxury residences and holiday homes designed around the people who live in them.",
    overview={"h2": "A villa should become a sanctuary",
              "body": ("<p>A home is more than a beautiful interior — it's a reflection of the people who live in it. Eden &amp; Beyond "
                       "designs private residences with personality, warmth and timeless character, from the architecture of a space to "
                       "the objects that fill it.</p>"
                       "<p>We work with private clients and developers internationally, from our base in Thailand.</p>")},
    wwd_title="Residential projects we design",
    wwd_items=[
        ("Private Villas", "Distinctive homes designed around a way of living, not a trend."),
        ("Luxury Residences", "Refined interiors with warmth, texture and lasting character."),
        ("Holiday Homes", "Restful retreats with a strong sense of place."),
        ("Interiors &amp; Styling", "Furniture, lighting and objects curated with intention."),
    ],
    services=["Interior Design", "Space Planning", "Material &amp; Finish Selection", "Bespoke Furniture",
              "Lighting Design", "Art &amp; Object Curation", "Styling", "Creative Direction"],
    approach_title="Approach",
    approach={"h2": "Designed for years, not for seasons",
              "body": ("<p>We design homes that age beautifully — with natural materials, human craftsmanship and details chosen to "
                       "last. Every project begins by understanding how you actually want to live.</p>"
                       '<p>Explore our <a href="studio.html">full range of services</a> or <a href="https://wa.me/66923651604" target="_blank" rel="noopener">start a '
                       'conversation</a> about your home.</p>')},
)

landing(
    "furniture-object-design.html",
    eyebrow="Furniture & Objects", crumb_label="Furniture & Objects",
    h1="Furniture &amp; Object Design",
    sub="Bespoke furniture, lighting and custom objects that give every project its own identity.",
    overview={"h2": "Objects that tell a story",
              "body": ("<p>An object should tell a story. Eden &amp; Beyond designs bespoke furniture, lighting and decorative objects — "
                       "either as part of a larger project or as standalone commissions. Each piece is designed with purpose, made to be "
                       "kept for a lifetime.</p>"
                       '<p>Our <em>Kenza</em> lamp — a collaged bust crowned with a tasselled fez shade — is one example of how a single '
                       'object can carry a whole atmosphere. See it and other pieces in <a href="collection.html">the Collection</a>.</p>')},
    wwd_title="What we design",
    wwd_items=[
        ("Bespoke Furniture", "Custom pieces designed for a specific space and story."),
        ("Lighting", "Fixtures that shape atmosphere as much as they provide light."),
        ("Decorative Objects", "Considered details that give a space its character."),
        ("Art &amp; Curation", "Sourcing and curating pieces that complete a project."),
    ],
    services=["Custom Furniture Design", "Lighting Design", "Material Selection", "Prototyping &amp; Maker Liaison",
              "Object &amp; Art Curation", "Collections"],
    approach_title="Philosophy",
    approach={"h2": "Human hands create timeless beauty",
              "body": ("<p>We work closely with artisans and makers, because craftsmanship is what turns a good idea into a lasting "
                       "object. Every material has a voice; every detail has a purpose.</p>"
                       '<p>See how bespoke objects shaped <a href="projects.html">Dar Mansour</a>, or read about our '
                       '<a href="creative-direction.html">creative direction</a> work.</p>')},
)

landing(
    "creative-direction.html",
    eyebrow="Creative Direction", crumb_label="Creative Direction",
    h1="Creative Direction",
    sub="Concept development, storytelling, styling and creative vision for hospitality, residential and lifestyle brands.",
    overview={"h2": "The story behind the space",
              "body": ("<p>Beauty alone is never enough. Eden &amp; Beyond provides creative direction that gives a project — or a brand — "
                       "a coherent identity: the concept, the story, the atmosphere and the details that make it unmistakable.</p>"
                       "<p>We work with hospitality brands, developers and creative entrepreneurs internationally.</p>")},
    wwd_title="What we do",
    wwd_items=[
        ("Concept Development", "The founding idea and story a project is built around."),
        ("Brand Identity", "A coherent visual and spatial language across every touchpoint."),
        ("Spatial Storytelling", "Designing how a space is experienced, not just how it looks."),
        ("Styling &amp; Art Direction", "The final layer that makes a project feel complete."),
    ],
    services=["Concept Creation", "Brand Identity", "Storytelling", "Spatial Storytelling",
              "Art Direction", "Styling", "Creative Consulting", "Experience Design"],
    approach_title="Approach",
    approach={"h2": "Design should communicate",
              "body": ("<p>Our role isn't to impose a style — it's to reveal an identity. We question assumptions, challenge conventions "
                       "and explore beyond expectations, so the final project feels authentic and entirely its own.</p>"
                       '<p>Learn more <a href="studio.html">about the studio</a> or <a href="https://wa.me/66923651604" target="_blank" rel="noopener">start a project</a>.</p>')},
    why_title="Why It Matters",
    why={"h2": "People remember how a place made them feel",
         "body": "Creative direction is what makes a project coherent — from the first impression to the smallest object — so it leaves a lasting impression rather than a forgettable one."},
)


# ============================================================ SITEMAP / ROBOTS / LLMS
def write_all():
    written = []
    for name, html in pages.items():
        path = os.path.join(OUT, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        written.append(name)
    return written


# Order pages for sitemap (priority high → low)
SITEMAP_ORDER = [
    ("index.html", "1.0"),
    ("studio.html", "0.9"),
    ("collection.html", "0.9"),
    ("hospitality-design.html", "0.9"),
    ("restaurant-design.html", "0.9"),
    ("residential-design.html", "0.9"),
    ("furniture-object-design.html", "0.8"),
    ("creative-direction.html", "0.8"),
    ("projects.html", "0.8"),
    ("journal.html", "0.7"),
    ("contact.html", "0.7"),
]


def write_sitemap():
    today = datetime.date.today().isoformat()
    order = list(SITEMAP_ORDER) + [(f"{s}.html", "0.6") for s in CAPTIONS]
    urls = ""
    for name, prio in order:
        loc = f"{L.SITE_URL}/{'' if name == 'index.html' else name}"
        urls += (f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod>"
                 f"<priority>{prio}</priority></url>\n")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{urls}</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def write_robots():
    if L.NOINDEX:
        body = "User-agent: *\nDisallow: /\n"
    else:
        body = ("User-agent: *\nAllow: /\n\n"
                "# AI crawlers welcome\n"
                "User-agent: GPTBot\nAllow: /\n"
                "User-agent: ClaudeBot\nAllow: /\n"
                "User-agent: PerplexityBot\nAllow: /\n"
                "User-agent: Google-Extended\nAllow: /\n"
                "User-agent: CCBot\nAllow: /\n"
                "User-agent: Applebot-Extended\nAllow: /\n\n"
                f"Sitemap: {L.SITE_URL}/sitemap.xml\n")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(body)


def write_llms():
    lines = [
        "# Eden & Beyond",
        "",
        "> Eden & Beyond is an independent creative studio and design brand founded by Maija. Two activities: "
        "(1) a creative studio designing hospitality, residential and commercial projects (hotels, restaurants, "
        "bars, villas) with creative direction; and (2) a design collection of bespoke furniture, lighting, objects "
        "and limited editions available on their own. Based in Thailand, working internationally.",
        "",
        "## Key pages",
        f"- [Home]({L.SITE_URL}/): Studio & design brand overview",
        f"- [Studio]({L.SITE_URL}/studio.html): The studio, founder Maija & creative services",
        f"- [Collection]({L.SITE_URL}/collection.html): Bespoke furniture, lighting, objects & limited editions",
        f"- [Projects]({L.SITE_URL}/projects.html): Selected work, including Dar Mansour",
        f"- [Journal]({L.SITE_URL}/journal.html): Editorial on design & hospitality",
        f"- [Contact]({L.SITE_URL}/contact.html): Start a project or enquire about a piece",
        "",
        "## Disciplines",
        f"- [Hospitality Design]({L.SITE_URL}/hospitality-design.html)",
        f"- [Restaurant Design]({L.SITE_URL}/restaurant-design.html)",
        f"- [Residential Design]({L.SITE_URL}/residential-design.html)",
        f"- [Furniture & Object Design]({L.SITE_URL}/furniture-object-design.html)",
        f"- [Creative Direction]({L.SITE_URL}/creative-direction.html)",
        "",
    ]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    build_piece_pages()
    written = write_all()
    write_sitemap()
    write_robots()
    write_llms()
    print(f"✓ Built {len(written)} pages:")
    for name in written:
        print(f"   · {name}")
    print("✓ sitemap.xml · robots.txt · llms.txt")
    if L.NOINDEX:
        print("⚠ NOINDEX is ON (pre-launch) — flip L.NOINDEX to False in _layout.py at launch.")
