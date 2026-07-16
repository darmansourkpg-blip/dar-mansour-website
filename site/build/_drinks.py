# -*- coding: utf-8 -*-
"""Wine pairing list & Mansour Bar cocktail list (verbatim from website content)."""

# ---- WINE ----
# group: (title, [cards]) ; card: dict
WINE_FEATURE = {
    "name": "Maynard's Fine Tawny Porto — 2019",
    "origin": "Portugal · Glass (10cl) 290 · Bottle 2300",
    "grapes": "",
    "pairing": "Berber's Lamb Tajine (prunes &amp; almonds)",
    "desc": "Smooth, amber and rich — a silk-sweet, surprising match that enhances the spices and deep savoury flavours of this unique tajine. “Unexpected? Yes. A revelation? Absolutely.”",
}

WINE_GROUPS = [
    ("Red Wines", [
        {"name":"LIGNAC Comte Tolosan IGP — 2021","origin":"France · House · Glass (12cl) 200 · Bottle 1200","grapes":"Syrah",
         "pairing":"Rabat &amp; Chefchaouen's Tajine, Couscous Darna","desc":"Bold and peppery Syrah with firm tannins, low acidity and full-bodied finesse."},
        {"name":"POGGIO ALTO Negroamaro Puglia IGT — 2020","origin":"Italy · 1350","grapes":"Negroamaro",
         "pairing":"Rabat &amp; Berber's Tajine, Couscous","desc":"Deep ruby hue with fruity, subtly spiced aromas. Smooth, round and balanced with soft tannins."},
        {"name":"CELLIERS DES PRINCES Sceau du Prince, Côtes-du-Rhône AOP — 2022","origin":"France · 1500","grapes":"Grenache, Syrah, Mourvèdre",
         "pairing":"Rabat &amp; Berber's Tajine, Couscous, Tanjia Marrakchia","desc":"Ruby red with purple glints, bursting with red fruits, light spice and silky tannins. Smooth, supple and fruit-forward."},
        {"name":"BURGO VIEJO Rioja Crianza DOC — 2019","origin":"Spain · 1650","grapes":"Tempranillo",
         "pairing":"Rabat &amp; Berber's Tajine, Tanjia Marrakchia","desc":"Ruby red with black fruits and vanilla notes. Powerful, complex and silky on the palate."},
        {"name":"CELLIERS DES PRINCES Blason du Prince, Châteauneuf-du-Pape AOC — 2022","origin":"France · 3700","grapes":"Grenache, Syrah, Mourvèdre, Cinsault",
         "pairing":"Rabat &amp; Berber's Tajine, Tanjia Marrakchia","desc":"Ruby red with red and black berries, hints of lavender, thyme and rosemary. Balanced palate with elegant, silky tannins."},
    ]),
    ("White Wines", [
        {"name":"PUNTI FERRER Limited Edition, Rapel Valley — 2021","origin":"Chile · House · Glass (12cl) 200 · Bottle 1200","grapes":"Sauvignon Blanc",
         "pairing":"Fez, Oualidia &amp; Chefchaouen's Tajine","desc":"Pale yellow with green reflections. Tropical fruit, citrus and mineral notes. Fresh, light-bodied with a crisp, zesty finish."},
        {"name":"LE PETIT BALTHAZAR Pays d'Oc IGP — 2024","origin":"France · 1550","grapes":"Viognier, Sauvignon Blanc",
         "pairing":"Fez, Oualidia &amp; Chefchaouen's Tajine, Couscous","desc":"Pale yellow with silver-green tints. Intense lime, grapefruit and exotic fruit. Crisp and fresh with a fruity finish."},
        {"name":"GRANGE MAZAN Côtes de Gascogne IGP — 2022","origin":"France · 1600","grapes":"Colombard, Sauvignon Blanc",
         "pairing":"Fez, Oualidia &amp; Chefchaouen's Tajine","desc":"Pale gold with vibrant lime, grapefruit and lychee. Refreshing and juicy with well-balanced acidity."},
        {"name":"CHÂTEAU DU JAUNAY Muscadet de Sèvre &amp; Maine sur Lie AOP, Vieilles Vignes — 2023","origin":"France · 1650","grapes":"Melon de Bourgogne",
         "pairing":"Fez, Oualidia &amp; Chefchaouen's Tajine","desc":"Shiny gold, crisp citrus and white-flower aromas with mineral hints. Smooth, elegant finish."},
    ]),
    ("Rosé Wines", [
        {"name":"FAMILIA CORREA LISONI Rosé, Central Valley DO — 2021","origin":"Chile · House · Glass (12cl) 200 · Bottle 1200","grapes":"Merlot",
         "pairing":"Fez &amp; Chefchaouen's Tajine, Couscous","desc":"Pale pink, wild flowers, red berries and herbal aromas. Balanced acidity with a smooth finish."},
        {"name":"COEUR DE MÉDITERRANÉE Rosé IGP — 2023","origin":"France · 1350","grapes":"Cinsault, Syrah",
         "pairing":"Fez &amp; Chefchaouen's Tajine, Couscous","desc":"Vibrant pale pink with fruity, floral aromas. Fresh and lively on the palate."},
        {"name":"CUVÉE DÉSIR, Côtes de Provence Rosé AOP — 2023/24","origin":"France · 1500","grapes":"Grenache, Syrah, Cinsault",
         "pairing":"Fez, Oualidia &amp; Chefchaouen's Tajine, Couscous","desc":"Light pink with orange hints. Red fruits give way to peach and pear. Fresh, supple, with a peachy finish."},
    ]),
]

