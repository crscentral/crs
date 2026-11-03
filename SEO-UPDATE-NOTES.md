# How to Update the "Last Updated" Date on CRS Central Pages

Whenever you edit the visible text on a page, update its modification date in **two places** inside that HTML file so the visible footer date and the search-engine schema stay identical:

### Step 1: Update the JSON-LD Schema in `<head>`
1. Open the HTML file you edited (for example, `index.html`, `services.html`, or `audit.html`).
2. Near the top inside `<head>`, find `<script type="application/ld+json">` and search for `"dateModified"`.
3. Change the date to the new go-live date in `YYYY-MM-DD` format:
   ```json
   "dateModified":"2026-11-04"
   ```

### Step 2: Update the Visible Footer `<time>` Tag
1. Scroll to the bottom of the same HTML file inside `<div class="footer-bottom">`.
2. Find the `<div class="footer-last-updated">` line right below the copyright line:
   ```html
   <div class="footer-last-updated"><span data-i18n="footer-last-updated">Last updated:</span> <time datetime="2026-11-04">November 4, 2026</time></div>
   ```
3. Update both `datetime="YYYY-MM-DD"` and the visible text (`Month D, YYYY`) to match Step 1.

---

# 3-Tier Form Fail-Safe Configuration (FormSubmit → Web3Forms → Email/WhatsApp)

All 5 forms on the site (`index.html`, `audit.html`, `contact.html`, `staycrs.html`, and `staycrs/index.html`) use a 3-tier fail-safe chain:
1. **Tier 1 (Primary):** Submits via AJAX to `https://formsubmit.co/ajax/info@crscentral.com` (6-second timeout).
2. **Tier 2 (Option B — Web3Forms Backup):** If FormSubmit times out or is down, automatically submits to `https://api.web3forms.com/submit`.
   - To activate Tier 2: visit `https://web3forms.com`, enter `info@crscentral.com`, copy the free Access Key emailed to you, and paste it into `const WEB3FORMS_ACCESS_KEY = 'YOUR_KEY_HERE';` in `assets/js/script-v2.js` (line 464), `assets/js/script-v2.min.js`, and `var W3KEY="YOUR_KEY_HERE"` in `assets/js/staycrs.min.js`.
3. **Tier 3 (Option A — Final Safety Net):** If both Tier 1 and Tier 2 fail, automatically opens the visitor's email app pre-filled with their submitted details to `info@crscentral.com` and redirects to `thanks.html?fallback=1` with one-click WhatsApp (`+91 91217 73501`) and Email confirmation buttons.
