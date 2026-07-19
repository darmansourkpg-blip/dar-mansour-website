# -*- coding: utf-8 -*-
"""Dar Mansour — static site generator. Run: python3 build/build.py  (from site/)"""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)  # site/

import _layout as L
from _menu import render_menu, render_legend
from _drinks import render_wine_feature, render_wine_groups, render_cocktails
import _journal

ARTICLES = _journal.load_articles()

WA = L.WA
A = L.ARROW
WI = L.WA_ICON
pages = {}


# ============================================================ HOME
home_body = f'''
<section class="hero">
  <div class="hero__media"><picture>
    <source media="(max-width: 720px)" srcset="assets/uploads/Dar%20Mansour%20Morocco%27s%20Kitchen%20Koh%20Phangan.webp">
    <img src="assets/uploads/entrance-%20dar%20mansour%20-%20koh%20phangan.webp" alt="The candlelit garden lounge and illuminated Dar Mansour sign in Koh Phangan" fetchpriority="high">
  </picture></div>
  <div class="wrap hero__inner">
    <span class="eyebrow">Slow Food · West Coast, Koh Phangan</span>
    <h1 class="display hero__title">Moroccan Restaurant<br>in Koh Phangan</h1>
    <p class="hero__sub">A boutique Moroccan slow-dining restaurant near Sri Thanu &amp; Hin Kong — fire-cooked tajines, slow-simmered tanjias and candlelit garden dinners, rooted in tradition and slow cooked with care.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">{WI} Reserve Your Evening</a>
      <a class="btn btn--light" href="moroccan-menu-koh-phangan.html">Discover the Menu</a>
    </div>
  </div>
  <span class="hero__scroll" aria-hidden="true">Scroll</span>
</section>

<div class="trust"><div class="wrap trust__inner">
  <span class="trust__item"><strong>By Reservation</strong></span>
  <span class="trust__item"><strong>Pre-order</strong> Philosophy</span>
  <span class="trust__item"><strong>Slow Cooked</strong> · Zero Waste</span>
  <span class="trust__item">Limited to <strong>40 Guests</strong> a Night</span>
  <span class="trust__item"><strong>Curated</strong> Wine Pairing</span>
</div></div>

<section class="section" id="experience"><div class="wrap"><div class="split">
  <div class="split__text reveal">
    <span class="eyebrow">The Experience</span>
    <h2>Come as a guest,<br>leave as family.</h2>
    <p class="lead">Tucked away near Sri Thanu and Hin Kong — just minutes from The Alcove, Orion Healing Center and Bliss Villas — Dar Mansour is a soulful, immersive dining experience on the west coast of Koh Phangan.</p>
    <p style="margin-top:1.2rem;">Rooted in the wisdom of the Dadas, our menu blends Berber, Andalusian, Jewish and Saharan influences — where sweet meets savoury, and vegetables are roasted with patience and care. Every detail, from handcrafted tiles to candlelit tables, is curated to slow you down and welcome you home.</p>
    <a class="textlink" href="dar-mansour-founders-vision.html">Read our story {A}</a>
  </div>
  <div class="split__media reveal" data-delay="1">
    <img src="assets/img/moroccan-restaurant-central-room-koh-phangan.webp" alt="Central dining room at Dar Mansour with handcrafted Moroccan interiors">
    <span class="tag">The Central Room</span>
  </div>
</div></div></section>

<section class="section band-dark"><div class="wrap quote">
  <div class="divider divider--light reveal"><span>◇◇◇</span></div>
  <blockquote class="reveal" data-delay="1" style="margin-top:2rem;">"Dar Mansour brings the soul of contemporary Moroccan hospitality to Koh Phangan."</blockquote>
  <cite class="reveal" data-delay="2">Slow food · Art · Culture · Human connection</cite>
</div></section>

<section class="section" id="concept"><div class="wrap">
  <div class="center reveal" style="max-width:720px;margin-inline:auto;">
    <span class="eyebrow">Concept &amp; Operating Model</span>
    <h2 style="margin:1.2rem 0 1.3rem;">The art of hosting, redefined</h2>
    <p class="lead" style="margin-inline:auto;">At Dar Mansour, the experience begins long before your arrival. As one of Koh Phangan's only Moroccan slow food restaurants, every dish is prepared to order, at the rhythm of traditional cooking. Reservations are highly recommended and our signature dishes are available by pre-order — ideally 5 hours ahead — because dishes like tanjia marrakchia and fire-cooked tajines need time, love and patience to reveal their full soul.</p>
  </div>
  <div class="features" style="margin-top:clamp(3rem,6vw,4.5rem);">
    <div class="feature reveal"><span class="feature__num">01</span><h3>By Reservation</h3><p>Advance reservations via WhatsApp allow us to welcome every guest with the time, care and hospitality that define the Dar Mansour experience.</p></div>
    <div class="feature reveal" data-delay="1"><span class="feature__num">02</span><h3>Pre-order Tradition</h3><p>Our signature main dishes are pre-ordered, ideally 5 hours in advance, honouring traditional cooking times so they're ready to be enjoyed the moment you arrive.</p></div>
    <div class="feature reveal"><span class="feature__num">03</span><h3>Zero Waste Philosophy</h3><p>Every dish is prepared to order, never mass-produced. By cooking only what is needed, we honour traditional cooking times while naturally reducing food waste and unnecessary excess.</p></div>
    <div class="feature reveal" data-delay="1"><span class="feature__num">04</span><h3>Intimate by Design</h3><p>Welcoming just 40 guests each evening, Dar Mansour was intentionally designed to preserve what matters most: time, craftsmanship, genuine hospitality, and the quality of every dish we serve.</p></div>
  </div>
  <div class="center reveal" style="margin-top:2.6rem;"><a class="textlink" href="moroccan-slow-dining-koh-phangan.html">Discover our slow-food concept {A}</a></div>
</div></section>

<section class="section" id="cuisine" style="background:var(--sand);"><div class="wrap">
  <div class="center reveal" style="max-width:680px;margin:0 auto clamp(2.5rem,5vw,3.5rem);">
    <span class="eyebrow">Our Moroccan Menu</span>
    <h2 style="margin:1.2rem 0;">A journey to the roots of Moroccan cuisine</h2>
    <p class="lead" style="margin-inline:auto;">Inspired by the Dadas — the silent guardians of Moroccan family recipes — our kitchen celebrates the authentic essence of Morocco: slow-cooked dishes full of generosity, depth and soul.</p>
  </div>
  <div class="dishes dishes--photos">
    <article class="dish reveal"><img src="assets/uploads/Couscous.jpg" alt="Moroccan couscous with slow-cooked vegetables at Dar Mansour" loading="lazy"><div class="dish__label"><h3>Couscous</h3></div></article>
    <article class="dish reveal" data-delay="1"><img src="assets/uploads/Berber%27s%20Tajine.jpg" alt="Berber tajine with prunes, almonds and cinnamon" loading="lazy"><div class="dish__label"><h3>Berber's Tajine</h3></div></article>
    <article class="dish reveal" data-delay="2"><img src="assets/uploads/Fez%27s%20Tajine.jpg" alt="Fez-style chicken tajine with olives and preserved lemon" loading="lazy"><div class="dish__label"><h3>Fez's Tajine</h3></div></article>
    <article class="dish reveal"><img src="assets/uploads/Chefchaouen%27s%20Tajine.jpg" alt="Chefchaouen vegetable tajine with courgette and carrots" loading="lazy"><div class="dish__label"><h3>Chefchaouen's Tajine</h3></div></article>
    <article class="dish reveal" data-delay="1"><img src="assets/uploads/Tanjia%20Marrakchia.jpg" alt="Tanjia Marrakchia slow-cooked in its clay urn over embers" loading="lazy"><div class="dish__label"><h3>Tanjia Marrakchia</h3></div></article>
    <article class="dish reveal" data-delay="2"><img src="assets/uploads/M%27semen.jpg" alt="Msemen, traditional Moroccan layered flatbread" loading="lazy"><div class="dish__label"><h3>M'semen</h3></div></article>
  </div>
  <div class="center reveal" style="margin-top:clamp(2.5rem,5vw,3.5rem);">
    <a class="btn btn--primary" href="moroccan-menu-koh-phangan.html">Explore the Full Menu</a>
    <p class="book__meta">Every main course is individually crafted, prepared to order to honour tradition and minimise waste.</p>
  </div>
</div></section>

<section class="section" id="story"><div class="wrap"><div class="split split--reverse">
  <div class="split__text reveal">
    <span class="eyebrow">Founders &amp; Vision</span>
    <h2>A love story — and a vision of Moroccan hospitality</h2>
    <p class="lead">Dar Mansour is the vision of <a class="ilink" href="dar-mansour-founders-vision.html">Maïja</a> — a creative spirit who spent over 30 years immersed in Moroccan culture — and Bruno, a French entrepreneur who fell in love not only with Morocco, but with its most inspired ambassador.</p>
    <p style="margin-top:1.2rem;">Together they imagined a place where every meal is a story, every guest is welcomed like family, and every detail — from spices to music — carries the soul of Moroccan hospitality.</p>
    <a class="textlink" href="dar-mansour-founders-vision.html">Meet the founders {A}</a>
  </div>
  <div class="split__media reveal" data-delay="1">
    <img src="assets/img/maija-art-direction-koh-phangan.webp" alt="Maïja's artistic direction and Moroccan décor at Dar Mansour">
    <span class="tag">Art Direction · Maïja</span>
  </div>
</div></div></section>

<section class="section pd" id="private">
  <div class="pd__bg"><img src="assets/uploads/main%20room-%20ambiance-dar-mansour-%20Koh%20Phangan.webp" alt="Warm ambient lighting in the main dining room at Dar Mansour Koh Phangan, creating an intimate Moroccan atmosphere" style="object-position:center 55%"></div>
  <div class="wrap"><div class="reveal" style="max-width:560px;">
    <span class="eyebrow">Private Dining &amp; Celebrations</span>
    <h2 style="margin:1.2rem 0 1.3rem;">Celebrate life's most beautiful moments around a Moroccan table</h2>
    <p class="lead" style="color:var(--on-dark-soft);">Some evenings deserve more than a restaurant. Birthdays, anniversaries, proposals, honeymoons or intimate gatherings — thoughtfully curated in our peaceful candlelit garden between Sri Thanu and Hin Kong.</p>
    <ul class="pd__tags"><li>Birthdays</li><li>Anniversaries</li><li>Proposals</li><li>Honeymoons</li><li>Family Gatherings</li><li>Wellness Retreats</li></ul>
    <a class="btn btn--light" href="private-dining-koh-phangan.html">Plan Your Celebration</a>
  </div></div>
</section>

<section class="section" id="wine"><div class="wrap"><div class="split">
  <div class="split__media reveal">
    <img src="assets/uploads/Wine%20Pairing.jpg" alt="Moroccan prune tajine paired with a tawny port on the Dar Mansour wine pairing list, Koh Phangan">
    <span class="tag">Wine Pairing</span>
  </div>
  <div class="split__text reveal" data-delay="1">
    <span class="eyebrow">Wine Pairing &amp; The Mansour Bar</span>
    <h2>On the spiced path of Morocco</h2>
    <p class="lead">Wine here is more than a drink — it's a dialogue with the dish. We are proud to offer Koh Phangan's only dedicated Moroccan wine pairing menu, each label selected to elevate the warmth and aromatic depth of our slow food.</p>
    <p style="margin-top:1.2rem;">At The Mansour Bar, cocktails are a story, a scent, a spark of memory — from <em>Rock the Casbah</em> with Ras El Hanout syrup to the infamous Mansour's Jasminade.</p>
    <a class="textlink" href="moroccan-wine-pairing-koh-phangan.html">Explore wine &amp; cocktails {A}</a>
  </div>
</div></div></section>

<section class="section" id="reviews" style="background:var(--sand);"><div class="wrap">
  <div class="reviews__head reveal">
    <span class="eyebrow">What Our Guests Say</span>
    <h2 style="margin-top:1.1rem;">More than a restaurant — an immersive Moroccan experience</h2>
    <div class="rating"><span class="rating__stars">★★★★★</span><span>Loved by guests from around the world</span></div>
  </div>
  <div class="reviews__grid">
    <figure class="review reveal"><p>"As half Moroccan… I was eating and crying, crying and eating. You can feel the love in every bite."</p><footer><span class="avatar">O</span><cite>Oren</cite></footer></figure>
    <figure class="review reveal" data-delay="1"><p>"We dined seated on the floor, surrounded by carpets and lanterns — just like a Moroccan riad. A magical family evening."</p><footer><span class="avatar">M</span><cite>Mo. A</cite></footer></figure>
    <figure class="review reveal" data-delay="2"><p>"Deeply authentic Moroccan cuisine that blew me away. Cozy, stylish and full of charm."</p><footer><span class="avatar">D</span><cite>Daliah</cite></footer></figure>
    <figure class="review reveal"><p>"We were welcomed like old friends by Maija and Bruno. Msemen starters, slow-cooked tajines — everything was perfect."</p><footer><span class="avatar">A</span><cite>Alberto</cite></footer></figure>
    <figure class="review reveal" data-delay="1"><p>"It felt like being transported to a secret riad in Marrakech. A hidden gem with a beating heart."</p><footer><span class="avatar">K</span><cite>Kodi</cite></footer></figure>
    <figure class="review reveal" data-delay="2"><p>"As a Moroccan living in Koh Phangan, it felt amazing to feel at home instantly. More than a meal — an experience."</p><footer><span class="avatar">S</span><cite>Soukaina</cite></footer></figure>
  </div>
  <div class="center reveal" style="margin-top:2.5rem;"><a class="textlink" href="moroccan-restaurant-reviews-koh-phangan.html">Read more reviews {A}</a></div>
</div></section>

<section class="section"><div class="wrap reco">
  <div class="reveal">
    <span class="eyebrow">Recognition</span>
    <h2 style="margin:1.1rem auto 1.2rem;max-width:22ch;">Featured by Golf du Maroc among the world's notable Moroccan restaurants</h2>
    <p class="lead" style="max-width:60ch;margin-inline:auto;">Featured in <em>Golf du Maroc</em> magazine among the world's notable Moroccan culinary destinations — just two months after opening. A table carrying the Moroccan soul across continents.</p>
    <div style="margin-top:1.8rem;"><a class="textlink" href="best-moroccan-restaurant-world-press.html">Read the recognition {A}</a></div>
  </div>
</div></section>

<section class="section" style="padding-top:0;"><div class="wrap">
  <div class="center reveal" style="margin-bottom:2.5rem;"><div class="divider"><span>◇◇◇</span></div><h2 style="margin-top:1.5rem;">An evening at Dar Mansour</h2></div>
  <div class="gallery">
    <a class="g-tall reveal" href="assets/img/dar-mansour-entrance-night-koh-phangan.webp"><img src="assets/img/dar-mansour-entrance-night-koh-phangan.webp" alt="Dar Mansour entrance and lantern at dusk in Koh Phangan" loading="lazy"></a>
    <a class="reveal" data-delay="1" href="assets/img/moroccan-garden-candlelight-koh-phangan.webp"><img src="assets/img/moroccan-garden-candlelight-koh-phangan.webp" alt="Candlelit garden lantern at Dar Mansour at night" loading="lazy"></a>
    <a class="reveal" data-delay="2" href="assets/img/moroccan-pastries-mint-tea-koh-phangan.webp"><img src="assets/img/moroccan-pastries-mint-tea-koh-phangan.webp" alt="Artisanal Moroccan pastries and traditional mint tea" loading="lazy"></a>
    <a class="reveal" href="assets/img/moroccan-restaurant-central-room-koh-phangan.webp"><img src="assets/img/moroccan-restaurant-central-room-koh-phangan.webp" alt="Warm candlelit Moroccan lounge with colourful lanterns at Dar Mansour" loading="lazy"></a>
    <a class="g-wide reveal" data-delay="1" href="assets/img/moroccan-garden-lounge-night-koh-phangan.webp"><img src="assets/img/moroccan-garden-lounge-night-koh-phangan.webp" alt="Moroccan garden lounge at night at Dar Mansour" loading="lazy"></a>
    <a class="reveal" data-delay="2" href="assets/img/moroccan-zellige-fountain-koh-phangan.webp"><img src="assets/img/moroccan-zellige-fountain-koh-phangan.webp" alt="Brass tap on a green zellige mosaic fountain at Dar Mansour" loading="lazy"></a>
  </div>
</div></section>
''' + L.cta_band("Ready to taste Morocco in Koh Phangan?",
    "Reservations are highly recommended, with main dishes pre-ordered via WhatsApp — ideally 5 hours ahead of your booking. Tell us of any allergies or dietary needs — we'll do our best to adapt while staying true to our recipes.")

