import os
import json
import re
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Target languages and their translation codes
LANGUAGES = {
    'th': 'th',
    'zh': 'zh-CN',
    'ar': 'ar',
    'vi': 'vi',
    'km': 'km'
}

FILES = ['index.html', 'services.html', 'thailand.html', 'faq.html', 'about.html']

def load_json(filepath):
    if not os.path.exists(filepath): return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

locales = {lang: load_json(f'assets/locales/{lang}.json') for lang in ['en'] + list(LANGUAGES.keys())}
new_translations_count = 0

def get_safe_key(base_key, index):
    return f"auto-{base_key}-{index}"

def extract_and_tag(soup, tag_name, base_key):
    global new_translations_count
    elements = soup.find_all(tag_name)
    idx = 0
    for el in elements:
        # Skip if already has data-i18n
        if el.has_attr('data-i18n'):
            continue
            
        # Get direct text, ignoring complex nested structures
        text = el.decode_contents().strip()
        if not text or '<' in text and not all(t in text for t in ['<b>', '</b>', '<strong>', '</strong>', '<br>', '<br/>']):
            # If it has complex HTML (other than simple formatting), skip it for automatic translation to avoid breaking HTML
            if len(el.find_all()) > 2:
                continue
                
        # Simple text extraction for translation
        pure_text = el.get_text().strip()
        if not pure_text or len(pure_text) < 2:
            continue
            
        # Generate key
        key = get_safe_key(base_key, idx)
        while key in locales['en']:
            idx += 1
            key = get_safe_key(base_key, idx)
            
        # Update HTML
        el['data-i18n'] = key
        
        # Save to EN
        locales['en'][key] = text
        
        # Translate to others
        for lang_code, trans_code in LANGUAGES.items():
            try:
                # We translate pure_text but what about inner HTML like <b>? 
                # Deep translator doesn't preserve HTML well, so if there's HTML, we'll try to translate it or just strip it.
                # Since this is a quick fix, if it has <b>, we might lose the bold. That's acceptable for now, or we translate the raw text.
                # Let's just translate the raw text and keep HTML as is? Google Translate API can handle HTML strings.
                translated = GoogleTranslator(source='en', target=trans_code).translate(text)
                locales[lang_code][key] = translated
            except Exception as e:
                print(f"Error translating to {lang_code}: {e}")
                locales[lang_code][key] = text # Fallback to english
                
        new_translations_count += 1
        idx += 1

for filepath in FILES:
    if not os.path.exists(filepath): continue
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    base = filepath.split('.')[0]
    
    # Target common text elements
    extract_and_tag(soup, 'p', base + '-p')
    extract_and_tag(soup, 'h2', base + '-h2')
    extract_and_tag(soup, 'h3', base + '-h3')
    extract_and_tag(soup, 'li', base + '-li')
    extract_and_tag(soup, 'b', base + '-b')
    
    # Save HTML
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# Save locales
for lang, data in locales.items():
    save_json(f'assets/locales/{lang}.json', data)

print(f"Done. Added {new_translations_count} new translations.")
