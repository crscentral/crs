with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Remove the previously added block
css = re.sub(r'/\* Vietnamese language specific overrides.*?\n\}\n', '', css, flags=re.DOTALL)

# Add it back but wrapped in a desktop media query
vi_override = '''
/* Vietnamese language specific overrides to prevent horizontal overflow */
@media (min-width: 1301px) {
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
}
'''

css = css.replace('justify-content: space-between;\n}', 'justify-content: space-between;\n}' + vi_override)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied media-query bounded Vietnamese css.")