# ---- COCKTAILS ----  group: (title, tagline, [items]) ; item: (name, price, desc)
COCKTAILS = [
    ("Mansour Signatures", "Inspiration everywhere — just look around.", [
        ("My name is Berber, James Berber!","250","A refreshing twist on the classic dry martini: extra-dry vermouth infused with olive oil and dry gin. (Vodka version on request.)"),
        ("Rock the Casbah","250","A bold Margarita with Ras El Hanout syrup, tequila, orange liqueur and fresh lime."),
        ("A Camel in Zen Beach","250","A daiquiri of date syrup, white rum and fresh lime."),
    ]),
    ("Mansour Classics", "To live without restrictions.", [
        ("Mojito","240","White rum, fresh lime, mint leaves, brown sugar, soda water."),
        ("Piña Colada","240","White &amp; dark rum, pineapple juice, coconut cream, brown sugar, coffee bean."),
        ("Margarita","240","Tequila, orange liqueur, fresh lime."),
        ("Negroni","300","Dry gin, Campari, red martini, orange slice."),
    ]),
    ("Oasis Pitcher · 1 Litre", "Stay wild and free.", [
        ("Lost in Eden","780","A refreshing lemonade with white rum, fresh lime, condensed milk and mint leaves — perfect for sharing."),
    ]),
    ("Nightcap Pleasures", "Live life to the fullest.", [
        ("Coquito","180","White rum, condensed milk, coconut cream, vanilla syrup, cinnamon."),
        ("Espresso Martini","290","Vodka, coffee liqueur, vanilla syrup, espresso."),
        ("Caramelito Martini","290","Vodka, coffee liqueur, salted caramel syrup, espresso."),
        ("Tulum Martini","290","Tequila, coffee liqueur, agave syrup, espresso."),
        ("Daiquiri Martini","290","White rum, coffee liqueur, vanilla syrup, espresso."),
        ("Chocolate Cookie Martini","290","Vodka, coffee liqueur, chocolate-cookie syrup, espresso."),
        ("Irish Martini","320","Baileys, vodka, espresso."),
        ("Very Special Martini","340","Cognac VS, vodka, coffee liqueur, espresso."),
    ]),
    ("Free-Spirits — No Alcohol", "Believe in your own magic!", [
        ("Mansour's Jasminade","100 / 390","The infamous Jasminade — jasmine tea, orange blossom water, lemon and fresh mint. (Glass / 1 litre.)"),
        ("Mojito for Beginners","120","Fresh mint, fresh lime, brown sugar, soda water — for sober souls."),
        ("Soft Drinks","60","Sprite, Coca-Cola, Coke Zero, Tonic, Soda or Mineral Water."),
    ]),
]

