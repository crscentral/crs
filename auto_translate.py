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

# Filter out image-only or svg-only strings
filtered_missing = []
for s in missing:
    soup = BeautifulSoup(s, 'html.parser')
    # If the string only contains img or svg tags and no visible text, skip
    text = soup.get_text().strip()
    if not text:
        continue
    filtered_missing.append(s)

def translate_html(html_str, target_lang):
    translator = GoogleTranslator(source='en', target=target_lang)
    if '<' not in html_str:
        try:
            return translator.translate(html_str)
        except Exception as e:
            print(f"Error (plain): {e}")
            time.sleep(2)
            return html_str
    
    soup = BeautifulSoup(html_str, 'html.parser')
    for text_node in soup.find_all(string=True):
        if not text_node.strip(): continue
        try:
            trans = translator.translate(text_node.strip())
            new_text = text_node.replace(text_node.strip(), trans)
            text_node.replace_with(new_text)
        except Exception as e:
            print(f"Error (html): {e}")
            time.sleep(2)
    return str(soup)

# Load existing dicts
en_dict = json.load(open('assets/locales/en.json', 'r', encoding='utf-8'))
for s in filtered_missing:
    if s not in en_dict:
        en_dict[s] = s
with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    json.dump(en_dict, f, ensure_ascii=False, indent=2)

for target_lang, lang_code in LANG_MAP.items():
    path = f'assets/locales/{lang_code}.json'
    loc_dict = {}
    if os.path.exists(path):
        loc_dict = json.load(open(path, 'r', encoding='utf-8'))
    
    count = 0
    print(f"Translating to {target_lang}...")
    for i, s in enumerate(filtered_missing):
        if s not in loc_dict:
            try:
                # Some manual mappings for Google Translate
                gt_lang = target_lang
                if gt_lang == 'zh-CN': gt_lang = 'zh-CN'
                
                trans = translate_html(s, gt_lang)
                loc_dict[s] = trans
                count += 1
                if count % 10 == 0:
                    print(f"  {target_lang}: {count}/{len(filtered_missing)}")
                    # Save progress to avoid losing data
                    with open(path, 'w', encoding='utf-8') as f:
                        json.dump(loc_dict, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Failed to translate: {s} -> {e}")
                loc_dict[s] = s # fallback
                time.sleep(2)
                
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(loc_dict, f, ensure_ascii=False, indent=2)
    print(f"Finished {target_lang}. Translated {count} new strings.")

