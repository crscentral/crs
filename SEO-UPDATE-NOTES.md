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
