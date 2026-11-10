const SITE_ROOT = document.body.dataset.root || "";   // "" on the home page, "../" one folder down, "../../" on product pages
/* ==========================================================================
   SCRIPT.JS - basic behavior for the Muhammad Furnitures site
   Each feature is its own small function (module) so you can edit or remove it easily.
   Sections:
     1. SETTINGS (currency, WhatsApp number, messages)
     2. Mobile menu
     3. Cart (counter + cart page, saved in the browser)
     3b. Call popup, social links, scroll animation
     4. Search
     5. Room filter (tiles + filter buttons)
     6. Quote form
     7. Newsletter
     8. Footer year
     9. Start everything
   ========================================================================== */

/* ==========================================================================
   1. SETTINGS - UPDATE CURRENCY, WHATSAPP NUMBER AND MESSAGES HERE
   ========================================================================== */
const SETTINGS = {
  currency: "Rs ",                                // UPDATE CURRENCY HERE (Pakistani rupees)
  addedMessage: " added to cart",                 // UPDATE "ADDED TO CART" MESSAGE HERE
  newsletterSuccess: "Thanks for subscribing!",   // UPDATE NEWSLETTER SUCCESS MESSAGE HERE
  cartStorageKey: "mfCart",                           // name used to save the cart in the browser

  // YOUR WHATSAPP NUMBER (0311 7420474). The quote form opens WhatsApp with this number.
  // Digits only, with country code and no "+" or spaces. CHANGE IT HERE (and in index.html) if your number changes.
  // If you empty it, the form asks visitors to use the contact details instead.
  whatsappNumber: "923117420474",
  quoteOpeningMessage: "Opening WhatsApp so you can send your request.",
  businessName: "Muhammad Furnitures",
  phoneDisplay: "0311 7420474",                   // shown in the call popup
  quoteNotConnected: "Our online quote form is not switched on yet. Please contact us using the details on this page."
};

/* Small helper: formats a price in rupees, for example 75000 becomes "Rs 75,000" */
function formatPrice(amount) {
  return SETTINGS.currency + Math.round(amount).toLocaleString("en-US");
}

/* Small helper: shows a popup message at the bottom of the screen (optionally with a link) */
function showToast(message, linkHref, linkText) {
  const toast = document.getElementById("toast");
  if (!toast) return;
  toast.textContent = message;
  if (linkHref) {
    const link = document.createElement("a");
    link.href = linkHref;
    link.textContent = linkText || "View";
    toast.appendChild(document.createTextNode(" "));
    toast.appendChild(link);
  }
  toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove("show"), linkHref ? 4200 : 2200);
}


/* ==========================================================================
   2. MOBILE MENU (hamburger button)
   ========================================================================== */
function initMobileMenu() {
  const toggle = document.getElementById("menuToggle");
  const nav = document.getElementById("mainNav");
  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("open");
    toggle.classList.toggle("active", isOpen);
    toggle.setAttribute("aria-expanded", isOpen);
  });

  // Close the menu after tapping a link
  nav.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.classList.remove("active");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}


/* ==========================================================================
   3. CART
   This is a simple demo cart: it stores items in the browser (localStorage) and updates the counter.
   CONNECT YOUR REAL CHECKOUT / CART PAGE / PAYMENT SYSTEM HERE LATER
   (Shopify, WooCommerce, Stripe, your own backend, etc.)
   ========================================================================== */
let cart = [];

function loadCart() {
  try {
    cart = JSON.parse(localStorage.getItem(SETTINGS.cartStorageKey)) || [];
  } catch (e) {
    cart = [];
  }
}

function saveCart() {
  try {
    localStorage.setItem(SETTINGS.cartStorageKey, JSON.stringify(cart));
  } catch (e) { /* storage unavailable - the cart just won't persist */ }
}

function updateCartCount() {
  const badge = document.getElementById("cartCount");
  if (!badge) return;
  const totalItems = cart.reduce((sum, item) => sum + item.qty, 0);
  badge.textContent = totalItems;
}

function addToCart(product) {
  const existing = cart.find(item => item.id === product.id);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ ...product, qty: 1 });
  }
  saveCart();
  updateCartCount();
  showToast(product.name + SETTINGS.addedMessage, SITE_ROOT + "cart/", "View cart");
}

