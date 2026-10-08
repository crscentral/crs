import re

country_dropdown = """<div data-i18n='&lt;label for="c"&gt;Country&lt;/label&gt;&lt;select id="c" required&gt;&lt;option value="" disabled selected&gt;Select Country&lt;/option&gt;&lt;option value="Thailand"&gt;Thailand&lt;/option&gt;&lt;option value="Laos"&gt;Laos&lt;/option&gt;&lt;option value="India"&gt;India&lt;/option&gt;&lt;option value="Nepal"&gt;Nepal&lt;/option&gt;&lt;option value="Malaysia"&gt;Malaysia&lt;/option&gt;&lt;option value="Vietnam"&gt;Vietnam&lt;/option&gt;&lt;option value="Other"&gt;Other&lt;/option&gt;&lt;/select&gt;'>
<label for="c" data-i18n="Country">Country</label>
<select id="c" name="Country" required style="width: 100%; padding: 0.8rem; border: 1px solid var(--border); border-radius: 4px; font-family: inherit; font-size: 1rem;">
  <option value="" disabled selected data-i18n="Select Country">Select Country</option>
  <option value="Thailand" data-i18n="Thailand">Thailand</option>
  <option value="Laos" data-i18n="Laos">Laos</option>
  <option value="India" data-i18n="India">India</option>
  <option value="Nepal" data-i18n="Nepal">Nepal</option>
  <option value="Malaysia" data-i18n="Malaysia">Malaysia</option>
  <option value="Vietnam" data-i18n="Vietnam">Vietnam</option>
  <option value="Other" data-i18n="Other">Other</option>
</select>
</div>
"""

with open('staycrs.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'name="Country"' not in html:
    html = re.sub(r'(<div[^>]*><label[^>]*>Hotel name</label><input[^>]*></div>)', rf'{country_dropdown}\n\1', html)
    with open('staycrs.html', 'w', encoding='utf-8') as f:
        f.write(html)
