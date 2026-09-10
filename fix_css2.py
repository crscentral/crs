import re

# Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'grid-template-columns:\s*1\.2fr\s+1fr\s+1\.2fr\s+0\.8fr\s+1fr;', 'grid-template-columns: 1.2fr 1fr 0.8fr 1.2fr 1fr;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update style.min.css
with open('assets/css/style.min.css', 'r', encoding='utf-8') as f:
    min_css = f.read()

min_css = re.sub(r'grid-template-columns:\s*1\.2fr\s+1fr\s+1\.2fr\s+\.?8fr\s+1fr', 'grid-template-columns:1.2fr 1fr .8fr 1.2fr 1fr', min_css)

with open('assets/css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(min_css)

print("Updated grid columns")
