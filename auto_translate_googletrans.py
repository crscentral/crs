import os
import json
import time
from bs4 import BeautifulSoup
from googletrans import Translator

LANG_MAP = {
    'vi': 'vi',
    'zh-CN': 'zh-cn',
    'th': 'th',
    'km': 'km',
    'ar': 'ar'
}

with open('all_missing.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

# Filter out empty
filtered_missing = []
for s in missing:
    soup = BeautifulSoup(s, 'html.parser')
    if not soup.get_text().strip(): continue
    filtered_missing.append(s)

translator = Translator()

for target_lang, lang_code in LANG_MAP.items():
    path = f'assets/locales/{target_lang}.json' # actually lang_map keys were correct for filepath
    if target_lang == 'zh-CN': path = 'assets/locales/zh-CN.json'
    
    loc_dict = {}
    if os.path.exists(path):
        loc_dict = json.load(open(path, 'r', encoding='utf-8'))
    
    print(f"Processing {target_lang}...")
    
    untranslated_items = [s for s in filtered_missing if s not in loc_dict or loc_dict[s] == s]
    print(f"Found {len(untranslated_items)} untranslated items.")
    
    for i, s in enumerate(untranslated_items):
        try:
            if '<' not in s:
                loc_dict[s] = translator.translate(s, dest=lang_code).text
            else:
                soup = BeautifulSoup(s, 'html.parser')
                text_nodes = [node for node in soup.find_all(string=True) if node.strip()]
                if not text_nodes:
                    loc_dict[s] = s
                    continue
                
                texts_to_translate = [node.strip() for node in text_nodes]
                translations = translator.translate(texts_to_translate, dest=lang_code)
                
                # handle if a single string returned
                if not isinstance(translations, list):
                    translations = [translations]
                    
                for node, trans in zip(text_nodes, translations):
                    if trans.text:
                        new_text = node.replace(node.strip(), trans.text)
                        node.replace_with(new_text)
                
                loc_dict[s] = str(soup)
            
        except Exception as e:
            print(f"Error on '{s}': {e}")
            loc_dict[s] = s
            # recreate translator if blocked
            translator = Translator()
            time.sleep(2)
            
        if i % 20 == 0:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(loc_dict, f, ensure_ascii=False, indent=2)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(loc_dict, f, ensure_ascii=False, indent=2)
    print(f"Done {target_lang}")

print("Done all.")
