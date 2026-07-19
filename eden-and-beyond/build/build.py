# -*- coding: utf-8 -*-
"""Eden & Beyond — static site generator.
Run from the eden-and-beyond/ folder:  python3 build/build.py
Header / footer / nav are defined once in _layout.py; never edit the generated
*.html at the root of eden-and-beyond/ by hand — they are overwritten."""

import datetime
import os
import re
import sys

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
home_body = f'''
{L.hero(
    eyebrow="Creative Studio · Hospitality · Living · Lifestyle",
    h1_html='F*** the Box.',
    sub=("A creative studio designing unforgettable places, objects &amp; experiences. "
         "From boutique hotels and restaurants to private villas and bespoke objects, "
         "we create projects with soul — where design, storytelling and craftsmanship "
         "come together to create lasting memories."),
    actions_html=(
        '<a class="btn btn--primary" href="contact.html">Start a Project</a>'
        '<a class="btn btn--light" href="projects.html">Explore Our Work</a>'),
)}

<div class="trust"><div class="wrap trust__inner">
  <span class="trust__item"><strong>Hospitality</strong></span>
  <span class="trust__item"><strong>Residential</strong></span>
  <span class="trust__item"><strong>Furniture &amp; Objects</strong></span>
  <span class="trust__item"><strong>Creative Direction</strong></span>
  <span class="trust__item">Working <strong>Internationally</strong></span>
</div></div>

<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:760px;margin-inline:auto;">
    <span class="eyebrow">Beyond Design</span>
    <h2 style="margin:1.2rem 0 1.6rem;">Great projects aren't built<br>around trends. They're built around stories.</h2>
    <p class="lead" style="margin-inline:auto;">At Eden &amp; Beyond, we believe every place, every object and every
    experience deserves its own identity. That's why we don't start with a style. We start by listening.
    Understanding. Questioning. Only then do we begin to create — and the result is never just beautiful. It's meaningful.</p>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin-inline:auto;margin-bottom:clamp(2.5rem,6vw,4rem);">
    <span class="eyebrow">What We Do</span>
    <h2 style="margin-top:1.1rem;">Four disciplines,<br>one way of thinking.</h2>
  </div>
  <div class="disc">
    <a class="disc__card reveal" href="hospitality-design.html">{ph('Boutique hotel — hospitality design', 'ph--dark')}
      <div class="disc__body"><h3>Hospitality</h3>
      <p>Memorable destinations through thoughtful design and storytelling.</p>
      <p class="disc__tags">Hotels · Restaurants · Bars · Beach Clubs · Cafés · Wellness</p></div></a>
    <a class="disc__card reveal" data-delay="1" href="residential-design.html">{ph('Private villa — residential design', 'ph--dark')}
      <div class="disc__body"><h3>Residential</h3>
      <p>Homes with personality, warmth and timeless character.</p>
      <p class="disc__tags">Private Villas · Luxury Residences · Holiday Homes</p></div></a>
    <a class="disc__card reveal" href="furniture-object-design.html">{ph('Bespoke furniture &amp; objects', 'ph--dark')}
      <div class="disc__body"><h3>Objects &amp; Furniture</h3>
      <p>Bespoke pieces that give every project its own identity.</p>
      <p class="disc__tags">Furniture · Lighting · Objects · Art Curation</p></div></a>
    <a class="disc__card reveal" data-delay="1" href="creative-direction.html">{ph('Creative direction &amp; storytelling', 'ph--dark')}
      <div class="disc__body"><h3>Creative Direction</h3>
      <p>Concept, storytelling and brand experiences from first idea to last detail.</p>
      <p class="disc__tags">Concept · Brand Identity · Art Direction · Styling</p></div></a>
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
  <p>Every project has a <span class="em">soul</span>. We don't believe in signature styles —
  we believe in revealing identities. Because every client, every location, every culture,
  every story deserves something uniquely its own.</p>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="split" style="align-items:flex-end;margin-bottom:clamp(2rem,5vw,3rem);">
    <div class="split__text reveal">
      <span class="eyebrow">Art by Maija</span>
      <h2 style="margin:1rem 0 1.2rem;">Where the studio<br>gets loud.</h2>
      <p class="lead">Maija's collages and objects collide Moroccan craft with a wink at Western art — fez and Mona Lisa,
      mint tea and Michelangelo. The same instinct runs through every project we design.</p>
      <a class="textlink" href="art.html" style="margin-top:1.4rem;">See the art {A}</a>
    </div>
  </div>
  <div class="artstrip reveal">
    {ph('Poppy Queen', 'ph--poppy ph--round')}
    {ph('Wondermint', 'ph--electric')}
    {ph('The Creation of Mint Tea', 'ph--teal ph--round')}
    {ph('Teapot Camel', 'ph--sun')}
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
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

{L.cta_band(
    title="Let's create something unforgettable.",
    text=("Whether you're developing a boutique hotel, designing a restaurant, building a private villa "
          "or imagining something entirely new, we'd love to hear your story."),
)}
'''

