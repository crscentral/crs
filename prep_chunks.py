import json
import math
from bs4 import BeautifulSoup
import os

with open('all_missing.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

# Filter empty/unnecessary
filtered = []
en_dict = json.load(open('assets/locales/en.json', 'r', encoding='utf-8'))
vi_dict = json.load(open('assets/locales/vi.json', 'r', encoding='utf-8')) if os.path.exists('assets/locales/vi.json') else {}

for s in missing:
    soup = BeautifulSoup(s, 'html.parser')
    if not soup.get_text().strip(): continue
    if s in vi_dict and vi_dict[s] != s:
        continue # already translated to vi, assuming others too
    filtered.append(s)

print(f"Total strings to translate: {len(filtered)}")

chunk_size = math.ceil(len(filtered) / 4)
for i in range(4):
    chunk = filtered[i*chunk_size : (i+1)*chunk_size]
    with open(f'chunk_{i}.json', 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)
    print(f"Chunk {i} has {len(chunk)} items.")
