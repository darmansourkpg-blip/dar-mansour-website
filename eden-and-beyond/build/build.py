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


def feat_tile(page, img_slug, title, rnd=False, meta="Table · One-of-a-kind", href=None):
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
    sub=("Collectible tables, lighting, artworks and dressed walls — one-of-a-kind and limited editions.<br>"
         "Creative direction and design for hospitality, residential and commercial projects."),
    actions_html=(
        f'<a class="btn btn--primary" href="collection.html">Explore the Collection</a>'
        '<a class="btn btn--light" href="studio.html">Meet the Studio</a>'),
    media_class=_home_hero_cls,
    media_html=_home_hero_media,
)}

<div class="trust"><div class="wrap trust__inner">
  <span class="trust__item"><strong>Tables</strong></span>
  <span class="trust__item"><strong>Lighting</strong></span>
  <span class="trust__item"><strong>Artworks</strong></span>
  <span class="trust__item"><strong>Dressed Walls</strong></span>
</div></div>

<section class="section"><div class="wrap">
  <div class="split" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow eyebrow--red">The Collection</span>
      <h2 style="margin:1rem 0 1.2rem;">Some ideas become spaces.<br>Others become objects.</h2>
      <p class="lead">Each piece is one-of-a-kind or part of a limited edition — transforming familiar forms into
      something unexpected, with character, contradiction and a life of their own.</p>
      <p style="margin-top:1rem;">Discover the collection, or commission a piece created for you.</p>
      <a class="btn btn--primary" href="collection.html" style="margin-top:1.6rem;">Explore the Collection {A}</a>
    </div>
    <div class="split__media reveal" data-delay="1">
      <a href="poppy-hobb.html">{('<img src="'+find_img('poppy-queen')+'" alt="Poppy Hobb — limited-edition table by Maija">') if find_img('poppy-queen') else ph('Poppy Hobb — table')}</a>
      <span class="tag">Poppy Hobb · Limited-edition table</span>
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
    {feat_tile('mouna-lisa', 'mona-lisa-fez', 'Mouna Lisa', rnd=True)}
    {feat_tile('and-man-created-atay', 'creation-of-mint-tea', 'And Man Created Atay', rnd=True)}
    {feat_tile('babouche', 'babouche-mandala', 'Babouche')}
    {feat_tile('kenza', 'kenza', 'Kenza', meta='Lighting · One-of-a-kind')}
    {feat_tile('', 'fountain-wall', 'Fountain Wall', meta='Dressed wall', href='collection.html#walls')}
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
        <p>One-of-a-kind and limited-edition tables, lighting, artworks and dressed walls. Created to stand on their own. Made to be lived with.</p>
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
      <h3>Bespoke Furniture &amp; Pieces</h3>
      <p>Made for a particular place, person or purpose.</p>
      <span class="disc-lite__tags">Furniture · Lighting · Artworks · Site-Specific Pieces</span>
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
    <div style="margin-top:1.8rem;"><a class="btn btn--light" href="projects.html">View the Project {A}</a></div>
  </div>
</section>

<section class="section"><div class="wrap manifesto reveal">
  <span class="eyebrow" style="display:block;text-align:center;margin-bottom:1.4rem;">Our Philosophy</span>
  <p>Every object has a <span class="em">soul</span>.</p>
  <p class="lead" style="max-width:56ch;margin:1.6rem auto 0;text-align:center;">We don't believe in signature styles — we believe
  in revealing identities. In creating pieces with character, presence and a life of their own.</p>
  <p style="max-width:56ch;margin:1rem auto 0;text-align:center;font-style:italic;color:var(--ink-soft);">Because beauty was never meant to behave.</p>
</div></section>

<section class="section book"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow eyebrow--red">Two ways in</span>
  <h2>One piece.<br>Or a whole new world.</h2>
  <div class="book__actions" style="justify-content:center;">
    <a class="btn btn--primary" href="collection.html">Explore the Collection {A}</a>
    <a class="btn btn--ghost" href="{L.wa('Hi Eden &amp; Beyond, I would like to talk about a project.')}" target="_blank" rel="noopener">{L.WA_ICON} Start a Project</a>
  </div>
</div></section>
'''

pages["index.html"] = L.page(
    title="Eden & Beyond | Creative Studio & Collectible Design · Thailand",
    desc=("Eden & Beyond is a creative studio and collectible design brand in Koh Phangan, Thailand, creating "
          "distinctive spaces, tables, lighting, artworks and dressed walls."),
    canonical="index.html",
    body=home_body,
)


# ============================================================ STUDIO (was About + Services)
_studio_wa = L.wa("Hi Eden &amp; Beyond, I would like to talk about a project.")
about_body = f'''
{L.subhero(
    eyebrow="The Studio",
    h1="We don't follow trends.<br>We create stories.",
    sub=("Eden & Beyond is an independent creative studio based in Koh Phangan, Thailand, creating distinctive "
         "spaces and bespoke pieces for hospitality, residential and commercial projects."),
)}

<section class="section"><div class="wrap wrap--narrow center reveal">
  <p class="lead">No signature style. No ready-made formula.<br>Every project begins with its own identity.</p>
  <div style="margin-top:1.8rem;"><a class="btn btn--primary" href="{_studio_wa}" target="_blank" rel="noopener">{L.WA_ICON} Start a Project</a></div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="split" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow">Our Approach</span>
      <h2>Start with the story.<br>Not the style.</h2>
      <p class="lead">We don't begin by deciding what a project should look like. We begin with the people, the place,
      the culture and the story behind it.</p>
      <p style="margin-top:1.1rem;">Then we build a world around them — from the atmosphere and spatial identity to
      furniture, lighting, artworks and the details that make it impossible to confuse with somewhere else.</p>
    </div>
    <div class="split__media reveal" data-delay="1">{ph('Studio / Maija at work', 'ph--dark')}<span class="tag">The Studio</span></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:660px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow">What We Do</span>
    <h2 style="margin-top:1rem;">Different briefs.<br>Same refusal to be ordinary.</h2>
  </div>
  <div class="disc-lite">
    <a class="disc-lite__item reveal" href="hospitality-design.html">
      <h3>Hospitality</h3><p>Places people remember.</p>
      <span class="disc-lite__tags">Hotels · Restaurants · Bars · Beach Clubs · Cafés · Wellness</span>
      <span class="disc-lite__more">Explore Hospitality {A}</span></a>
    <a class="disc-lite__item reveal" data-delay="1" href="residential-design.html">
      <h3>Residential</h3><p>Homes with a point of view.</p>
      <span class="disc-lite__tags">Private Villas · Residences · Holiday Homes</span>
      <span class="disc-lite__more">Explore Residential {A}</span></a>
    <a class="disc-lite__item reveal" data-delay="2" href="furniture-object-design.html">
      <h3>Bespoke Furniture &amp; Pieces</h3><p>Made for a particular place, person or purpose.</p>
      <span class="disc-lite__tags">Furniture · Lighting · Artworks · Site-Specific Pieces</span>
      <span class="disc-lite__more">Explore {A}</span></a>
    <a class="disc-lite__item reveal" data-delay="3" href="creative-direction.html">
      <h3>Creative Direction</h3><p>The idea behind everything.</p>
      <span class="disc-lite__tags">Concept · Storytelling · Brand Identity · Art Direction · Styling</span>
      <span class="disc-lite__more">Explore {A}</span></a>
  </div>
</div></section>

<section class="feat">{ph('Dar Mansour — Koh Phangan (selected project)', 'ph--dark')}
  <div class="wrap feat__inner reveal">
    <span class="eyebrow">Selected Project</span>
    <h2>Dar Mansour</h2>
    <p class="feat__place">One place. A complete world.</p>
    <p>For Dar Mansour in Koh Phangan, Eden &amp; Beyond shaped the creative world of the restaurant across interiors,
    furniture, lighting, dressed walls, artworks and atmosphere — a project where every element belongs to the same story.</p>
    <div style="margin-top:1.8rem;"><a class="btn btn--light" href="projects.html">Discover Dar Mansour {A}</a></div>
  </div>
</section>

