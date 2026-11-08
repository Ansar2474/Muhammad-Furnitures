# Muhammad Furnitures website

Multi-page website for **Muhammad Furnitures** (made-to-order furniture). Plain HTML, CSS and JavaScript. No build step is needed to run it: open `index.html` in a browser, or upload the files to any web host.

## Pages
`index.html` (home), `shop.html`, `collections.html`, `custom-furniture.html`, `about.html`, `contact.html`, `cart.html`, `furniture-buying-guide.html`, and one page for each product (for example `sofa-set-5-seater.html`).

## Things to update (search the files for `UPDATE` and `PUT YOUR`)
- Your **city** and **website address**: set `CITY` and `SITE_URL` at the top of `tools/build_site.py`, then run `python3 tools/build_site.py`. This fills in titles, canonical links, share images, `sitemap.xml`, `robots.txt` and `llms.txt`.
- Real **prices, sizes and product names**: edit the `PRODUCTS` list in `tools/build_site.py` and rebuild.
- **Street address and opening hours** (About and Contact pages, and the business data in `local_ld()`).
- **Social media links** in the footer (Instagram, LinkedIn, X, YouTube, TikTok) when those accounts exist.
- **Photos**: the images in `images/` are 3D renders, not photographs. Replace them with real photos of your work using the same file names.
- The "last updated" date (`UPDATED_ISO` and `UPDATED_TEXT` in `tools/build_site.py`) whenever you change prices or text.

## Notes
- Contact: 0311 7420474 (call and WhatsApp), mr.genius2474@gmail.com.
- `sitemap.xml`, `robots.txt` and `llms.txt` contain `YOUR-DOMAIN` until `SITE_URL` is set. Rebuild before uploading them.
- `style.css` holds the colours at the top (`:root`), `script.js` holds the cart, call popup and forms.
