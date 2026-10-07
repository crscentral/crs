with open('original_style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Add white-space: nowrap to elements to prevent wrapping in long languages
css = re.sub(r'(\.nav-link\s*\{[^}]*)padding:\s*0\.5rem\s*0;', r'\1padding: 0.5rem 0;\n  white-space: nowrap;', css)
css = re.sub(r'(\.dropdown-toggle\s*\{[^}]*)padding:\s*0\.5rem\s*0;', r'\1padding: 0.5rem 0;\n  white-space: nowrap;', css)
css = re.sub(r'(\.lang-btn\s*\{[^}]*)padding:\s*0\.5rem\s*1rem;', r'\1padding: 0.5rem 1rem;\n  white-space: nowrap;', css)

vi_override = '''
/* Vietnamese language specific overrides to prevent horizontal overflow */
@media (min-width: 1025px) {
  html[lang="vi"] .header-container {
    max-width: 1440px;
  }
  html[lang="vi"] .nav-menu {
    gap: 0.8rem !important;
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

print("Restored CSS to original and applied Vietnamese fixes.")
