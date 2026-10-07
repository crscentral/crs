import os
import json
import re
import time
from bs4 import BeautifulSoup, NavigableString
from deep_translator import GoogleTranslator

LANGUAGES = {
    'th': 'th',
    'zh': 'zh-CN',
    'ar': 'ar',
    'vi': 'vi',
    'km': 'km'
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
texts_to_translate = [] # List of tuples: (key, original_text)
elements_to_tag = []

def has_meaningful_text(text):
    if not text: return False
    text = text.strip()
    return len(text) > 1 and re.search(r'[a-zA-Z]', text)

def should_process(element):
    if element.has_attr('data-i18n'):
        return False
    # Don't process script, style
    if element.name in ['script', 'style', 'svg', 'path', 'symbol']:
        return False
    return True

base_idx = 0

for filepath in FILES:
    if not os.path.exists(filepath): continue
    print(f"Scanning {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # We look for common text-holding elements
    for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'a', 'span', 'li', 'button', 'b', 'strong', 'td', 'th']:
        for el in soup.find_all(tag_name):
            if not should_process(el): continue
            
            # Check if it contains mostly text or simple formatting
            inner_html = el.decode_contents().strip()
            if not has_meaningful_text(inner_html): continue
            
            # If the element has nested block elements, skip it (let the inner elements be caught)
            if any(child.name in ['p', 'div', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5'] for child in el.children if child.name):
                continue
                
            # OK, we want to translate inner_html
            # Let's check if we already have this text in en.json
            existing_key = None
            for k, v in locales['en'].items():
                if v == inner_html:
                    existing_key = k
                    break
                    
            if existing_key:
                el['data-i18n'] = existing_key
            else:
                key = f"auto_gen_{base_idx}"
                base_idx += 1
                el['data-i18n'] = key
                locales['en'][key] = inner_html
                texts_to_translate.append((key, inner_html))
                
    # Save the updated HTML immediately
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print(f"Found {len(texts_to_translate)} new strings to translate.")

# Now translate in batches
def translate_batch(texts, target_lang):
    # Deep translator translates a list of strings
    translator = GoogleTranslator(source='en', target=target_lang)
    results = []
    # Batch size 10 to avoid too large requests
    batch_size = 10
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        try:
            res = translator.translate_batch(batch)
            results.extend(res)
            time.sleep(1) # Sleep to avoid rate limits
        except Exception as e:
            print(f"Error translating batch to {target_lang}: {e}")
            # fallback to original
            results.extend(batch)
    return results

if texts_to_translate:
    keys = [item[0] for item in texts_to_translate]
    original_texts = [item[1] for item in texts_to_translate]
    
    for lang_code, trans_code in LANGUAGES.items():
        print(f"Translating {len(original_texts)} items to {lang_code}...")
        translated_texts = translate_batch(original_texts, trans_code)
        
        for i, key in enumerate(keys):
            if i < len(translated_texts) and translated_texts[i]:
                locales[lang_code][key] = translated_texts[i]
            else:
                locales[lang_code][key] = original_texts[i]
                
# Save JSON files
for lang, data in locales.items():
    save_json(f'assets/locales/{lang}.json', data)

print("Translations generated and saved.")
