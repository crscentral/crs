import os
import json
import time
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

LANG_MAP = {
    'vi': 'vi',
    'zh-CN': 'zh-CN',
    'th': 'th',
    'km': 'km',
    'ar': 'ar'
}

with open('all_missing.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

# Filter out image-only or empty strings
filtered_missing = []
for s in missing:
    soup = BeautifulSoup(s, 'html.parser')
    text = soup.get_text().strip()
    if not text:
        continue
    filtered_missing.append(s)

# Pre-populate en.json
en_dict = json.load(open('assets/locales/en.json', 'r', encoding='utf-8'))
for s in filtered_missing:
    if s not in en_dict:
        en_dict[s] = s
with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    json.dump(en_dict, f, ensure_ascii=False, indent=2)

def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

for target_lang, lang_code in LANG_MAP.items():
    path = f'assets/locales/{lang_code}.json'
    loc_dict = {}
    if os.path.exists(path):
        loc_dict = json.load(open(path, 'r', encoding='utf-8'))
    
    print(f"Processing {target_lang}...")
    
    gt_lang = target_lang
    if gt_lang == 'zh-CN': gt_lang = 'zh-CN'
    translator = GoogleTranslator(source='en', target=gt_lang)
    
    untranslated_items = [s for s in filtered_missing if s not in loc_dict or loc_dict[s] == s]
    print(f"Found {len(untranslated_items)} untranslated items.")
    
    for i, s in enumerate(untranslated_items):
        try:
            if '<' not in s:
                loc_dict[s] = translator.translate(s)
            else:
                soup = BeautifulSoup(s, 'html.parser')
                # Extract text nodes
                text_nodes = [node for node in soup.find_all(string=True) if node.strip()]
                if not text_nodes:
                    loc_dict[s] = s
                    continue
                
                # Batch translate nodes
                texts_to_translate = [node.strip() for node in text_nodes]
                translated_texts = translator.translate_batch(texts_to_translate)
                
                # Replace nodes
                for node, trans in zip(text_nodes, translated_texts):
                    if trans:
                        new_text = node.replace(node.strip(), trans)
                        node.replace_with(new_text)
                
                loc_dict[s] = str(soup)
            
            time.sleep(0.5)  # slight delay to avoid rate limit
            
        except Exception as e:
            print(f"Error on '{s}': {e}")
            loc_dict[s] = s
            time.sleep(5)
            
        if i % 20 == 0:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(loc_dict, f, ensure_ascii=False, indent=2)
            print(f"  {i}/{len(untranslated_items)}")

    # Final save
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(loc_dict, f, ensure_ascii=False, indent=2)

print("Done all.")