<section class="section"><div class="wrap">
  <div class="split split--reverse" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow eyebrow--red">Behind Eden &amp; Beyond</span>
      <h2 style="margin:1rem 0 .4rem;">Maïja Disseau</h2>
      <p class="feat__place" style="margin-bottom:1.2rem;">Founder &amp; Creative Troublemaker</p>
      <p>Born in Italy to French parents, shaped by more than thirty years in Morocco and now creating from Thailand,
      Maïja has spent her life moving between cultures, languages and ways of seeing.</p>
      <p style="margin-top:1rem;">Before Eden &amp; Beyond, twelve years as a psychotherapist, hypnotherapist and family
      constellation practitioner taught her to look beyond appearances — at character, symbols and what often remains unspoken.</p>
      <p style="margin-top:1rem;">Today, she translates that instinct into spaces, furniture, lighting, artworks and walls.</p>
      <p class="lead" style="font-style:italic;margin-top:1.2rem;">&ldquo;I don't create objects for people. I reveal people through objects.&rdquo;</p>
      <div style="margin-top:1.6rem;"><a class="btn btn--ghost" href="about-maija.html">Discover Maïja's Story {A}</a></div>
    </div>
    <div class="split__media reveal" data-delay="1">
      {('<img src="'+find_img('maija')+'" alt="Maïja Disseau, founder of Eden &amp; Beyond">') if find_img('maija') else ph('Portrait — Maïja')}
      <span class="tag">Maïja · Founder</span>
    </div>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;margin-bottom:clamp(2.5rem,6vw,3.5rem);">
    <span class="eyebrow">How We Work</span>
    <h2 style="margin-top:1rem;">No formula.<br>But there is a process.</h2>
  </div>
  <div class="steps">
    <div class="step reveal"><span class="step__num">01</span><h3>Discover</h3><p>We listen, observe and understand the people, place and ambition behind the project.</p></div>
    <div class="step reveal" data-delay="1"><span class="step__num">02</span><h3>Imagine</h3><p>We shape the concept, creative direction and world the project will inhabit.</p></div>
    <div class="step reveal" data-delay="2"><span class="step__num">03</span><h3>Create</h3><p>Space, furniture, lighting, artworks and details begin to take form.</p></div>
    <div class="step reveal" data-delay="3"><span class="step__num">04</span><h3>Bring It to Life</h3><p>We work across disciplines to keep the original idea alive through every detail.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;">
    <span class="eyebrow">Who We Work With</span>
    <h2 style="margin:1rem 0 1.6rem;">Visionaries with a story to tell</h2>
    <ul class="tags reveal">
      <li>Hotels</li><li>Restaurants</li><li>Bars</li><li>Developers</li>
      <li>Private Villas</li><li>Residences</li><li>Independent Brands</li>
    </ul>
    <p style="margin-top:1.4rem;color:var(--muted);">Thailand &amp; international projects.</p>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="split" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow eyebrow--red">The Collection</span>
      <h2 style="margin:1rem 0 1.2rem;">Not every idea<br>needs a whole project.</h2>
      <p class="lead">Discover one-of-a-kind and limited-edition tables, lighting, artworks and dressed walls —
      available independently from our studio projects.</p>
      <a class="btn btn--light" href="collection.html" style="margin-top:1.6rem;">Explore the Collection {A}</a>
    </div>
    <div class="split__media reveal" data-delay="1">{('<img src="'+find_img('mona-lisa-fez')+'" alt="Mouna Lisa — collectible table by Eden &amp; Beyond">') if find_img('mona-lisa-fez') else ph('The Collection', 'ph--teal')}<span class="tag">The Collection</span></div>
  </div>
</div></section>

<section class="section book"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">Have a project in mind?</span>
  <h2>Bring us the idea.<br>We'll take it beyond.</h2>
  <div class="book__actions" style="justify-content:center;">
    <a class="btn btn--primary" href="{_studio_wa}" target="_blank" rel="noopener">{L.WA_ICON} Start a Project</a>
  </div>
</div></section>
'''
pages["studio.html"] = L.page(
    title="Creative Design Studio Thailand | Eden & Beyond",
    desc=("Eden & Beyond is an independent creative studio in Koh Phangan, Thailand, creating hospitality, "
          "residential and commercial spaces, bespoke furniture, lighting and artworks."),
    canonical="studio.html",
    body=about_body,
)


# ============================================================ ABOUT · MAÏJA
_about_wa = L.wa("Hi Eden &amp; Beyond, I found you through Maïja's story and would love to talk.")
maija_body = f'''
{L.subhero(
    eyebrow="Behind Eden & Beyond",
    h1="Maïja Disseau",
    sub="Founder &amp; Creative Troublemaker · Eden &amp; Beyond",
)}

<section class="section"><div class="wrap wrap--narrow prose reveal">
  <p class="lead" style="font-style:italic;">&ldquo;I don't create objects for people. I reveal people through objects.&rdquo;</p>
  <p>I have always been a creator — but I spent much of my life following conventional paths rather than acting on it.
  There is a world inside me that has never been fully revealed, one that has relentlessly knocked at the door of my mind,
  asking to be released and allowed to exist. Eden &amp; Beyond is the key to that door.</p>
  <p>I create furniture and lighting, transform familiar forms and dress walls — through one-of-a-kind pieces and limited
  editions. Using paper, paint, stencils and layered collage, I take familiar forms and let them reveal the invisible life
  they carry within.</p>
  <p>For commissioned pieces, the process becomes deeply personal. I don't simply design something for someone. I observe,
  sense and interpret what lives beneath the surface — then reveal it through the piece. Each creation becomes a mirror:
  not a literal portrait, but a material expression of the person who inspired it.</p>

  <h3>Before objects, the invisible</h3>
  <p>Before working with objects, I spent twelve years exploring the invisible dimensions of human beings — as a
  psychotherapist, hypnotherapist and family constellation practitioner. That exploration of the unconscious, of symbols,
  hidden loyalties and unseen energies, still inhabits everything I create. The language has changed. The intention has not.</p>

  <h3>Several worlds, on purpose</h3>
  <p>Born in Italy to French parents, raised within the Montessori system, shaped by thirty years in Morocco and now living
  in Thailand, I carry several worlds — and several languages — within me. I am not interested in choosing between them, or
  in making them behave. I let them collide, spark and come alive.</p>

  <h3>Where the name came from</h3>
  <p>Eden &amp; Beyond was born from <em>Eden</em>, Koh Phangan's iconic dance floor — the place that first made me want to
  live on this island. <em>Beyond</em> stands for everything that came after, and for the infinite possibilities that begin
  when we stop accepting the limits handed to us.</p>
  <p>I have no interest in conventional good taste. I am interested in character, contradiction, instinct and life. Some
  pieces are created freely; others are commissioned for private spaces, restaurants and hotels — places that refuse to look
  like anywhere else. All are made to provoke something: curiosity, desire, recognition, discomfort, fascination —
  sometimes all at once.</p>

  <blockquote>F*** the Box is my manifesto, my philosophy of life. Because the Box was never the problem — believing we had to live inside it was.</blockquote>
</div></section>

<section class="section book"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow eyebrow--red">Work with Maïja</span>
  <h2>Own a piece,<br>or commission a project.</h2>
  <div class="book__actions" style="justify-content:center;">
    <a class="btn btn--primary" href="collection.html">Explore the Collection {A}</a>
    <a class="btn btn--ghost" href="{_about_wa}" target="_blank" rel="noopener">{L.WA_ICON} Start a Conversation</a>
  </div>
</div></section>
'''
pages["about-maija.html"] = L.page(
    title="Maïja Disseau — Founder | Eden & Beyond",
    desc=("Maïja Disseau is the founder and creative director of Eden & Beyond in Koh Phangan, Thailand — artist and "
          "designer of collectible tables, lighting, artworks and dressed walls, and former psychotherapist."),
    canonical="about-maija.html",
    body=maija_body,
    extra_head=L.person_maija_schema(),
)


# ============================================================ PROJECTS
def _chapter(num, kicker, title_html, body, media):
    return f'''<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="split{' split--reverse' if int(num)%2==0 else ''}" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow eyebrow--red">{num} · {kicker}</span>
      <h2 style="margin:.7rem 0 1rem;">{title_html}</h2>
      <p class="lead">{body}</p>
    </div>
    <div class="split__media reveal" data-delay="1">{media}</div>
  </div>
</div></section>'''


_pt_tables = "".join(
    feat_tile(s, img, t, rnd=r) for s, img, t, r in [
        ("poppy-hobb", "poppy-queen", "Poppy Hobb", True),
        ("mouna-lisa", "mona-lisa-fez", "Mouna Lisa", True),
        ("and-man-created-atay", "creation-of-mint-tea", "And Man Created Atay", True)])
_pt_walls = ((f'<img src="{find_img("fountain-wall")}" alt="Dressed wall at Dar Mansour by Eden &amp; Beyond">')
             if find_img("fountain-wall") else ph("Dressed wall — Dar Mansour"))
projects_body = f'''
{L.breadcrumb(("Projects", None))}
{L.subhero(
    eyebrow="Projects",
    h1="One remarkable project<br>says more than a hundred ordinary ones.",
    sub="We don't measure our work by how many projects fill a portfolio. We care about how deeply an idea can be carried — through a space, its furniture, lighting, walls, art and atmosphere.",
)}

<section class="feat" style="min-height:72vh;">{ph('Dar Mansour — Koh Phangan', 'ph--dark')}
  <div class="wrap feat__inner reveal">
    <span class="eyebrow">01 · Restaurant · Koh Phangan, Thailand</span>
    <h2>Dar Mansour</h2>
    <p class="feat__place">A little Morocco. Without pretending to be Morocco.</p>
    <p>Dar Mansour began with a question: how do you create a restaurant rooted in Morocco, on a tropical island in
    Thailand, without turning either place into a cliché? The answer wasn't to reproduce Morocco. It was to interpret it.</p>
  </div>
