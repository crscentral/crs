import json
import os
import sys

# 1. Update English first
with open('staycrs_missing_strings.json', 'r', encoding='utf-8') as f:
    en_new = json.load(f)
    
with open('assets/locales/en.json', 'r', encoding='utf-8') as f:
    en_main = json.load(f)

for k, v in en_new.items():
    en_main[k] = v

with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    json.dump(en_main, f, ensure_ascii=False, indent=2)

# 2. Update the others
langs = {
    'th': 'translated_th_staycrs.json',
    'zh-CN': 'translated_zh_staycrs.json',
    'ar': 'translated_ar_staycrs.json',
    'vi': 'translated_vi_staycrs.json',
    'km': 'translated_km_staycrs.json'
}

all_successful = True
for lang, trans_file in langs.items():
    if not os.path.exists(trans_file):
        print(f"Waiting on {trans_file}...")
        all_successful = False
        continue
        
    with open(trans_file, 'r', encoding='utf-8') as f:
        new_trans = json.load(f)
        
    main_file = f'assets/locales/{lang}.json'
    with open(main_file, 'r', encoding='utf-8') as f:
        main_trans = json.load(f)
        
    for k, v in new_trans.items():
        main_trans[k] = v
        
    with open(main_file, 'w', encoding='utf-8') as f:
        json.dump(main_trans, f, ensure_ascii=False, indent=2)
        
    print(f"Merged {lang}!")

if all_successful:
    print("All translations merged successfully!")
    
    # Bump cache
    with open('assets/js/script-v2.js', 'r', encoding='utf-8') as f:
        js = f.read()
    import re
    js = re.sub(r'\.json\?v=\d+', '.json?v=9', js)
    with open('assets/js/script-v2.js', 'w', encoding='utf-8') as f:
        f.write(js)

    with open('assets/js/script-v2.min.js', 'r', encoding='utf-8') as f:
        js_min = f.read()
    js_min = re.sub(r'\.json\?v=\d+', '.json?v=9', js_min)
    with open('assets/js/script-v2.min.js', 'w', encoding='utf-8') as f:
        f.write(js_min)
        
    print("Bumped cache to v9")
    sys.exit(0)
else:
    sys.exit(1)
