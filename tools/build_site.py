#!/usr/bin/env python3
"""Generates the multi-page Muhammad Furnitures site into /home/claude/site.

The header, footer, WhatsApp button and product cards are shared pieces, so every page stays identical
where it should. The output is plain HTML (no build step needed by the owner).
"""
import os
import json
from urllib.parse import quote

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_content import PRODUCT_SEO, COLLECTION_EXTRA, ROOM_ALT, GUIDE_SECTIONS, GUIDE_FAQ, GUIDE_SHORT, QUICK

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))   # the website folder (one level up)

# ---- SEO SETTINGS (UPDATE THESE TWO LINES WHEN YOU KNOW THEM, THEN REBUILD) ----
CITY = ""        # PUT YOUR CITY HERE, e.g. "Lahore". It goes into titles, headings and Google business data.
SITE_URL = ""    # PUT YOUR WEBSITE ADDRESS HERE once it is live, e.g. "https://www.muhammadfurnitures.com" (no slash at the end)
UPDATED_ISO = "2026-11-08"          # UPDATE THIS DATE whenever you change prices or text; it is shown on the page and in the data for Google
UPDATED_TEXT = "8 November 2026"
LOC = CITY or "Pakistan"   # used in titles and headings: "... in Pakistan" or "... in Lahore"
NAME = "Muhammad Furnitures"
PHONE = "0311 7420474"
TEL = "+923117420474"
WA = "923117420474"
EMAIL = "mr.genius2474@gmail.com"
WA_PATH = '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
FB = "https://www.facebook.com/share/1KevMHNxmj/"
GOOGLE = "https://share.google/vqhgRHfPlE7DO94DB"

NAV = [
    ("Home", "index.html", "home"),
    ("About Us", "about.html", "about"),
    ("Shop", "shop.html", "shop"),
    ("Collections", "collections.html", "collections"),
    ("Custom Furniture", "custom-furniture.html", "custom"),
    ("Contact", "contact.html", "contact"),
]

FONTS = (
    '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700'
    '&family=Playfair+Display:wght@600;700&display=swap">\n'
)

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' "
    "fill='%234a2c1a'/%3E%3Ctext x='32' y='46' font-size='40' font-family='Georgia' font-weight='700' text-anchor='middle' "
    "fill='%23d19a1e'%3EM%3C/text%3E%3C/svg%3E"
)