RESTAURANT_SCHEMA = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Restaurant","@id":"https://darmansour.com/#restaurant","name":"Dar Mansour - Morocco's Kitchen","alternateName":"Dar Mansour","slogan":"Rooted in tradition, slow cooked with care.","description":"Dar Mansour is a boutique Moroccan slow dining restaurant in Koh Phangan, Thailand, celebrating Moroccan hospitality through handcrafted cuisine, traditional slow cooking, curated wine pairings, contemporary art, music and immersive cultural experiences inspired by Morocco's rich culinary heritage.","servesCuisine":"Moroccan","priceRange":"$$$","url":"https://darmansour.com/","telephone":"+66822767757","email":"hello@darmansour.com","image":"https://darmansour.com/assets/img/moroccan-garden-dining-koh-phangan.jpg","hasMenu":"https://darmansour.com/moroccan-menu-koh-phangan.html","sameAs":["https://instagram.com/darmansour.kohphangan","https://www.facebook.com/people/Dar-Mansour/","https://share.google/Rp8YllnPe9Z9E9Va0","https://www.tripadvisor.com/Restaurant_Review-d32851492","https://www.wikidata.org/wiki/Q140585802","https://www.crunchbase.com/organization/dar-mansour-morocco-s-kitchen","https://www.openstreetmap.org/node/14021567355","https://maps.apple.com/place?place-id=I620A58D27664AA56&address=5%2F5+O+Bo+to+Ko+Pa-Ngan+Road%2C+Ko+Pha-Ngan%2C+Ko+Pha-Ngan+District%2C+Surat+Thani+84280%2C+Thailand&coordinate=9.753081%2C99.968740&name=Dar+Mansour+-+Morocco%27s+Kitchen&_provider=9902","https://www.bing.com/maps?ss=ypid.YN8178x5570947916035674182","https://www.pinterest.com/darmansourkohphangan/"],"address":{"@type":"PostalAddress","streetAddress":"Hin Kong Road, Sri Thanu area","addressLocality":"Koh Phangan","addressRegion":"Surat Thani","postalCode":"84280","addressCountry":"TH"},"geo":{"@type":"GeoCoordinates","latitude":9.753356308284413,"longitude":99.96873999581217},"acceptsReservations":"True","openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"19:00","closes":"22:30"}]}
</script>'''
HOME_SCHEMA = RESTAURANT_SCHEMA

pages["index.html"] = L.page(
    "Dar Mansour | Best Moroccan Restaurant in Koh Phangan — Slow Food &amp; Soulful Dining",
    "Discover Dar Mansour, a Moroccan restaurant in Koh Phangan. Authentic slow-cooked cuisine, romantic garden dinners and soulful hospitality. Book your table for a slow Moroccan dinner.",
    "", home_body, extra_head=HOME_SCHEMA)


# ============================================================ CONCEPT
concept_body = L.breadcrumb(("Concept", None)) + L.subhero(
    "Concept &amp; Operating Model", "Moroccan Slow Dining in Koh Phangan",
    "The art of hosting, redefined — pre-ordered dinners, reservations recommended, cooked with care and zero waste.",
    "assets/img/moroccan-arty-table-koh-phangan.jpg", "Artfully set Moroccan table at Dar Mansour") + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="lead">At Dar Mansour, the experience begins long before your arrival. As one of Koh Phangan's only Moroccan slow food restaurants, we embrace a rare and intentional philosophy: every dish is prepared to order, at the rhythm of traditional Moroccan cooking. While reservations are highly recommended, our signature slow-cooked dishes are available by pre-order, ideally with 5 hours' notice, allowing every meal to be crafted with patience, care and authenticity.</p>
  <p>Why? Because iconic Moroccan dishes like <strong>tanjia marrakchia</strong> and <a class="ilink" href="moroccan-menu-koh-phangan.html">fire-cooked tajines</a> need time, love and patience to reveal their full soul. Because we believe in honest, fresh cuisine — crafted without shortcuts, at the rhythm of the ingredients and those who cook them.</p>
  <div class="note"><p>"A thoughtful system designed with love — for the planet, for tradition, and for those who take time to eat well."</p></div>
  <h2>Our operating principles</h2>
  <ul class="bullets">
    <li><strong>By reservation</strong> — advance reservations via WhatsApp let us welcome every guest with the time, care and hospitality that define the Dar Mansour experience.</li>
    <li><strong>Pre-order tradition</strong> — our signature main dishes are pre-ordered, ideally 5 hours in advance, honouring traditional cooking times so they're ready the moment you arrive.</li>
    <li><strong>Zero waste philosophy</strong> — every dish is prepared to order, never mass-produced; by cooking only what is needed, we naturally reduce food waste and unnecessary excess.</li>
    <li><strong>Intimate by design</strong> — welcoming just 40 guests each evening, Dar Mansour was intentionally designed to preserve time, craftsmanship, genuine hospitality and the quality of every dish.</li>
  </ul>
  <div class="note"><p>Arriving without a reservation? You are always warmly welcome. Depending on the evening, we will be delighted to compose a selection from our menu for you. As each signature dish is slow-cooked to order in limited quantities, some may already have found their table, and a little patience is part of the ritual. For the full Dar Mansour experience, we simply invite you to reserve and pre-order your main dishes ahead.</p></div>
  <p>Located between Sri Thanu and Hin Kong — just minutes from The Alcove and Orion Healing Center — Dar Mansour is more than a restaurant. It's a slow food sanctuary for <a class="ilink" href="private-dining-koh-phangan.html">private dinners</a>, soulful celebrations and food-conscious travellers seeking meaning, beauty and flavour.</p>
</div></section>
''' + L.cta_band("Book your experience &amp; pre-order",
    "Perfect for private dinners, slow dining lovers and food-conscious travellers seeking a soulful culinary experience in Koh Phangan.") + L.related(
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Moroccan couscous"),
    ("Reservation", "How to Book", "moroccan-restaurant-reservation-koh-phangan.html", "assets/img/moroccan-restaurant-central-room-koh-phangan.jpg", "Central dining room"),
    ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"))
pages["moroccan-slow-dining-koh-phangan.html"] = L.page(
    "Concept &amp; Operating Model — Moroccan Slow Dining Koh Phangan",
    "Discover how Dar Mansour redefines hospitality in Koh Phangan through its Moroccan slow food concept. Reservations recommended, pre-ordered dinners, zero waste, cooked with care.",
    "moroccan-slow-dining-koh-phangan.html", concept_body,
    og_image="assets/img/moroccan-arty-table-koh-phangan.jpg")


# ============================================================ MENU
menu_body = L.breadcrumb(("Menu", None)) + L.subhero(
    "Our Moroccan Menu", "A tribute to Moroccan roots &amp; soulful flavours",
    "From ancient Berber staples to the aromatic influences of Moorish, Andalusian, Jewish and sub-Saharan cultures — slow cooked, served with soul.",
    "assets/uploads/Fez%27s%20Tajine.jpg", "A Fez-style chicken tajine with olives, herbs and preserved lemon at Dar Mansour", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap">
  <div class="prose reveal" style="text-align:center;">
    <h2>A journey to the roots of Moroccan cuisine — inspired by the Dadas</h2>
    <p>In the heart of Moroccan homes, the <a class="ilink" href="moroccan-hospitality-values-koh-phangan.html">Dadas</a> stand as iconic figures, preserving a culinary heritage passed down from generation to generation. Originally from Mali or Senegal, these women became the silent guardians of Moroccan family recipes — slow-cooked dishes full of generosity, depth and soul. It is their legacy we honour at Dar Mansour: food as love, patience and memory.</p>
  </div>
  <div style="max-width:820px;margin:2.5rem auto 0;">{render_legend()}</div>
  <div class="note reveal" style="max-width:820px;margin:1.4rem auto 0;"><p>All prices are in Thai Baht (฿). A 3% surcharge applies to card payments. Our Tajines, Tanjias and Couscous are freshly prepared to order in limited quantities — most requiring 1 to 5 hours of slow cooking. Pre-ordering via WhatsApp, ideally 5 hours ahead, is advised.</p></div>

{render_menu()}

  <div class="menu-note note reveal"><p>Each main dish is an individual serving, crafted for one guest. Like many slow-cooked meals, our dishes often taste even better the next day — don't hesitate to take home any leftovers to enjoy later.</p></div>
</div></section>
''' + L.cta_band("Ready to taste Morocco in Koh Phangan?",
    "Book now via WhatsApp to reserve your table and pre-order your soulful Moroccan dinner.") + L.related(
    ("Wine", "Wine Pairing", "moroccan-wine-pairing-koh-phangan.html", "assets/uploads/Wine%20Pairing.jpg", "Moroccan prune tajine paired with a tawny port at Dar Mansour"),
    ("Pantry", "Moroccan Pantry", "moroccan-pantry-koh-phangan.html", "assets/uploads/Preserved%20Lemons.jpg", "Jars of Moroccan preserved lemons"),
    ("Reservation", "Reserve &amp; Pre-order", "moroccan-restaurant-reservation-koh-phangan.html", "assets/uploads/Romantic%20Dinner-Dar-Mansour-Koh%20Phangan.webp", "A candlelit table set for a romantic dinner at Dar Mansour"))
pages["moroccan-menu-koh-phangan.html"] = L.page(
    "Moroccan Menu Koh Phangan — Tagines, Couscous &amp; Slow Food | Dar Mansour",
    "Explore Dar Mansour's menu in Koh Phangan: authentic Moroccan cuisine with tagines, couscous, tanjias and homemade bread. Cooked slow, served with soul.",
    "moroccan-menu-koh-phangan.html", menu_body,
    og_image="assets/img/moroccan-pastries-mint-tea-koh-phangan.jpg")


# ============================================================ RESERVATION
res_body = L.breadcrumb(("Reservation", None)) + L.subhero(
    "Reservation &amp; Pre-Order Recommended", "Slow-cooked Moroccan dishes, lovingly prepared just for you",
    "We highly recommend reserving your table and pre-ordering your main dishes in advance, to honour our slow food philosophy.",
    "assets/img/moroccan-restaurant-central-room-koh-phangan.jpg", "Central dining room at Dar Mansour") + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="lead">At Dar Mansour, each dish is a tribute to Moroccan tradition — infused with patience, soul and care. To honour this <a class="ilink" href="moroccan-slow-dining-koh-phangan.html">slow food philosophy</a>, we highly recommend reserving your table and pre-ordering your main dishes in advance.</p>
</div>
<div class="wrap" style="margin-top:clamp(2.5rem,5vw,3.5rem);">
  <div class="steps">
    <div class="step reveal"><span class="step__num">01</span><h3>Reserve via WhatsApp</h3><p>Message us to request your table. Reserving ahead secures your seat in our intimate garden and lets us prepare especially for you.</p></div>
    <div class="step reveal" data-delay="1"><span class="step__num">02</span><h3>Pre-order in advance</h3><p>We'll share the pre-order menu ahead of your visit. Choose your main dishes — ideally 5 hours ahead — so they're ready in time.</p></div>
    <div class="step reveal" data-delay="2"><span class="step__num">03</span><h3>Arrive &amp; savour</h3><p>Settle into the candlelit garden. Everything is made fresh to order — no shortcuts, no reheating.</p></div>
  </div>
</div>
<div class="wrap prose reveal" style="margin-top:clamp(2.5rem,5vw,3.5rem);">
  <h2>Why pre-order?</h2>
  <p>Our <a class="ilink" href="moroccan-menu-koh-phangan.html">Tajines, Tanjias and Couscous</a> are slow-cooked in small quantities, taking between 1 and 5 hours to cook. To ensure dish availability and avoid a long wait upon arrival (often more than an hour), we kindly ask guests to pre-order via WhatsApp, ideally 5 hours ahead of their booking. This lets us:</p>
  <ul class="bullets">
    <li>Cook at the rhythm of our traditions</li>
    <li>Maintain high quality and freshness</li>
    <li>Eliminate waste and preserve the planet</li>
    <li>Offer you a seamless, soulful dining experience</li>
  </ul>
  <div class="note"><p><strong>Allergy &amp; dietary notes:</strong> please inform us of any allergies or dietary restrictions when placing your pre-order. We'll do our best to adapt while staying true to our recipes.</p></div>
</div></section>
''' + L.cta_band("I want to book a table &amp; pre-order",
    "Dinner only, Tuesday to Saturday. Reserve your evening and pre-order your slow-cooked Moroccan feast.") + L.related(
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Moroccan couscous"),
    ("Wine", "Wine Pairing", "moroccan-wine-pairing-koh-phangan.html", "assets/uploads/Wine%20Pairing.jpg", "Moroccan prune tajine paired with a tawny port at Dar Mansour"),
    ("FAQ", "Good to Know", "faq.html", "assets/img/moroccan-pastries-mint-tea-koh-phangan.jpg", "Pastries and mint tea"))
pages["moroccan-restaurant-reservation-koh-phangan.html"] = L.page(
    "Reservation at Dar Mansour — Moroccan Slow Food in Koh Phangan",
    "Book your table at Dar Mansour, the Moroccan restaurant in Koh Phangan. Pre-order recommended for slow-cooked tajines, couscous and tanjias. Dine with love.",
    "moroccan-restaurant-reservation-koh-phangan.html", res_body,
    og_image="assets/img/moroccan-restaurant-central-room-koh-phangan.jpg")


# ============================================================ WINE
wine_body = L.breadcrumb(("Wine Pairing", None)) + L.subhero(
    "Wine Pairing Experience", "Crafted to enhance every bite — on the spiced path of Morocco",
    "Koh Phangan's only dedicated Moroccan wine pairing list — natural, characterful labels chosen to elevate the soul of our slow food.",
    "assets/uploads/Wine%20Pairing.jpg", "Moroccan prune tajine paired with a Porto Maynard's tawny at Dar Mansour", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap">
  <div class="prose reveal" style="text-align:center;">
    <p class="lead">At Dar Mansour, wine is more than a drink — it's a dialogue with the dish. Each label in our curated list is selected to elevate the complexity, warmth and aromatic depth of <a class="ilink" href="moroccan-slow-dining-koh-phangan.html">Moroccan slow food</a>.</p>
  </div>
  <div style="margin-top:clamp(2.5rem,5vw,3.5rem);">
{render_wine_feature()}
{render_wine_groups()}
  </div>
  <div class="center reveal" style="margin-top:2.6rem;">
    <p class="lead" style="max-width:60ch;margin:0 auto 1.4rem;">Let us guide you to the perfect pairing — every wine has been carefully matched to highlight the soul of Moroccan cuisine.</p>
    <a class="textlink" href="moroccan-cocktails-koh-phangan.html">Discover The Mansour Bar &amp; cocktails {A}</a>
  </div>
</div></section>
''' + L.cta_band("Book your dinner &amp; discover your perfect pairing",
    "Reserve your evening and let us match each dish to a wine that sings.") + L.related(
    ("The Bar", "Cocktails &amp; Classics", "moroccan-cocktails-koh-phangan.html", "assets/img/mansour-bar-cocktail-sand-koh-phangan.jpg", "Signature Mansour Bar cocktail"),
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Moroccan couscous"),
    ("Private Dining", "Celebrations", "private-dining-koh-phangan.html", "assets/img/moroccan-round-table-koh-phangan.jpg", "Round table"))
pages["moroccan-wine-pairing-koh-phangan.html"] = L.page(
    "Moroccan Wine Pairing — Slow Food &amp; Natural Wines Koh Phangan | Dar Mansour",
    "Discover Koh Phangan's only curated Moroccan wine pairing list. Wines selected to elevate each dish, from tagines to couscous, at Dar Mansour.",
    "moroccan-wine-pairing-koh-phangan.html", wine_body,
    og_image="assets/uploads/Wine%20Pairing.jpg", body_class="page-wine")


# ============================================================ MANSOUR BAR / COCKTAILS
bar_body = L.breadcrumb(("The Mansour Bar", None)) + L.subhero(
    "The Mansour Bar", "Cocktails, classics &amp; nightcaps — a Moroccan-inspired experience",
    "Blending spices, flowers, herbs and local infusions — playful mixology, relaxed barefoot nights and beautiful company.",
    "assets/uploads/mansour-bar-hero.webp", "Artwork for The Mansour Bar at Dar Mansour, Koh Phangan", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap">
  <div class="prose reveal" style="text-align:center;">
    <p class="lead">At Dar Mansour, cocktails are more than a drink — they're a story, a scent, a spark of memory. The Mansour Bar invites you to explore <a class="ilink" href="moroccan-menu-koh-phangan.html">Moroccan flavours</a> through playful mixology.</p>
  </div>
  <div style="margin-top:clamp(2.5rem,5vw,3.5rem);">
{render_cocktails()}
  </div>
  <div class="drink-group reveal" style="margin-top:clamp(2.5rem,5vw,3.5rem);">
    <span class="drink-group__title">Hot Drinks</span>
    <div class="menu-item"><div class="menu-item__head"><span class="menu-item__name">Traditional Mint Tea</span><span class="menu-item__leader"></span><span class="menu-item__price">90 / 180</span></div><p class="menu-item__desc">Green tea steeped with fresh mint and sugar, poured to aerate and served warm. (Glass / pot.)</p></div>
    <div class="menu-item"><div class="menu-item__head"><span class="menu-item__name">Moroccan Coffee</span><span class="menu-item__leader"></span><span class="menu-item__price">100</span></div><p class="menu-item__desc">Dark roasted coffee blended with cinnamon, ginger, nutmeg, cardamom, clove, black pepper and star anise.</p></div>
  </div>
  <p class="book__meta center" style="margin-top:2.2rem;">All prices in Thai Baht. A 3% surcharge applies to card payments. Please drink responsibly.</p>
</div></section>
''' + L.cta_band("Toast to the moment", "Reserve your evening and sip Moroccan flavours under the stars.") + L.related(
    ("Wine", "Wine Pairing", "moroccan-wine-pairing-koh-phangan.html", "assets/uploads/Wine%20Pairing.jpg", "Moroccan prune tajine paired with a tawny port at Dar Mansour"),
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Moroccan couscous"),
    ("Private Dining", "Celebrations", "private-dining-koh-phangan.html", "assets/img/moroccan-round-table-koh-phangan.jpg", "Round table"))
pages["moroccan-cocktails-koh-phangan.html"] = L.page(
    "The Mansour Bar — Moroccan-Inspired Cocktails in Koh Phangan | Dar Mansour",
    "Discover the art of mixology at The Mansour Bar in Koh Phangan. Moroccan-inspired cocktails, timeless classics and non-alcoholic creations in a soulful atmosphere.",
    "moroccan-cocktails-koh-phangan.html", bar_body,
    og_image="assets/img/moroccan-arty-table-koh-phangan.jpg")


# ============================================================ ARTISTIC DIRECTION
art_body = L.breadcrumb(("Artistic Direction", None)) + L.subhero(
    "Artistic Direction &amp; Décor", "Art as identity",
    "A soulful space where Moroccan craftsmanship meets bold artistic vision — a living gallery of visual culture and culinary heritage.",
    "assets/uploads/Stay%20Calm%20and%20Drink%20Berber%20Whisky.webp", "Stay Calm and Drink Berber Whisky — a playful artwork celebrating Moroccan mint tea at Dar Mansour", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="lead">At Dar Mansour, art is not an afterthought — it's who we are. From ancestral Moroccan craft to striking contemporary works, the space is curated as a living gallery where visual culture and culinary heritage come together. Every detail tells a story; every corner speaks of identity.</p>
  <h2>Currently on display</h2>
  <ul class="bullets">
    <li><strong>Ghita Benlamlih</strong> reimagines cultural icons with humour and audacity — think Madonna in Berber dress, or Mandela in a red tarbouch.</li>
    <li><strong>Kamel Ghabte</strong>, with his <em>Echoes of Morocco</em> series, explores memory and identity through powerful digital compositions.</li>
  </ul>
  <p>Each piece is credited and presented with love — even in unexpected corners (yes, even the restrooms), because at Dar Mansour, art belongs everywhere.</p>
  <h2>Design as immersion</h2>
  <p>The design of Dar Mansour, signed by <strong>Eden &amp; Beyond</strong> (<a class="ilink" href="https://www.instagram.com/edenandbeyond.kpg/" target="_blank" rel="noopener">Maïja</a>'s interior and creative studio), blends the sensual warmth of Moroccan tradition with contemporary aesthetics. From handcrafted zellige mosaic fountains to earthen steps, from textured lime-washed walls to tables reimagined as sculptures — every material, light source and tactile element invites you to slow down and feel, with all your senses.</p>
  <p><strong>This is Moroccan design reinterpreted.</strong> Eden &amp; Beyond works with the raw authenticity of a "F**k the Box" mindset, revealing a universe of one-of-a-kind pieces: no two tables are alike, each one a unique art piece in a contemporary Moroccan idiom. Even the lamps have names — Kenzo, Kenza, Leïla — individual characters as much as light sources.</p>
  <h2>Music Direction</h2>
  <p>The soundtrack is part of the evening. <em>Dar Mansour Groove — Volume I</em> is our first official playlist — a cosmopolitan blend of North African heritage, European alternative culture and global rhythms, balancing vintage sensuality, desert mystique and underground elegance. <a class="ilink" href="https://open.spotify.com/playlist/5A0Qw5uEZiCyLNweh4nQ76" target="_blank" rel="noopener">Listen on Spotify ↗</a></p>
  <p>A second, more private set plays in an unexpected corner. Curated by <strong>DJ Mans</strong>, the restroom playlist is a fully old-school Moroccan selection — Berber vinyl classics, Gnawa rhythms and Casablanca beats from the '60s and '70s — turning a simple pause into a small detour of its own.</p>
</div></section>
''' + L.cta_band("Experience it in person",
    "The best way to feel our artistic direction is around a candlelit table. Reserve your evening at Dar Mansour.") + L.related(
    ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"),
    ("Spirit", "The Mansour Spirit", "moroccan-hospitality-values-koh-phangan.html", "assets/uploads/mansour-spirit-monk.webp", "A Buddhist monk arranging artwork — the spirit of hospitality and cultural respect"),
    ("Experience", "The Experience", "index.html", "assets/uploads/Kamel%20Ghabte-%20women%20-men%20-rest%20room-%20dar%20mansour-koh%20phangan.webp", "Colourful Kamel Ghabte pop-art portraits at Dar Mansour, Koh Phangan"))
pages["moroccan-interior-art-koh-phangan.html"] = L.page(
    "Moroccan Art &amp; Interior Design in Koh Phangan — Dar Mansour",
    "Step inside Dar Mansour — a soulful space where Moroccan craftsmanship and bold artistic vision meet. A celebration of identity, heritage and creative expression.",
    "moroccan-interior-art-koh-phangan.html", art_body,
    og_image="assets/img/maija-art-direction-koh-phangan.jpg")


# ============================================================ RECOGNITION
reco_body = L.breadcrumb(("Recognition", None)) + L.subhero(
    "Recognition", "Featured by Golf du Maroc among the world's notable Moroccan restaurants",
    "As seen in Golf du Maroc magazine — a table carrying the Moroccan soul across continents.",
    "assets/uploads/Dar%20Mansour%20Morocco%27s%20Kitchen%20Koh%20Phangan.jpg", "The illuminated Dar Mansour entrance sign with a Moroccan candle lantern at dusk in Koh Phangan", tall=True, focus="center 22%") + f'''
<section class="section"><div class="wrap prose reveal">
  <span class="eyebrow">Golf du Maroc Magazine · Gastronomy</span>
  <h2>"Morocco under different skies"</h2>
  <p>In an international gastronomy feature titled <em>Morocco Under Different Skies</em>, journalist Carole Belahrach set out, for <strong>Golf du Maroc</strong> magazine, to find the tables that carry Morocco's soul beyond its borders: <em>"When traveling abroad, you want to get away from it all and taste the local cuisine — just as you might want to discover the places that showcase Morocco and its gastronomy."</em> From Hamburg to New York and Los Angeles, the magazine's journey led — among a handful of chosen addresses — to a small tropical island in Thailand.</p>
  <figure class="tearsheet reveal">
    <a href="assets/uploads/Golf%20du%20Maroc%20english%20version.jpg" target="_blank" rel="noopener">
      <img src="assets/uploads/Golf%20du%20Maroc%20english%20version.jpg" alt="Dar Mansour featured in Golf du Maroc magazine among the world's notable Moroccan culinary destinations" loading="lazy">
    </a>
    <figcaption>As featured in Golf du Maroc Magazine</figcaption>
  </figure>
  <article class="press__card press__card--feature reveal">
    <span class="press__source">Golf du Maroc — "Dar Mansour, a tribute to dadas"</span>
    <p class="press__quote">"This is a place imagined as an oasis for nomads in search of new experiences. At Dar Mansour, guests savor traditional, generous, and authentic home-style Moroccan cuisine, lovingly prepared by two 'veterans of Morocco.' But Dar Mansour is more than just a restaurant — it's a space that embodies the values of Moroccan hospitality."</p>
    <p>"The cooking follows time-honored practices: tanjia, tajines, salads, msemmen, tafernout… The owners lived in Morocco for nearly 30 years, long enough to master the country's culinary traditions. They also trained under professionals in Marrakech — and with a dada (traditional female cook), to whom every dish pays tribute. From ingredients to tableware and décor, everything has been brought straight from Morocco. Absolutely everything is homemade — even the smen (fermented butter) and preserved lemons. The restaurant works on a pre-order basis to honor the principle of slow cooking and to reduce waste, embracing an eco-conscious philosophy."</p>
    <span class="press__byline">Feature by Carole Belahrach · Golf du Maroc Magazine</span>
  </article>
  <h2>In extraordinary company</h2>
  <p>The feature gathered some of the most celebrated Moroccan tables in the world. We are humbled to be listed alongside:</p>
  <ul class="bullets">
    <li><strong>Piment</strong> — Hamburg. The Michelin-starred restaurant of Casablanca-born chef Wahabi Nouri.</li>
    <li><strong>Café Mogador</strong> — New York. A beloved family-run institution since 1983, in the East Village and Williamsburg.</li>
    <li><strong>Zerza</strong> — New York. A Lower East Side favourite for zaalouk, couscous and tajines.</li>
    <li><strong>Tagine Beverly Hills</strong> — Los Angeles. Co-founded in 2004 by actor Ryan Gosling, with chef Ben (Abdessamad Benameur) from Larache.</li>
  </ul>
  <p>And now, Dar Mansour — born not in Casablanca or Marrakech, but on a small tropical island in Thailand — proud to represent the spirit of Morocco with heart, care and authenticity.</p>
  <h2>Read the full feature</h2>
  <p>The complete article — <em>Morocco Under Different Skies</em>, by Carole Belahrach, as published in Golf du Maroc magazine. Tap any page to read it in the viewer, then use the arrows to flip through.</p>
  <div class="pressgallery reveal">
    <figure><a href="assets/uploads/Golf%20du%20Maroc1.jpg" target="_blank" rel="noopener"><img src="assets/uploads/Golf%20du%20Maroc1.jpg" alt="Golf du Maroc feature cover — Morocco Under Different Skies" loading="lazy"></a><figcaption>The cover</figcaption></figure>
    <figure><a href="assets/uploads/golf%20du%20maroc%202.jpg" target="_blank" rel="noopener"><img src="assets/uploads/golf%20du%20maroc%202.jpg" alt="Magazine page featuring Dar Mansour (Thailand) and Piment (Germany)" loading="lazy"></a><figcaption>Dar Mansour &amp; Piment</figcaption></figure>
    <figure><a href="assets/uploads/golf%20du%20Maroc%203.jpg" target="_blank" rel="noopener"><img src="assets/uploads/golf%20du%20Maroc%203.jpg" alt="Magazine page featuring Café Mogador, Zerza and Tagine Beverly Hills in the United States" loading="lazy"></a><figcaption>United States</figcaption></figure>
  </div>
  <h2>A Moroccan table in Koh Phangan</h2>
  <p>This recognition came just two months after our opening. It honours not just our cuisine, but the values we hold dear:</p>
  <ul class="bullets">
    <li>The warmth of Moroccan hospitality</li>
    <li>The legacy of <a class="ilink" href="moroccan-slow-dining-koh-phangan.html">slow, soulful cooking</a></li>
    <li>The beauty of gathering and sharing a table</li>
  </ul>
  <p>We're incredibly grateful for this acknowledgment — and we dedicate it to everyone who believed in this journey.</p>
  <h2>Featured in the local press</h2>
  <p>Closer to home, Koh Phangan's own publications have shared our story too.</p>
  <div class="press">
    <article class="press__card reveal">
      <span class="press__source">Phanganist</span>
      <p class="press__quote">"If Koh Phangan had a secret door to another world, it might open somewhere in Sri Thanu — behind warm light, textured walls, and a soundtrack designed to slow the rhythm of the evening."</p>
      <a class="textlink" href="https://phanganist.com/koh-phangan/dar-mansour-morocco-kitchen-slow-dining-big-soul-and-taste-morocco-koh-phangan" target="_blank" rel="noopener">Read the full article {A}</a>
    </article>
    <article class="press__card reveal" data-delay="1">
      <span class="press__source">Phangan Life</span>
      <p class="press__quote">Dar Mansour, Morocco's Kitchen — featured among the island's finest world-cuisine tables in the Phangan Life guide.</p>
      <a class="textlink" href="https://phanganlife.com/catalog/restaurants-and-cafes/world-cuisine/dar-mansour-moroccos-kitchen" target="_blank" rel="noopener">View the listing {A}</a>
    </article>
  </div>
</div></section>
''' + L.cta_band("Taste what the world is talking about",
    "Reserve your evening and discover the slow-cooked Moroccan cuisine that carries our soul across continents.") + L.related(
    ("Reviews", "What Guests Say", "moroccan-restaurant-reviews-koh-phangan.html", "assets/img/moroccan-garden-lounge-koh-phangan.jpg", "Interior"),
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Couscous"),
    ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"))
pages["best-moroccan-restaurant-world-press.html"] = L.page(
    "Dar Mansour — Featured by Golf du Maroc | Notable Moroccan Dining",
    "Featured in Golf du Maroc, Phanganist and Phangan Life, Dar Mansour is recognised among the world's notable Moroccan culinary destinations and celebrated on Koh Phangan for its slow-cooked Moroccan soul food.",
    "best-moroccan-restaurant-world-press.html", reco_body,
    og_image="assets/img/dar-mansour-front-koh-phangan.jpeg")


# ============================================================ REVIEWS
REVIEWS = [
    ("Oren","O","As half Moroccan… I was eating and crying, crying and eating. Maija is a kind, authentic woman — you can feel the love in every bite."),
    ("Mo. A","M","We dined seated on the floor, surrounded by elegant décor, carpets and lanterns — just like in a Moroccan riad. A magical family evening."),
    ("Daliah","D","The food was absolutely out of this world… deeply authentic Moroccan cuisine that blew me away. Cozy, stylish and full of charm."),
    ("Valesca","V","Communication via WhatsApp was smooth… every dish was packed with love and flavour. Highly recommended."),
    ("Alberto","A","We were welcomed like old friends by Maija and Bruno. Msemen starters, slow-cooked tajines, a lovely bottle of wine — everything was perfect."),
    ("Soukaina","S","As a Moroccan living in Koh Phangan, it felt amazing to step in and feel at home instantly. It's more than just a meal — it's an experience."),
    ("Simon","S","A romantic dinner that brought back so many memories of Morocco. We ate wonderfully and can't wait to return."),
    ("Kodi","K","The flavours, the ambiance, the music… it felt like being transported to a secret riad in Marrakech. A hidden gem with a beating heart."),
]
rev_cards = "".join(f'''      <figure class="review reveal">
        <p>"{q}"</p>
        <footer><span class="avatar">{i}</span><cite>{n}</cite></footer>
      </figure>''' for n,i,q in REVIEWS)
reviews_body = L.breadcrumb(("Reviews", None)) + L.subhero(
    "What Our Guests Say", "More than a restaurant — an immersive Moroccan experience",
    "From our tajines to the warmth of our welcome, discover why guests from around the world call us one of the best Moroccan restaurants in Thailand.",
    "assets/img/maija-art-direction-koh-phangan.jpg", "Warm candlelit Moroccan interior at Dar Mansour") + f'''
<section class="section"><div class="wrap">
  <div class="center reveal" style="margin-bottom:2.5rem;"><div class="rating"><span class="rating__stars">★★★★★</span><span>Google Reviews</span></div></div>
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;margin:2rem 0 1.5rem;color:#1a1a1a;">Featured Guest Reviews</h3>
  <div class="reviews__grid">
{rev_cards}
  </div>
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;margin:3rem 0 1.5rem;color:#1a1a1a;">All Google Reviews</h3>
  <script src="https://elfsightcdn.com/platform.js" async></script>
  <div class="elfsight-app-5bfc57f3-42b7-4a48-9677-31510ee6435e" data-elfsight-app-lazy style="margin:2rem 0;"></div>
</div></section>
''' + L.cta_band("Come and write your own story", "Reserve your evening and discover the experience for yourself.") + L.related(
    ("Recognition", "In the Press", "best-moroccan-restaurant-world-press.html", "assets/img/dar-mansour-front-koh-phangan.jpeg", "Storefront"),
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Couscous"),
    ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"))
pages["moroccan-restaurant-reviews-koh-phangan.html"] = L.page(
    "Reviews of Dar Mansour — Best Moroccan Restaurant in Koh Phangan",
    "Discover what guests say about Dar Mansour in Koh Phangan. A soulful Moroccan dining experience praised for its authenticity, atmosphere and heart.",
    "moroccan-restaurant-reviews-koh-phangan.html", reviews_body,
    og_image="assets/img/maija-art-direction-koh-phangan.jpg")


# ============================================================ PANTRY
PANTRY = [
    ("Charmoula","More than a marinade, charmoula is a beloved base in Moroccan kitchens — a vibrant blend used as sauce, condiment or seasoning for everything from grilled fish to roasted vegetables. Made with garlic, olive oil, lemon juice, fresh herbs and spices, it varies from region to region and even family to family."),
    ("Couscous","Made from coarsely ground durum wheat (semolina), moistened with water and olive oil, hand-rolled, then steamed in a couscoussière and fluffed for a light, airy texture. The steaming is repeated up to four times until perfectly tender."),
    ("Couscoussier","A traditional steamer with two chambers: the lower pot simmers meats or vegetables, while the upper couscoussière steams the couscous, letting it absorb the rising aromatic vapours through tiny holes in its base."),
    ("Harissa","A traditional Moroccan condiment, typically made by grinding fresh garlic and dried chilies with spices and olive oil. Our version balances mild dried chilies with dried tomatoes, garlic, coriander, fennel seeds and a touch of salt."),
    ("Organic Saffron from Taliouine","From a women-led cooperative of 20 families cultivating it at 1,200 metres in the Anti-Atlas Mountains. Known as Morocco's “Red Gold,” it is hand-harvested from thousands of delicate purple flowers and sun-dried in traditional clay ovens."),
    ("Preserved Lemon","Organic lemons from Cha-Am Lemon Farm in Thailand's Phetchaburi region, preserved in salt for several months. They offer an intense, tangy brightness to tajines and other dishes — and keep for up to two years."),
    ("Ras el Hanout","A complex spice blend often used in tagines and couscous. The name means “head of the shop,” signifying the best the merchant has to offer. Our recipe blends over 15 spices in-house."),
    ("Smen","Clarified cow butter fermented for months and lightly salted, used to elevate tajines and tanjias. Ours is infused with oregano for an earthy, tangy aroma."),
    ("Tfaya","A traditional topping of onions and raisins slowly caramelised with cinnamon, honey and butter. Tfaya adds a signature sweetness to savoury dishes, especially couscous."),
]
pantry_cards = "".join(f'''    <div class="pantry__item reveal"><h3>{n}</h3><p>{d}</p></div>''' for n,d in PANTRY)
pantry_body = L.breadcrumb(("Moroccan Pantry", None)) + L.subhero(
    "Moroccan Pantry: Stories &amp; Staples", "Our culinary roots, one ingredient at a time",
    "From the red hills of Taliouine to the family kitchens of Rabat — a pantry of soul, taste and tradition.",
    "assets/uploads/Ras%20El%20Hanout-2.jpg", "Ras el Hanout and Moroccan spices, the heart of the Dar Mansour pantry", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap">
  <div class="prose reveal" style="text-align:center;margin-bottom:clamp(2.5rem,5vw,3.5rem);">
    <p class="lead">At Dar Mansour, every ingredient carries a story. Our pantry is filled with traditions passed down by <a class="ilink" href="moroccan-hospitality-values-koh-phangan.html">generations of Moroccan women</a>. Here are some of the staples we love and use — with care and authenticity.</p>
  </div>
  <div class="dishes dishes--photos" style="margin-bottom:clamp(2.5rem,5vw,3.5rem);">
    <article class="dish reveal"><img src="assets/uploads/Preserved%20Lemons.jpg" alt="Jars of Moroccan preserved lemons with fresh lemons" loading="lazy"><div class="dish__label"><h3>Preserved Lemons</h3></div></article>
    <article class="dish reveal" data-delay="1"><img src="assets/uploads/Ras%20El%20Hanout-2.jpg" alt="Ras el Hanout Moroccan spice blend surrounded by bowls of spices" loading="lazy"><div class="dish__label"><h3>Ras el Hanout</h3></div></article>
    <article class="dish reveal" data-delay="2"><img src="assets/uploads/Smen-2.jpg" alt="Smen, Moroccan fermented clarified butter in a painted bowl" loading="lazy"><div class="dish__label"><h3>Smen</h3></div></article>
  </div>
  <div class="pantry">
{pantry_cards}
  </div>
</div></section>
''' + L.cta_band("Want to taste it all?", "Discover how these staples come alive across our slow-cooked menu.") + L.related(
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Couscous"),
    ("Wine", "Wine Pairing", "moroccan-wine-pairing-koh-phangan.html", "assets/uploads/Wine%20Pairing.jpg", "Moroccan prune tajine paired with a tawny port at Dar Mansour"),
    ("Concept", "Slow Dining", "moroccan-slow-dining-koh-phangan.html", "assets/uploads/Arty%20table-Dar-Mansour-%20Koh%20Phangan.webp", "Moroccan art books and candlelight on an arty table at Dar Mansour"))
pages["moroccan-pantry-koh-phangan.html"] = L.page(
    "Moroccan Pantry &amp; Ingredients — Dar Mansour Koh Phangan",
    "Discover the stories behind Moroccan ingredients like charmoula, saffron and preserved lemon. A pantry of soul, taste and tradition.",
    "moroccan-pantry-koh-phangan.html", pantry_body,
    og_image="assets/img/moroccan-restaurant-central-room-koh-phangan.jpg")


# ============================================================ MANSOUR SPIRIT
spirit_body = L.breadcrumb(("Mansour Spirit", None)) + L.subhero(
    "The Mansour Spirit", "Savour the beautiful, the good, and the moment",
    "A peaceful oasis where Moroccan hospitality meets Thai cultural respect — harmony, gratitude and barefoot freedom.",
    "assets/uploads/mansour-spirit-monk.webp", "A Buddhist monk arranging framed artwork on an ochre wall — the spirit of hospitality and cultural respect", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="lead">Mansour Spirit is about more than food — it's about embracing the values of the place we're in. As proud guests of the Kingdom of Thailand, we hold deep respect for its culture, its laws and the spirit of harmony that defines it. Honouring Thai values is not just a duty — it's a sincere expression of gratitude.</p>
  <h2>A few gentle requests</h2>
  <p>To preserve this peaceful energy, we kindly ask our guests to:</p>
  <ul class="bullets">
    <li>Dress respectfully (no bare chests)</li>
    <li>Remove shoes where required</li>
    <li>Refrain from disruptive behaviour</li>
  </ul>
  <p>To maintain the calm and welcoming nature of the space, we reserve the right to refuse service to intoxicated guests. In accordance with Thai law and our commitment to responsible hospitality, no illegal substances — including marijuana — are permitted on the premises.</p>
  <h2>A peaceful oasis</h2>
  <p>Dar Mansour is a place of <a class="ilink" href="moroccan-slow-dining-koh-phangan.html">slowness</a>, barefoot freedom and quiet joy — anchored in gratitude for Thai hospitality and open cultural dialogue. We believe in harmony, presence and generosity — in savouring life, dish by dish, moment by moment.</p>
  <p style="font-family:var(--serif);font-style:italic;font-size:1.4rem;color:var(--green-deep);">With gratitude,<br>Mansour's Family.</p>
</div></section>
''' + L.cta_band("Come and feel it",
    "Slow down, breathe, and savour the moment around a Moroccan table. Reserve your evening at Dar Mansour.") + L.related(
    ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"),
    ("Art", "Artistic Direction", "moroccan-interior-art-koh-phangan.html", "assets/img/maija-art-direction-koh-phangan.jpg", "Art direction"),
    ("Experience", "The Experience", "index.html", "assets/uploads/amabiance-arty-dar%20mansour-koh%20phangan.webp", "Warm candlelit tables in the main room at Dar Mansour"))
pages["moroccan-hospitality-values-koh-phangan.html"] = L.page(
    "Mansour Spirit — Moroccan Hospitality &amp; Thai Values in Koh Phangan",
    "Dar Mansour is a peaceful oasis where Moroccan hospitality meets Thai cultural respect. Discover our values of harmony, gratitude and barefoot freedom in Koh Phangan.",
    "moroccan-hospitality-values-koh-phangan.html", spirit_body,
    og_image="assets/img/moroccan-garden-dining-koh-phangan.jpg")


# ============================================================ FOUNDERS
founders_body = L.breadcrumb(("Founders", None)) + L.subhero(
    "Founders &amp; Vision", "A love story — and a vision of Moroccan hospitality",
    "Meet Maïja and Bruno, who created a soulful Moroccan dining experience rooted in love and tradition.",
    "assets/uploads/mod_aimant1.jpg", "Maïja and Bruno, founders of Dar Mansour, sharing a tender embrace", tall=True, variant="portrait") + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="lead">Dar Mansour is the vision of <strong>Maïja</strong> — a creative spirit who spent over 30 years immersed in Moroccan culture — and <strong>Bruno</strong>, a French entrepreneur who once lived in China, and who fell in love… not only with Morocco, but with its most inspired ambassador.</p>
  <p>Together, they imagined a place where every meal is a story, every guest is welcomed like family, and every detail — from spices to music — carries the soul of Moroccan hospitality.</p>
  <p>Dar Mansour is more than a restaurant. It's the meeting point of two lives, two cultures, and a shared dream: to celebrate slow food, meaningful connection and the timeless elegance of Moroccan cuisine and culture — from a quiet garden in Koh Phangan.</p>
  <p>Many of the recipes we serve today were passed down through the <a class="ilink" href="journal-the-dadas-guardians-of-moroccan-recipes.html">Dadas</a> who cooked for Maïja's stepmother's family in Morocco — never written in cookbooks, but learned side by side, gesture by gesture, across generations.</p>
  <p>Every corner of the restaurant carries her hand, too. The design of Dar Mansour is signed by <a class="ilink" href="https://www.instagram.com/edenandbeyond.kpg/" target="_blank" rel="noopener">Eden &amp; Beyond</a>, Maïja's interior and creative studio — the handcrafted zellige fountains, earthen steps and lime-washed walls are as considered as anything on the menu. See more of the space in our <a class="ilink" href="moroccan-interior-art-koh-phangan.html">artistic direction</a>.</p>
  <div class="note"><p>Guided by the wisdom of the Dadas, Maïja carries forward the spirit of Moroccan hospitality with a contemporary soul. In the kitchen, P'Jae, our local partner and Head of Kitchen, brings these traditions to life each evening through refined, <a class="ilink" href="moroccan-menu-koh-phangan.html">slow-cooked dishes</a> prepared with patience, care, and respect for time-honoured recipes.</p></div>
</div></section>
''' + L.cta_band("Share our table",
    "Come and become part of the story. Reserve your evening at Dar Mansour and be welcomed like family.") + L.related(
    ("Reviews", "Through Our Guests' Eyes", "moroccan-restaurant-reviews-koh-phangan.html", "assets/img/moroccan-garden-lounge-koh-phangan.jpg", "Interior"),
    ("Art", "Artistic Direction", "moroccan-interior-art-koh-phangan.html", "assets/img/maija-art-direction-koh-phangan.jpg", "Art direction"),
    ("Spirit", "The Mansour Spirit", "moroccan-hospitality-values-koh-phangan.html", "assets/uploads/mansour-spirit-monk.webp", "A Buddhist monk arranging artwork — the spirit of hospitality and cultural respect"))
pages["dar-mansour-founders-vision.html"] = L.page(
    "The Story of Dar Mansour — Founders &amp; Vision",
    "Meet the founders of Dar Mansour in Koh Phangan. Discover how Maïja and Bruno created a soulful Moroccan dining experience rooted in love and tradition.",
    "dar-mansour-founders-vision.html", founders_body,
    og_image="assets/img/moroccan-restaurant-entrance-koh-phangan.jpg")


# ============================================================ PRIVATE DINING
pd_body = L.breadcrumb(("Private Dining", None)) + L.subhero(
    "Private Dining &amp; Celebrations", "Celebrate life's most beautiful moments around a Moroccan table",
    "Birthdays, anniversaries, proposals and intimate gatherings — thoughtfully curated in our peaceful candlelit garden.",
    "assets/img/moroccan-restaurant-central-room-koh-phangan.jpg", "Warm candlelit Moroccan lounge with low tables and lanterns, set for a private celebration", tall=True) + f'''
<section class="section"><div class="wrap prose reveal">
  <p class="lead">Some evenings deserve more than a restaurant. Whether you're celebrating a birthday, anniversary, engagement, family gathering, honeymoon, or simply bringing together people you love, Dar Mansour offers an intimate Moroccan dining experience designed to create lasting memories.</p>
  <p>Set in our peaceful candlelit garden between Sri Thanu and Hin Kong, every celebration is thoughtfully curated with the warmth of <a class="ilink" href="moroccan-hospitality-values-koh-phangan.html">Moroccan hospitality</a>, slow-cooked cuisine, beautiful music and attentive service. Because every gathering is unique, we tailor your evening to feel personal, elegant and meaningful.</p>
  <h2>Perfect for</h2>
  <ul class="bullets">
    <li>Birthday celebrations</li><li>Anniversary dinners</li><li>Marriage proposals</li><li>Honeymoon dinners</li>
    <li>Family celebrations</li><li>Friends gathering</li><li>Small corporate dinners</li><li>Wellness retreat dinners</li><li>Private group experiences</li>
  </ul>
  <h2>An intimate setting</h2>
  <p>Unlike traditional event venues, Dar Mansour welcomes only a limited number of guests each evening, allowing us to dedicate our full attention to every table. Our reservation-led philosophy ensures a relaxed atmosphere where every dish is prepared especially for your guests and every detail is cared for with intention.</p>
  <h2>Tailored experiences</h2>
  <ul class="bullets">
    <li>Personalised table decoration</li><li>Birthday surprises</li><li>Anniversary celebrations</li><li>Proposal dinners</li>
    <li>Wine pairing experiences</li><li>Group menus</li><li>Vegetarian and dietary adaptations</li><li>Private venue booking (upon request)</li>
  </ul>
  <div class="note"><p>"The most beautiful celebrations aren't measured by the number of guests, but by the memories shared around the table."</p></div>
</div></section>
''' + L.cta_band("Plan your celebration",
    "Tell us a little about the occasion — the date, the number of guests and what you have in mind — and we'll craft an evening around it. We'll be delighted to answer any questions and guide you through the details.",
    eyebrow="Private Dining &amp; Celebrations",
    btn_label="Enquire via WhatsApp",
    wa_message="Hello Dar Mansour, I'd like to enquire about private dining. Here are a few details about my celebration:") + L.related(
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Couscous"),
    ("Wine", "Wine Pairing", "moroccan-wine-pairing-koh-phangan.html", "assets/uploads/Wine%20Pairing.jpg", "Moroccan prune tajine paired with a tawny port at Dar Mansour"),
    ("Reviews", "What Guests Say", "moroccan-restaurant-reviews-koh-phangan.html", "assets/img/moroccan-garden-lounge-koh-phangan.jpg", "Interior"))
pages["private-dining-koh-phangan.html"] = L.page(
    "Private Dining in Koh Phangan | Celebrate at Dar Mansour",
    "Celebrate life's special moments with a private Moroccan dining experience at Dar Mansour in Koh Phangan. Birthdays, anniversaries, proposals and intimate celebrations.",
    "private-dining-koh-phangan.html", pd_body,
    og_image="assets/img/moroccan-restaurant-central-room-koh-phangan.jpg")


# ============================================================ FAQ
FAQ = [
    ("What Moroccan dishes can you try at Dar Mansour in Koh Phangan?","At Dar Mansour you'll discover authentic Moroccan soul food — slow-cooked tajines, saffron couscous, roasted seasonal vegetables and sweet-savoury touches like prunes, apricots and preserved lemon. Everything is handmade and slow-cooked to order, using traditional recipes passed down through generations."),
    # NOTE: "hidden gem" is a charter-banned word, but kept ONLY here on purpose:
    # "hidden gem restaurant koh phangan" is a real search query and Google does
    # not penalise it. Whitelisted in the static linter (STATIC_LINT_ALLOW).
    ("Why is Dar Mansour considered a hidden gem restaurant in Koh Phangan?","Dar Mansour is a hidden gem Moroccan restaurant near Sri Thanu and Hin Kong, designed for romantic, slow and meaningful dining. From candlelit garden tables to handcrafted interiors, every detail invites you to slow down and reconnect — with food, with art and with yourself."),
    ("Where exactly is Dar Mansour located in Koh Phangan?","Dar Mansour is on the west coast of Koh Phangan, minutes from Sri Thanu, Hin Kong, The Alcove and Orion Healing Centre. Tucked away in a quiet garden, it blends Moroccan warmth with island calm."),
    ("What are Dar Mansour's opening hours for dinner?","We are open for dinner only, from 7:00 PM to 10:30 PM, Tuesday to Saturday. We are closed on Sundays and Mondays. Reservations are highly recommended, as we welcome only a limited number of guests each evening."),
    ("How do I book a table at Dar Mansour?",'Reservations are made via WhatsApp: <a class="ilink" href="https://wa.me/66822767757" target="_blank" rel="noopener">+66 82 276 7757</a>. Because Dar Mansour offers a boutique dining experience with limited seats, we highly recommend reserving in advance.'),
    ("How does the pre-order dining system work?","Our signature main dishes are pre-ordered, ideally 5 hours in advance, honouring traditional cooking times so they're ready to be enjoyed the moment you arrive. Ahead of your visit we'll send you the pre-order menu via WhatsApp; every dish is then prepared to order, just for you, which naturally reduces food waste and unnecessary excess."),
    ("Can I dine at Dar Mansour without a reservation?","Absolutely. Walk-in guests are always warmly welcome, subject to availability. As every dish at Dar Mansour is freshly prepared to order and many of our signature Moroccan specialties require several hours of slow cooking, some dishes may no longer be available without advance notice. During busy evenings, waiting times can also exceed one hour. To enjoy the full Dar Mansour experience and guarantee the availability of our signature tajines, couscous and tanjias, we highly recommend reserving your table and pre-ordering your main dishes in advance."),
    ("Is Dar Mansour a kid-friendly restaurant?","We are not a typical kid-friendly restaurant. Dar Mansour is an intimate, peaceful setting. We welcome babies under 2 and children over 9 who can enjoy the calm of the space. Please inform us in advance if you're bringing children so we can prepare accordingly."),
    ("Can I bring my dog to Dar Mansour?","Unfortunately dogs are not allowed, even in the garden area. We love animals, but we prioritise hygiene, safety and a tranquil atmosphere for all our guests."),
    ("Does Dar Mansour serve wine and cocktails?","Yes. Our selection includes a curated wine list paired with Moroccan dishes, signature cocktails with Moroccan twists, and homemade non-alcoholic drinks."),
    ("Are there vegetarian, vegan or gluten-free options?","Yes. Many of our dishes are naturally vegetarian or vegan. Please let us know your dietary needs when booking — we'll be happy to accommodate you."),
    ("Are the portions large enough to share?","Each dish is crafted as an individual portion — generous, satisfying and designed to serve one person. We don't recommend sharing a single main course between two guests. Our slow-cooked meals often taste even better the next day, so you're welcome to take home any leftovers."),
    ("How many guests can Dar Mansour host per evening?","To preserve our slow, soulful experience, we welcome just 40 guests each evening. This intentionally intimate setting lets us give every table our full attention — perfect for quiet couples' dinners, artistic gatherings and private celebrations."),
    ("Can I book a private dinner or event?","Yes. We host private dinners, birthdays, artist residencies and bespoke events in a serene, elegant setting. Dar Mansour is a top pick for private dining in Koh Phangan thanks to its beauty, warmth and discretion."),
    ("What payment methods are accepted?","We accept cash, Thai QR Code (PromptPay) and credit card. A 3% surcharge applies to card payments."),
    ("What makes the experience unique in Thailand?","Dar Mansour is one of the few places in Thailand offering a truly immersive North African dining journey, with personalised service, candlelit ambiance and a deep sense of care and storytelling."),
    ("How can I contact Dar Mansour or follow on social media?",'Contact us via WhatsApp at <a class="ilink" href="https://wa.me/66822767757" target="_blank" rel="noopener">+66 82 276 7757</a>. Follow us on Instagram @darmansour.kohphangan and on Facebook, Dar Mansour Koh Phangan.'),
]
faq_items = "".join(f'''      <details class="faq__item reveal"><summary>{q}</summary><div class="faq__answer"><p>{a}</p></div></details>''' for q,a in FAQ)
faq_schema = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"',"'"), re.sub(r'<[^>]+>', '', a).replace('"',"'")) for q,a in FAQ) + ']}'
faq_body = L.breadcrumb(("FAQ", None)) + L.subhero(
    "Frequently Asked Questions", "Best Moroccan restaurant in Koh Phangan — rooted in tradition, slow cooked with care",
    "Everything you need to know before your visit — reservations, food, wine, location and more.",
    "assets/img/moroccan-garden-dining-koh-phangan.jpg", "Candlelit Moroccan garden dining at Dar Mansour") + f'''
<section class="section"><div class="wrap">
  <div class="faq">
{faq_items}
  </div>
</div></section>
''' + L.cta_band("Still have a question?", "Message us on WhatsApp — we usually respond within a few hours.") + L.related(
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Couscous"),
    ("Reservation", "Reserve &amp; Pre-order", "moroccan-restaurant-reservation-koh-phangan.html", "assets/img/moroccan-arty-table-koh-phangan.jpg", "Candlelit table set for the evening at Dar Mansour"),
    ("Contact", "Find Us", "contact-dar-mansour-koh-phangan.html", "assets/img/dar-mansour-street-view-koh-phangan.jpeg", "Street view"))
pages["faq.html"] = L.page(
    "FAQ — Best Moroccan Restaurant in Koh Phangan | Dar Mansour",
    "Answers to common questions about Dar Mansour in Koh Phangan: reservations, pre-order dining, opening hours, dietary options, private dining and location.",
    "faq.html", faq_body,
    og_image="assets/img/moroccan-pastries-mint-tea-koh-phangan.jpg",
    extra_head=f'<script type="application/ld+json">{faq_schema}</script>')


# ============================================================ CONTACT
contact_body = L.breadcrumb(("Contact", None)) + L.subhero(
    "Contact &amp; Location", "Let's Plan Your Evening",
    "Dinner by reservation and pre-order via WhatsApp.",
    "assets/img/moroccan-garden-lounge-night-koh-phangan.jpg", "Candlelit Moroccan garden lounge at Dar Mansour, Koh Phangan") + f'''
<section class="section"><div class="wrap">
  <div class="contact-grid">
    <div class="contact-info reveal">
      <dl>
        <div><dt>Reservations &amp; Pre-order</dt><dd><a href="{WA}" target="_blank" rel="noopener"><strong>WhatsApp</strong> · +66 82 276 7757</a><span class="contact-note">For the fastest response and reservations.</span></dd></div>
        <div><dt>General Enquiries</dt><dd><a href="mailto:hello@darmansour.com">hello@darmansour.com</a><span class="contact-note">For partnerships, private events, media, and general enquiries.</span></dd></div>
        <div><dt>Address</dt><dd><a href="https://share.google/Rp8YllnPe9Z9E9Va0" target="_blank" rel="noopener">Hin Kong Road (Sri Thanu area)<br>Koh Phangan 84280, Thailand</a></dd></div>
        <div><dt>Opening Hours</dt><dd>Tuesday to Saturday · 7:00 PM – 10:30 PM<br>Closed Sunday &amp; Monday</dd></div>
        <div><dt>Follow</dt><dd><a href="https://instagram.com/darmansour.kohphangan" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/people/Dar-Mansour/" target="_blank" rel="noopener">Facebook</a></dd></div>
      </dl>
      <a class="btn btn--primary" style="margin-top:2rem;" href="{WA}" target="_blank" rel="noopener">{WI} Book a table &amp; pre-order</a>
    </div>
    <div class="contact-map reveal" data-delay="1">
      <iframe title="Dar Mansour on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=Dar+Mansour+Koh+Phangan+Hin+Kong+Sri+Thanu&output=embed"></iframe>
    </div>
  </div>
</div></section>
'''
pages["contact-dar-mansour-koh-phangan.html"] = L.page(
    "Contact Dar Mansour — Moroccan Slow Food in Koh Phangan",
    "Want to book a table at Dar Mansour? Contact us on WhatsApp, check our location in Koh Phangan and get directions to our Moroccan restaurant.",
    "contact-dar-mansour-koh-phangan.html", contact_body,
    og_image="assets/img/moroccan-garden-lounge-night-koh-phangan.jpg", extra_head=RESTAURANT_SCHEMA)


# ============================================================ BLOG / JOURNAL
PILLARS = [
    ("The Menu — Tajines, Couscous, Chhiwats, Msemen",
     "Every dish at Dar Mansour is a piece of Morocco brought to Koh Phangan. From saffron couscous steamed four times, to tajines that simmer for hours, to msemen and chhiwats that echo the streets of Marrakech — a soulful journey through Moroccan culinary heritage.",
     "moroccan-menu-koh-phangan.html", "Explore the menu"),
    ("Mansour Spirit — Hospitality, Dadas &amp; Family Rituals",
     "Hospitality is sacred in Morocco. We continue the traditions of the Dadas — women who carried recipes, wisdom and rituals from one generation to the next. Here, every guest is welcomed like family, every dinner a ritual of care.",
     "moroccan-hospitality-values-koh-phangan.html", "Discover the spirit"),
    ("Morocco's Kitchen — Slow Cooking &amp; Sacred Pantry",
     "In Morocco, patience is flavour. Our tajines, couscous and tanjias are prepared the slow way — hours of cooking, layers of spices and care in every step. We believe in sacred cooking: food that nourishes body and soul.",
     "moroccan-pantry-koh-phangan.html", "Enter the pantry"),
    ("Morocco &amp; Koh Phangan — Inspirations, Travel &amp; Culture",
     "Dar Mansour is a bridge between Morocco and Koh Phangan. We highlight Moroccan cities and traditions while guiding you through the island's hidden beaches, artistic inspirations and cultural gems.",
     "index.html", "Discover the experience"),
    ("Mansour Bar — Cocktails &amp; Artful Evenings",
     "Our bar is a celebration of creativity: Moroccan-inspired cocktails, curated wines and evenings filled with art and conversation. From citrus-infused gin to spiced rum creations, each drink is designed to complement our food.",
     "moroccan-cocktails-koh-phangan.html", "Step into the bar"),
]
pillar_cards = "".join(f'''    <div class="feature reveal"><h3>{t}</h3><p>{d}</p><a class="textlink" href="{href}" style="margin-top:1rem;">{lbl} {A}</a></div>''' for t,d,href,lbl in PILLARS)
journal_cards = _journal.render_index_cards(ARTICLES)
universe_nav = _journal.render_universe_nav(ARTICLES)

blog_body = L.breadcrumb(("Journal", None)) + L.subhero(
    "Journal &amp; Stories", "Stories of Morocco &amp; Koh Phangan",
    "Travel more thoughtfully. Discover more deeply.",
    "assets/uploads/where-to-watch-the-sunset-in-koh-phangan2.jpg", "Aerial view of a turquoise bay and white-sand beach on the west coast of Koh Phangan") + f'''
<section class="jmast reveal"><div class="wrap">
  <div class="jmast__rule"></div>
  <span class="jmast__kicker">The Journal</span>
  <p class="jmast__name">The Dar Mansour Journal</p>
  <p class="jmast__sub">Exploring Koh Phangan beyond the obvious, and Morocco beyond the clichés — through thoughtful travel guides, cultural stories and timeless tradition.</p>
</div></section>
{journal_cards}
{universe_nav}
<section class="section"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin:0 auto clamp(2rem,4vw,3rem);">
    <span class="eyebrow">The Worlds We Write From</span>
    <h2 style="margin-top:1rem;">Five doorways into Dar Mansour</h2>
  </div>
  <div class="features">
{pillar_cards}
  </div>
</div></section>

<section class="section" style="background:var(--sand);"><div class="wrap">
  <div class="center reveal" style="max-width:640px;margin:0 auto 2.5rem;">
    <span class="eyebrow">Authors &amp; Credibility</span>
    <h2 style="margin-top:1rem;">The voices behind our stories</h2>
    <p class="lead" style="margin-inline:auto;">Every word is rooted in real experience, real recipes and real people.</p>
  </div>
  <div class="pantry">
    <div class="pantry__item reveal"><h3><a class="ilink" href="dar-mansour-founders-vision.html">Maïja</a> — Co-Founder</h3><p>A creative spirit who has spent more than 30 years immersed in Moroccan culture, carrying forward its culinary heritage with a modern soul. Guided by the wisdom of the Dadas, she co-founded Dar Mansour as a sanctuary of food, culture and soulful hospitality in Koh Phangan.</p></div>
    <div class="pantry__item reveal" data-delay="1"><h3><a class="ilink" href="dar-mansour-founders-vision.html">P'Jae</a> — Head of Kitchen</h3><p>Our local partner and Head of Kitchen, P'Jae brings daily hands-on expertise to Dar Mansour, translating Moroccan traditions into refined, slow-cooked dishes prepared with patience and care — rooted in respect for sacred cooking and island hospitality.</p></div>
  </div>
</div></section>

<section class="section band-dark"><div class="wrap quote">
  <div class="divider divider--light reveal"><span>◇◇◇</span></div>
  <blockquote class="reveal" data-delay="1" style="margin-top:2rem;">"Where Morocco meets Koh Phangan — every story is a bridge between two worlds."</blockquote>
  <cite class="reveal" data-delay="2">The Dar Mansour Journal</cite>
</div></section>
''' + L.cta_band("Live the story, don't just read it",
    "The best chapters are written around the table. Reserve your evening at Dar Mansour.") + L.related(
    ("Menu", "Our Moroccan Menu", "moroccan-menu-koh-phangan.html", "assets/uploads/Couscous.jpg", "Couscous"),
    ("Founders", "Our Story", "dar-mansour-founders-vision.html", "assets/uploads/Founders%20-%20Our%20Story%20-Dar-Mansour-1.jpg", "Maïja and Bruno, arm in arm before a Thai temple in Koh Phangan — the founders of Dar Mansour"),
    ("Pantry", "Moroccan Pantry", "moroccan-pantry-koh-phangan.html", "assets/uploads/Preserved%20Lemons.jpg", "Jars of Moroccan preserved lemons"))
pages["blog.html"] = L.page(
    "Dar Mansour Journal — Stories of Morocco &amp; Koh Phangan",
    "A slow travel and culture journal where Koh Phangan's quieter side meets Morocco's timeless heritage — through cuisine, hospitality, art, music, traditions and craftsmanship.",
    "blog.html", blog_body,
    og_image="assets/img/maija-art-direction-koh-phangan.jpg", body_class="journal")


# ============================================================ JOURNAL ARTICLES
# One page per markdown file in content/journal/ (authored via Decap CMS).
for _a in ARTICLES:
    pages[_a["url"]] = _journal.render_article(_a, ARTICLES)

# Editorial-universe hub pages (cluster pages), one per category with articles.
for _key, _cat, _arts in _journal.universe_hubs(ARTICLES):
    pages[_cat["url"]] = _journal.render_category(_cat, _arts)

# Journal author / editorial-team page (credibility + E-E-A-T).
pages["journal-authors.html"] = _journal.render_authors()


# ============================================================ IMAGE DIMENSIONS
# Add intrinsic width/height to every <img> that lacks them, by reading the real
# file size — reserves aspect ratio in the browser and avoids layout shift (CLS).
import urllib.parse
_dim_cache = {}
def _img_size(src):
    if src.startswith(("http", "data:")):
        return None
    key = src.split("?")[0]
    if key in _dim_cache:
        return _dim_cache[key]
    dims = None
    try:
        from PIL import Image
        path = os.path.join(OUT, urllib.parse.unquote(key).lstrip("/"))
        with Image.open(path) as im:
            dims = im.size
    except Exception:
        dims = None
    _dim_cache[key] = dims
    return dims

_IMG_RE = re.compile(r"<img\b[^>]*>")
def add_img_dims(html):
    def repl(m):
        tag = m.group(0)
        if " width=" in tag or " height=" in tag:
            return tag
        ms = re.search(r'src="([^"]+)"', tag)
        if not ms:
            return tag
        dims = _img_size(ms.group(1))
        if not dims:
            return tag
        return tag.replace("<img", f'<img width="{dims[0]}" height="{dims[1]}"', 1)
    return _IMG_RE.sub(repl, html)

# ============================================================ LINT (static pages)
# The Journal linter only checks blog markdown. This runs the same banned-word
# rules over the generated static pages' visible text, so marketing copy stays
# on-voice too. Non-blocking (warnings only). Intentional exceptions — real
# guest-review quotes (never edited) and one deliberate SEO FAQ — are allowed.
STATIC_LINT_ALLOW = [
    "a hidden gem with a beating heart",                # Kodi's real review quote
    "hidden gem restaurant in koh phangan",             # deliberate SEO FAQ question
    "dar mansour is a hidden gem moroccan restaurant",  # deliberate SEO FAQ answer
    "it felt amazing",                                  # Soukaina's real review quote
    "more than just a meal",                            # Soukaina's real review quote
    "more than just a restaurant",                      # Golf du Maroc press quote
]

def _visible_text(html):
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", t)

def lint_static_pages(pages):
    allow = [a.lower() for a in STATIC_LINT_ALLOW]
    total_hits = 0
    for fname, html in pages.items():
        low = _visible_text(html).lower()
        for p in _journal.BANNED_PHRASES:
            found = len(re.findall(r"\b" + re.escape(p) + r"\b", low))
            if not found:
                continue
            allowed = sum(a.count(p) * low.count(a) for a in allow)
            extra = found - allowed
            if extra > 0:
                print(f"  ⚠ [{fname}] banned word in page copy: «{p}» ×{extra}")
                total_hits += extra
    if total_hits:
        print(f"  → {total_hits} banned-word warning(s) in static pages "
              f"(edit the source in build.py / _menu.py / _drinks.py, or whitelist).")

lint_static_pages(pages)

# ============================================================ WRITE
for fname, html in pages.items():
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(add_img_dims(html))
    print("wrote", fname)

# Standalone 'link in bio' page (darmansour.com/links) — written directly, kept
# out of `pages` so it stays out of the sitemap and site chrome.
import _links
with open(os.path.join(OUT, "links.html"), "w", encoding="utf-8") as f:
    f.write(_links.render())
print("wrote links.html")

# ---- robots.txt (+ sitemap.xml only once the site is open for indexing) ----
from datetime import date
SITE = L.SITE_URL.rstrip("/")
sitemap_path = os.path.join(OUT, "sitemap.xml")
if L.NOINDEX:
    # Pre-launch: pages carry a noindex meta. Keep crawling allowed so bots can
    # actually see that noindex, but don't advertise a sitemap. Drop any stale one.
    if os.path.exists(sitemap_path):
        os.remove(sitemap_path)
    _llms_path = os.path.join(OUT, "llms.txt")
    if os.path.exists(_llms_path):
        os.remove(_llms_path)
    robots = ("# Pre-launch — every page carries a 'noindex' meta so search engines\n"
              "# keep this site out of results. Crawling stays allowed so the\n"
              "# noindex is actually seen. Remove this once the site goes public.\n"
              "User-agent: *\nAllow: /\n")
    print("wrote robots.txt (noindex mode — sitemap omitted)")
else:
    today = date.today().isoformat()
    def _loc(fn):
        return SITE + "/" if fn == "index.html" else f"{SITE}/{fn}"
    _urls = "".join(
        f"  <url><loc>{_loc(fn)}</loc><lastmod>{today}</lastmod></url>\n"
        for fn in pages)
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + _urls + '</urlset>\n')
    # Explicitly welcome the major AI / LLM crawlers (GEO). `Allow: /` already
    # covers them via the wildcard, but naming them is an unambiguous opt-in and
    # a positive signal — and makes it obvious we want to be cited, not blocked.
    _ai_bots = ("GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot",
                "Claude-Web", "anthropic-ai", "PerplexityBot", "Perplexity-User",
                "Google-Extended", "CCBot", "Applebot-Extended", "cohere-ai")
    _ai_block = "\n\n".join(f"User-agent: {b}\nAllow: /" for b in _ai_bots)
    robots = ("User-agent: *\nAllow: /\n\n"
              "# AI / generative-engine crawlers are welcome (GEO).\n"
              f"{_ai_block}\n\n"
              f"Sitemap: {SITE}/sitemap.xml\n"
              f"# llms.txt: {SITE}/llms.txt\n")

    # ---- llms.txt (a curated, AI-facing map of the site — the emerging GEO
    # standard). Markdown, human-readable, points crawlers at the best pages.
    _key_pages = [
        ("moroccan-menu-koh-phangan.html", "Our Menu", "The full slow-cooked Moroccan menu — tajines, couscous, pastilla and more."),
        ("moroccan-restaurant-reservation-koh-phangan.html", "Reservations", "How to book a table or pre-order via WhatsApp (dinner only, Tue–Sat)."),
        ("moroccan-slow-dining-koh-phangan.html", "The Concept", "Slow food, Moroccan art de vivre and the philosophy behind Dar Mansour."),
        ("moroccan-wine-pairing-koh-phangan.html", "Wine Pairing", "Our approach to pairing wine with Moroccan cuisine."),
        ("moroccan-cocktails-koh-phangan.html", "Mansour Bar", "Signature cocktails and the bar programme."),
        ("private-dining-koh-phangan.html", "Private Dining", "Private events and group dining at Dar Mansour."),
        ("dar-mansour-founders-vision.html", "Founders & Story", "Maïja and Bruno, and the story behind the restaurant."),
        ("moroccan-restaurant-reviews-koh-phangan.html", "Reviews", "What guests say about dining at Dar Mansour."),
        ("faq.html", "FAQ", "Practical questions: hours, booking, location, dietary options."),
        ("contact-dar-mansour-koh-phangan.html", "Contact & Location", "Address in the Sri Thanu / Hin Kong area, phone, email and map."),
    ]
    def _abs(fn):
        return SITE + "/" if fn == "index.html" else f"{SITE}/{fn}"
    _lines = [
        "# Dar Mansour - Morocco's Kitchen",
        "",
        "> Moroccan slow-food restaurant on the west coast of Koh Phangan, Thailand "
        "(Sri Thanu / Hin Kong area). Dinner only, Tuesday to Saturday, reservation "
        "recommended. Also publishes The Journal: independent local guides to eating "
        "and living on Koh Phangan, plus Moroccan culture.",
        "",
        "Founded by Maïja and Bruno. WhatsApp +66 82 276 7757 · hello@darmansour.com.",
        "",
        "## The Restaurant",
        "",
    ]
    _lines += [f"- [{t}]({_abs(fn)}): {d}" for fn, t, d in _key_pages]
    _lines += ["", "## The Journal (guides & stories)", ""]
    _lines += [f"- [{a['title']}]({_abs(a['url'])}): {a['description']}"
               for a in ARTICLES]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(_lines) + "\n")
    print("wrote sitemap.xml + robots.txt + llms.txt")
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)

print(f"\n{len(pages)} pages generated.")
