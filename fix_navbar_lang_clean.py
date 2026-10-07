with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Reset max-width to 1200px
css = re.sub(r'(\.header-container\s*\{[^}]*)max-width:\s*1440px;', r'\1max-width: 1200px;', css)

vi_override = '''
/* Vietnamese language specific overrides to prevent horizontal overflow */
@media (min-width: 1301px) {
  html[lang="vi"] .header-container {
    max-width: 1440px;
  }
  html[lang="vi"] .nav-menu {
    gap: 0.8rem !important;
    margin-right: 1rem !important;
  }
  html[lang="vi"] .nav-link,
  html[lang="vi"] .dropdown-toggle,
  html[lang="vi"] .lang-btn {
    font-size: 0.85rem !important;
  }
}
'''

css = css.replace('justify-content: space-between;\n}', 'justify-content: space-between;\n}' + vi_override)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied clean css.")