pages["index.html"] = L.page(
    title="Eden & Beyond — Creative Studio for Hospitality, Living & Lifestyle",
    desc=("Eden & Beyond is a multidisciplinary creative studio designing places, objects and experiences — "
          "boutique hotels, restaurants, private villas, bespoke furniture and creative direction. Based in Thailand, working internationally."),
    canonical="index.html",
    body=home_body,
)


# ============================================================ ABOUT
about_body = f'''
{L.subhero(
    eyebrow="About the Studio",
    h1="We don't follow trends.<br>We create stories.",
    sub=("Eden & Beyond is an independent multidisciplinary creative studio creating places, objects and "
         "experiences for hospitality, residential and lifestyle projects."),
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
  <div class="split split--reverse">
    <div class="split__text reveal">
      <span class="eyebrow">Meet Maija</span>
      <h2>Founder &amp; Creative Director</h2>
      <p class="lead">Maija founded Eden &amp; Beyond with one conviction: design should create emotion before admiration.</p>
      <p style="margin-top:1.1rem;">Her multidisciplinary approach combines creative direction, interior design, craftsmanship
      and storytelling to create projects that feel authentic, timeless and deeply personal. Rather than designing around a
      recognisable style, she believes every project should become a reflection of its own story.</p>
      <p class="note" style="margin-top:1.6rem;"><em>Placeholder — full founder bio to be written with Maija (background, path, notable work). This is the most important page for trust and E-E-A-T.</em></p>
    </div>
    <div class="split__media reveal" data-delay="1">
      {ph('Portrait — Maija')}
      <span class="tag">Maija · Founder</span>
    </div>
  </div>
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

{L.cta_band(
    title="Let's create something unforgettable.",
    text="If you believe your project deserves more than a beautiful design, we'd love to hear your story.",
)}
'''
pages["about.html"] = L.page(
    title="About — Eden & Beyond Creative Studio | Maija",
    desc=("Eden & Beyond is an independent multidisciplinary creative studio founded by Maija, designing places, "
          "objects and experiences for hospitality, residential and lifestyle projects. Based in Thailand."),
    canonical="about.html",
    body=about_body,
    body_class="",
)