</section>

<section class="section"><div class="wrap wrap--narrow prose reveal">
  <span class="eyebrow">The Brief</span>
  <h2 style="margin:.6rem 0 1rem;">Create somewhere that couldn't exist anywhere else.</h2>
  <p>Dar Mansour was conceived as an intimate Moroccan restaurant in Koh Phangan — warm, generous, unexpected and deeply
  connected to the culture behind its food. The creative challenge was to bring that identity into the space without
  reproducing a traditional Moroccan interior.</p>
</div></section>

<section class="section band-dark" style="padding-block:clamp(3rem,7vw,5rem);"><div class="wrap wrap--narrow prose reveal">
  <span class="eyebrow">The Idea</span>
  <h2 style="margin:.6rem 0 1rem;">Not Morocco recreated.<br>Morocco remembered.</h2>
  <p style="color:var(--on-dark-soft);">References to Morocco appear throughout the restaurant, but rarely in the way you
  expect them to. Colours, patterns, familiar forms, found references and cultural fragments are taken apart, reinterpreted
  and allowed to become something new in Thailand.</p>
  <p style="color:var(--on-dark-soft);">The result belongs to neither place entirely. It belongs to Dar Mansour.</p>
</div></section>

<section class="section"><div class="wrap center reveal" style="margin-bottom:.5rem;">
  <span class="eyebrow">The Complete World</span>
  <h2 style="margin-top:1rem;">One idea. Every detail.</h2>
</div></section>

{_chapter("01", "The Space", "An intimate world", "Built around warmth, colour, conversation and the ritual of sharing food.", ph('Dar Mansour — the space', 'ph--dark'))}
<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="reveal" style="margin-bottom:1.4rem;"><span class="eyebrow eyebrow--red">02 · The Tables</span>
  <h2 style="margin:.7rem 0 .4rem;">Not furniture added to the restaurant.</h2>
  <p class="lead">Pieces of the restaurant itself — several now live beyond it, in the Collection.</p></div>
  <div class="artgrid">{_pt_tables}</div>
</div></section>
{_chapter("03", "The Lighting", "When the sun goes down,<br>the restaurant becomes another place.", "Light does as much as any wall — turning the room into somewhere else after dark.", ph('Dar Mansour — lighting at night', 'ph--dark'))}
{_chapter("04", "The Walls", "The architecture ends.<br>The story keeps going.", "Dressed walls carry the identity onto the surfaces themselves.", _pt_walls)}
{_chapter("05", "The Art", "Not decoration.<br>Part of the conversation.", "Artworks belong to the same world as the food and the room.", ph('Dar Mansour — artworks', 'ph--dark'))}
{_chapter("06", "The Details", "The things you notice.<br>And the things you only feel.", "Objects, materials and small gestures that make the room impossible to confuse with anywhere else.", ph('Dar Mansour — details', 'ph--dark'))}

<section class="section band-dark"><div class="wrap">
  <div class="split" style="align-items:start;gap:clamp(2rem,5vw,4rem);">
    <div class="reveal">
      <span class="eyebrow">Project</span>
      <h2 style="margin:.6rem 0 1.4rem;">Dar Mansour — Morocco's Kitchen</h2>
      <dl class="piece-specs" style="border-color:rgba(244,239,230,.18);">
        <div style="border-color:rgba(244,239,230,.18);"><dt>Location</dt><dd style="color:var(--on-dark);">Koh Phangan, Thailand</dd></div>
        <div style="border-color:rgba(244,239,230,.18);"><dt>Type</dt><dd style="color:var(--on-dark);">Restaurant</dd></div>
        <div style="border-color:rgba(244,239,230,.18);"><dt>Status</dt><dd style="color:var(--on-dark);">Completed</dd></div>
        <div style="border-color:rgba(244,239,230,.18);"><dt>Website</dt><dd style="color:var(--on-dark);"><a href="https://darmansour.com" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline;">darmansour.com</a></dd></div>
      </dl>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Eden &amp; Beyond Scope</span>
      <ul class="tags" style="justify-content:flex-start;margin-top:1rem;">
        <li>Creative Direction</li><li>Interior &amp; Spatial Design</li><li>Furniture</li>
        <li>Lighting</li><li>Artworks</li><li>Dressed Walls</li><li>Styling &amp; Atmosphere</li>
      </ul>
      <p style="margin-top:1.2rem;color:var(--on-dark-soft);font-size:.9rem;">Full project credits available on request.</p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow eyebrow--red">From the Restaurant to the Collection</span>
    <h2 style="margin-top:1rem;">Some pieces live<br>beyond the restaurant.</h2>
    <p class="lead" style="margin-inline:auto;">Discover tables, lighting and artworks from the Eden &amp; Beyond Collection.</p>
  </div>
  <div class="artgrid">{_pt_tables}</div>
  <div class="center reveal" style="margin-top:2.6rem;"><a class="btn btn--primary" href="collection.html">Explore the Collection {A}</a></div>
</div></section>

<section class="section band-dark"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">Every place deserves its own world</span>
  <h2 style="margin-top:1rem;">The next project<br>shouldn't look like it.</h2>
  <p class="lead" style="margin-inline:auto;color:var(--on-dark-soft);">Dar Mansour looks like Dar Mansour because its story belongs to Dar Mansour. That's the point — we don't bring a signature style to the next one.</p>
</div></section>

{L.cta_band(
    title="What should the next one be?",
    text="Bring us the ambition. We'll build the world around it.",
    eyebrow="Start a Project", btn_label="Start a Project",
)}
'''
pages["projects.html"] = L.page(
    title="Dar Mansour Restaurant Design | Eden & Beyond Thailand",
    desc=("Discover Eden & Beyond's creative direction and design for Dar Mansour, a Moroccan restaurant in Koh Phangan, "
          "Thailand — from interiors to furniture, lighting, art and dressed walls."),
    canonical="projects.html",
    body=projects_body,
    extra_head=L.project_schema(
        "Dar Mansour — Morocco's Kitchen",
        "Creative direction and design by Eden & Beyond for Dar Mansour, a Moroccan restaurant in Koh Phangan, Thailand — interiors, furniture, lighting, artworks and dressed walls.",
        "https://darmansour.com",
        "Koh Phangan, Thailand"),
)


# ============================================================ JOURNAL
_journal_soon = [
    ("Hospitality", "Why the restaurants we remember are never just about the food"),
    ("Places &amp; Culture", "Morocco was never beige"),
    ("Behind the Work", "I have no interest in good taste"),
    ("Objects &amp; Art", "Why we surround ourselves with the things we do"),
    ("Design", "Not Morocco recreated. Morocco remembered — the story behind Dar Mansour"),
    ("Places &amp; Culture", "What an island teaches you about space"),
]
_soon_html = "".join(
    f'<li class="jsoon reveal"><span class="jsoon__cat">{c}</span><span class="jsoon__title">{t}</span></li>'
    for c, t in _journal_soon)
journal_body = f'''
{L.breadcrumb(("Journal", None))}
{L.subhero(
    eyebrow="Journal",
    h1="Ideas, places,<br>people &amp; beautiful trouble.",
    sub="Stories and perspectives on design, art, hospitality, culture and the things that inspire Eden & Beyond.",
)}

<section class="section"><div class="wrap wrap--narrow center reveal">
  <h2 style="margin-bottom:1rem;">Not everything belongs<br>in a portfolio.</h2>
  <p class="lead">Some things deserve a conversation. The Journal is where Eden &amp; Beyond thinks out loud — about design,
  Morocco, Thailand, objects, art and the ideas behind the work.</p>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap wrap--narrow center reveal">
  <p style="font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);">
  Design · Hospitality · Objects &amp; Art · Places &amp; Culture · Behind the Work</p>
</div></section>

<section class="section band-dark"><div class="wrap wrap--narrow reveal">
  <div class="center" style="margin-bottom:clamp(2rem,5vw,3rem);">
    <span class="eyebrow eyebrow--red">In the works</span>
    <h2 style="margin-top:1rem;">The first stories<br>are being written.</h2>
  </div>
  <ul class="jsoon-list">{_soon_html}</ul>
  <p class="center" style="margin-top:2rem;color:var(--on-dark-soft);">Quality over cadence — a few strong stories, not filler.</p>
</div></section>