def local_ld():
    biz = {
        "@context": "https://schema.org",
        "@type": "FurnitureStore",
        "@id": (SITE_URL + "/#business") if SITE_URL else "#business",
        "name": "Muhammad Furnitures",
        "description": "Handcrafted, made-to-order furniture for homes, shops and offices: sofa sets, beds, wardrobes, dining tables and office desks.",
        "telephone": "+923117420474",
        "email": "mr.genius2474@gmail.com",
        "priceRange": "Rs 22,000 - Rs 120,000",
        "currenciesAccepted": "PKR",
        "address": {"@type": "PostalAddress", "addressCountry": "PK"},
        "areaServed": {"@type": "Country", "name": "Pakistan"},
        "sameAs": ["https://www.facebook.com/share/1KevMHNxmj/", "https://share.google/vqhgRHfPlE7DO94DB"],
        "slogan": "Handcrafted. Made to order. Built to last.",
        "knowsAbout": ["Custom furniture", "Sofa sets", "Bed sets", "Wardrobes", "Dining tables", "Office desks", "TV units", "Wooden furniture"],
        "makesOffer": {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Made-to-order furniture"}},
    }
    if CITY:
        biz["address"]["addressLocality"] = CITY
        biz["areaServed"] = {"@type": "City", "name": CITY}
    if SITE_URL:
        biz["url"] = SITE_URL + "/"
        biz["image"] = SITE_URL + "/images/hero.jpg"
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Muhammad Furnitures", "inLanguage": "en-PK"}
    if SITE_URL:
        site["url"] = SITE_URL + "/"
    return ("  <!-- GOOGLE STRUCTURED DATA (helps your business show up in local search).\n"
            "       TO FINISH: add your street address (streetAddress, addressLocality) and opening hours (openingHoursSpecification)\n"
            "       once you have them, and set CITY and SITE_URL at the top of build_site.py. -->\n"
            + ld_script(biz) + ld_script(site))


def ld_script(data):
    return '  <script type="application/ld+json">\n  ' + json.dumps(data, indent=2, ensure_ascii=False).replace("\n", "\n  ") + "\n  </script>\n"


def absurl(path):
    return (SITE_URL + "/" + path) if SITE_URL else None


def crumb_ld(items):
    """items = [(label, filename or None)]; returns a BreadcrumbList script"""
    lst = []
    for n, (label, href) in enumerate(items, 1):
        e = {"@type": "ListItem", "position": n, "name": label}
        if href and SITE_URL:
            e["item"] = absurl("" if href == "index.html" else href)
        lst.append(e)
    return ld_script({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": lst})

# --------------------------------------------------------------------------------------------
# PRODUCTS (shared by the Home page, which shows the first 6, and the Shop page, which shows all)
# --------------------------------------------------------------------------------------------
PRODUCTS = [
    dict(id=1, name="Dining Table, 6 Seater", price=75000, cat="dining", catlabel="Dining Room", spec="180 × 90 × 76 cm",
         desc="Gather the whole family around a table built to last. Sturdy construction, smooth finish, and sizes to suit your dining room.",
         badge="Custom size", alt="Dining table, 6 seater"),
    dict(id=2, name="Double Bed with Storage", price=95000, cat="bedroom", catlabel="Bedroom", spec="Fits a 160 × 200 cm mattress",
         desc="A strong bed frame with practical storage underneath, made to fit your mattress and room size.", alt="Double bed with storage"),
    dict(id=3, name="Wardrobe, 3 Door", price=85000, cat="storage", catlabel="Storage", spec="150 × 60 × 210 cm",
         desc="Plenty of space for hanging and folded clothes, with a clean finish that suits any bedroom.", alt="Three door wardrobe"),
    dict(id=4, name="Sofa Set, 5 Seater", price=120000, cat="living", catlabel="Living Room", spec="3 + 1 + 1 seats, your choice of fabric",
         desc="A comfortable, well-built sofa set for family evenings and guests. Choose your fabric and colour.", alt="Five seater sofa set"),
    dict(id=5, name="Office Desk", price=35000, cat="office", catlabel="Office", spec="140 × 70 × 75 cm",
         desc="A sturdy work desk with room for your computer and papers, made to fit your space.", alt="Office desk"),
    dict(id=6, name="TV Unit with Shelves", price=45000, cat="living", catlabel="Living Room", spec="180 × 40 × 50 cm",
         desc="A tidy home for your TV, decoder and decor, built to the size of your wall.", alt="TV unit with shelves"),
    dict(id=7, name="Coffee Table", price=22000, cat="living", catlabel="Living Room", spec="100 × 55 × 45 cm",
         desc="A low table for the middle of your living room, with space for books, a tray and guests.", alt="Coffee table"),
    dict(id=8, name="Dressing Table with Mirror", price=55000, cat="bedroom", catlabel="Bedroom", spec="110 × 45 × 140 cm",
         desc="A dressing table with a mirror and drawers for your daily essentials.", alt="Dressing table with mirror"),
    dict(id=9, name="Bookshelf, 5 Shelf", price=30000, cat="storage", catlabel="Storage", spec="90 × 30 × 180 cm",
         desc="Open shelves for books, files and decor, sized to fit your wall.", alt="Five shelf bookshelf"),
]


def product_card(p, first_comment=False, level=3):
    badge = '              <span class="badge">%s</span>\n' % p["badge"] if p.get("badge") else ""
    c1 = ("          <!-- data-id must be UNIQUE. data-name and data-price feed the cart (script.js). "
          "data-category = living, bedroom, dining, office or storage -->\n") if first_comment else ""
    return f"""          <!-- ================= PRODUCT {p['id']}: {p['name']} ================= -->
{c1}          <article class="product-card" data-id="{p['id']}" data-name="{p['name']}" data-price="{p['price']}" data-category="{p['cat']}">
            <div class="product-image">
{badge}              <!-- PUT PRODUCT IMAGE HERE (square photo works best; change src and alt) -->
              <a href="{PRODUCT_SEO[p['id']]['slug']}.html" aria-label="{p['name']}: details and price"><img src="images/product{p['id']}.jpg" width="600" height="600" alt="{p['alt']}, made to order in {LOC} by {NAME}" loading="lazy"></a>
            </div>
            <div class="product-info">
              <span class="product-category">{p['catlabel']}</span>
              <h{level} class="product-title"><a href="{PRODUCT_SEO[p['id']]['slug']}.html">{p['name']}</a></h{level}>
              <!-- UPDATE PRODUCT SIZE HERE (width × depth × height) -->
              <span class="product-spec">{p['spec']}</span>
              <p class="product-desc">{p['desc']}</p>
              <a class="text-link" href="contact.html">Order a custom size</a>
              <div class="product-bottom">
                <!-- UPDATE PRODUCT PRICE HERE (in Pakistani rupees; also update data-price above so the cart matches) -->
                <span class="price">Rs {p['price']:,}</span>
                <button class="btn btn-navy btn-sm add-to-cart">Add to Cart</button>
              </div>
              <!-- ORDER ON WHATSAPP: opens WhatsApp with this product already written in the message -->
              <a class="product-order" href="https://wa.me/{WA}?text={quote("Hello %s, I would like to order: %s (Rs %s). Please share the details." % (NAME, p['name'], format(p['price'], ',')))}" target="_blank" rel="noopener">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{WA_PATH}</svg> Order on WhatsApp
              </a>
            </div>
          </article>
"""


# --------------------------------------------------------------------------------------------
# SHARED PIECES
# --------------------------------------------------------------------------------------------
ICON_ATTR = 'width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"'
SOCIALS = [
    # (name, url, svg inner, is_ready)
    ("Facebook", FB, '<path fill="currentColor" d="M22 12a10 10 0 1 0-11.56 9.88v-6.99H7.9V12h2.54V9.8c0-2.51 1.49-3.89 3.77-3.89 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56V12h2.78l-.44 2.89h-2.34v6.99A10 10 0 0 0 22 12z"/>', True),
    ("Instagram", "#", '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.3" fill="currentColor"/>', False),
    ("LinkedIn", "#", '<rect x="3" y="3" width="18" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8" cy="8.2" r="1.3" fill="currentColor"/><path d="M8 11v6M12 17v-6M12 13.5c0-1.4 1-2.5 2.5-2.5S17 12 17 13.5V17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>', False),
    ("X (Twitter)", "#", '<path d="M5 4h3.5L19 20h-3.5z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M18.5 4 5.5 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>', False),
    ("YouTube", "#", '<rect x="2.5" y="5.5" width="19" height="13" rx="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 9.5v5l4.5-2.5z" fill="currentColor"/>', False),
    ("TikTok", "#", '<path d="M14 4v10.2a3.7 3.7 0 1 1-3.7-3.7M14 4c.3 2.4 1.9 4 4.3 4.2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>', False),
]


def social_html(indent="        "):
    out = []
    out.append(indent + ("<!-- SOCIAL MEDIA ICONS. Facebook is already linked to your page. FOR EACH OTHER ICON: when you create the account, "
                       "replace href=\"#\" with your page address and delete data-social-pending=\"...\". To add another network, copy one <a> line. -->"))
    for name, url, svg, ready in SOCIALS:
        if ready:
            out.append(f'{indent}<a href="{url}" aria-label="{NAME} on {name}" target="_blank" rel="noopener"><svg {ICON_ATTR}>{svg}</svg></a>')
        else:
            out.append(f'{indent}<!-- PUT YOUR {name.upper()} LINK HERE -->')
            out.append(f'{indent}<a href="{url}" aria-label="{NAME} on {name}" data-social-pending="{name}"><svg {ICON_ATTR}>{svg}</svg></a>')
    return "\n".join(out)


def nav_html(active):
    items = []
    for label, href, key in NAV:
        cur = ' aria-current="page"' if key == active else ""
        items.append(f'          <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(items)


def header(active):
    return f"""  <!-- ============================================================
       HEADER (THE SAME ON EVERY PAGE: if you change it, change it in all 6 .html files)
       ============================================================ -->
  <!-- ANNOUNCEMENT BAR (top of every page). UPDATE THE MESSAGE HERE. Only promise offers you really give. -->
  <div class="announce">
    <div class="container announce-inner">
      <span><span class="hide-sm">Made-to-order furniture &bull; </span>Get a clear quote on WhatsApp</span>
      <span class="announce-links"><a href="tel:{TEL}">Call {PHONE}</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></span>
    </div>
  </div>

  <header class="site-header">
    <div class="container header-inner">

      <!-- Mobile menu toggle button (don't remove, JS uses it) -->
      <button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>

      <!-- PUT YOUR LOGO HERE. To use a logo image, replace the two <span>s with <img src="logo.png" alt="{NAME}" height="44"> -->
      <a href="index.html" class="logo" aria-label="{NAME}, home">
        <span class="logo-name">Muhammad</span>
        <span class="logo-sub">Furnitures</span>
      </a>

      <!-- NAVIGATION LINKS: ADD / REMOVE / RENAME LINKS HERE -->
      <nav class="main-nav" id="mainNav" aria-label="Main navigation">
        <ul>
{nav_html(active)}
        </ul>
      </nav>

      <div class="header-actions">

        <!-- SEARCH: the magnifier opens the search bar under the header -->
        <button type="button" class="icon-btn" id="searchToggle" aria-label="Search furniture" aria-expanded="false" aria-controls="searchPanel">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </button>

        <!-- PHONE: taps to call on a phone. CHANGE THE NUMBER HERE (keep the +92 format in href, no spaces) -->
        <a class="header-phone" href="tel:{TEL}" aria-label="Call {PHONE}">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>{PHONE}</span>
        </a>

        <!-- CART ICON: opens the cart page (cart.html). The badge number updates automatically via script.js -->
        <a href="cart.html" class="cart-link" id="cartLink" aria-label="View cart">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span class="cart-count" id="cartCount">0</span>
        </a>
      </div>
    </div>

    <!-- SEARCH BAR (hidden until the magnifier is tapped). Searching takes visitors to the Shop page. -->
    <div class="search-panel" id="searchPanel" hidden>
      <div class="container">
        <form class="search-form" id="searchForm" action="shop.html" role="search">
          <input type="search" id="searchInput" placeholder="Search furniture, for example sofa, bed, wardrobe" aria-label="Search furniture">
          <button type="submit" class="btn btn-gold btn-sm">Search</button>
        </form>
      </div>
    </div>
  </header>
"""


def footer():
    links = "\n".join(
        f'          <li><a href="{href}">{label}</a></li>' for label, href, _ in NAV)
    return f"""  <!-- ============================================================
       FOOTER (THE SAME ON EVERY PAGE: if you change it, change it in all 6 .html files)
       ============================================================ -->
  <footer class="site-footer">
    <div class="container footer-grid">

      <!-- FOOTER COLUMN 1: BRAND + CONTACT -->
      <div class="footer-col">
        <a href="index.html" class="logo logo-light" aria-label="{NAME}, home">
          <span class="logo-name">Muhammad</span>
          <span class="logo-sub">Furnitures</span>
        </a>
        <!-- UPDATE SHORT BRAND DESCRIPTION HERE -->
        <p>Handcrafted furniture for homes, shops and offices. Made to order, built to last.</p>
        <p class="footer-contact"><a href="tel:{TEL}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>

      <!-- FOOTER COLUMN 2: QUICK LINKS -->
      <div class="footer-col">
        <h4>Quick links</h4>
        <ul>
{links}
          <li><a href="furniture-buying-guide.html">Furniture Buying Guide</a></li>
          <li><a href="{GOOGLE}" target="_blank" rel="noopener">Find Us on Google</a></li>
        </ul>
      </div>

      <!-- FOOTER COLUMN 3: NEWSLETTER + SOCIAL -->
      <!-- CONNECT TO YOUR EMAIL SERVICE HERE (Mailchimp, Klaviyo, etc.) by editing the form action or the handler in script.js -->
      <div class="footer-col">
        <h4>Get offers and new designs</h4>
        <p>Join our list for new designs, seasonal offers and updates.</p>
        <form class="newsletter-form" id="newsletterForm" action="#">
          <input type="email" id="newsletterEmail" placeholder="Your email address" required aria-label="Email address">
          <button type="submit" class="btn btn-gold">Subscribe</button>
        </form>
        <p class="form-message" id="newsletterMessage" aria-live="polite"></p>

        <div class="social-icons">
{social_html("          ")}
        </div>
      </div>
    </div>

    <!-- COPYRIGHT LINE (year updates automatically) -->
    <div class="footer-bottom">
      <div class="container">
        <p>&copy; <span id="year"></span> {NAME}. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- STICKY WHATSAPP BUTTON (the only sticky button: stays on screen while scrolling, on phones too). CHANGE THE NUMBER in the href (digits only, country code first, no +) and the message after text= -->
  <a class="whatsapp-float" href="https://wa.me/{WA}?text=Hello%20Muhammad%20Furnitures%2C%20I%20would%20like%20to%20ask%20about%20your%20furniture." target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">
    <svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>

  <!-- CALL POPUP: on computers (no calling app) and as a backup on phones. CHANGE THE NUMBER here and in the links above. Don't remove, JS uses it -->
  <div class="call-dialog" id="callDialog" role="dialog" aria-modal="true" aria-labelledby="callTitle" hidden>
    <div class="call-box">
      <button type="button" class="call-close" id="callClose" aria-label="Close">&times;</button>
      <h2 id="callTitle">Call {NAME}</h2>
      <p class="call-number">{PHONE}</p>
      <p class="call-note">On a phone, tap Call now. On a computer, please call this number from your phone, or message us on WhatsApp.</p>
      <div class="call-actions">
        <a class="btn btn-gold" href="tel:{TEL}" data-no-dialog>Call now</a>
        <button type="button" class="btn btn-outline" id="callCopy">Copy number</button>
        <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener" data-no-dialog>WhatsApp</a>
      </div>
    </div>
  </div>

  <!-- Small popup message shown when an item is added to the cart (don't remove, JS uses it) -->
  <div class="toast" id="toast" role="status" aria-live="polite"></div>

  <!-- All behavior (mobile menu, cart, call popup, search, category filter, quote form, newsletter) lives in script.js -->
  <script src="script.js"></script>
</body>
</html>
"""


def cta_band(title="Ready to furnish your home?", text="Call or message us with your size and style. We will reply with a clear price."):
    return f"""    <!-- ============================================================
         CALL TO ACTION BAND (same on most pages)
         ============================================================ -->
    <section class="cta-band">
      <div class="container">
        <h2>{title}</h2>
        <p>{text}</p>
        <div class="cta-actions">
          <a href="tel:{TEL}" class="btn btn-gold btn-lg">Call {PHONE}</a>
          <a href="https://wa.me/{WA}" class="btn btn-wa btn-lg" target="_blank" rel="noopener">WhatsApp Us</a>
        </div>
      </div>
    </section>
"""


def qa_box(text, extra=""):
    return f'''    <section class="quick-answer-wrap"><div class="container"><div class="quick-answer"><span class="qa-label">Quick answer</span><p>{text}</p>{extra}</div></div></section>\n'''


def quick(key, **kw):
    prices = [p["price"] for p in PRODUCTS]
    d = dict(name=NAME, loc=LOC, phone=PHONE, email=EMAIL, pmin=f"Rs {min(prices):,}", pmax=f"Rs {max(prices):,}")
    d.update(kw)
    return qa_box(QUICK[key].format(**d))


def banner(title, text, crumb, crumbs=None):
    if crumbs:
        crumb_html = "\n".join(
            (f'          <li><a href="{h}">{l}</a></li>' if h else f'          <li aria-current="page">{l}</li>') for l, h in crumbs)
    else:
        crumb_html = f'''          <li><a href="index.html">Home</a></li>
          <li aria-current="page">{crumb}</li>'''
    return f"""    <!-- ============================================================
         PAGE BANNER
         ============================================================ -->
    <section class="page-banner">
      <div class="container">
        <ul class="breadcrumb" aria-label="Breadcrumb">
{crumb_html}
        </ul>
        <h1>{title}</h1>
        <p>{text}</p>
      </div>
    </section>
"""


def page(filename, key, title, desc, main_html, ld=False, faq=False, noindex=False, extra_ld="", og_image="images/hero.jpg"):
    robots_meta = "" if noindex else '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">'
    canon = (SITE_URL + "/" + ("" if filename == "index.html" else filename)) if SITE_URL else None
    canon_tag = (f'<link rel="canonical" href="{canon}">' if canon else
                 f'<!-- CANONICAL: set SITE_URL in build_site.py and this becomes <link rel="canonical" href="https://YOUR-DOMAIN/{filename}"> -->')
    og_url = f'<meta property="og:url" content="{canon}">' if canon else ""
    og_img = (f'<meta property="og:image" content="{SITE_URL}/{og_image}">\n  <meta name="twitter:image" content="{SITE_URL}/{og_image}">' if SITE_URL else
              '<!-- og:image appears automatically once SITE_URL is set in build_site.py -->')
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- PAGE TITLE (browser tab + Google results). TIP: add your city, e.g. "... in Lahore | {NAME}" -->
  <title>{title}</title>

  <!-- SEO META DESCRIPTION (keep under 155 characters). TIP: add your city name here too -->
  <meta name="description" content="{desc}">

  <!-- SOCIAL SHARING PREVIEW (WhatsApp, Facebook). ADD og:image WITH A REAL PHOTO URL WHEN YOUR SITE IS LIVE -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:locale" content="en_PK">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  {og_url}
  {og_img}
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#4a2c1a">
  {robots_meta}
  {canon_tag}

  <!-- FAVICON: simple "M" icon, no file needed. REPLACE WITH YOUR OWN favicon.png IF YOU HAVE ONE -->
  <link rel="icon" href="{FAVICON}">

{local_ld() if ld else ''}{faq_ld() if faq else ''}{extra_ld}{'  <meta name="robots" content="noindex">' + chr(10) if noindex else ''}  <!-- FONTS: Playfair Display (big headings) + Montserrat (menus, buttons, text). Only the weights used are loaded, with display=swap. -->
{FONTS}
  <!-- All colors, fonts and spacing live in style.css (see ":root" at the top) -->
  <link rel="stylesheet" href="style.css">
</head>
<body>

"""
    body = header(key) + f'\n  <main data-page="{key}">\n\n' + main_html + "\n  </main>\n\n" + footer()
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(head + body)


# --------------------------------------------------------------------------------------------
# CATEGORY CARD ICONS
# --------------------------------------------------------------------------------------------
ICONS = {
    "living": '<path d="M4 11V8a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3v3"/><path d="M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2z"/><path d="M5 18v2M19 18v2"/>',
    "bedroom": '<path d="M3 20V6"/><path d="M3 15h18v5"/><path d="M21 15v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11.5" r="1.8"/>',
    "dining": '<path d="M3 10h18"/><path d="M5 10v10M19 10v10"/><path d="M9 10V6h6v4"/>',
    "office": '<rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8M12 16v4"/>',
    "storage": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M12 3v18M9.5 12h.01M14.5 12h.01"/>',
}
CATS = [
    ("living", "Living Room", "roomliving", "Sofa sets, TV units and coffee tables built to the size of your room."),
    ("bedroom", "Bedroom", "roombedroom", "Beds with storage and dressing tables, made to fit your mattress and your space."),
    ("dining", "Dining Room", "roomdining", "Dining tables for family meals, in the size and finish you choose."),
    ("office", "Office Furniture", "roomoffice", "Work desks made to fit your office or home study."),
    ("storage", "Storage", "roomstorage", "Wardrobes and shelves with plenty of space and a clean finish."),
]


def svg_icon(key):
    return ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % ICONS[key])


def cat_cards():
    out = []
    for key, label, seed, _ in CATS:
        out.append(f"""          <a href="shop.html#{key}" class="cat-card">
            <span class="cat-image"><img src="images/{seed}.jpg" width="480" height="360" alt="{ROOM_ALT[key]}" loading="lazy"></span>
            <span class="cat-icon">{svg_icon(key)}</span>
            <strong class="cat-name">{label}</strong>
            <span class="cat-link">Explore now</span>
          </a>""")
    return "\n".join(out)


TRUST = """    <!-- ============================================================
         TRUST CARD (floats over the bottom of the hero)
         ============================================================ -->
    <section class="trust">
      <div class="container">
        <div class="trust-card">
          <div class="trust-item">
            <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="9" r="6"/><path d="M8.5 14 7 22l5-3 5 3-1.5-8"/></svg>
            <div><strong>Quality Materials</strong><span>Chosen for lasting strength</span></div>
          </div>
          <div class="trust-item">
            <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21.3 8.7 8.7 21.3a1 1 0 0 1-1.4 0L2.7 16.7a1 1 0 0 1 0-1.4L15.3 2.7a1 1 0 0 1 1.4 0l4.6 4.6a1 1 0 0 1 0 1.4z"/><path d="m7.5 10.5 2 2M10.5 7.5l2 2M13.5 4.5l2 2M4.5 13.5l2 2"/></svg>
            <div><strong>Made to Order</strong><span>Built to your size and finish</span></div>
          </div>
          <div class="trust-item">
            <svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 3h15v13H1z"/><path d="M16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/></svg>
            <!-- UPDATE: confirm delivery details before publishing -->
            <div><strong>Delivery and Setup</strong><span>Ask us about delivery to your door</span></div>
          </div>
        </div>
      </div>
    </section>
"""

STEPS_FINISHES = """    <!-- ============================================================
         HOW A CUSTOM ORDER WORKS + FINISHES
         The steps are a real sequence, so they are numbered. KEEP ONLY WHAT MATCHES HOW YOU REALLY WORK.
         ============================================================ -->
    <section class="measure" id="custom-orders">
      <div class="container measure-grid">

        <div>
          <h2>Made to your measure</h2>
          <p class="measure-intro">From your first message to the finished piece.</p>
          <ol class="steps">
            <li>
              <span class="step-num">1</span>
              <div><h3>Tell us what you need</h3><p>Send photos, measurements or an idea by phone, WhatsApp or message.</p></div>
            </li>
            <li>
              <span class="step-num">2</span>
              <div><h3>Get a clear quote</h3><p>We confirm the design, materials, price and timeline.</p></div>
            </li>
            <li>
              <span class="step-num">3</span>
              <div><h3>We build it</h3><p>Your furniture is made to your size and checked before it leaves.</p></div>
            </li>
            <li>
              <span class="step-num">4</span>
              <div><h3>Delivery</h3><p>We bring it to your door and can help with setup.</p></div>
            </li>
          </ol>
        </div>

        <!-- FINISHES: EXAMPLES ONLY. Rename them and change the colours in style.css (.swatch-oak, .swatch-walnut, ...) to match your real finishes, or replace each .swatch-chip with a photo of a sample -->
        <div class="finishes">
          <h3>Pick a finish</h3>
          <div class="swatch-grid">
            <div class="swatch"><span class="swatch-chip swatch-oak"></span><strong>Natural oak</strong></div>
            <div class="swatch"><span class="swatch-chip swatch-walnut"></span><strong>Walnut</strong></div>
            <div class="swatch"><span class="swatch-chip swatch-espresso"></span><strong>Dark espresso</strong></div>
            <div class="swatch"><span class="swatch-chip swatch-white"></span><strong>Matt white</strong></div>
          </div>
          <p class="finishes-note">Looking for something else? Send us a photo and we will match it where we can.</p>
          <a href="contact.html" class="btn btn-gold">Request a Quote</a>
        </div>

      </div>
    </section>
"""

CRAFT_POINTS = """        <div class="craft-points">
          <div>
            <h3>Planned with you</h3>
            <p>We confirm the size, design and materials with you before any cutting starts.</p>
          </div>
          <div>
            <h3>Cut and joined</h3>
            <p>Careful assembly with strong joints, built to last through everyday family use.</p>
          </div>
          <div>
            <h3>Finished by hand</h3>
            <p>Smooth, clean finishing, then a last check before delivery.</p>
          </div>
        </div>
"""

PROOF = f"""    <!-- ============================================================
         REVIEWS LINKS (real links to your pages, no invented reviews)
         ============================================================ -->
    <section class="proof">
      <div class="container proof-inner">
        <h2>See our work and real customer reviews</h2>
        <p>Our latest pieces and what customers say are on our Google and Facebook pages.</p>
        <div class="proof-links">
          <!-- YOUR GOOGLE BUSINESS PAGE (the link you gave me) -->
          <a class="btn btn-outline" href="{GOOGLE}" target="_blank" rel="noopener">Our Google page</a>
          <!-- YOUR FACEBOOK PAGE (the link you gave me) -->
          <a class="btn btn-outline" href="{FB}" target="_blank" rel="noopener">Our Facebook page</a>
        </div>
      </div>
    </section>
"""


def _ic(path):
    return ('<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % path)


WHY = f"""    <!-- ============================================================
         WHY CHOOSE US (builds trust). CONFIRM EVERY POINT MATCHES HOW YOU REALLY WORK, then keep it.
         ============================================================ -->
    <section class="why">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">Why choose {NAME}</h2>
          <p>Furniture made by people you can speak to, built around your home.</p>
        </div>
        <div class="why-grid">
          <div class="why-card">
            <span class="why-icon">{_ic('<path d="M21.3 8.7 8.7 21.3a1 1 0 0 1-1.4 0L2.7 16.7a1 1 0 0 1 0-1.4L15.3 2.7a1 1 0 0 1 1.4 0l4.6 4.6a1 1 0 0 1 0 1.4z"/><path d="m7.5 10.5 2 2M10.5 7.5l2 2M13.5 4.5l2 2M4.5 13.5l2 2"/>')}</span>
            <h3>Made to your size</h3>
            <p>Tell us your space. We build to your measurements, so nothing is too big, too small or wasted.</p>
          </div>
          <div class="why-card">
            <span class="why-icon">{_ic('<path d="M12 3 4 6v6c0 4.5 3.2 8 8 9 4.8-1 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>')}</span>
            <h3>Strong, honest build</h3>
            <p>Solid joints and careful finishing, checked before your furniture leaves our workshop.</p>
          </div>
          <div class="why-card">
            <span class="why-icon">{_ic('<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>')}</span>
            <h3>A clear quote first</h3>
            <p>You get the price and timeline on WhatsApp before we start, so there are no surprises.</p>
          </div>
          <div class="why-card">
            <span class="why-icon">{_ic('<circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="10" r="1.2"/><circle cx="12" cy="7.5" r="1.2"/><circle cx="15.5" cy="10" r="1.2"/><path d="M12 21a3 3 0 0 1 0-6h2a2 2 0 0 0 0-4"/>')}</span>
            <h3>Your finish, your colour</h3>
            <p>Choose a wood tone or colour you love, or send a photo and we will match it where we can.</p>
          </div>
          <div class="why-card">
            <span class="why-icon">{_ic('<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>')}</span>
            <h3>Talk to the maker</h3>
            <p>You deal directly with the people who build your furniture. Quick answers, no call centre.</p>
          </div>
          <div class="why-card">
            <!-- UPDATE: confirm your delivery areas before publishing -->
            <span class="why-icon">{_ic('<path d="M1 3h15v13H1z"/><path d="M16 8h4l3 3v5h-7z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/>')}</span>
            <h3>Delivery to your door</h3>
            <p>We can deliver and help with setup. Ask us about your area when you request your quote.</p>
          </div>
        </div>
      </div>
    </section>
"""

HOW = f"""    <!-- ============================================================
         HOW IT WORKS (short version for the home page)
         ============================================================ -->
    <section class="how">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">Order in 3 easy steps</h2>
          <p>From your first message to furniture in your home.</p>
        </div>
        <ol class="how-steps">
          <li><span class="how-num">1</span><h3>Message us</h3><p>Send a photo, your size or just an idea on WhatsApp or by phone.</p></li>
          <li><span class="how-num">2</span><h3>Get your quote</h3><p>We confirm the design, finish, price and timeline with you.</p></li>
          <li><span class="how-num">3</span><h3>We build and deliver</h3><p>Your piece is made, checked and brought to your home.</p></li>
        </ol>
        <div class="how-cta">
          <a class="btn btn-wa btn-lg" href="https://wa.me/{WA}?text=Hello%20Muhammad%20Furnitures%2C%20I%20would%20like%20a%20quote." target="_blank" rel="noopener">Get a Quote on WhatsApp</a>
          <a class="btn btn-outline btn-lg" href="custom-furniture.html">How custom orders work</a>
        </div>
      </div>
    </section>
"""

# FAQ: shown on the page AND sent to Google as structured data (they must match). EDIT ANSWERS TO MATCH YOUR BUSINESS.
FAQS = [
    ("Can you make furniture to my size?",
     "Yes. We build beds, wardrobes, sofas, tables and more to your measurements, so the piece fits your room properly."),
    ("How do I get a price?",
     f"Send us a photo, your measurements or an idea on WhatsApp ({PHONE}). We reply with a clear price and timeline."),
    ("Can I choose the finish and colour?",
     "Yes. Pick a wood tone or colour, or send us a photo of the look you want and we will match it where we can."),
    ("What is the price of a sofa set, bed or wardrobe?",
     f"Prices start at Rs {min(p['price'] for p in PRODUCTS):,} and depend on the size, wood or board, fabric and finish. For example, our 5 seater sofa set starts at Rs 120,000 and our 3 door wardrobe at Rs 85,000. Send us your size and we give you the exact price before we start."),
    ("Can you make a full bed set?",
     "Yes. We build beds with storage and dressing tables, and we can plan them to match each other. Tell us which pieces you need and your mattress size."),
    ("Do you deliver?",
     f"We can deliver and help with setup in {LOC}. Tell us your area when you ask for a quote and we will confirm the details."),
    ("Can I see examples of your work?",
     "Yes. You can see our latest pieces and customer reviews on our Facebook page and our Google page."),
]


def faq_html():
    items = "\n".join(
        f"""          <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>""" for q, a in FAQS)
    return f"""    <!-- ============================================================
         FAQ (answers common worries, which builds trust and helps Google).
         If you edit an answer here, edit the same answer in the structured data in the <head> of this page.
         ============================================================ -->
    <section class="faq">
      <div class="container faq-inner">
        <div class="section-head">
          <h2 class="section-title">Questions? We have answers</h2>
          <p>Still unsure? Message us on WhatsApp and we will help.</p>
        </div>
        <div class="faq-list">
{items}
        </div>
      </div>
    </section>
"""


def faq_ld():
    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return ('  <!-- FAQ STRUCTURED DATA (must match the visible FAQ on the page) -->\n  <script type="application/ld+json">\n  '
            + json.dumps(data, indent=2).replace("\n", "\n  ") + "\n  </script>\n")


# --------------------------------------------------------------------------------------------
# PAGES
# --------------------------------------------------------------------------------------------
def build():
    os.makedirs(OUT, exist_ok=True)

    # ---------------- HOME ----------------
    home_products = "\n".join(product_card(p, first_comment=(i == 0)) for i, p in enumerate(PRODUCTS[:6]))
    home = f"""    <!-- ============================================================
         HERO SECTION
         ============================================================ -->
    <section class="hero" id="home">
      <!-- PUT YOUR BEST PHOTO HERE (a bright, wide room photo works best, about 1600 wide by 700 tall). Change src and alt. Keep fetchpriority so it loads first. -->
      <img class="hero-bg" src="images/hero.jpg" width="1600" height="760" alt="Living room with a handcrafted sofa set, centre table and TV unit made to order in {LOC}" fetchpriority="high">

      <div class="container">
        <div class="hero-text">
          <!-- UPDATE THE THREE WORDS IN THE TAG HERE -->
          <span class="hero-tag">Handcrafted &bull; Made to order &bull; Built to last</span>

          <!-- HERO HEADLINE: the first line is navy, the second is gold -->
          <h1><span class="h1-navy">Muhammad</span> <span class="h1-gold">Furnitures</span> <span class="h1-sub">Custom furniture maker in {LOC}</span></h1>

          <!-- UPDATE HERO TEXT HERE. TIP: add your city, e.g. "...made in Lahore" -->
          <p class="hero-sub">Made-to-order sofa sets, beds, wardrobes, dining tables and office furniture in {LOC}. Choose a ready design or tell us your size, style and budget, and our craftsmen will build it for you.</p>

          <div class="hero-actions">
            <a href="shop.html" class="btn btn-gold btn-lg">Shop Now</a>
            <a href="https://wa.me/{WA}?text=Hello%20Muhammad%20Furnitures%2C%20I%20would%20like%20a%20quote." class="btn btn-wa btn-lg" target="_blank" rel="noopener">Get a Quote</a>
            <a href="collections.html" class="link-explore">Explore Collections</a>
          </div>

          <ul class="hero-points">
            <li>Made to your size</li>
            <li>Clear price before we start</li>
            <li>Quick replies on WhatsApp</li>
          </ul>
        </div>
      </div>
    </section>

{TRUST}
    <!-- ============================================================
         SHOP BY CATEGORY (each card opens the Shop page already filtered)
         ============================================================ -->
    <section class="categories" id="categories">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">Shop by category</h2>
          <p>Find the perfect furniture for every space in your home.</p>
        </div>

        <div class="cat-grid">
          <!-- PUT CATEGORY PHOTOS HERE (change src and alt on each card) -->
{cat_cards()}
        </div>
      </div>
    </section>

{WHY}
    <!-- ============================================================
         PROMO BANNER
         REPLACE WITH A REAL OFFER ONLY IF YOU HAVE ONE (for example "Up to 30% off on selected items").
         ============================================================ -->
    <section class="promo">
      <!-- PUT BANNER PHOTO HERE (a bedroom or living room photo, about 900 wide by 700 tall) -->
      <img src="images/promo.jpg" width="900" height="700" alt="Custom made wardrobe with measurement lines: furniture built to your size in {LOC}" loading="lazy">
      <div class="promo-text">
        <span class="promo-label">Custom orders welcome</span>
        <h2>Built to <span>your size</span></h2>
        <p>In your choice of finish.</p>
        <a href="contact.html" class="btn btn-navy">Request a Quote</a>
      </div>
    </section>

    <!-- ============================================================
         FEATURED PRODUCTS
         These are the first 6 products from the Shop page. If you change one here, change it on shop.html too.
         NOTE: product names, sizes, prices and photos below are EXAMPLES. Replace them with your real pieces.
         ============================================================ -->
    <section class="products" id="featured">
      <div class="container">

        <div class="section-head">
          <h2 class="section-title">Featured products</h2>
          <p>Handpicked pieces that combine elegance, comfort and durability.</p>
        </div>

        <div class="product-grid">

{home_products}
        </div><!-- /.product-grid -->

        <div class="view-all"><a href="shop.html" class="btn btn-outline btn-lg">View All Products</a></div>
      </div>
    </section>

{HOW}
    <!-- ============================================================
         ABOUT TEASER (green band)
         ============================================================ -->
    <section class="craft">
      <div class="container">
        <div class="craft-top">
          <div>
            <h2>Built, not just assembled</h2>
            <p>Strong joints, clean finishing and furniture that is checked before it leaves. Every piece is planned with you, so it fits your room and your budget.</p>
            <a href="about.html" class="btn btn-gold" style="margin-top:26px">About Us</a>
          </div>
          <!-- PUT A WORKSHOP PHOTO HERE (craftsmen at work, a joint, a finish close-up) -->
          <img src="images/craft.jpg" width="900" height="675" alt="Furniture being built by hand at {NAME}" loading="lazy">
        </div>
      </div>
    </section>

{PROOF}
{home_seo()}
{faq_html()}
{cta_band()}"""
    page("index.html", "home", f"Furniture in {LOC} | Sofa Sets, Beds, Wardrobes | {NAME}",
         f"{NAME} makes sofa sets, beds, wardrobes and dining tables to your size in {LOC}. Clear prices. Quote on WhatsApp {PHONE}.",
         home, ld=True, faq=True)

    # ---------------- SHOP ----------------
    shop_products = "\n".join(product_card(p, first_comment=(i == 0), level=2) for i, p in enumerate(PRODUCTS))
    shop = f"""{banner(f"Shop furniture online in {LOC}", "Sofa sets, beds, wardrobes, dining tables and office desks. Every piece can be made to your size and finish.", "Shop")}
{quick("shop")}
    <!-- ============================================================
         PRODUCTS: every product lives here
         To add a product: copy one whole <article class="product-card"> block and paste it below the last one.
         To remove a product: delete its whole <article> block.
         NOTE: product names, sizes, prices and photos below are EXAMPLES. Replace them with your real pieces.
         ============================================================ -->
    <section class="products" id="shop">
      <div class="container">

        <!-- FILTER BUTTONS: rename or remove categories to match your range. The data-filter value must match a product's data-category -->
        <div class="filters" role="group" aria-label="Filter furniture by category">
          <button type="button" class="filter-chip is-active" data-filter="all" aria-pressed="true">All</button>
          <button type="button" class="filter-chip" data-filter="living" aria-pressed="false">Living Room</button>
          <button type="button" class="filter-chip" data-filter="bedroom" aria-pressed="false">Bedroom</button>
          <button type="button" class="filter-chip" data-filter="dining" aria-pressed="false">Dining Room</button>
          <button type="button" class="filter-chip" data-filter="office" aria-pressed="false">Office</button>
          <button type="button" class="filter-chip" data-filter="storage" aria-pressed="false">Storage</button>
        </div>

        <div class="product-grid">

{shop_products}
        </div><!-- /.product-grid -->

        <!-- Shown automatically when a filter or search has no products (don't remove, JS uses it) -->
        <p class="no-results" id="noResults" hidden>No pieces found. Tell us what you need and we will build it.</p>

        <!-- CUSTOM ORDER PANEL: for visitors who do not see the size or style they want -->
        <div class="shop-custom">
          <div class="shop-custom-text">
            <h2>Can't find the size or style you need?</h2>
            <p>Every piece can be made to your measurements and finish. Send us a photo or your idea and we will reply with a clear price.</p>
          </div>
          <div class="shop-custom-actions">
            <a class="btn btn-gold btn-lg" href="custom-furniture.html">Order Custom Furniture</a>
            <a class="btn btn-wa btn-lg" href="https://wa.me/{WA}?text=Hello%20Muhammad%20Furnitures%2C%20I%20need%20a%20custom%20size%20or%20style.%20I%20will%20send%20a%20photo." target="_blank" rel="noopener">Send a Photo on WhatsApp</a>
          </div>
        </div>
      </div>
    </section>

{price_table()}
    <!-- SHOP SEO TEXT (helps Google understand the page and reassures buyers). EDIT TO MATCH YOUR RANGE. -->
    <section class="seo-text">
      <div class="container seo-inner">
        <h2>Furniture made well, made for your home</h2>
        <p>At {NAME} every bed, sofa set, wardrobe, dining table and office desk is built by our own craftsmen with strong joints and a clean finish. Because we make the furniture ourselves, we can change the size, colour and finish to suit your room and your budget.</p>
        <p>Not sure what will fit? Send us a photo of your room and your measurements on WhatsApp. We will suggest a design and give you a clear price before we start.</p>
      </div>
    </section>

{cta_band()}"""
    page("shop.html", "shop", f"Buy Furniture Online in {LOC} | Sofa Sets, Beds | {NAME}",
         f"Buy sofa sets, beds, wardrobes, dining tables and office desks in {LOC}. See starting prices in Rs. Made to your size by {NAME}.", shop,
         extra_ld=shop_ld())

    # ---------------- COLLECTIONS ----------------
    rows = []
    for key, label, seed, text in CATS:
        rows.append(f"""        <div class="collection-row">
          <!-- PUT COLLECTION PHOTO HERE (change src and alt) -->
          <img src="images/{seed}.jpg" width="800" height="600" alt="{ROOM_ALT[key]}" loading="lazy">
          <div>
            <h2>{COLLECTION_EXTRA[key][0]}</h2>
            <!-- UPDATE COLLECTION TEXT HERE -->
            <p>{text}</p>
            {collection_extra(key)}
            <a href="shop.html#{key}" class="btn btn-navy">View {label}</a>
          </div>
        </div>""")
    collections = f"""{banner(f"Furniture collections for every room in {LOC}", "Living room, bedroom, dining room, office and storage furniture, made to your size.", "Collections")}
{quick("collections")}
    <!-- ============================================================
         COLLECTIONS (one block per room; copy a whole .collection-row to add another)
         ============================================================ -->
    <section class="collections">
      <div class="container">
        <p class="collections-intro">Every collection is made by our craftsmen and can be adjusted to your size and finish. Pick a room to see what we build.</p>
{chr(10).join(rows)}
      </div>
    </section>

{cta_band()}"""
    page("collections.html", "collections", f"Furniture Collections: Sofa Sets, Beds, Office | {NAME}",
         f"Explore sofa sets, bed sets, dining tables, office desks and wardrobes made to your size in {LOC} by {NAME}.", collections,
         extra_ld=crumb_ld([("Home", "index.html"), ("Collections", "collections.html")]))

    # ---------------- CUSTOM FURNITURE ----------------
    custom = f"""{banner(f"Custom furniture made to order in {LOC}", "Tell us the size, pick a finish, and we build it.", "Custom Furniture")}
{quick("custom")}
    <!-- ============================================================
         WHAT WE CAN BUILD (EDIT THE LIST TO MATCH WHAT YOU REALLY MAKE)
         ============================================================ -->
    <section class="what-we-build">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">What we can build</h2>
          <p>If you can describe it or show us a photo, we can plan it with you.</p>
        </div>
        <ul class="check-list">
          <li>Beds and bed frames</li>
          <li>Wardrobes and cupboards</li>
          <li>Sofa sets</li>
          <li>Dining tables and chairs</li>
          <li>Office desks</li>
          <li>TV units and shelves</li>
        </ul>
      </div>
    </section>

{STEPS_FINISHES}
    <!-- ============================================================
         HOW TO MEASURE (helpful for your customers)
         ============================================================ -->
    <section class="measure-tips">
      <div class="container tips-grid">
        <div>
          <h2>How to measure your space</h2>
          <p>A few simple measurements help us give you a quick, accurate quote.</p>
        </div>
        <ul class="tips">
          <li><strong>Width, depth and height.</strong> Measure the space in centimetres where the furniture will stand.</li>
          <li><strong>Doors and stairs.</strong> Note the width of doorways and stairs the piece must pass through.</li>
          <li><strong>Sockets and windows.</strong> Mention anything on the wall that the furniture must work around.</li>
          <li><strong>Send photos.</strong> A photo of the space and any design you like helps us understand your idea.</li>
        </ul>
      </div>
    </section>

{faq_html()}
{cta_band("Have a design in mind?", "Send us your measurements or a photo on WhatsApp, or call us. We will reply with a clear quote.")}"""
    page("custom-furniture.html", "custom", f"Custom Furniture Maker in {LOC} | Made to Order | {NAME}",
         f"Order custom sofa sets, beds, wardrobes and tables made to your size and finish in {LOC}. Send your measurements to {NAME} for a clear quote.", custom, faq=True,
         extra_ld=crumb_ld([("Home", "index.html"), ("Custom Furniture", "custom-furniture.html")]))

    # ---------------- ABOUT ----------------
    about = f"""{banner("About us", f"Meet {NAME}, a local furniture maker.", "About Us")}
{quick("about")}
    <!-- ============================================================
         ABOUT SECTION
         ============================================================ -->
    <section class="about" id="about">
      <div class="container about-inner">
        <!-- PUT YOUR ABOUT IMAGE HERE (a photo of your workshop or your craftsmen) -->
        <img src="images/about.jpg" width="900" height="720" alt="Craftsmen building furniture at {NAME}" loading="lazy">
        <div class="about-text">
          <h2>About {NAME}</h2>
          <!-- UPDATE ABOUT TEXT: add your city and the year you started, e.g. "based in Lahore. Since 2012, we have built..." -->
          <p>{NAME} is a local furniture maker. We build beds, sofas, wardrobes and tables for homes, shops and offices.</p>
          <p>We work with you from the first measurement to the final polish. You tell us what you need, we suggest the right design and materials, and our craftsmen build it. Because we make everything ourselves, we can adjust sizes, colours and finishes to match your space and your budget.</p>
          <p>We care about simple things: strong joints, clean finishing, honest prices and delivery on the day we promise.</p>
          <a href="contact.html" class="btn btn-outline">Get in Touch</a>
        </div>
      </div>
    </section>

{facts_block()}
{WHY}
    <!-- ============================================================
         CRAFT SECTION (green band)
         CONFIRM THESE STATEMENTS MATCH YOUR REAL PROCESS BEFORE PUBLISHING.
         ============================================================ -->
    <section class="craft" id="craft">
      <div class="container">
        <div class="craft-top">
          <div>
            <h2>Built, not just assembled</h2>
            <p>Every step is under our control. That means strong joints, clean finishing, and furniture that is checked before it leaves.</p>
          </div>
          <!-- PUT A WORKSHOP PHOTO HERE (craftsmen at work, a joint, a finish close-up) -->
          <img src="images/craft.jpg" width="900" height="675" alt="Furniture being built by hand at {NAME}" loading="lazy">
        </div>
{CRAFT_POINTS}      </div>
    </section>

{PROOF}
{cta_band()}"""
    page("about.html", "about", f"About {NAME} | Furniture Maker in {LOC}",
         f"{NAME} is a furniture maker in {LOC} building sofa sets, beds, wardrobes and tables with strong joints and clean finishing.", about,
         extra_ld=crumb_ld([("Home", "index.html"), ("About Us", "about.html")]) + page_ld("AboutPage", "About " + NAME, "about.html"))

    # ---------------- CONTACT ----------------
    contact = f"""{banner("Contact us", "Call, WhatsApp or send a request. We will reply with a clear price and timeline.", "Contact")}
{quick("contact")}
    <!-- ============================================================
         CONTACT + QUOTE FORM
         ============================================================ -->
    <section class="contact" id="contact">
      <div class="container contact-grid">

        <div>
          <h2>Request a quote</h2>
          <p>Tell us what you want built and roughly what size. We will reply with a clear price and timeline.</p>

          <!-- CONTACT DETAILS: change the number in BOTH the href and the visible text. Keep the +92 format in href. -->
          <dl class="contact-list">
            <div><dt>Phone</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd></div>
            <div><dt>WhatsApp</dt><dd><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{PHONE}</a></dd></div>
            <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
            <div><dt>Address</dt><dd><!-- PUT YOUR ADDRESS HERE (copy it exactly as on your Google listing) -->[Add your address]</dd></div>
            <div><dt>Hours</dt><dd><!-- PUT YOUR OPENING HOURS HERE -->[Add days and hours]</dd></div>
          </dl>

          <div class="contact-quick">
            <a class="btn btn-wa btn-lg" href="https://wa.me/{WA}?text=Hello%20Muhammad%20Furnitures%2C%20I%20would%20like%20a%20quote." target="_blank" rel="noopener">Chat on WhatsApp</a>
            <a class="btn btn-outline btn-lg" href="{GOOGLE}" target="_blank" rel="noopener">Find us on Google</a>
          </div>
          <div class="social-icons social-icons-dark">
{social_html("            ")}
          </div>
        </div>

        <!-- QUOTE FORM: opens WhatsApp with the details filled in (number is set in script.js, SETTINGS.whatsappNumber) -->
        <form class="quote-form" id="quoteForm" action="#">
          <div class="form-row">
            <div class="field">
              <label for="quoteName">Your name</label>
              <input type="text" id="quoteName" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="quotePhone">Phone / WhatsApp</label>
              <input type="tel" id="quotePhone" name="phone" autocomplete="tel" required>
            </div>
          </div>
          <div class="field">
            <label for="quoteItem">What do you need?</label>
            <select id="quoteItem" name="item">
              <option>Living room furniture</option>
              <option>Bedroom furniture</option>
              <option>Dining table or chairs</option>
              <option>Office furniture</option>
              <option>Wardrobe or storage</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="field">
            <label for="quoteDetails">Size and details</label>
            <textarea id="quoteDetails" name="details" rows="4" placeholder="For example: a wardrobe 180 cm wide, white finish"></textarea>
          </div>
          <button type="submit" class="btn btn-gold btn-lg">Send on WhatsApp</button>
          <p class="form-message" id="quoteMessage" aria-live="polite"></p>
        </form>

      </div>
    </section>

{PROOF}"""
    page("contact.html", "contact", f"Contact {NAME} | Get a Furniture Quote in {LOC}",
         f"Call or WhatsApp {PHONE}, email {EMAIL}, or send a quote request to {NAME}. Custom furniture made to your size in {LOC}.", contact,
         extra_ld=crumb_ld([("Home", "index.html"), ("Contact", "contact.html")]) + page_ld("ContactPage", "Contact " + NAME, "contact.html"))

    # ---------------- CART ----------------
    cart = f"""{banner("Your cart", "Check your items, then send your order to us on WhatsApp. We confirm the final price and delivery with you.", "Cart")}
    <!-- ============================================================
         CART PAGE (filled in by script.js from the items visitors add)
         CONNECT A REAL CHECKOUT / PAYMENT SYSTEM HERE LATER. For now the order is sent to your WhatsApp.
         ============================================================ -->
    <section class="cart-page">
      <div class="container">

        <div class="cart-empty" id="cartEmpty" hidden>
          <h2>Your cart is empty</h2>
          <p>Browse our furniture and add the pieces you like.</p>
          <a class="btn btn-gold btn-lg" href="shop.html">Browse Furniture</a>
        </div>

        <div class="cart-layout" id="cartLayout" hidden>
          <ul class="cart-list" id="cartList"></ul>

          <aside class="cart-summary">
            <h2>Order summary</h2>
            <div class="sum-row"><span>Items</span><strong id="cartItems">0</strong></div>
            <div class="sum-row sum-total"><span>Estimated total</span><strong id="cartTotal">Rs 0</strong></div>
            <p class="sum-note">Delivery and custom changes are confirmed by us on WhatsApp before you pay anything.</p>
            <a class="btn btn-wa btn-lg" id="cartCheckout" href="https://wa.me/{WA}" target="_blank" rel="noopener">Order on WhatsApp</a>
            <a class="btn btn-outline" href="shop.html">Continue Shopping</a>
            <button type="button" class="link-btn" id="cartClear">Clear cart</button>
          </aside>
        </div>
      </div>
    </section>

{cta_band("Need help choosing?", "Call or message us. We will help you pick the right size and finish.")}"""
    page("cart.html", "cart", f"Your Cart | {NAME}", f"Review your selected furniture and send your order to {NAME} on WhatsApp.", cart, noindex=True)

    build_product_pages()
    build_guide()
    build_sitemap()


# --------------------------------------------------------------------------------------------
# SEO PIECES: home keyword text, price table, product pages, buying guide, sitemap
# --------------------------------------------------------------------------------------------
PBYID = {p["id"]: p for p in PRODUCTS}


def money(n):
    return f"Rs {n:,}"


def plink(pid, text=None):
    return f'<a href="{PRODUCT_SEO[pid]["slug"]}.html">{text or PBYID[pid]["name"]}</a>'


def home_seo():
    return f"""    <!-- ============================================================
         HOME SEO TEXT (real words for Google and for buyers: what we make, where, and links to every product).
         EDIT TO MATCH YOUR RANGE. Set CITY in build_site.py to put your city in these sentences.
         ============================================================ -->
    <section class="seo-text home-seo">
      <div class="container seo-inner">
        <h2>Made-to-order furniture in {LOC}</h2>
        <p>{NAME} makes sofa sets, beds, wardrobes, dining tables, office desks, TV units and centre tables for homes, shops and offices in {LOC}. Every piece is built to your size, in the wood tone, fabric and finish you choose, and you get a clear price before we start.</p>
        <p>Popular pieces: {plink(4, "5 seater sofa set")}, {plink(2, "double bed with storage")}, {plink(3, "3 door wardrobe")}, {plink(1, "6 seater dining table")}, {plink(5, "office desk")}, {plink(6, "TV unit")}, {plink(7, "centre table")} and {plink(8, "dressing table with mirror")}.</p>
        <p>Not sure what size or style to choose? Read our <a href="furniture-buying-guide.html">furniture buying guide</a>, or send your measurements on WhatsApp and we will suggest a design.</p>
      </div>
    </section>
"""


def price_table():
    rows = "\n".join(
        f'            <tr><th scope="row">{plink(p["id"])}</th><td>{p["spec"]}</td><td>{money(p["price"])}</td></tr>' for p in PRODUCTS)
    return f"""    <!-- ============================================================
         PRICE GUIDE (people search "price in Pakistan". These numbers come from the PRODUCTS list in build_site.py, so they always match the cards.)
         ============================================================ -->
    <section class="price-guide">
      <div class="container seo-inner">
        <h2>Furniture prices in {LOC}: starting prices</h2>
        <p>These are starting prices in Pakistani rupees for the standard size shown. Your exact price depends on your size, the wood or board, the fabric and the finish. Send your measurements on WhatsApp and we will confirm the price before we start.</p>
        <div class="table-wrap">
          <table class="price-table">
            <thead><tr><th scope="col">Furniture</th><th scope="col">Standard size</th><th scope="col">Starting price</th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""


def product_ld(p, full=False):
    seo = PRODUCT_SEO[p["id"]]
    d = {"@type": "Product", "name": p["name"],
         "description": seo["lead"], "brand": {"@type": "Brand", "name": NAME},
         "category": p["catlabel"], "sku": "MF-" + str(p["id"]).zfill(3), "itemCondition": "https://schema.org/NewCondition",
         "offers": {"@type": "Offer", "price": str(p["price"]), "priceCurrency": "PKR",
                    "availability": "https://schema.org/MadeToOrder"}}
    if SITE_URL:
        d["image"] = absurl(f"images/product{p['id']}.jpg")
        d["offers"]["url"] = absurl(seo["slug"] + ".html")
    if full:
        d = {"@context": "https://schema.org", **d}
    return d


def shop_ld():
    items = []
    for n, p in enumerate(PRODUCTS, 1):
        e = {"@type": "ListItem", "position": n, "name": p["name"], "item": product_ld(p)}
        if SITE_URL:
            e["url"] = absurl(PRODUCT_SEO[p["id"]]["slug"] + ".html")
        items.append(e)
    lst = {"@context": "https://schema.org", "@type": "ItemList", "name": f"Furniture made to order by {NAME}", "itemListElement": items}
    return crumb_ld([("Home", "index.html"), ("Shop", "shop.html")]) + ld_script(lst)


def collection_extra(key):
    _, ids, text = COLLECTION_EXTRA[key]
    links = ", ".join(plink(i) for i in ids)
    return f'<p class="coll-extra">{text} See: {links}.</p>'


def faq_ld_for(pairs):
    data = {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}
    return ld_script(data)


def fmt(text, p):
    return text.replace("{price}", money(p["price"])).replace("{name}", NAME).replace("{phone}", PHONE)


def build_product_pages():
    for p in PRODUCTS:
        seo = PRODUCT_SEO[p["id"]]
        pid = p["id"]
        title = f"{seo['title']} | {NAME}"
        meta = seo["meta"].replace("{name}", NAME).replace("{price}", money(p["price"])).replace("{phone}", PHONE)
        faq_pairs = [(q, fmt(a, p)) for q, a in seo["faq"]]
        feats = "\n".join(f"            <li>{f}</li>" for f in seo["features"])
        paras = "\n".join(f"        <p>{t}</p>" for t in seo["paras"])
        faq_items = "\n".join(
            f'          <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in faq_pairs)
        related = "\n".join(
            f"""          <a class="related-card" href="{PRODUCT_SEO[r]['slug']}.html">
            <img src="images/product{r}.jpg" width="600" height="600" alt="{PBYID[r]['alt']}, made to order by {NAME}" loading="lazy">
            <strong>{PBYID[r]['name']}</strong>
            <span>From {money(PBYID[r]['price'])}</span>
          </a>""" for r in seo["related"])
        wa_msg = quote("Hello %s, I would like to order: %s (Rs %s). Please share the details." % (NAME, p["name"], format(p["price"], ",")))
        main = f"""{banner(seo['h1'], seo['lead'], p['name'], crumbs=[('Home', 'index.html'), ('Shop', 'shop.html'), (p['name'], None)])}
{qa_box(QUICK['product'].format(name=NAME, item=p['name'], price=money(p['price']), spec=p['spec']))}
    <!-- ============================================================
         PRODUCT PAGE: {p['name']}
         EDIT THE TEXT BELOW (the details come from the PRODUCTS list in build_site.py and seo_content.py)
         ============================================================ -->
    <section class="pdp">
      <div class="container pdp-grid">
        <div class="pdp-media">
          <!-- PUT PRODUCT IMAGE HERE (square photo works best; change src and alt) -->
          <img src="images/product{pid}.jpg" width="600" height="600" alt="{p['alt']}, made to order in {LOC} by {NAME}" fetchpriority="high">
        </div>
        <article class="product-card pdp-card" data-id="{pid}" data-name="{p['name']}" data-price="{p['price']}" data-category="{p['cat']}">
          <span class="product-category">{p['catlabel']}</span>
          <p class="pdp-price"><span class="price">{money(p['price'])}</span> <small>starting price, made to your size</small></p>
          <span class="product-spec">Standard size: {p['spec']}</span>
          <p class="pdp-lead">{seo['lead']}</p>
          <ul class="pdp-features">
{feats}
          </ul>
          <div class="pdp-actions">
            <button class="btn btn-navy add-to-cart">Add to Cart</button>
            <a class="btn btn-wa" href="https://wa.me/{WA}?text={wa_msg}" target="_blank" rel="noopener">Order on WhatsApp</a>
          </div>
          <p class="pdp-note">Final price depends on your size, wood or board, fabric and finish. We confirm it with you before we start.</p>
        </article>
      </div>
    </section>

    <section class="seo-text pdp-long">
      <div class="container seo-inner pdp-inner">
        <h2>About the {p['name'].lower()}</h2>
{paras}
        <h2>{p['name']}: key facts</h2>
        <dl class="facts">
          <div><dt>Starting price</dt><dd>{money(p['price'])} (standard size)</dd></div>
          <div><dt>Standard size</dt><dd>{p['spec']}</dd></div>
          <div><dt>Made to order</dt><dd>Yes. Size, colour and finish can be changed.</dd></div>
          <div><dt>Materials</dt><dd>Chosen with you and named in your written quote</dd></div>
          <div><dt>How to order</dt><dd>WhatsApp or call {PHONE}, or add to cart</dd></div>
          <div><dt>Delivery</dt><dd>Can be arranged in {LOC}. Tell us your area when you ask.</dd></div>
          <div><dt>Last updated</dt><dd><time datetime="{UPDATED_ISO}">{UPDATED_TEXT}</time></dd></div>
        </dl>
        <p>Want to see more? Browse the <a href="shop.html">full shop</a>, read the <a href="furniture-buying-guide.html">furniture buying guide</a>, or <a href="custom-furniture.html">order a custom size</a>.</p>
      </div>
    </section>

    <section class="faq pdp-faq">
      <div class="container faq-inner">
        <div class="section-head"><h2 class="section-title">Questions about the {p['name'].lower()}</h2></div>
        <div class="faq-list">
{faq_items}
        </div>
      </div>
    </section>

    <section class="related">
      <div class="container">
        <div class="section-head"><h2 class="section-title">You may also like</h2></div>
        <div class="related-grid">
{related}
        </div>
      </div>
    </section>

{cta_band("Want this " + p['name'].lower() + " in your size?", "Send your measurements or a photo on WhatsApp, or call us. We will reply with a clear quote.")}"""
        ld = crumb_ld([("Home", "index.html"), ("Shop", "shop.html"), (p["name"], seo["slug"] + ".html")]) \
            + ld_script(product_ld(p, full=True)) + faq_ld_for(faq_pairs)
        page(seo["slug"] + ".html", "shop", title, meta, main, extra_ld=ld, og_image=f"images/product{pid}.jpg")


def build_guide():
    toc = "\n".join(f'          <li><a href="#{sid}">{h}</a></li>' for sid, h, _, _ in GUIDE_SECTIONS)
    secs = []
    for sid, h, paras, links in GUIDE_SECTIONS:
        ps = "\n".join(f"          <p>{t}</p>" for t in paras)
        ln = ""
        if links:
            ln = '\n          <p class="guide-links">See: ' + ", ".join(plink(i, t) for _, t, i in links) + ".</p>"
        secs.append(f"""        <section class="guide-section" id="{sid}">
          <h2>{h}</h2>
          <p class="short-answer"><strong>Short answer:</strong> {GUIDE_SHORT[sid]}</p>
{ps}{ln}
        </section>""")
    faq_items = "\n".join(f'          <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>' for q, a in GUIDE_FAQ)
    main = f"""{banner("Furniture buying guide for Pakistan", "How to choose a sofa set, bed, wardrobe, dining table and office desk, what to ask about wood and finish, and how to measure your space.", "Furniture Guide", crumbs=[("Home", "index.html"), ("Furniture Guide", None)])}
{quick("guide")}
    <!-- ============================================================
         BUYING GUIDE (helpful, honest advice. People search "sofa set design", "bed set", "wardrobe design" before they buy.)
         ============================================================ -->
    <article class="guide">
      <div class="container guide-inner">
        <p class="byline">Written by the team at {NAME}. Last updated <time datetime="{UPDATED_ISO}">{UPDATED_TEXT}</time>.</p>
        <nav class="guide-toc" aria-label="In this guide">
          <h2>In this guide</h2>
          <ol>
{toc}
          </ol>
        </nav>
{chr(10).join(secs)}
        <section class="guide-section" id="faq">
          <h2>Furniture buying questions</h2>
          <div class="faq-list">
{faq_items}
          </div>
        </section>
      </div>
    </article>

{cta_band("Ready to plan your furniture?", "Send your measurements or a photo on WhatsApp, or call us. We will suggest a design and give you a clear price.")}"""
    art = {"@context": "https://schema.org", "@type": "Article", "headline": "Furniture buying guide for Pakistan",
           "description": "How to choose a sofa set, bed, wardrobe, dining table and office desk, and what to ask about wood and finish.",
           "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO, "inLanguage": "en-PK",
           "author": {"@type": "Organization", "name": NAME}, "publisher": {"@type": "Organization", "name": NAME}}
    if SITE_URL:
        art["mainEntityOfPage"] = absurl("furniture-buying-guide.html")
    ld = crumb_ld([("Home", "index.html"), ("Furniture Guide", "furniture-buying-guide.html")]) + ld_script(art) + faq_ld_for(GUIDE_FAQ)
    page("furniture-buying-guide.html", "guide", f"Furniture Buying Guide: Sofa Set, Bed, Wardrobe | {NAME}",
         f"How to choose a sofa set, bed, wardrobe, dining table and office desk, plus wood, finish and measuring tips from {NAME}.",
         main, extra_ld=ld)


def page_ld(kind, name, filename):
    d = {"@context": "https://schema.org", "@type": kind, "name": name, "inLanguage": "en-PK",
         "dateModified": UPDATED_ISO, "about": {"@id": (SITE_URL + "/#business") if SITE_URL else "#business"}}
    if SITE_URL:
        d["url"] = absurl(filename)
    return ld_script(d)


def facts_block():
    where = CITY + ", Pakistan" if CITY else "Pakistan"
    return f"""    <!-- ============================================================
         AT A GLANCE (clear facts about the business: easy for Google and AI answers to quote. UPDATE with your address and hours when you have them.)
         ============================================================ -->
    <section class="at-a-glance">
      <div class="container">
        <div class="section-head"><h2 class="section-title">{NAME} at a glance</h2></div>
        <dl class="facts facts-wide">
          <div><dt>Business</dt><dd>{NAME}, furniture maker</dd></div>
          <div><dt>What we make</dt><dd>Sofa sets, beds, wardrobes, dining tables, office desks, TV units, centre tables, dressing tables, bookshelves</dd></div>
          <div><dt>How we work</dt><dd>Made to order, to your size, colour and finish</dd></div>
          <div><dt>Where</dt><dd>{where}</dd></div>
          <!-- ADD YOUR STREET ADDRESS AND OPENING HOURS HERE -->
          <div><dt>Phone and WhatsApp</dt><dd><a href="tel:{TEL}">{PHONE}</a></dd></div>
          <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div><dt>Prices</dt><dd>In Pakistani rupees (Rs). Clear price confirmed before we start.</dd></div>
          <div><dt>Last updated</dt><dd><time datetime="{UPDATED_ISO}">{UPDATED_TEXT}</time></dd></div>
        </dl>
      </div>
    </section>
"""


AI_BOTS = [
    ("OAI-SearchBot", "ChatGPT search"), ("ChatGPT-User", "ChatGPT when a person asks it to open a page"), ("GPTBot", "OpenAI"),
    ("PerplexityBot", "Perplexity"), ("Perplexity-User", "Perplexity when a person asks"),
    ("ClaudeBot", "Anthropic Claude"), ("Claude-SearchBot", "Claude search"), ("Claude-User", "Claude when a person asks"),
    ("Google-Extended", "Google Gemini"), ("Applebot-Extended", "Apple"), ("CCBot", "Common Crawl, used by many AI tools"),
]


def build_sitemap():
    base = SITE_URL or "https://YOUR-DOMAIN"
    pages = [("", "1.0"), ("shop.html", "0.9"), ("collections.html", "0.8"), ("custom-furniture.html", "0.9"),
             ("furniture-buying-guide.html", "0.7"), ("about.html", "0.6"), ("contact.html", "0.7")]
    pages += [(PRODUCT_SEO[p["id"]]["slug"] + ".html", "0.8") for p in PRODUCTS]
    urls = "\n".join(f"  <url><loc>{base}/{u}</loc><lastmod>{UPDATED_ISO}</lastmod><priority>{pr}</priority></url>" for u, pr in pages)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<!-- Replace https://YOUR-DOMAIN with your real website address (or set SITE_URL in build_site.py and rebuild) -->\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n")
    bots = "\n".join(f"# {why}\nUser-agent: {name}\nAllow: /\nDisallow: /cart.html\n" for name, why in AI_BOTS)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("# Replace YOUR-DOMAIN with your real website address (or set SITE_URL in build_site.py and rebuild)\n"
                "User-agent: *\nAllow: /\nDisallow: /cart.html\n\n"
                "# AI search and answer engines are allowed, so your furniture can be found and quoted in AI answers.\n"
                "# To stop one of them, change its 'Allow: /' line to 'Disallow: /'.\n\n"
                + bots + f"\nSitemap: {base}/sitemap.xml\n")
    # llms.txt: an optional plain-text summary for AI tools (Google says it does not need it; other tools may read it)
    lines = [f"# {NAME}", "",
             f"> {NAME} is a furniture maker in {LOC}. We build sofa sets, beds, wardrobes, dining tables, office desks, TV units, centre tables, dressing tables and bookshelves to order, to your size, colour and finish. Prices are in Pakistani rupees (Rs).", "",
             "## Contact", f"- Phone and WhatsApp: {PHONE}", f"- Email: {EMAIL}", "",
             "## Main pages",
             f"- [Shop and starting prices]({base}/shop.html): all furniture with starting prices",
             f"- [Custom furniture]({base}/custom-furniture.html): how made-to-order works",
             f"- [Furniture buying guide]({base}/furniture-buying-guide.html): how to choose and measure",
             f"- [Collections]({base}/collections.html): living room, bedroom, dining, office, storage",
             f"- [About]({base}/about.html) and [Contact]({base}/contact.html)", "", "## Products"]
    for p in PRODUCTS:
        lines.append(f"- [{p['name']}]({base}/{PRODUCT_SEO[p['id']]['slug']}.html): from {money(p['price'])}, {p['spec']}")
    lines += ["", f"Last updated: {UPDATED_ISO}", ""]
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    build()
    print("pages written to", OUT)
    print(sorted(f for f in os.listdir(OUT) if f.endswith(".html")))
