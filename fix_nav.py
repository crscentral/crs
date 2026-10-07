import re
import os

css_files = ['assets/css/style.css', 'assets/css/style.min.css']
for css_file in css_files:
    if not os.path.exists(css_file): continue
    with open(css_file, 'r', encoding='utf-8') as f:
        css = f.read()
    
    # In style.css
    css = re.sub(r'(\.nav-menu\s*\{[^}]*?gap:\s*)1\.5rem', r'\g<1>0.8rem', css)
    css = re.sub(r'(\.nav-link\s*\{[^}]*?font-size:\s*)0\.95rem', r'\g<1>0.85rem', css)
    css = re.sub(r'(\.dropdown-toggle\s*\{[^}]*?font-size:\s*)0\.95rem', r'\g<1>0.85rem', css)
    
    # For minified
    css = css.replace('gap:1.5rem', 'gap:0.8rem')
    css = css.replace('font-size:0.95rem', 'font-size:0.85rem')
    
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css)

print("Nav fixed.")
