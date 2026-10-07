import json
import re
import time
from googletrans import Translator
from bs4 import BeautifulSoup
import bs4

languages = {'vi': 'vi', 'zh-CN': 'zh-cn', 'th': 'th', 'km': 'km', 'ar': 'ar'}

with open('/Users/sumantsingh/Desktop/S/Websites/crs/chunk_3.json', 'r', encoding='utf-8') as f:
    strings = json.load(f)

translator = Translator()

def do_translate(text, dest_lang, retries=3):
    global translator
    for i in range(retries):
        try:
            time.sleep(0.5)
            # handle cases where translation returns None
            res = translator.translate(text, dest=dest_lang)
            if res and res.text:
                return res.text
            return text
        except Exception as e:
            print(f"Error on retry {i}: {e}")
            time.sleep(2)
            # re-init translator on error
            translator = Translator()
    return text

def translate_preserve_tags(text, dest_lang):
    if not text.strip():
        return text
    
    if '<' not in text and '>' not in text:
        return do_translate(text, dest_lang)

    soup = BeautifulSoup(text, 'html.parser')
    for node in soup.find_all(string=True):
        if isinstance(node, bs4.element.NavigableString):
            if isinstance(node, (bs4.element.Comment, bs4.element.CData, bs4.element.ProcessingInstruction, bs4.element.Declaration, bs4.element.Doctype)):
                continue
            
            s = str(node).strip()
            if s and any(c.isalpha() for c in s):
                translated = do_translate(str(node), dest_lang)
                node.replace_with(translated)
                    
    return str(soup)

result = {}
total = len(strings)

for i, s in enumerate(strings):
    print(f"Translating {i+1}/{total}...")
    result[s] = {}
    for lang_code, google_code in languages.items():
        result[s][lang_code] = translate_preserve_tags(s, google_code)
        
    # save incremental progress
    with open('/Users/sumantsingh/Desktop/S/Websites/crs/trans_chunk_3.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

print("Done!")
