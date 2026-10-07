with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Remove margin-left: auto and margin-right: 2rem from .nav-menu block
def replace_nav(match):
    block = match.group(0)
    block = re.sub(r'\s*margin-left:\s*auto;', '', block)
    block = re.sub(r'\s*margin-right:\s*2rem;', '', block)
    block = re.sub(r'gap:\s*1\.5rem;', 'gap: 2rem;', block)
    return block

# The first nav-menu is the desktop one.
css = re.sub(r'\.nav-menu\s*\{[^}]*\}', replace_nav, css, count=1)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored gap and removed margins.")
