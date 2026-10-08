import json
import re

# Fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_text = "CRS Central delivers expert hotel revenue management across Thailand, Laos, India, Nepal, Malaysia and Vietnam — dynamic pricing, OTA optimization &amp; reservations outsourcing for Independent hotels."
new_text = "Hotel revenue management for independent hotels across Thailand, Laos, India, Nepal, Malaysia and Vietnam. Dynamic pricing, OTA management and a free revenue audit."

html = html.replace(old_text, new_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Fix en.json
with open('assets/locales/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

en["home-hero-desc"] = new_text

with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, indent=2, ensure_ascii=False)

print("Fixed hero and meta description")
