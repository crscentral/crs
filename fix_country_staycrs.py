import re

country_dropdown = """
<div class="form-group">
  <label>Country</label>
  <select name="Country" class="form-input" required>
    <option value="" disabled selected>Select Country</option>
    <option value="Thailand">Thailand</option>
    <option value="Laos">Laos</option>
    <option value="India">India</option>
    <option value="Nepal">Nepal</option>
    <option value="Malaysia">Malaysia</option>
    <option value="Vietnam">Vietnam</option>
    <option value="Other">Other</option>
  </select>
</div>
"""

with open('staycrs.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'name="Country"' not in html:
    # Look for the Hotel Name label in staycrs.html
    # It might be <label data-i18n="Hotel Name">Hotel Name</label>
    html = re.sub(r'(<div class="form-group">\s*<label[^>]*>Hotel Name)', rf'{country_dropdown}\n\1', html)
    if 'name="Country"' not in html:
        # Let's try matching just the Hotel Name input
        html = re.sub(r'(<div class="form-group">\s*<label[^>]*>Hotel Name.*?</label>\s*<input)', rf'{country_dropdown}\n\1', html, flags=re.DOTALL)
        
    with open('staycrs.html', 'w', encoding='utf-8') as f:
        f.write(html)
