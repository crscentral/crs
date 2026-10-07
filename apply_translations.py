import os
import json
import re
from bs4 import BeautifulSoup

LANGUAGES = {
    'th': 'translated_th.json',
    'zh': 'translated_zh.json',
    'ar': 'translated_ar.json',
    'vi': 'translated_vi.json',
    'km': 'translated_km.json'
}

FILES = ['index.html', 'services.html', 'thailand.html', 'about.html', 'audit.html', 'blog.html', 'contact.html', 'staycrs.html']

def load_json(filepath):
    if not os.path.exists(filepath): return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

locales = {lang: load_json(f'assets/locales/{lang}.json') for lang in ['en'] + list(LANGUAGES.keys())}
translations = {lang: load_json(filepath) for lang, filepath in LANGUAGES.items()}

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

base_idx = 0
added_count = 0

for filepath in FILES:
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    modified = False
    
    for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'a', 'span', 'li', 'button', 'b', 'strong', 'td', 'th']:
        for el in soup.find_all(tag_name):
            if not should_process(el): continue
            
            inner_html = el.decode_contents().strip()
            if not has_meaningful_text(inner_html): continue
            
            if any(child.name in ['p', 'div', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5'] for child in el.children if child.name):
                continue
                
            # Check if this exact text exists in en.json
            existing_key = None
            for k, v in locales['en'].items():
                if v == inner_html:
                    existing_key = k
                    break
                    
            if existing_key:
                el['data-i18n'] = existing_key
                modified = True
            else:
                # Add it!
                key = f"auto-gen-{base_idx}"
                base_idx += 1
                el['data-i18n'] = key
                locales['en'][key] = inner_html
                
                # Check if we have translations for it
                for lang in LANGUAGES:
                    if inner_html in translations[lang]:
                        locales[lang][key] = translations[lang][inner_html]
                    else:
                        locales[lang][key] = inner_html # fallback
                
                added_count += 1
                modified = True
                
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}")

# Save the locale files
for lang, data in locales.items():
    save_json(f'assets/locales/{lang}.json', data)

print(f"Applied {added_count} new unique translations across all languages and updated HTML files!")
