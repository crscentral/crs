with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# 1. Reset .header-container max-width to 1200px
css = re.sub(r'(\.header-container\s*\{[^}]*)max-width:\s*1440px;', r'\1max-width: 1200px;', css)

# 2. Add language-specific override for Vietnamese
vi_override = '''
/* Vietnamese language specific overrides to prevent wrapping */
html[lang="vi"] .header-container {
  max-width: 1440px;
}
html[lang="vi"] .nav-menu {
  gap: 0.8rem;
  margin-right: 1rem;
}
html[lang="vi"] .nav-link,
html[lang="vi"] .dropdown-toggle,
html[lang="vi"] .lang-btn {
  font-size: 0.85rem;
}
'''

# insert it after .header-container { ... }
if vi_override not in css:
    css = css.replace('justify-content: space-between;\n}', 'justify-content: space-between;\n}' + vi_override)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied language-specific css.")