{L.cta_band(
    title="While the first stories take shape,",
    text="explore the pieces and the project that started it all.",
    eyebrow="Meanwhile", btn_label="Start a Project",
)}
'''
pages["journal.html"] = L.page(
    title="Design, Art & Hospitality Journal | Eden & Beyond",
    desc=("The Eden & Beyond Journal explores design, art, hospitality, culture, Morocco, Thailand and the ideas "
          "behind spaces and pieces with character."),
    canonical="journal.html",
    body=journal_body,
)


# ============================================================ CONTACT
_c_project = L.wa("Hi Eden &amp; Beyond, I would like to start a project. Here is what I'm working on:")
_c_commission = L.wa("Hi Eden &amp; Beyond, I would like to commission a piece. Here is what I have in mind:")
contact_body = f'''
{L.breadcrumb(("Contact", None))}
{L.subhero(
    eyebrow="Contact",
    h1="Let's make something<br>worth remembering.",
    sub="A space. A piece. An idea that hasn't quite found its form yet. Tell us where you'd like to begin.",
)}

<section class="section"><div class="wrap">
  <div class="duo">
    <div class="duo__card reveal">
      <div class="duo__body">
        <span class="eyebrow">01 — A Project</span>
        <h3>Start a Project</h3>
        <p>Restaurant, hotel, villa, commercial space or creative direction. Tell us what you're working on.</p>
        <a class="btn btn--light" href="{_c_project}" target="_blank" rel="noopener">{L.WA_ICON} Start a Project</a>
      </div>
    </div>
    <div class="duo__card duo__card--red reveal" data-delay="1">
      <div class="duo__body">
        <span class="eyebrow">02 — A Piece</span>
        <h3>Commission a Piece</h3>
        <p>A table, light, artwork, dressed wall or something created specifically for you or your space.</p>
        <a class="btn btn--light" href="{_c_commission}" target="_blank" rel="noopener">{L.WA_ICON} Commission a Piece</a>
      </div>
    </div>
  </div>
  <div class="center reveal" style="margin-top:2.2rem;">
    <p style="color:var(--muted);">Looking for a piece you've already seen? <a class="ilink" href="collection.html">Explore the Collection {A}</a></p>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="contact-grid">
    <div class="contact-info reveal">
      <span class="eyebrow">Direct</span>
      <h2 style="margin:1rem 0 1.4rem;color:#fff;">Prefer to talk?</h2>
      <p style="margin-bottom:2rem;color:var(--on-dark-soft);">WhatsApp is the fastest way to reach the studio — it opens with a message ready to send. For a fuller brief, email works too.</p>
      <dl style="color:var(--on-dark);">
        <div><dt>WhatsApp</dt><dd><a href="{L.wa('Hi Eden &amp; Beyond, I found you through your website and would love to talk.')}" target="_blank" rel="noopener" style="color:#fff;">{L.WHATSAPP_DISPLAY}</a><span class="contact-note" style="color:var(--on-dark-soft);">Maïja — the fastest response.</span></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{L.EMAIL}" style="color:#fff;">{L.EMAIL}</a></dd></div>
        <div><dt>Instagram</dt><dd><a href="{L.INSTAGRAM}" target="_blank" rel="noopener" style="color:#fff;">{L.INSTAGRAM_HANDLE}</a></dd></div>
      </dl>
    </div>
    <div class="contact-info reveal" data-delay="1">
      <span class="eyebrow">Studio</span>
      <h2 style="margin:1rem 0 1.4rem;color:#fff;">Based on an island.<br>Not limited by it.</h2>
      <p style="color:var(--on-dark-soft);">Eden &amp; Beyond is based in Koh Phangan, Thailand, and works with private and professional clients in Thailand and internationally.</p>
      <p style="margin-top:1.2rem;color:var(--on-dark-soft);">Meetings and viewings are available by appointment. International enquiries welcome — feasibility, shipping and installation are discussed individually.</p>
    </div>
  </div>
