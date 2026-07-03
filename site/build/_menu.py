# -*- coding: utf-8 -*-
"""Full menu data (verbatim from Menu Dar Mansour.pdf) + renderer."""

# tag codes -> (short label, full label)
TAGS = {
    "VEG":     ("Veg", "Vegetarian"),
    "VEGAN":   ("Vegan", "Vegan"),
    "GF":      ("GF", "Gluten-free"),
    "SPICY":   ("Spicy", "Spicy mild"),
    "LTD":     ("Ltd", "Limited · pre-order advised"),
    "CAF":     ("Caffeine", "Contains caffeine"),
}

# section: (id, title, intro, price_hint, items[])
# item: (name, price, desc, [tags])
MENU = [
    ("chiiwats", "Chiiwats",
     "Discover a variety of tasty warm salads. Each Chiiwat brings a burst of flavour to your meal — ideal for sharing as a starter.",
     "Small 90 · Large 180",
     [
        ("Gar'a M'asla", "90 / 180",
         "A mix of sweet and savoury: tender pumpkin confit with brown sugar and butter, brightened by orange blossom water, cinnamon and salt. Topped with toasted sesame seeds and nuts.", ["VEG","GF"]),
        ("Batata M'chermla", "90 / 180",
         "Tender potatoes cooked in homemade charmoula (fresh cilantro, parsley, garlic, cumin, sweet paprika, ginger, turmeric, olive oil and lemon juice), garnished with fresh herbs and olives.", ["VEGAN","GF"]),
        ("Zaalouk", "90 / 180",
         "Eggplant caviar of roasted eggplants cooked with olive oil, fresh tomatoes, cilantro, parsley, garlic, paprika and cumin, finished with preserved lemons.", ["VEGAN","GF"]),
        ("Taktouka", "90 / 180",
         "Vegetable stew of smoky grilled green peppers, fresh tomatoes and cilantro, infused with olive oil, garlic, paprika and cumin. Topped with fresh herbs.", ["VEGAN","GF"]),
     ]),

    ("msemen", "M'semen",
     "Traditional foliated crepes, plain or filled. Eat by hand — tear apart the layers, roll them up and dip into your Tajine or Chiiwat. (2 portions served.)",
     "",
     [
        ("Cheese M'semen", "190", "A blend of cheddar and mozzarella infused with oregano for a smooth, indulgent flavour.", ["VEG"]),
        ("Beef Kefta M'semen", "160", "Filled with seasoned minced beef, fresh parsley and cilantro, cumin, paprika, salt and pepper — a rich, savoury filling.", []),
        ("Vegetarian M'semen", "130", "Stuffed with sautéed onions, paprika, cumin and fresh herbs — flavourful and aromatic.", ["VEG"]),
        ("M'semen (plain)", "100", "Light, foliated crepes of fine semolina, wheat flour and mineral water, repeatedly stretched and folded with butter, oil and semolina for a signature layered texture.", ["VEG"]),
     ]),

    ("kemia", "Kemia to Share",
     "Generous sharing platters to open the evening, Moroccan-style.",
     "",
     [
        ("2 Small Chiiwats &amp; 2 M'semens", "350", "Of your choice (1 piece each).", []),
        ("4 Small Chiiwats", "350", "Of your choice.", []),
        ("4 M'semens", "280", "1 piece of each type.", []),
     ]),

    ("tajines", "Tajines",
     "Uncover the rich, slow-cooked flavours of our regional Tajines, traditionally prepared in Moroccan clay pots and gently simmered over charcoal. Each Tajine is an individual serving for one guest, accompanied by Tafarnout bread.",
     "",
     [
        ("Berber's Tajine — Lamb Shank, Prunes &amp; Almonds", "580",
         "Succulent lamb shank slow-cooked with organic Taliouine saffron, fresh cilantro, ginger, turmeric, onion, garlic and olive oil. Enriched with prunes pre-soaked in black tea then simmered in cinnamon-honey syrup. Finished with toasted almonds, sesame and a cinnamon stick. A memorable clash of Atlas flavours — sweet and savoury.", ["GF","LTD"]),
        ("Oualidia's Tajine — Sea Bass, Vegetables &amp; Charmoula", "560",
         "Daily catch of sea bass marinated in homemade charmoula, simmered with olive oil, ginger, turmeric, fresh tomatoes, onions, potatoes, carrots, lemon slices and bell peppers. Finished with preserved lemon, olives and fresh chili — straight to the Atlantic coast.", ["GF","LTD"]),
        ("Fez's Tajine — Chicken, Preserved Lemon &amp; Olives", "390",
         "Tender chicken thighs simmered with homemade preserved lemons, green olives and olive oil, infused with organic Taliouine saffron, fresh parsley, cilantro, ginger, turmeric, garlic and onions. A classic that captures the soul of our kitchen.", ["GF","LTD"]),
        ("Rabat's Tajine — Beef Kefta, Tomato Sauce &amp; Egg", "360",
         "Spiced minced-beef meatballs simmered in a savoury fresh tomato sauce with onions, garlic, olive oil, cumin, paprika and cilantro. Topped with an egg. Ask for the mild spicy version.", ["GF","SPICY","LTD"]),
        ("Chefchaouen's Tajine — 4 Seasonal Vegetables", "330",
         "Simmered zucchini, pumpkin, sweet potatoes and carrots on a bed of olive oil, onions and chickpeas. Infused with ginger, paprika, turmeric and salt. Pure vegetable goodness in a pot.", ["VEGAN","GF","LTD"]),
     ]),

    ("tanjia", "Tanjia — Kitchen's Recommendation",
     "Our tribute to slowness. This traditional Marrakech dish is gently simmered for over 5 hours in a sealed clay jar nestled among glowing embers, creating a rich concentration of deep flavours. An individual serving for one guest, accompanied by Tafarnout bread.",
     "",
     [
        ("Tanjia Marrakchia — Beef Shank, Preserved Lemon &amp; Smen", "580",
         "Slow-cooked beef shank (350 g) with homemade preserved lemon and smen, organic Taliouine saffron, cumin, garlic cloves and olive oil. “A magical explosion of aromas released after long hours of cooking.”", ["GF","LTD"]),
     ]),

    ("couscous", "Couscous",
     "Morocco's national dish — hand-rolled couscous patiently steamed four times in a traditional couscoussière, absorbing the fragrant vapours of a gently spiced broth. An individual serving for one guest. Served every Friday only.",
     "Fridays only",
     [
        ("Couscous Beldi — Chuck Roll Beef with Couscous &amp; Tfaya", "540",
         "Tender chuck roll beef slow-cooked over 5 hours in a broth of onions, tomato juice, olive oil, smen, coriander, ginger, turmeric and black pepper. Served with its six vegetables over light hand-rolled couscous, crowned with Tfaya, chickpeas and warm spiced broth. A traditional version for true meat lovers.", ["LTD"]),
        ("Couscous Darna — Six Vegetables with Couscous &amp; Tfaya", "480",
         "Each vegetable cooked separately in its own pot and spice blend, then served over light hand-rolled couscous topped with Tfaya, chickpeas and warm broth. A celebration of Morocco's generous home cooking.", ["VEG","LTD"]),
     ]),

    ("sides", "Side Dishes",
     "The perfect companions to your slow-cooked mains.",
     "",
     [
        ("Couscous", "150", "Semolina steamed four times, infused with the rising vapours of spiced broth. Topped with Tfaya, caramelised onions and raisins. (Fridays only.)", ["VEG"]),
        ("Homemade Double-Cooked Fries", "140", "Crisp, golden, twice-cooked.", ["VEGAN","GF"]),
        ("Quinoa", "120", "Quinoa with dried raisins, olive oil, cumin and garlic.", ["VEGAN","GF"]),
        ("Basmati Rice", "100", "Infused with turmeric, cumin and caramelised onions, finished with fresh coriander.", ["VEGAN","GF"]),
        ("Tafarnout Bread", "90", "Authentic Berber bread baked in a handmade clay oven on hot river pebbles. (Per piece.)", ["VEG"]),
     ]),

    ("tea", "Tea &amp; Coffee",
     "The Moroccan ritual to close — or accompany — your meal.",
     "",
     [
        ("Traditional Mint Tea", "90 / 180", "Green tea rinsed and steeped with fresh mint and sugar, poured back and forth to aerate, served warm in small glasses. (Glass / pot, 2–3 glasses.)", ["CAF"]),
        ("Moroccan Coffee", "100", "Dark roasted coffee blended with cinnamon, ginger, nutmeg, cardamom, clove, black pepper and star anise — ground and brewed into a fragrant, spiced coffee.", ["CAF"]),
     ]),
]


