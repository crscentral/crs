import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Revert header container to 1200px
css = re.sub(r'\.header-container\s*\{\s*max-width:\s*1440px;', '.header-container {\n  max-width: 1200px;', css)

# 2. Fix Vietnamese specific override that was also 1440px
css = re.sub(r'html\[lang="vi"\] \.header-container\s*\{\s*max-width:\s*1440px;\s*\}', 'html[lang="vi"] .header-container {\n    max-width: 1200px;\n  }', css)

# 3. Reduce font-size to 1.05rem for nav items
css = re.sub(r'\.nav-link\s*\{[^}]*font-size:\s*1\.25rem;', lambda m: m.group(0).replace('1.25rem', '1.05rem'), css)
css = re.sub(r'\.dropdown-toggle\s*\{[^}]*font-size:\s*1\.25rem;', lambda m: m.group(0).replace('1.25rem', '1.05rem'), css)
css = re.sub(r'\.lang-btn\s*\{[^}]*font-size:\s*1\.25rem;', lambda m: m.group(0).replace('1.25rem', '1.05rem'), css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied 1200px max-width and 1.05rem fonts.")
