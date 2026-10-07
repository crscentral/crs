with open('original_style.css', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    curr = f.read()

import re

# We will completely rip out the current .header-container down to .hero and replace it with original, 
# then re-apply our specific necessary fixes.

# 1. Rip out current header section
# Find index of .header-container {
start_idx = curr.find('.header-container {')
# Find index of /* Hero Section */
end_idx = curr.find('/* Hero Section */')

curr_top = curr[:start_idx]
curr_bottom = curr[end_idx:]

# 2. Extract original header section
orig_start = orig.find('.header-container {')
orig_end = orig.find('/* Hero Section */')
orig_header = orig[orig_start:orig_end]

# 3. Add white-space: nowrap to original .nav-link and .dropdown-toggle
orig_header = re.sub(r'(\.nav-link\s*\{[^}]*)padding:\s*0\.5rem\s*0;', r'\1padding: 0.5rem 0;\n  white-space: nowrap;', orig_header)
orig_header = re.sub(r'(\.dropdown-toggle\s*\{[^}]*)padding:\s*0\.5rem\s*0;', r'\1padding: 0.5rem 0;\n  white-space: nowrap;', orig_header)
orig_header = re.sub(r'(\.lang-btn\s*\{[^}]*)padding:\s*0\.5rem\s*1rem;', r'\1padding: 0.5rem 1rem;\n  white-space: nowrap;', orig_header)

# 4. Re-inject Vietnamese logic right after .header-container
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
orig_header = orig_header.replace('justify-content: space-between;\n}', 'justify-content: space-between;\n}' + vi_override)

# 5. Fix the mobile menu .nav-menu in media query to ensure no weird artifacts from subagent
# The subagent changed the mobile menu gap from 2rem to 0.8rem and added margin-left: 2rem. Let's fix that.
# Let's just find the media query block in curr_bottom and restore it if needed.
# Actually, the original media query block is better. Let's just restore the entire file from original_style.css, 
# then apply our few needed patches!