# ============================================================ SERVICES
services_body = f'''
{L.subhero(
    eyebrow="Creative Services",
    h1="From concept to completion.",
    sub=("We design places, objects and experiences with identity, purpose and lasting impact — "
         "across hospitality, residential, furniture and creative direction."),
)}

<section class="section"><div class="wrap">
  <div class="center reveal" style="margin-bottom:clamp(2.5rem,6vw,3.5rem);">
    <span class="eyebrow">Our Expertise</span>
    <h2 style="margin-top:1rem;">Four disciplines</h2>
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
      <p>Bespoke furniture, lighting and custom objects that give every project its own identity.</p></div></a>
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

<section class="section"><div class="wrap wrap--narrow">
  <div class="center reveal">
    <span class="eyebrow">How We Work</span>
    <h2 style="margin:1rem 0 1.6rem;">We collaborate with</h2>
  </div>
  <ul class="tags reveal" style="margin-bottom:2rem;">
    <li>Hotel Owners</li><li>Restaurateurs</li><li>Private Clients</li><li>Developers</li>
    <li>Architects</li><li>Hospitality Brands</li><li>Commercial Businesses</li>
  </ul>
  <p class="lead center reveal" style="margin-inline:auto;">Whether we're involved from day one or joining an existing team, our role
  remains the same: to create projects with identity, coherence and lasting value.</p>
</div></section>

{L.cta_band(
    title="Looking for more than a beautiful space?",
    text="Let's create something people will remember.",
)}
'''
pages["services.html"] = L.page(
    title="Creative Services — Hospitality, Residential, Furniture & Creative Direction | Eden & Beyond",
    desc=("Eden & Beyond creative services: hospitality design, residential design, bespoke furniture and object "
          "design, and creative direction. From concept to completion, designed around your story."),
    canonical="services.html",
    body=services_body,
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
      <h2 style="margin:1rem 0 1.4rem;">Every project begins<br>with a conversation.</h2>
      <p style="margin-bottom:2rem;">Tell us about your vision, your ambitions and your project. We'll take it from there.</p>
      <dl>
        <div><dt>Email</dt><dd><a href="mailto:{L.EMAIL}">{L.EMAIL}</a></dd></div>
        <div><dt>Instagram</dt><dd><a href="{L.INSTAGRAM}" target="_blank" rel="noopener">{L.INSTAGRAM_HANDLE}</a></dd></div>
        <div><dt>Location</dt><dd>Working internationally.<span class="contact-note">Based in Thailand.</span></dd></div>
      </dl>
    </div>

    <form class="enquiry reveal" data-delay="1" action="#" method="post" aria-label="Project enquiry">
      <span class="eyebrow" style="margin-bottom:1.2rem;">Project Enquiry</span>
      <div class="field--row">
        <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
        <div class="field"><label for="company">Company</label><input id="company" name="company" type="text"></div>
      </div>
      <div class="field--row">
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
        <div class="field"><label for="phone">Phone (optional)</label><input id="phone" name="phone" type="tel"></div>
      </div>
      <div class="field--row">
        <div class="field"><label for="location">Location</label><input id="location" name="location" type="text"></div>
        <div class="field"><label for="type">Project Type</label>
          <select id="type" name="type">
            <option>Hospitality</option><option>Residential</option>
            <option>Furniture &amp; Objects</option><option>Creative Direction</option><option>Other</option>
          </select></div>
      </div>
      <div class="field--row">
        <div class="field"><label for="timeline">Estimated Timeline</label><input id="timeline" name="timeline" type="text"></div>
        <div class="field"><label for="budget">Estimated Budget (optional)</label><input id="budget" name="budget" type="text"></div>
      </div>
      <div class="field"><label for="message">Tell us about your project</label><textarea id="message" name="message"></textarea></div>
      <button class="btn btn--primary" type="submit">Send Enquiry {A}</button>
      <p class="enquiry__note">Form handling to be connected (e.g. Formspree / Web3Forms) at launch.</p>
    </form>
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
pages["contact.html"] = L.page(
    title="Contact — Start a Project | Eden & Beyond Creative Studio",
    desc=("Start a project with Eden & Beyond. Boutique hotels, restaurants, private villas, bespoke furniture and "
          "creative direction. Working internationally, based in Thailand. hello@edenandbeyond.studio"),
    canonical="contact.html",
    body=contact_body,
)


# ============================================================ ART (Maija's work)
# Working titles + tints per piece the client shared. `img` is filled once the
# real files land in assets/img/ (kebab-case, WebP, SEO alt) — until then a
# vivid tinted placeholder named after the piece stands in.
ARTWORKS = [
    # slug,                       title,                         medium,                       shape,          tint,          img
    ("poppy-queen",              "Poppy Queen",                 "Collage · tondo",            "art--round",   "ph--poppy",    None),
    ("wondermint-camel",         "Wondermint",                  "Collage",                    "",             "ph--electric", None),
    ("mona-lisa-fez",            "Mona, Fez",                   "Collage · tondo",            "art--round",   "ph--teal",     None),
    ("babouche-mandala",         "Babouche Mandala",            "Collage",                    "",             "ph--magenta",  None),
    ("creation-of-mint-tea",     "The Creation of Mint Tea",    "Collage · tondo",            "art--round",   "ph--teal",     None),
    ("chefchaouen-framed",       "Chefchaouen, Framed",         "Collage",                    "",             "ph--electric", None),
    ("desert-caravan-neon",      "Desert Caravan",              "Collage · tondo",            "art--round",   "ph--magenta",  None),
    ("teapot-camel",             "Teapot Camel",                "Collage",                    "",             "ph--sun",      None),
    ("rue-yves-saint-laurent",   "Rue Yves Saint Laurent",      "Photograph · Marrakech",     "",             "ph--teal",     None),
    ("fez-lamp",                 "Fez Lamp",                    "Object · mixed media",       "art--tall",    "ph--poppy",    None),
]


def artwork(slug, title, medium, shape, tint, img):
    cls = f"art {shape}".strip()
    if img:
        media = f'<img src="assets/img/{img}" alt="{title} — artwork by Maija, Eden &amp; Beyond" loading="lazy">'
    else:
        media = ph(title, tint)
    return f'''<a class="{cls} reveal" href="contact.html" id="{slug}">
      <div class="art__media">{media}</div>
      <div class="art__cap"><span class="art__title">{title}</span>
      <span class="art__meta">{medium}</span></div>
    </a>'''


art_grid = "\n    ".join(artwork(*a) for a in ARTWORKS)
art_body = f'''
{L.breadcrumb(("Art by Maija", None))}
{L.subhero(
    eyebrow="Art by Maija",
    h1="Where Morocco meets pop.",
    sub=("Collages, tondos and objects that borrow from Moroccan craft and Western art history in equal measure — "
         "fez and Mona Lisa, mint tea and Michelangelo, babouches and Warhol. Playful, saturated, unmistakably her."),
)}

<section class="section"><div class="wrap wrap--narrow center reveal">
  <p class="lead">Maija's art is where the studio's spirit is loudest. Each piece takes something instantly Moroccan —
  a camel, a teapot, a fez, a wall of zellige — and collides it with a wink at Western art and pop culture.
  It's the same instinct behind every Eden &amp; Beyond project: take the familiar, break the frame, make it feel new.</p>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="artgrid">
    {art_grid}
  </div>
  <p class="center reveal" style="margin-top:2.4rem;color:var(--muted);font-size:.86rem;">
    Titles, media and dimensions are working placeholders — final captions and images to be added.
    For availability, editions or commissions, <a class="ilink" href="contact.html">get in touch</a>.
  </p>
</div></section>

{L.cta_band(
    title="Want a piece — or a commission?",
    text="Maija creates original collages and bespoke objects for private collectors and hospitality projects. Tell us what you have in mind.",
    btn_label="Enquire",
)}
'''
pages["art.html"] = L.page(
    title="Art by Maija — Moroccan Pop Collage & Objects | Eden & Beyond",
    desc=("Original collage art and objects by Maija of Eden & Beyond — Moroccan iconography meets Western pop and art "
          "history. Fez, camels, mint tea and zellige, reimagined. Commissions and pieces available."),
    canonical="art.html",
    body=art_body,
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
                       'or read more about our <a href="services.html">creative process</a>.</p>')},
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
                       '<p>Explore our <a href="services.html">full range of services</a> or <a href="contact.html">start a '
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
                       '<p>Our <em>Fez Lamp</em> — a collaged bust crowned with a tasselled fez shade — is one example of how a single '
                       'object can carry a whole atmosphere. See it and other pieces in <a href="art.html">Art by Maija</a>.</p>')},
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
                       '<p>Learn more <a href="about.html">about the studio</a> or <a href="contact.html">start a project</a>.</p>')},
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
    ("services.html", "0.9"),
    ("hospitality-design.html", "0.9"),
    ("restaurant-design.html", "0.9"),
    ("residential-design.html", "0.9"),
    ("furniture-object-design.html", "0.8"),
    ("creative-direction.html", "0.8"),
    ("projects.html", "0.8"),
    ("art.html", "0.8"),
    ("about.html", "0.7"),
    ("journal.html", "0.7"),
    ("contact.html", "0.7"),
]


def write_sitemap():
    today = datetime.date.today().isoformat()
    urls = ""
    for name, prio in SITEMAP_ORDER:
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
        "> Eden & Beyond is an independent multidisciplinary creative studio designing places, objects and "
        "experiences — boutique hotels, restaurants, private villas, bespoke furniture and creative direction. "
        "Based in Thailand, working internationally.",
        "",
        "## Key pages",
        f"- [Home]({L.SITE_URL}/): Studio overview",
        f"- [About]({L.SITE_URL}/about.html): The studio & founder Maija",
        f"- [Services]({L.SITE_URL}/services.html): Creative services & process",
        f"- [Projects]({L.SITE_URL}/projects.html): Selected work, including Dar Mansour",
        f"- [Art by Maija]({L.SITE_URL}/art.html): Moroccan pop collage art & objects",
        f"- [Journal]({L.SITE_URL}/journal.html): Editorial on design & hospitality",
        f"- [Contact]({L.SITE_URL}/contact.html): Start a project",
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