</div></section>
'''
pages["contact.html"] = L.page(
    title="Contact Eden & Beyond | Creative Studio Thailand",
    desc=("Contact Eden & Beyond in Koh Phangan, Thailand, for hospitality, residential and commercial design projects "
          "or bespoke furniture, lighting and art commissions."),
    canonical="contact.html",
    body=contact_body,
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
     "Not just somewhere to put things.", [
        # Maija's collection order (1–16). Slug = its own page when a caption exists,
        # otherwise the tile opens a WhatsApp enquiry. img = webp file stem in assets/img/.
        ("saint-exupery",       "Saint-Exupéry",         "Table · One-of-a-kind", "",           "ph--teal",     "saint-exupery-camel"),
        ("qaftan",              "Qaftan",                "Table · One-of-a-kind", "",           "ph--sun",      "qaftan-silk-drape"),
        ("chaouen",             "Chaouen",               "Table · One-of-a-kind", "",           "ph--electric", "chefchaouen-framed"),
        ("tanja",               "Tanja",                 "Table · One-of-a-kind", "",           "ph--teal",     "tanja-calligraphy"),
        ("and-man-created-atay","And Man Created Atay",  "Table · One-of-a-kind", "art--round", "ph--teal",     "creation-of-mint-tea"),
        ("ysl",                 "YSL",                   "Table · One-of-a-kind", "",           "ph--teal",     "rue-yves-saint-laurent"),
        ("zaynab",              "Zaynab",                "Table · One-of-a-kind", "",           "ph--sun",      "zaynab-jewels"),
        ("tiziri",              "Tiziri",                "Table · One-of-a-kind", "",           "ph--magenta",  "tiziri-portrait"),
        ("al-kass-hlou",        "Al Kass Hlou",          "Table · One-of-a-kind", "art--round", "ph--sun",      "teapot-camel"),
        ("flash",               "Flash",                 "Table · One-of-a-kind", "",           "ph--electric", "wondermint-camel"),
        ("babouche",            "Babouche",              "Table · One-of-a-kind", "",           "ph--magenta",  "babouche-mandala"),
        ("qif",                 "Qif",                   "Table · One-of-a-kind", "",           "ph--electric", "qif-stop-sign"),
        ("qif-in-the-oasis",    "Qif in the Oasis",      "Table · One-of-a-kind", "",           "ph--magenta",  "desert-caravan-neon"),
        ("taxi-superlux",       "Taxi Superlux",         "Table · One-of-a-kind", "",           "ph--electric", "taxi-superlux"),
        ("poppy-hobb",          "Poppy Hobb",            "Table · One-of-a-kind", "",           "ph--poppy",    "poppy-queen"),
        ("mouna-lisa",          "Mouna Lisa",            "Table · One-of-a-kind", "art--round", "ph--teal",     "mona-lisa-fez"),
     ]),
    ("lighting", "Lighting",
     "Some stories look better after dark.", [
        ("kenza",  "Kenza",  "Lighting · One-of-a-kind",  "art--tall",  "ph--poppy"),
        ("kenzo",  "Kenzo",  "Lighting · One-of-a-kind",  "art--tall",  "ph--dark"),
     ]),
    ("artworks", "Artworks",
     "Some stories refuse to stay on the table.", []),
    ("walls", "Dressed Walls",
     "Because walls don't have to behave either.", [
        ("fountain-wall",  "Fountain Wall",  "Dressed wall · Site-specific", "",  "ph--dark"),
        ("entrance-wall",  "Entrance Wall",  "Dressed wall · Site-specific", "",  "ph--teal"),
        ("star-wall",      "Star Wall",      "Dressed wall · Site-specific", "",  "ph--sun"),
        ("floral-wall",    "Floral Wall",    "Dressed wall · Site-specific", "",  "ph--magenta"),
     ]),
]


# ---- Per-piece caption pages (Maija's texts, verbatim). Blank line = new stanza.
CAPTIONS = {
    "saint-exupery": dict(title="Saint-Exupéry", kicker="Table · One-of-a-kind", img="saint-exupery-camel", shape="",
        lead="Exotic. Cool. Expected. Or is it?", text="""Exotic.
Cool.
Expected.

Or is it?

Wrapped in colors, dressed in codes—
you think you know the story.
But look again.

Because style isn't a costume.
And identity isn't a trend.

It's worn.
Owned.
Rewritten."""),
    "chaouen": dict(title="Chaouen", kicker="Table · One-of-a-kind", img="chefchaouen-framed", shape="",
        lead="Put it in a frame… and suddenly it matters.", text="""Put it in a frame…
and suddenly it matters.

Gold edges. Perfect lines.
Now you're supposed to admire it.

But what really changed?
The view…
or the way you were told to see it?

Because value is often just a story.
And rules are just well-decorated limits."""),
    "and-man-created-atay": dict(title="And Man Created Atay", kicker="Table · One-of-a-kind", img="creation-of-mint-tea", shape="round",
        lead="An offering. Or a command.", text="""An offering.
Or a command.

Sweetness in one hand.
Freshness in the other.

Take it.
Or wait to be allowed.

A quiet game of control—
where desire isn't rushed,
it's held.
Stretched.

Because the most powerful exchanges
aren't given freely.

They're felt…
and surrendered to."""),
    "ysl": dict(title="YSL", kicker="Table · One-of-a-kind", img="rue-yves-saint-laurent", shape="",
        lead="Luxury had an address. A real one.", text="""Luxury had an address.
A real one.
Rue Yves Saint Laurent,
Marrakech.

But even icons who built their legacy
in gardens and walls…
don't get to own the story forever.

Because places evolve.
Meanings shift.

And what was once sacred
can be taken somewhere else entirely.

Not imitation.
A continuation—with attitude."""),
    "flash": dict(title="Flash", kicker="Table · One-of-a-kind", img="wondermint-camel", shape="",
        lead="Extra fresh. Extra cool. Extra… not what you think.", text="""Extra fresh.
Extra cool.
Extra… not what you think.

Minty perfection. Smooth attitude. Zero flaws.
That's the promise.

Reality?
A little weirder. A little louder.
A lot less obedient.

Because perfection is boring.
And boxes are meant to be chewed."""),
    "babouche": dict(title="Babouche", kicker="Table · One-of-a-kind", img="babouche-mandala", shape="",
        lead="Get closer. And then try to look away.", text="""Get closer.
And then try to look away.

A ritual of repetition.
Color. Pattern. Pulse.

What seems controlled… starts to move.
What looks playful… becomes obsessive.

This is where order turns into trance.
Where beauty loops until it takes over.

Not decoration.
A frequency."""),
    "qif-in-the-oasis": dict(title="Qif in the Oasis", kicker="Table · One-of-a-kind", img="desert-caravan-neon", shape="",
        lead="Move. Travel. Follow the line. And then — stop.", text="""Move.
Travel.
Follow the line.
And then—
stop.

A command in the middle of the journey.
A break in the flow.

But what if stopping…
is just another way of moving?

Between desert and signal,
tradition and interruption,
this piece plays with direction — and refuses to obey it."""),
    "poppy-hobb": dict(title="Poppy Hobb", kicker="Table · One-of-a-kind", img="poppy-queen", shape="",
        lead="She looks soft. She isn't.", text="""She looks soft.
She isn't.

Crowned in silence, wrapped in beauty —
but don't get too close.

This piece lives in the tension:
delicacy and danger,
ritual and rebellion,
a place where form becomes feeling.

Not just a table.
A presence."""),
    "mouna-lisa": dict(title="Mouna Lisa", kicker="Table · One-of-a-kind", img="mona-lisa-fez", shape="round",
        lead="Even icons get bored.", text="""Even icons get bored.

Perfect smile. Perfect pose.
Perfect… cage.

So what happens
when she decides to move?

A shift. A clash. A quiet rebellion.

Not ruined.
Reclaimed.

Because timeless doesn't mean untouchable.
And beauty was never meant to behave."""),
    "kenza": dict(title="Kenza", kicker="Lighting · One-of-a-kind", img="kenza", shape="tall",
        lead="Handle with care.", text="""Handle with care.

She is stitched together from old stories, other people's expectations, stamps of approval, souvenirs of who she was supposed to be.

Then she switched on.

And suddenly, all that remained… was her light."""),
    "kenzo": dict(title="Kenzo", kicker="Lighting · One-of-a-kind", img="kenzo", shape="tall",
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
        prv = order[(i - 1) % len(order)]
        nd = CAPTIONS[nxt]
        pd = CAPTIONS[prv]
        # Practical layer — factual fields Maija confirms later show "On request".
        edition = "One-of-a-kind" if "One-of-a-kind" in d["kicker"] else d["kicker"].split("·")[-1].strip()
        specs = [
            ("Dimensions", "On request"),
            ("Materials", "On request"),
            ("Technique", "Mixed media"),
            ("Edition", edition),
            ("Created", "Koh Phangan, Thailand"),
            ("Availability", "Available on enquiry"),
        ]
        specs_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in specs)
        pair = ('\n      <p class="piece__pair">Part of the Kenza &amp; Kenzo pair · '
                f'<a href="{("kenzo" if slug=="kenza" else "kenza")}.html">Discover '
                f'{("Kenzo" if slug=="kenza" else "Kenza")}</a></p>') if slug in ("kenza", "kenzo") else ""
        body = f'''
{L.breadcrumb(("Collection", "collection.html"), (d["title"], None))}
<section class="section" style="padding-top:1.4rem;"><div class="wrap">
  <div class="piece">
    <div class="{media_cls} reveal">{media}</div>
    <div class="piece__body reveal" data-delay="1">
      <span class="eyebrow eyebrow--red">{d["kicker"]}</span>
      <h1>{d["title"]}</h1>
      <div class="piece__caption">{_caption_html(d["text"])}</div>
      <p class="piece__sig">F<span class="fbox__stars">&#9733;&#9733;&#9733;</span> the Box</p>{pair}
      <div class="piece__actions">
        <a class="btn btn--primary" href="{_piece_wa(d["title"], d["kicker"])}" target="_blank" rel="noopener">{L.WA_ICON} Enquire about this piece</a>
        <a class="btn btn--ghost" href="collection.html">Back to the Collection</a>
      </div>
      <dl class="piece-specs">{specs_html}</dl>
    </div>
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="piece-nav">
    <a class="piece-nav__link piece-nav__prev reveal" href="{prv}.html">
      <span class="eyebrow eyebrow--red">Previous piece</span>
      <span class="piece-nav__row">{A}<span class="piece-nav__title">{pd["title"]}</span></span>
    </a>
    <a class="piece-nav__link piece-nav__next reveal" href="{nxt}.html">
      <span class="eyebrow eyebrow--red">Next piece</span>
      <span class="piece-nav__row"><span class="piece-nav__title">{nd["title"]}</span>{A}</span>
    </a>
  </div>
</div></section>
'''
        pages[f"{slug}.html"] = L.page(
            title=f'{d["title"]} — {d["kicker"]} | Eden & Beyond',
            desc=f'{d["title"]} by Maija, {d["kicker"].lower()} from the Eden & Beyond collection. {d["lead"]}',
            canonical=f"{slug}.html",
            body=body,
            body_class="page-collection page-piece",
        )


_wa_wall = L.wa("Hi Eden &amp; Beyond, I would like to commission a dressed wall for my space.")
_col_enquire = L.wa("Hi Eden &amp; Beyond, I would like to enquire about a piece from your collection "
                    "— availability, dimensions and price.")
_col_commission = L.wa("Hi Eden &amp; Beyond, I would like to commission my own piece.")


def collection_section(anchor, title, blurb, pieces):
    if pieces:
        grid = "\n    ".join(piece(*p) for p in pieces)
        content = f'<div class="artgrid">{grid}</div>'
    else:
        content = ('<p class="lead" style="max-width:56ch;color:var(--muted);">Maïja\'s artworks are being added to the '
                   'Collection. Ask the studio what is available today.</p>')
    cta = ''
    if anchor == "walls":
        cta = (f'<div style="margin-top:1.8rem;"><a class="btn btn--ghost" href="{_wa_wall}" target="_blank" '
               f'rel="noopener">{L.WA_ICON} Commission a Wall</a></div>')
    return f'''
<section class="section" id="{anchor}" style="padding-top:0;"><div class="wrap">
  <div class="reveal" style="margin-bottom:clamp(1.6rem,4vw,2.4rem);">
    <span class="eyebrow eyebrow--red">{title}</span>
    <h2 style="margin-top:.5rem;">{blurb}</h2>
  </div>
  {content}{cta}
</div></section>'''


collection_nav = " · ".join(
    f'<a class="ilink" href="#{a}">{t}</a>' for a, t, _, _ in COLLECTION)
collection_sections = "\n".join(collection_section(*c) for c in COLLECTION)
_col_cls, _col_media = subhero_media("hero-collection")
collection_body = f'''
{L.breadcrumb(("Collection", None))}
{L.subhero(
    eyebrow="The Collection",
    h1="Pieces with a life<br>of their own.",
    sub=("One-of-a-kind and limited-edition tables, lighting, artworks and dressed walls. "
         "Created to be lived with, not simply looked at."),
    media_class=_col_cls,
    media_html=_col_media,
)}

<section class="section"><div class="wrap wrap--narrow center reveal">
  <h2 style="margin-bottom:1rem;">No two stories<br>should look the same.</h2>
  <p class="lead">Each piece begins with its own character, references and contradictions — then takes a form entirely its own.
  Some are one-of-a-kind. Others exist as limited editions. And some begin with you.</p>
  <p style="margin-top:1.2rem;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);">{collection_nav}</p>
</div></section>

{collection_sections}

<section class="section band-dark"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">Commissions</span>
  <h2 style="margin-top:1rem;">Made for you.<br>Not made to match.</h2>
  <p class="lead" style="margin-inline:auto;color:var(--on-dark-soft);">A commissioned piece begins with you — your story, your
  space, your contradictions, your way of seeing things. The result isn't a variation of something that already exists.
  It's a piece with an identity of its own.</p>
  <div style="margin-top:1.6rem;"><a class="btn btn--light" href="{_col_commission}" target="_blank" rel="noopener">{L.WA_ICON} Commission a Piece</a></div>
