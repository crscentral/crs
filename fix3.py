import json

with open('assets/locales/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

en["PMS & Channel Manager by StayCRS"] = "PMS & Channel Manager by StayCRS"
en["PMS &amp; Channel Manager by StayCRS"] = "PMS & Channel Manager by StayCRS"

with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, indent=2, ensure_ascii=False)
print("Updated en.json with StayCRS title")
