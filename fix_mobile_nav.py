with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# In the mobile media query, restore nav-link and dropdown-toggle to 1.2rem
css = re.sub(r'(\.nav-link,\s*\.dropdown-toggle\s*\{\s*font-size:\s*)0\.95rem(;\s*\})', r'\1 1.2rem\2', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