</div></section>

<section class="section"><div class="wrap wrap--narrow center reveal">
  <span class="eyebrow">About the Work</span>
  <h2 style="margin-top:1rem;">The familiar,<br>seen differently.</h2>
  <p class="lead">Tables, lamps, walls and artworks become surfaces for another way of seeing — bringing together
  references, memories, symbols, humour and instinct. The form may be familiar. What it becomes isn't.</p>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="split" style="align-items:center;">
    <div class="split__text reveal">
      <span class="eyebrow">The Studio</span>
      <h2 style="margin:1rem 0 1.2rem;">Sometimes one piece<br>becomes a whole world.</h2>
      <p class="lead">Eden &amp; Beyond also creates complete spaces for hospitality, residential and commercial projects.</p>
      <a class="btn btn--ghost" href="studio.html" style="margin-top:1.6rem;">Discover the Studio {A}</a>
    </div>
    <div class="split__media reveal" data-delay="1">{('<img src="'+find_img('wondermint-camel')+'" alt="Flash — collectible table by Eden &amp; Beyond">') if find_img('wondermint-camel') else ph('The Studio', 'ph--electric')}<span class="tag">The Studio</span></div>
  </div>
</div></section>

<section class="section book"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow eyebrow--red">The Collection</span>
  <h2>Found something<br>you can't forget?</h2>
  <div class="book__actions" style="justify-content:center;">
    <a class="btn btn--primary" href="{_col_enquire}" target="_blank" rel="noopener">{L.WA_ICON} Enquire about a piece</a>
    <a class="btn btn--ghost" href="{_col_commission}" target="_blank" rel="noopener">Commission your own</a>
  </div>
</div></section>
'''
pages["collection.html"] = L.page(
    title="Collectible Furniture, Lighting & Art | Eden & Beyond",
    desc=("Discover Eden & Beyond's collection of one-of-a-kind and limited-edition tables, lighting, artworks and "
          "dressed walls, created in Koh Phangan, Thailand."),
    canonical="collection.html",
    body=collection_body,
    body_class="page-collection",
)


# ============================================================ SERVICE PAGES (V2)
def _chips(items, start=True):
    align = "flex-start" if start else "center"
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<ul class="tags reveal" style="justify-content:{align};">{lis}</ul>'


def _cap_block(eyebrow, title_html, items):
    return f'''<section class="section band-dark"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">{eyebrow}</span>
  <h2 style="margin:1rem 0 1.4rem;">{title_html}</h2>
  {_chips(items)}
</div></section>'''


def _dar_feat(eyebrow, h2, place, body, label="Discover the Project"):
    return f'''<section class="feat">{ph('Dar Mansour — Koh Phangan', 'ph--dark')}
  <div class="wrap feat__inner reveal">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{h2}</h2>
    <p class="feat__place">{place}</p>
    <p>{body}</p>
    <div style="margin-top:1.8rem;"><a class="btn btn--light" href="projects.html">{label} {A}</a></div>
  </div>
</section>'''


def _svc_collection(title_html, body):
    return f'''<section class="section"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow eyebrow--red">The Collection</span>
  <h2 style="margin-top:1rem;">{title_html}</h2>
  <p class="lead" style="margin-inline:auto;">{body}</p>
  <div style="margin-top:1.6rem;"><a class="btn btn--primary" href="collection.html">Explore the Collection {A}</a></div>
</div></section>'''


def _svc_final(eyebrow, title_html, wa_msg, label):
    return f'''<section class="section book"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">{eyebrow}</span>
  <h2>{title_html}</h2>
  <div class="book__actions" style="justify-content:center;">
    <a class="btn btn--primary" href="{L.wa(wa_msg)}" target="_blank" rel="noopener">{L.WA_ICON} {label}</a>
  </div>
</div></section>'''


def _svc_point(eyebrow, title_html, body_html):
    return f'''<section class="section"><div class="wrap wrap--narrow prose reveal">
  <span class="eyebrow">{eyebrow}</span>
  <h2 style="margin:.6rem 0 1rem;">{title_html}</h2>
  {body_html}
</div></section>'''


def _svc_bespoke(title_html, body, label="Discover Bespoke Furniture &amp; Pieces"):
    return f'''<section class="section band-dark"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">Bespoke Pieces</span>
  <h2 style="margin-top:1rem;">{title_html}</h2>
  <p class="lead" style="margin-inline:auto;color:var(--on-dark-soft);">{body}</p>
  <div style="margin-top:1.6rem;"><a class="btn btn--light" href="furniture-object-design.html">{label} {A}</a></div>
</div></section>'''


# ---- 15 · HOSPITALITY -------------------------------------------------------
_wa_hosp = "Hi Eden &amp; Beyond, I would like to talk about a hospitality project."
hospitality_body = f'''
{L.breadcrumb(("Hospitality Design", None))}
{L.subhero(eyebrow="Hospitality Design", h1="Places people remember.",
    sub="Creative direction and design for hotels, restaurants, bars, beach clubs, cafés and wellness spaces — built around character, atmosphere and a story of their own.")}
<section class="section"><div class="wrap wrap--narrow center reveal">
  <div style="margin-bottom:.4rem;"><a class="btn btn--primary" href="{L.wa(_wa_hosp)}" target="_blank" rel="noopener">{L.WA_ICON} Start a Hospitality Project</a></div>
</div></section>
{_svc_point("Positioning", "Beautiful isn't enough.",
  "<p>A hospitality space has to do more than look good. It has to make people want to enter, stay, come back — and remember where they were.</p><p>We create places with an identity of their own, where space, furniture, lighting, art and atmosphere work together as one complete experience.</p>")}
<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(1.6rem,4vw,2.4rem);"><span class="eyebrow">What We Design</span><h2 style="margin-top:1rem;">Hospitality spaces with a point of view</h2></div>
  {_chips(["Boutique Hotels","Restaurants","Bars","Beach Clubs","Cafés","Wellness &amp; Spa","Hospitality Concepts"], start=False)}
</div></section>
{_cap_block("What We Do", "From the big idea<br>to the smallest detail.",
  ["Creative Concept &amp; Direction","Spatial Identity &amp; Interior Design","Furniture &amp; Lighting","Artworks &amp; Dressed Walls","Materials &amp; Finishes","Styling &amp; Atmosphere","Brand &amp; Guest Experience"])}
{_svc_point("How We Think About Hospitality", "People don't remember floor plans.",
  "<p>They remember how a place made them feel. The table they wanted to sit at. The light at dinner. The music. The wall they photographed. The detail they told someone about the next day.</p><p>That's where hospitality becomes memorable — and it's designed on purpose.</p>")}
{_dar_feat("Hospitality in Practice", "Dar Mansour", "A restaurant designed as a complete world.",
  "For Dar Mansour in Koh Phangan, Eden &amp; Beyond shaped the restaurant across interiors, furniture, lighting, dressed walls, artworks and atmosphere. Nothing was treated as an isolated design decision — every element contributes to the same experience.")}
{_svc_bespoke("Sometimes the space needs something that doesn't exist yet.",
  "Furniture, lighting, artworks and site-specific pieces can be created as part of the project — giving the space details that belong nowhere else.")}
<section class="section"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">Who We Work With</span>
  <h2 style="margin:1rem 0 1.4rem;">Independent, boutique, unmistakable</h2>
  {_chips(["Independent Hotels","Boutique Resorts","Restaurants &amp; Bars","Beach Clubs","Wellness Concepts","Property Developers","Hospitality Entrepreneurs"])}
  <p style="margin-top:1.6rem;color:var(--muted);">Based in Koh Phangan, Thailand. Working with hospitality clients in Thailand and internationally. See also our <a class="ilink" href="restaurant-design.html">restaurant design</a> and <a class="ilink" href="creative-direction.html">creative direction</a>.</p>
</div></section>
{_svc_collection("Not planning a complete project?", "Discover one-of-a-kind and limited-edition tables, lighting, artworks and dressed walls from the Eden &amp; Beyond Collection.")}
{_svc_final("Ready when you are", "Planning a place<br>people won't forget?", _wa_hosp, "Start a Hospitality Project")}
'''
pages["hospitality-design.html"] = L.page(
    title="Hospitality Design Studio Thailand | Eden & Beyond",
    desc="Hospitality design and creative direction for boutique hotels, restaurants, bars, resorts and wellness spaces in Thailand and internationally.",
    canonical="hospitality-design.html", body=hospitality_body)


# ---- 16 · RESTAURANT --------------------------------------------------------
_wa_rest = "Hi Eden &amp; Beyond, I would like to talk about a restaurant project."
restaurant_body = f'''
{L.breadcrumb(("Restaurant Design", None))}
{L.subhero(eyebrow="Restaurant Design", h1="A restaurant should<br>have a point of view.",
    sub="Creative direction and design for restaurants, bars and dining concepts — from the first idea to the atmosphere guests remember.")}
