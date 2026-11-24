# Muhammad Furnitures website

Multi-page website for **Muhammad Furnitures** (made-to-order furniture). Plain HTML, CSS and JavaScript. No build step is needed to run it: open `index.html` in a browser, or upload the files to any web host.

## Pages
`index.html` (home), `shop.html`, `collections.html`, `custom-furniture.html`, `about.html`, `contact.html`, `cart.html`, `furniture-buying-guide.html`, and one page for each product (for example `sofa-set-5-seater.html`).

## Things to update
- City, address, hours, email and social links: the admin page (Site settings), saved in `content/site.json`.
- Products, prices and sizes: the admin page, saved in `content/products/`.
- Page text for articles and category pages: `tools/insights_content.py` and `tools/more_content.py`.
- After any change to `content/` or `tools/`, the "Rebuild website" action regenerates every page. To rebuild by hand, run `python3 tools/build_site.py`.
- `google072384fc5a431183.html` is the Google Search Console ownership file. Do not delete it.
- The "last updated" date is `UPDATED_ISO` and `UPDATED_TEXT` in `tools/build_site.py`.

## Notes
- Contact: 0311 7420474 (call and WhatsApp). Email, address, hours, social links, homepage text and FAQs are edited on the admin page (Site settings) and saved in `content/site.json`.
- The website address used in `sitemap.xml`, `robots.txt` and `llms.txt` is the "Website address" field in Site settings.
- `style.css` holds the colours at the top (`:root`), `script.js` holds the cart, call popup and forms.
