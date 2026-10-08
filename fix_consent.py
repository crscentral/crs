import re

consent_html = """
<div class="form-group" style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
  <input type="checkbox" name="Privacy_Consent" id="privacyConsent" required style="width: auto;">
  <label for="privacyConsent" style="margin: 0; font-size: 0.9rem;">I agree to the <a href="privacy.html" style="color: var(--c1); text-decoration: underline;" target="_blank">Privacy Policy</a></label>
</div>
"""

for filename in ['index.html', 'staycrs.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'name="Privacy_Consent"' not in html:
        # Match <button ... type="submit" ...> OR <button type="submit" ...>
        html = re.sub(r'(<button[^>]*type="submit"[^>]*>)', rf'{consent_html}\n\1', html)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