<section class="section"><div class="wrap wrap--narrow center reveal">
  <div><a class="btn btn--primary" href="{L.wa(_wa_rest)}" target="_blank" rel="noopener">{L.WA_ICON} Start a Restaurant Project</a></div>
</div></section>
{_svc_point("Positioning", "More than a place to eat.",
  "<p>The best restaurants create a world around the food. The light, the furniture, the walls, the music, the objects, the way a table feels at night — every detail contributes to the experience.</p><p>We bring those elements together around one clear identity.</p>")}
<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(1.6rem,4vw,2.4rem);"><span class="eyebrow">What We Create</span><h2 style="margin-top:1rem;">Rooms built around a story</h2></div>
  {_chips(["Restaurants","Bars","Cafés","Dining Concepts","Restaurant &amp; Bar Areas within Hotels"], start=False)}
</div></section>
{_cap_block("From Concept to Experience", "From concept<br>to last detail.",
  ["Creative Concept &amp; Direction","Restaurant Identity &amp; Storytelling","Interior &amp; Spatial Design","Furniture &amp; Lighting","Artworks &amp; Dressed Walls","Materials &amp; Finishes","Styling &amp; Atmosphere","Brand Experience"])}
{_svc_point("The Restaurant Point of View", "The food isn't the whole story.",
  "<p>People remember where they sat. How the room changed after dark. The table they photographed before dinner arrived. The music. The light. The feeling that, for a few hours, they had stepped somewhere else.</p><p><strong>A great restaurant gives the food a world to belong to.</strong></p>")}
{_dar_feat("Selected Restaurant Project", "Dar Mansour — Morocco's Kitchen", "From a restaurant to a world of its own.",
  "Dar Mansour began with a simple ambition: to create a restaurant in Koh Phangan that felt genuinely rooted in Morocco without becoming a reproduction of it. Eden &amp; Beyond shaped the creative world around that idea — interiors, furniture, lighting, dressed walls, artworks and atmosphere, in one coherent experience.",
  label="Discover Dar Mansour")}
<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:2rem;"><span class="eyebrow">Project Depth</span><h2 style="margin-top:1rem;">One idea, every detail</h2></div>
  {_chips(["The Space","The Tables","The Lighting","The Walls","The Art","The Details"], start=False)}
</div></section>
{_svc_bespoke("Some details shouldn't exist anywhere else.",
  "Tables, lighting, artworks and site-specific pieces can be created especially for the restaurant — making the identity tangible in the things guests see, touch and remember.")}
{_svc_point("Creative Direction", "Before the space, there's the idea.",
  "<p>For new restaurant concepts, Eden &amp; Beyond can help shape the creative direction from the beginning — defining the story, personality, visual language and atmosphere that guide the entire project. Explore our <a href='creative-direction.html'>creative direction</a> work.</p>")}
<section class="section band-dark"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">Who We Work With</span>
  <h2 style="margin:1rem 0 1.4rem;">New concept, or a new chapter.</h2>
  {_chips(["Independent Restaurants","Restaurant Groups","Hotels &amp; Resorts","Chefs &amp; Founders","Property Developers","Hospitality Entrepreneurs"])}
  <p style="margin-top:1.4rem;color:var(--on-dark-soft);">From restaurants created from the ground up to existing places ready for a new identity. Based in Koh Phangan, Thailand — working in Thailand and internationally.</p>
</div></section>
{_svc_collection("Don't need the whole studio?", "A single piece can change a room. Discover one-of-a-kind and limited-edition tables, lighting and artworks from the Eden &amp; Beyond Collection.")}
{_svc_final("Opening a restaurant?", "Let's give the food<br>a world to belong to.", _wa_rest, "Start a Restaurant Project")}
'''
pages["restaurant-design.html"] = L.page(
    title="Restaurant Design Studio Thailand | Eden & Beyond",
    desc="Restaurant design and creative direction in Thailand and internationally, creating distinctive interiors, furniture, lighting, artworks and dining experiences.",
    canonical="restaurant-design.html", body=restaurant_body)


# ---- 17 · RESIDENTIAL -------------------------------------------------------
_wa_resi = "Hi Eden &amp; Beyond, I would like to talk about a residential project."
residential_body = f'''
{L.breadcrumb(("Residential Design", None))}
{L.subhero(eyebrow="Residential Design", h1="Homes with character.<br>Never someone else's idea of beautiful.",
    sub="Creative direction and design for private villas, residences and holiday homes — shaped around the people who live in them, not a predefined style.")}
<section class="section"><div class="wrap wrap--narrow center reveal">
  <div><a class="btn btn--primary" href="{L.wa(_wa_resi)}" target="_blank" rel="noopener">{L.WA_ICON} Start a Residential Project</a></div>
</div></section>
{_svc_point("Positioning", "Your home shouldn't<br>look like anyone else's.",
  "<p>A home is personal. It carries the people who live there — their histories, contradictions, travels, habits and the things they choose to surround themselves with.</p><p>We don't bring a signature look into your home. We create one around you.</p>")}
<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(1.6rem,4vw,2.4rem);"><span class="eyebrow">What We Design</span><h2 style="margin-top:1rem;">From a whole villa to a single room</h2></div>
  {_chips(["Private Villas","Residences","Holiday Homes","Residential Developments","Selected Rooms &amp; Spaces"], start=False)}
</div></section>
{_cap_block("What We Do", "From the way you live<br>to the things you live with.",
  ["Creative Direction","Interior &amp; Spatial Design","Furniture &amp; Lighting","Artworks &amp; Dressed Walls","Materials &amp; Finishes","Styling &amp; Curation","Bespoke Pieces"])}
{_svc_point("The Residential Point of View", "A home isn't a showroom.",
  "<p>It has to live. It changes with the light, collects memories, gets imperfect, fills with people and becomes more personal with time.</p><p>We create homes with enough character to be remembered — and enough freedom to become yours.</p>")}
{_svc_point("Our Approach", "It starts with you.",
  "<p>Before we think about colours, furniture or finishes, we want to understand who we're creating for. How you live. What you love. What you keep. What you reject. Where you've been. What feels like home to you.</p><p>Those things become part of the creative direction.</p>")}
{_svc_bespoke("Sometimes a home only needs one thing.",
  "A table. A light. An artwork. A wall. Eden &amp; Beyond can create a bespoke piece for your home without turning it into a complete design project.",
  label="Commission a Piece")}
{_svc_collection("Or maybe it already exists.", "Discover one-of-a-kind and limited-edition tables, lighting and artworks from the Eden &amp; Beyond Collection.")}
<section class="section band-dark"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow eyebrow--red">For Developers</span>
  <h2 style="margin:1rem 0 1.2rem;">Not another<br>copy-paste villa.</h2>
  <p class="lead" style="color:var(--on-dark-soft);">For boutique residential developments, Eden &amp; Beyond can shape a distinctive creative identity across interiors, furniture, lighting and art — while allowing each residence to retain its own character.</p>
  <div style="margin-top:1.6rem;"><a class="btn btn--light" href="{L.wa('Hi Eden &amp; Beyond, I would like to discuss a residential development.')}" target="_blank" rel="noopener">{L.WA_ICON} Discuss a Development</a></div>
</div></section>
<section class="section"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">Who We Work With</span>
  <h2 style="margin:1rem 0 1.4rem;">Already have an architect? Good.</h2>
  {_chips(["Villa Owners","Private Clients","Homeowners","Property Developers","Boutique Residential Projects","Architects &amp; Creative Partners"])}
  <p style="margin-top:1.4rem;color:var(--muted);">Eden &amp; Beyond can work alongside architects, developers and existing project teams. Based in Koh Phangan, Thailand — creating in Thailand and internationally.</p>
</div></section>
{_svc_final("Creating a home that should feel like yours?", "Let's make sure it does.", _wa_resi, "Start a Residential Project")}
'''
pages["residential-design.html"] = L.page(
    title="Residential & Villa Design Thailand | Eden & Beyond",
    desc="Residential design and creative direction for private villas, residences and holiday homes in Thailand and internationally, by Eden & Beyond.",
    canonical="residential-design.html", body=residential_body)


# ---- 18 · BESPOKE FURNITURE & PIECES ---------------------------------------
_wa_besp = 'Hi Eden &amp; Beyond, I would like to commission a bespoke piece.'
bespoke_body = f'''
{L.breadcrumb(("Bespoke Furniture &amp; Pieces", None))}
{L.subhero(eyebrow="Bespoke Furniture &amp; Pieces", h1="Made for a particular<br>place, person or purpose.",
    sub="Commissioned tables, lighting, artworks and site-specific pieces — created individually for private homes, hospitality spaces and commercial projects.")}
<section class="section"><div class="wrap wrap--narrow center reveal">
  <div><a class="btn btn--primary" href="{L.wa(_wa_besp)}" target="_blank" rel="noopener">{L.WA_ICON} Commission a Piece</a></div>
