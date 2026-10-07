import json
import os
from bs4 import BeautifulSoup

missing = json.load(open('missing_strings_clean.json'))

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

count = 0
for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'a', 'span', 'li', 'button', 'b', 'strong', 'td', 'th', 'div']:
    for el in soup.find_all(tag_name):
        if el.has_attr('data-i18n'):
            continue
        
        inner_html = el.decode_contents().strip()
        if inner_html in missing:
            el['data-i18n'] = inner_html
            count += 1

print(f"Matched {count} elements in index.html.")
