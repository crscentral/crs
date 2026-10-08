import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Reduce fonts to 1.0rem
css = re.sub(r'\.nav-link\s*\{[^}]*font-size:\s*1\.05rem;', lambda m: m.group(0).replace('1.05rem', '1.0rem'), css)
css = re.sub(r'\.dropdown-toggle\s*\{[^}]*font-size:\s*1\.05rem;', lambda m: m.group(0).replace('1.05rem', '1.0rem'), css)
css = re.sub(r'\.lang-btn\s*\{[^}]*font-size:\s*1\.05rem;', lambda m: m.group(0).replace('1.05rem', '1.0rem'), css)

# 2. Change hamburger breakpoint from 1300px to 1000px
# The first instance of @media (max-width: 1300px) is the hamburger logic.
# The second one is for form grids (which we should leave alone, or also change? 1300px is fine for form grids, let's just change the first one)
css = css.replace('@media (max-width: 1300px) {\n  :root {', '@media (max-width: 1000px) {\n  :root {')

# 3. Remove margin-left: 2rem; from .nav-menu inside the hamburger block
bad_margin = "gap: 0.8rem;\n  margin-left: 2rem;\n    transition: left 0.3s ease;"
good_margin = "gap: 0.8rem;\n    transition: left 0.3s ease;"
css = css.replace(bad_margin, good_margin)

# Also there might be intermediate viewports compressing spacing
css = css.replace('@media (min-width: 1025px) and (max-width: 1200px) {', '@media (min-width: 1001px) and (max-width: 1200px) {')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied fixes for crscentral mobile/ipad views.")
