import json
import os
import re
from bs4 import BeautifulSoup

FILES = ['index.html', 'services.html', 'thailand.html', 'about.html', 'audit.html', 'blog.html', 'contact.html', 'staycrs.html', 'laos.html', 'india.html', 'nepal.html', 'malaysia.html', 'vietnam.html']

with open('all_missing.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

# Convert to set for faster lookup
missing_set = set(missing)

def is_valid_text(text):
    text = text.strip()
    if not text: return False
    if re.match(r'^[\d\s\.,%+\-$€£]+$', text): return False
    if text in ['☰', '▼', '→', '←', '©']: return False
    if 'data-i18n' in text: return False
    return True

modified_files = 0
for filepath in FILES:
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    count = 0
    
    for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'span', 'li', 'button', 'td', 'th', 'div', 'strong', 'b', 'label', 'option']:
        for el in soup.find_all(tag_name):
            if el.has_attr('data-i18n'):
                continue
            
            parent_has_i18n = False
            p = el.parent
            while p:
                if p.name == '[document]': break
                if p.has_attr('data-i18n'):
                    parent_has_i18n = True
                    break
                p = p.parent
            
            if parent_has_i18n:
                continue
                
            has_block_children = any(c.name in ['p', 'div', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table'] for c in el.children if c.name)
            if has_block_children and el.name in ['div', 'li', 'td']:
                continue
            
            inner_html = el.decode_contents().strip()
            inner_html_clean = re.sub(r'\s+', ' ', inner_html)
            
            if inner_html_clean in missing_set:
                el['data-i18n'] = inner_html_clean
                changed = True
                count += 1
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        modified_files += 1
        print(f"Updated {filepath} ({count} elements)")

print(f"Done applying data-i18n. Modified {modified_files} files.")