# simple price lists (name, price) with a heading
COCKTAIL_LISTS = [
    ("Long Drinks", [("Cuba Libre","220"),("Gin Tonic","220"),("Whisky Coca","220"),("Vodka Lime","220")]),
    ("Aperitifs", [("Leo","100"),("Pastis","160"),("Martini Red","250"),("Martini Extra Dry Vermouth","250"),("Campari","250"),
                   ("House Red / White / Rosé Wine","200"),("Prosecco (Amore Rubato Extra Dry)","260"),("Fine Tawny Porto (Maynard's)","290")]),
    ("Spirits", [("Vodka Smirnoff","200"),("Premium Vodka Hlibny Dar","200"),("Rum Bacardi Carta Blanca","200"),
                 ("Traditional Rum Chauvet (White or Dark)","200"),("Tequila José Cuervo","200"),("Gin Gordon's","200"),("Whisky Red Label","200")]),
    ("Digestifs", [("Homemade Infused Caramel Vodka","150"),("Limoncello","190"),("Kahlúa","220"),("Baileys","220"),
                   ("Cointreau","320"),("Cognac VS Grande Champagne (François Voyer)","360")]),
]


def render_wine_feature():
    f = WINE_FEATURE
    return f'''    <div class="drink-group reveal">
      <span class="drink-group__title">Start with the Unexpected</span>
      <div class="wine-card wine-card--feature">
        <div class="wine-card__head">
          <span class="wine-card__name">{f['name']} <span class="wine-card__origin">— {f['origin']}</span></span>
        </div>
        <p class="wine-card__meta"><b>Pairs with:</b> {f['pairing']}</p>
        <p class="wine-card__meta">{f['desc']}</p>
      </div>
    </div>'''


def render_wine_groups():
    out = []
    for title, cards in WINE_GROUPS:
        rows = []
        for c in cards:
            grapes = f'<b>Grapes:</b> {c["grapes"]} &nbsp;·&nbsp; ' if c["grapes"] else ""
            price = c["origin"].split("·",1)[1].strip() if "·" in c["origin"] else ""
            rows.append(f'''        <div class="wine-card">
          <div class="wine-card__head">
            <span class="wine-card__name">{c['name']}<br><span class="wine-card__origin">{c['origin']}</span></span>
          </div>
          <p class="wine-card__meta">{grapes}<b>Pairs with:</b> {c['pairing']}</p>
          <p class="wine-card__meta">{c['desc']}</p>
        </div>''')
        out.append(f'''    <div class="drink-group reveal">
      <span class="drink-group__title">{title}</span>
{chr(10).join(rows)}
    </div>''')
    return "\n".join(out)


def render_cocktails():
    out = []
    for title, tagline, items in COCKTAILS:
        rows = []
        for name, price, desc in items:
            rows.append(f'''        <div class="menu-item">
          <div class="menu-item__head">
            <span class="menu-item__name">{name}</span>
            <span class="menu-item__leader"></span>
            <span class="menu-item__price">{price}</span>
          </div>
          <p class="menu-item__desc">{desc}</p>
        </div>''')
        out.append(f'''    <div class="drink-group reveal">
      <span class="drink-group__title">{title}</span>
      <p style="color:var(--muted);font-style:italic;margin:-.6rem 0 1rem;">{tagline}</p>
{chr(10).join(rows)}
    </div>''')
    # simple lists
    for title, items in COCKTAIL_LISTS:
        rows = []
        for name, price in items:
            rows.append(f'''        <div class="menu-item">
          <div class="menu-item__head">
            <span class="menu-item__name">{name}</span>
            <span class="menu-item__leader"></span>
            <span class="menu-item__price">{price}</span>
          </div>
        </div>''')
        out.append(f'''    <div class="drink-group reveal">
      <span class="drink-group__title">{title}</span>
{chr(10).join(rows)}
    </div>''')
    return "\n".join(out)