</div></section>
{_svc_point("Positioning", "Not customised.<br>Created for you.",
  "<p>A commission isn't about taking an existing piece and changing the colour, size or finish. It begins from somewhere else — a person, a place, a story, a feeling, sometimes a contradiction.</p><p>From there, something new takes form.</p>")}
<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(1.6rem,4vw,2.4rem);"><span class="eyebrow">What Can Be Commissioned</span><h2 style="margin-top:1rem;">A new creation, not a variation</h2></div>
  {_chips(["Tables","Lighting","Artworks","Dressed Walls","Site-Specific Pieces"], start=False)}
</div></section>
{_svc_point("For a Person", "Some pieces<br>begin with a person.",
  "<p>For private commissions, the starting point can be deeply personal. Maïja observes, listens and interprets what lies beneath the obvious — memories, references, contradictions, symbols and fragments of a life.</p><p>The result isn't a portrait. It's a piece that could only have begun with you.</p>")}
{_svc_point("For a Place", "Others begin<br>with a place.",
  "<p>For restaurants, hotels, villas and commercial spaces, a bespoke piece can grow directly from the identity of the project. A table, a light, an artwork or a wall becomes part of the world around it — rather than something added afterwards.</p>")}
<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:660px;margin-inline:auto;margin-bottom:clamp(2rem,5vw,3rem);"><span class="eyebrow">How a Commission Begins</span><h2 style="margin-top:1rem;">Four steps, one creation.</h2></div>
  <div class="steps">
    <div class="step reveal"><span class="step__num">01</span><h3>Conversation</h3><p>Tell us about you — or the place. The starting point might be a story, a space, a need or an obsession.</p></div>
    <div class="step reveal" data-delay="1"><span class="step__num">02</span><h3>Interpretation</h3><p>Maïja takes it from there. References, materials, forms and ideas collide until a direction emerges.</p></div>
    <div class="step reveal" data-delay="2"><span class="step__num">03</span><h3>Creation</h3><p>The piece takes form — developed as an individual creation, not a variation of an existing design.</p></div>
    <div class="step reveal" data-delay="3"><span class="step__num">04</span><h3>Delivery</h3><p>From our world to yours. Delivery and installation are arranged according to the piece and its destination.</p></div>
  </div>
</div></section>
{_svc_point("Creative Freedom", "A commission<br>needs a little trust.",
  "<p>You bring the starting point. Maïja brings the interpretation. That's where the interesting part begins.</p>")}
{_svc_collection("Found it already?", "Not every piece needs to begin from scratch. Explore the Eden &amp; Beyond Collection for existing one-of-a-kind and limited-edition tables, lighting and artworks.")}
<section class="section"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">For Hospitality &amp; Developers</span>
  <h2 style="margin-top:1rem;">One piece.<br>Or fifty details.</h2>
  <p class="lead" style="margin-inline:auto;">For hospitality and development projects, Eden &amp; Beyond can create bespoke furniture, lighting, artworks and site-specific pieces as part of a wider creative direction. Individual pieces can also be commissioned independently.</p>
  <p style="margin-top:1.2rem;color:var(--muted);">Based in Koh Phangan. Commissioned for Thailand and international destinations, subject to scale, installation and shipping.</p>
</div></section>
{_svc_final("What should exist that doesn't yet?", "Let's find out<br>together.", _wa_besp, "Commission a Piece")}
'''
pages["furniture-object-design.html"] = L.page(
    title="Bespoke Furniture & Art Commissions Thailand | Eden & Beyond",
    desc="Commission bespoke tables, lighting, artworks and site-specific pieces from Eden & Beyond in Thailand, for private homes, hospitality and commercial spaces.",
    canonical="furniture-object-design.html", body=bespoke_body)


# ---- 19 · CREATIVE DIRECTION ------------------------------------------------
_wa_cd = "Hi Eden &amp; Beyond, I would like to discuss creative direction for a project."
creative_body = f'''
{L.breadcrumb(("Creative Direction", None))}
{L.subhero(eyebrow="Creative Direction", h1="The idea<br>behind everything.",
    sub="Creative direction for hospitality, residential and commercial projects — shaping the concept, identity and visual world before the details take over.")}
<section class="section"><div class="wrap wrap--narrow center reveal">
  <div><a class="btn btn--primary" href="{L.wa(_wa_cd)}" target="_blank" rel="noopener">{L.WA_ICON} Discuss a Project</a></div>
</div></section>
{_svc_point("Positioning", "Before you design the place,<br>you need to know what it is.",
  "<p>A beautiful interior can't rescue an idea that was never clear. We help define what a project should feel like, what makes it different and the creative language that will hold everything together.</p><p>Then every decision has somewhere to come from.</p>")}
{_cap_block("What We Can Shape", "One idea.<br>A thousand decisions.",
  ["Concept &amp; Positioning","Story &amp; Identity","Visual Language","Interior Direction","Furniture &amp; Lighting Direction","Art &amp; Styling","Guest / Customer Experience","Creative Guidelines"])}
{_svc_point("When to Involve Us", "The earlier, the better.",
  "<p>Creative direction has the greatest impact when it begins before the answers have already been decided. A new restaurant. A boutique hotel. A villa development. A bar. A hospitality concept. An existing place ready to become something else.</p><p><strong>Bring us the ambition before you bring us the moodboard.</strong></p>")}
{_svc_point("Existing Projects", "Sometimes the place exists.<br>The idea doesn't.",
  "<p>Creative direction can also give an existing business a new chapter — clarifying its identity, atmosphere and visual language without necessarily starting again from zero.</p>")}
<section class="section band-dark"><div class="wrap wrap--narrow reveal center">
  <span class="eyebrow">Collaboration</span>
  <h2 style="margin-top:1rem;">Already have a team? Good.</h2>
  <p class="lead" style="margin-inline:auto;color:var(--on-dark-soft);">Eden &amp; Beyond can work alongside architects, interior designers, brand teams, developers and other creative partners — establishing the creative direction and keeping the original idea coherent as different disciplines bring it to life.</p>
</div></section>
{_dar_feat("Creative Direction in Practice", "Dar Mansour", "One identity. Many expressions.",
  "At Dar Mansour, the creative direction became the thread connecting the space, furniture, lighting, walls, art and atmosphere. Different elements, but one unmistakable world.")}
<section class="section"><div class="wrap wrap--narrow reveal">
  <span class="eyebrow">Direction, or the Whole World</span>
  <h2 style="margin:1rem 0 1rem;">Two ways to work with us</h2>
  <p class="lead">Some clients need Eden &amp; Beyond to establish the creative direction and collaborate with their existing team. Others want us to carry that direction into the space, furniture, lighting, artworks and details.</p>
  <p style="margin-top:1rem;">Both can begin with the same conversation. Learn more <a href="studio.html">about the studio</a>.</p>
</div></section>
{_svc_final("Have the project but not yet the world around it?", "That's a good<br>place to start.", _wa_cd, "Discuss Creative Direction")}
'''
pages["creative-direction.html"] = L.page(
    title="Creative Direction Studio Thailand | Eden & Beyond",
    desc="Creative direction for hospitality, residential and commercial projects in Thailand and internationally — concept, identity, visual language and experience.",
    canonical="creative-direction.html", body=creative_body)



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
    ("about-maija.html", "0.7"),
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
        "> Eden & Beyond is an independent multidisciplinary creative studio and collectible design brand founded by "
        "Maïja Disseau, based in Koh Phangan, Thailand. Two complementary sides: (1) The Collection — one-of-a-kind and "
        "limited-edition tables, lighting, artworks and dressed walls, available independently; and (2) The Studio — "
        "creative direction and design for hospitality, residential and commercial projects. Working in Thailand and "
        "internationally. Selected project: Dar Mansour, a Moroccan restaurant in Koh Phangan.",
        "",
        "## Key pages",
        f"- [Home]({L.SITE_URL}/): Collection & studio overview",
        f"- [Collection]({L.SITE_URL}/collection.html): One-of-a-kind & limited-edition tables, lighting, artworks & dressed walls",
        f"- [Studio]({L.SITE_URL}/studio.html): The creative studio & how it works",
        f"- [About Maïja]({L.SITE_URL}/about-maija.html): Founder & creative director Maïja Disseau",
        f"- [Projects]({L.SITE_URL}/projects.html): Dar Mansour case study",
        f"- [Journal]({L.SITE_URL}/journal.html): Ideas on design, art, hospitality & culture",
        f"- [Contact]({L.SITE_URL}/contact.html): Start a project or commission a piece",
        "",
        "## Studio services",
        f"- [Hospitality Design]({L.SITE_URL}/hospitality-design.html)",
        f"- [Restaurant Design]({L.SITE_URL}/restaurant-design.html)",
        f"- [Residential Design]({L.SITE_URL}/residential-design.html)",
        f"- [Bespoke Furniture & Pieces]({L.SITE_URL}/furniture-object-design.html)",
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