def _tags(codes):
    if not codes:
        return ""
    spans = "".join(f'<span class="mtag" title="{TAGS[c][1]}">{TAGS[c][0]}</span>' for c in codes)
    return f'<div class="menu-item__tags">{spans}</div>'


def render_menu():
    out = []
    for _id, title, intro, hint, items in MENU:
        hint_html = f'<p style="margin-top:.6rem;color:var(--muted);font-size:.82rem;letter-spacing:.04em;">{hint}</p>' if hint else ""
        rows = []
        for name, price, desc, tags in items:
            rows.append(f'''      <div class="menu-item">
        <div class="menu-item__head">
          <span class="menu-item__name">{name}</span>
          <span class="menu-item__leader"></span>
          <span class="menu-item__price">{price}</span>
        </div>
        <p class="menu-item__desc">{desc}</p>
        {_tags(tags)}
      </div>''')
        out.append(f'''  <div class="menu-section reveal" id="{_id}">
    <div class="menu-section__head">
      <span class="eyebrow">Menu</span>
      <h2>{title}</h2>
      <p>{intro}</p>
      {hint_html}
    </div>
    <div class="menu-list">
{chr(10).join(rows)}
    </div>
  </div>''')
    return "\n".join(out)


def render_legend():
    items = "".join(f'<span><span class="mtag">{TAGS[c][0]}</span> {TAGS[c][1]}</span>' for c in TAGS)
    return f'<div class="menu-legend reveal">{items}</div>'