function initCart() {
  loadCart();
  updateCartCount();

  // Every "Add to Cart" button reads data-id, data-name and data-price from its product card in index.html
  document.querySelectorAll(".add-to-cart").forEach(button => {
    button.addEventListener("click", () => {
      const card = button.closest(".product-card");
      addToCart({
        id: card.dataset.id,
        name: card.dataset.name,
        price: parseFloat(card.dataset.price),
        image: card.dataset.image || ""
      });
    });
  });

  // The cart icon in the header is a normal link to cart.html (nothing to do here).

  // On the cart page, draw the items
  renderCartPage();
}


/* ---- Cart page (cart.html): shows the items, quantity buttons, total and the WhatsApp order button ---- */
function renderCartPage() {
  const list = document.getElementById("cartList");
  if (!list) return;                       // not the cart page
  const layout = document.getElementById("cartLayout");
  const empty = document.getElementById("cartEmpty");

  function draw() {
    list.innerHTML = "";
    const hasItems = cart.length > 0;
    layout.hidden = !hasItems;
    empty.hidden = hasItems;
    if (!hasItems) { updateCartCount(); return; }

    cart.forEach(item => {
      const li = document.createElement("li");
      li.className = "cart-item";
      // Product photo: saved with the item when it was added (older carts fall back to images/product<ID>.jpg)
      li.innerHTML =
        '<img alt="" width="96" height="96">' +
        '<div class="cart-item-info"><strong></strong><span class="cart-item-price"></span></div>' +
        '<div class="qty" role="group" aria-label="Quantity">' +
          '<button type="button" data-act="minus" aria-label="Decrease quantity">&minus;</button>' +
          '<span class="qty-num"></span>' +
          '<button type="button" data-act="plus" aria-label="Increase quantity">+</button>' +
        '</div>' +
        '<strong class="cart-line-total"></strong>' +
        '<button type="button" class="cart-remove" data-act="remove" aria-label="Remove item">&times;</button>';
      li.querySelector("img").src = SITE_ROOT + (item.image || ("images/product" + encodeURIComponent(item.id) + ".jpg"));
      li.querySelector(".cart-item-info strong").textContent = item.name;
      li.querySelector(".cart-item-price").textContent = formatPrice(item.price) + " each";
      li.querySelector(".qty-num").textContent = item.qty;
      li.querySelector(".cart-line-total").textContent = formatPrice(item.price * item.qty);
      li.addEventListener("click", (event) => {
        const act = event.target.closest("[data-act]");
        if (!act) return;
        if (act.dataset.act === "plus") item.qty += 1;
        if (act.dataset.act === "minus") item.qty = Math.max(1, item.qty - 1);
        if (act.dataset.act === "remove") cart = cart.filter(c => c !== item);
        saveCart(); updateCartCount(); draw();
      });
      list.appendChild(li);
    });

    const count = cart.reduce((sum, item) => sum + item.qty, 0);
    const total = cart.reduce((sum, item) => sum + item.price * item.qty, 0);
    document.getElementById("cartItems").textContent = count;
    document.getElementById("cartTotal").textContent = formatPrice(total);

    // The order message that opens in WhatsApp
    const lines = ["Hello " + SETTINGS.businessName + ", I would like to order:"];
    cart.forEach(item => lines.push("- " + item.name + " x " + item.qty + " (" + formatPrice(item.price * item.qty) + ")"));
    lines.push("Estimated total: " + formatPrice(total));
    lines.push("Please confirm the price, delivery and timeline.");
    document.getElementById("cartCheckout").href =
      "https://wa.me/" + SETTINGS.whatsappNumber + "?text=" + encodeURIComponent(lines.join("\n"));
    updateCartCount();
  }

  const clear = document.getElementById("cartClear");
  if (clear) clear.addEventListener("click", () => { cart = []; saveCart(); draw(); });
  draw();
}


/* ==========================================================================
   3b. CALL POPUP, SOCIAL LINKS, SCROLL ANIMATION
   ========================================================================== */

/* Phone numbers: on a phone a tap starts the call. Computers have no calling app, so a popup shows the number
   with a Copy button instead. The popup also appears on phones as a backup. */
