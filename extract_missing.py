import os
import json
import re
from bs4 import BeautifulSoup

FILES = ['index.html', 'services.html', 'thailand.html', 'about.html', 'audit.html', 'blog.html', 'contact.html', 'staycrs.html']

def load_json(filepath):
    if not os.path.exists(filepath): return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

en_locales = load_json('assets/locales/en.json')
missing_texts = []

def has_meaningful_text(text):
    if not text: return False
    text = text.strip()
    return len(text) > 1 and re.search(r'[a-zA-Z]', text)

def should_process(element):
    if element.has_attr('data-i18n'):
        return False
    if element.name in ['script', 'style', 'svg', 'path', 'symbol']:
        return False
    return True

for filepath in FILES:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'a', 'span', 'li', 'button', 'b', 'strong', 'td', 'th']:
        for el in soup.find_all(tag_name):
            if not should_process(el): continue
            
            inner_html = el.decode_contents().strip()
            if not has_meaningful_text(inner_html): continue
            
            if any(child.name in ['p', 'div', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5'] for child in el.children if child.name):
                continue
                
            # Check if this text already exists in en.json
            found = False
            for v in en_locales.values():
                if v == inner_html:
                    found = True
                    break
            
            if not found and inner_html not in missing_texts:
                missing_texts.append(inner_html)

with open('missing_strings.json', 'w', encoding='utf-8') as f:
    json.dump(missing_texts, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(missing_texts)} unique missing strings.")
