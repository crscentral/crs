import json

with open('assets/locales/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)
with open('assets/locales/th.json', 'r', encoding='utf-8') as f:
    th = json.load(f)

untranslated = {}
for k, v in th.items():
    if k in en and en[k] == v and "crs" not in v.lower() and "staycrs" not in v.lower():
        # Maybe it's a short generic word? Or an actual sentence.
        if len(v) > 5:
            untranslated[k] = v

print("Keys with identical English/Thai text:")
for k, v in untranslated.items():
    print(f"{k}: {v}")
