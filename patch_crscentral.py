import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update header-container max-width
css = re.sub(r'(\.header-container\s*\{[^}]*)max-width:\s*1200px;', r'\1max-width: 1440px;', css)

# 2. Update nav-menu to spread
def replace_nav_menu(match):
    block = match.group(0)
    # Remove existing gap
    block = re.sub(r'\s*gap:\s*[^;]+;', '', block)
    # Remove existing margins if any
    block = re.sub(r'\s*margin-(left|right):\s*[^;]+;', '', block)
    # Add flex properties
    block = block.replace('align-items: center;', 'align-items: center;\n  flex: 1;\n  justify-content: space-evenly;\n  margin: 0 2rem;')
    return block

css = re.sub(r'\.nav-menu\s*\{[^}]*\}', replace_nav_menu, css, count=1)

# 3. Update nav-link font-size
# Need to make sure we only update the main desktop nav-link, not the mobile ones.
def replace_nav_link(match):
    block = match.group(0)
    return re.sub(r'font-size:\s*0\.95rem;', 'font-size: 1.05rem;', block)

css = re.sub(r'\.nav-link\s*\{[^}]*\}', replace_nav_link, css, count=1)

# 4. Update lang-btn font-size
# The main lang-btn doesn't explicitly have font-size in the root, it inherits. But it has it in the vi override.
# Let's just explicitly set font-size on .lang-btn block
def replace_lang_btn(match):
    block = match.group(0)
    if 'font-size' in block:
        block = re.sub(r'font-size:\s*[^;]+;', 'font-size: 1.05rem;', block)
    else:
        block = block.replace('background: transparent;', 'font-size: 1.05rem;\n  background: transparent;')
    return block

css = re.sub(r'\.lang-btn\s*\{[^}]*\}', replace_lang_btn, css, count=1)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied CRS Central layout updates.")
