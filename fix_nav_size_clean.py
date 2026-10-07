with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# 1. nav-menu gap and margins
css = re.sub(r'\.nav-menu\s*\{\s*display:\s*flex;\s*align-items:\s*center;\s*gap:\s*0\.8rem;\s*margin-left:\s*auto;\s*margin-right:\s*1rem;\s*\}', 
             '.nav-menu {\n  display: flex;\n  align-items: center;\n  gap: 1.5rem;\n  margin-left: auto;\n  margin-right: 2rem;\n}', css)

# 2. nav-link font size
css = re.sub(r'(\.nav-link\s*\{[^}]*)font-size:\s*0\.85rem;', r'\1font-size: 0.95rem;', css)

# 3. dropdown-toggle font size
css = re.sub(r'(\.dropdown-toggle\s*\{[^}]*)font-size:\s*0\.85rem;', r'\1font-size: 0.95rem;', css)

# 4. lang-btn font size
css = re.sub(r'(\.lang-btn\s*\{[^}]*)font-size:\s*0\.85rem;', r'\1font-size: 0.95rem;', css)

# 5. header-container max-width
css = re.sub(r'(\.header-container\s*\{[^}]*)max-width:\s*1350px;', r'\1max-width: 1440px;', css)

# 6. Change mobile breakpoint to 1300px
css = css.replace('@media (max-width: 1200px)', '@media (max-width: 1300px)')

# Write back
with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css cleanly.")