function initCallLinks() {
  const dialog = document.getElementById("callDialog");
  if (!dialog) return;
  const copyBtn = document.getElementById("callCopy");
  const closeBtn = document.getElementById("callClose");
  const isTouch = window.matchMedia("(pointer: coarse)").matches;

  function open() {
    dialog.hidden = false;
    document.body.classList.add("no-scroll");
    const first = dialog.querySelector(".btn");
    if (first) first.focus();
  }
  function close() {
    dialog.hidden = true;
    document.body.classList.remove("no-scroll");
  }

  document.querySelectorAll('a[href^="tel:"]').forEach(link => {
    if (link.hasAttribute("data-no-dialog")) return;
    link.addEventListener("click", (event) => {
      event.preventDefault();
      open();
      if (isTouch) window.location.href = link.getAttribute("href");   // phones: start the call right away
    });
  });

  closeBtn.addEventListener("click", close);
  dialog.addEventListener("click", (event) => { if (event.target === dialog) close(); });
  document.addEventListener("keydown", (event) => { if (event.key === "Escape" && !dialog.hidden) close(); });

  copyBtn.addEventListener("click", () => {
    const number = SETTINGS.phoneDisplay;
    function done() { copyBtn.textContent = "Copied!"; setTimeout(() => { copyBtn.textContent = "Copy number"; }, 1800); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(number).then(done).catch(fallback);
    } else { fallback(); }
    function fallback() {
      const box = document.createElement("textarea");
      box.value = number; document.body.appendChild(box); box.select();
      try { document.execCommand("copy"); done(); } catch (e) { copyBtn.textContent = number; }
      box.remove();
    }
  });
}

/* Social icons that are not linked yet: tell the visitor instead of jumping to the top of the page.
   When you add the real link, delete the data-social-pending attribute from that icon. */
function initSocialLinks() {
  document.querySelectorAll("[data-social-pending]").forEach(link => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      showToast(link.dataset.socialPending + " page coming soon");
    });
  });
}

/* Gentle fade-in when sections scroll into view. Remove this function call at the bottom to switch it off. */
function initReveal() {
  const targets = document.querySelectorAll(
    ".section-head, .cat-card, .product-card, .why-card, .how-steps li, .collection-row, .faq-item, .promo-text, .craft-top > div, .about-text, .check-list li, .steps li, .tips li, .contact-grid > *, .seo-inner, .shop-custom");
  if (!("IntersectionObserver" in window) || window.matchMedia("(prefers-reduced-motion: reduce)").matches || !targets.length) return;
  document.documentElement.classList.add("js-reveal");
  const seen = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add("is-visible"); seen.unobserve(entry.target); }
    });
  }, { threshold: 0.08, rootMargin: "0px 0px -4% 0px" });
  targets.forEach((el, i) => { el.classList.add("reveal"); el.style.transitionDelay = (i % 4) * 70 + "ms"; seen.observe(el); });
  // Safety: never leave anything hidden
  setTimeout(() => targets.forEach(el => el.classList.add("is-visible")), 4000);
}


/* ==========================================================================
   4. SEARCH
   Demo behavior: filters the visible product cards by title.
   CONNECT TO YOUR REAL SEARCH (search results page or backend) HERE LATER.
   ========================================================================== */
function initSearch() {
  const form = document.getElementById("searchForm");
  const input = document.getElementById("searchInput");
  if (!form || !input) return;

  const main = document.querySelector("main");
  const onShop = main && main.dataset.page === "shop";

  function filterProducts() {
    const query = input.value.trim().toLowerCase();
    // Searching looks across every room, so reset the room filter first
    if (query) applyRoomFilter("all");
    let visible = 0;
    document.querySelectorAll(".product-card").forEach(card => {
      const text = (card.dataset.name + " " + card.textContent).toLowerCase();
      const match = text.includes(query);
      card.style.display = match ? "" : "none";
      if (match) visible++;
    });
    return visible;
  }

  // Live filtering only makes sense on the Shop page, where the products are
  if (onShop) input.addEventListener("input", filterProducts);

  // The magnifier in the header opens and closes the search bar
  const toggle = document.getElementById("searchToggle");
  const panel = document.getElementById("searchPanel");
  function setSearchOpen(open) {
    if (!toggle || !panel) return;
    panel.hidden = !open;
    toggle.setAttribute("aria-expanded", open);
    if (open) input.focus();
  }
  if (toggle && panel) {
    toggle.addEventListener("click", () => setSearchOpen(panel.hidden));
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !panel.hidden) { setSearchOpen(false); toggle.focus(); }
    });
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!onShop) {
      // On other pages: remember the words and open the Shop page, which applies them
      try { sessionStorage.setItem("searchQuery", input.value.trim()); } catch (e) { /* ignore */ }
      window.location.href = SITE_ROOT + "shop/";
      return;
    }
    const visible = filterProducts();
    setSearchOpen(false);
    const grid = document.querySelector(".product-grid");
    if (grid) grid.scrollIntoView({ behavior: "smooth" });
    if (visible === 0) showToast("No products found");
  });

  // Arriving on the Shop page from a search made on another page
  if (onShop) {
    let saved = "";
    try { saved = sessionStorage.getItem("searchQuery") || ""; sessionStorage.removeItem("searchQuery"); } catch (e) { /* ignore */ }
    if (saved) {
      input.value = saved;
      const visible = filterProducts();
      if (visible === 0) showToast("No products found");
    }
  }
}


