import json

def add_translations(new_dict):
    try:
        with open('/Users/sumantsingh/Desktop/S/Websites/crs/translated_th.json', 'r', encoding='utf-8') as f:
            d = json.load(f)
    except FileNotFoundError:
        d = {}
    
    d.update(new_dict)
    
    with open('/Users/sumantsingh/Desktop/S/Websites/crs/translated_th.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    pass
