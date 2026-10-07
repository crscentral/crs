import json
import os

chunks = ['trans_chunk_0.json', 'trans_chunk_1.json', 'trans_chunk_2.json', 'trans_chunk_3.json']
locales = {
    'vi': {},
    'zh-CN': {},
    'th': {},
    'km': {},
    'ar': {}
}

for chunk in chunks:
    with open(chunk, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for english_key, trans_dict in data.items():
            for lang, trans_val in trans_dict.items():
                if lang in locales:
                    locales[lang][english_key] = trans_val

for lang, new_trans in locales.items():
    filepath = f'assets/locales/{lang}.json'
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = {}
        
    for k, v in new_trans.items():
        existing[k] = v
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
        
print("Merged into locale files successfully.")
