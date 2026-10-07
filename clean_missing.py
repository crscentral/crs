import json
import re
from bs4 import BeautifulSoup

with open('missing_strings.json', 'r', encoding='utf-8') as f:
    strings = json.load(f)

cleaned = []
for s in strings:
    # Check if it has actual text content, not just HTML tags
    soup = BeautifulSoup(s, 'html.parser')
    text = soup.get_text().strip()
    if len(text) > 2 and re.search(r'[a-zA-Z]', text):
        cleaned.append(s)

with open('missing_strings_clean.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)

print(f"Cleaned. {len(cleaned)} strings remain.")