/* ==========================================================================
   5. ROOM FILTER
   Works with the "Shop by room" tiles and the filter buttons. Both use data-filter.
   The value must match a product's data-category (living, bedroom, dining, office) or be "all".
   ========================================================================== */
function applyRoomFilter(value) {
  let visible = 0;
  document.querySelectorAll(".product-card").forEach(card => {
    const match = value === "all" || card.dataset.category === value;
    card.hidden = !match;
    if (match) visible++;
  });

  document.querySelectorAll(".filter-chip").forEach(chip => {
    const active = chip.dataset.filter === value;
    chip.classList.toggle("is-active", active);
    chip.setAttribute("aria-pressed", active);
  });

  const empty = document.getElementById("noResults");
  if (empty) empty.hidden = visible !== 0;
}

function initRoomFilter() {
  document.querySelectorAll("[data-filter]").forEach(element => {
    element.addEventListener("click", () => {
      // Clear any search text so the two don't fight each other
      const input = document.getElementById("searchInput");
      if (input && input.value) {
        input.value = "";
        document.querySelectorAll(".product-card").forEach(card => { card.style.display = ""; });
      }
      applyRoomFilter(element.dataset.filter);
    });
  });

  // Links like shop.html#living open the Shop page already filtered
  const valid = Array.from(document.querySelectorAll(".filter-chip")).map(chip => chip.dataset.filter);
  function applyFromHash() {
    const value = window.location.hash.replace("#", "");
    if (valid.includes(value)) applyRoomFilter(value);
  }
  if (valid.length) {
    applyFromHash();
    window.addEventListener("hashchange", applyFromHash);
  }
}


/* ==========================================================================
   6. QUOTE FORM
   Opens WhatsApp with the customer's details filled in. Set SETTINGS.whatsappNumber to switch it on.
   OR CONNECT TO YOUR EMAIL SERVICE / FORM BACKEND HERE INSTEAD.
   ========================================================================== */
function initQuoteForm() {
  const form = document.getElementById("quoteForm");
  const message = document.getElementById("quoteMessage");
  if (!form || !message) return;

  form.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!SETTINGS.whatsappNumber) {
      message.textContent = SETTINGS.quoteNotConnected;
      return;
    }

    const data = new FormData(form);
    const text = [
      "Quote request for Muhammad Furnitures",
      "Name: " + data.get("name"),
      "Phone: " + data.get("phone"),
      "Looking for: " + data.get("item"),
      "Size and details: " + (data.get("details") || "-")
    ].join("\n");

    window.open("https://wa.me/" + SETTINGS.whatsappNumber + "?text=" + encodeURIComponent(text), "_blank", "noopener");
    message.textContent = SETTINGS.quoteOpeningMessage;
    form.reset();
  });
}


/* ==========================================================================
   7. NEWSLETTER
   Demo behavior: shows a success message only.
   CONNECT TO YOUR EMAIL SERVICE HERE (Mailchimp, Klaviyo, ConvertKit, etc.)
   ========================================================================== */
function initNewsletter() {
  const form = document.getElementById("newsletterForm");
  const message = document.getElementById("newsletterMessage");
  if (!form || !message) return;

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    // const email = document.getElementById("newsletterEmail").value;  // <-- send this to your email service
    message.textContent = SETTINGS.newsletterSuccess;
    form.reset();
  });
}


/* ==========================================================================
   8. FOOTER YEAR (keeps the copyright year current automatically)
   ========================================================================== */
function initYear() {
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
}


/* ==========================================================================
   9. START EVERYTHING when the page has loaded
   Comment out any line below to disable that feature.
   ========================================================================== */
document.addEventListener("DOMContentLoaded", () => {
  initMobileMenu();
  initCart();
  initCallLinks();
  initSocialLinks();
  initReveal();
  initSearch();
  initRoomFilter();
  initQuoteForm();
  initNewsletter();
  initYear();
});
