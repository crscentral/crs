import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the 3-line format with a forced 2-line format
content = content.replace(
    '<h1 class="hero-title" data-i18n="home-hero-title">Hotel Revenue <br> Management Consultancy <span>— Across South and Southeast Asia.</span></h1>',
    '<h1 class="hero-title" data-i18n="home-hero-title">Hotel Revenue Management <br> Consultancy <span>— Across South and Southeast Asia.</span></h1>'
)

# And if there are any other places where <br> is between Revenue and Management
content = content.replace('Hotel Revenue <br> Management Consultancy', 'Hotel Revenue Management <br> Consultancy')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update en.json as well
with open('assets/locales/en.json', 'r', encoding='utf-8') as f:
    en_json = f.read()
    
en_json = en_json.replace('Hotel Revenue <br> Management Consultancy', 'Hotel Revenue Management <br> Consultancy')

with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    f.write(en_json)

print("Fixed lines.")
