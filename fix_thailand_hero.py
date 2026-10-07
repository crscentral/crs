import json
import os
from deep_translator import GoogleTranslator

LANGUAGES = {
    'th': 'th',
    'zh': 'zh-CN',
    'ar': 'ar',
    'vi': 'vi',
    'km': 'km'
}

keys_to_translate = [
    "thailand-intro2",
    "thailand-choose",
    "thailand-btn-bkk",
    "thailand-btn-hh",
    "thailand-btn-pty",
    "thailand-btn-hkt"
]

def load_json(filepath):
    if not os.path.exists(filepath): return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

en_locales = load_json('assets/locales/en.json')

for lang_code, trans_code in LANGUAGES.items():
    locales = load_json(f'assets/locales/{lang_code}.json')
    translator = GoogleTranslator(source='en', target=trans_code)
    
    for key in keys_to_translate:
        if key in en_locales:
            original = en_locales[key]
            # Translate it
            translated = translator.translate(original)
            print(f"[{lang_code}] {key}: {translated}")
            locales[key] = translated
            
    save_json(f'assets/locales/{lang_code}.json', locales)

print("Finished translating thailand hero keys.")
