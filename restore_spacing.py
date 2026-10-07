with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# 1. Fix the main .nav-menu
css = re.sub(
    r'\.nav-menu\s*\{\s*display:\s*flex;\s*align-items:\s*center;\s*gap:\s*1\.5rem;\s*margin-left:\s*auto;\s*margin-right:\s*2rem;\s*\}',
    r'.nav-menu {\n  display: flex;\n  align-items: center;\n  gap: 2rem;\n}',
    css
)

# Wait, maybe it's not EXACTLY that string. Let's do a more robust replace.
