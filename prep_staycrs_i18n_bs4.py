from bs4 import BeautifulSoup, NavigableString
import json

files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

lang_dropdown = """
<select id="languageSelect" class="lang-selector" style="font-size: 0.9rem; padding: 4px; margin-left: 10px;">
  <option value="en">English</option>
  <option value="th">ภาษาไทย</option>
  <option value="zh-CN">中文(简体)</option>
  <option value="ar">العربية</option>
  <option value="vi">Tiếng Việt</option>
  <option value="km">ភាសាខ្មែរ</option>
</select>
"""

script_tag = '<script src="assets/js/script-v2.js" defer></script>'

extracted_strings = {}
counter = 0

def clean_text(text):
    return " ".join(text.split()).strip()

tags_to_translate = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'a', 'span', 'li', 'button', 'b', 'strong', 'td', 'th', 'label']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Add Language Dropdown to Nav
    nav_links = soup.select_one('.nav .links')
    if nav_links and not soup.select_one('#languageSelect'):
        dropdown_soup = BeautifulSoup(lang_dropdown, 'html.parser')
        nav_links.append(dropdown_soup)
        
    # 2. Add Script Tag
    if not soup.find(lambda tag: tag.name == 'script' and 'script-v2.js' in tag.get('src', '')):
        script_soup = BeautifulSoup(script_tag, 'html.parser')
        body = soup.find('body')
        if body:
            body.append(script_soup)
            
    # 3. Add data-i18n tags
    for tag in soup.find_all(tags_to_translate):
        # Only tag elements that actually have direct text content, not just nested tags
        # and skip if already tagged
        if tag.has_attr('data-i18n'):
            continue
            
        # We only want to translate tags that have meaningful text
        text_content = clean_text(tag.get_text(separator=' ', strip=True))
        
        if len(text_content) > 1 and not text_content.isdigit():
            # If the tag has no inner tags, just text:
            if len(tag.find_all()) == 0:
                key = f"staycrs-auto-{counter}"
                counter += 1
                tag['data-i18n'] = key
                extracted_strings[key] = tag.decode_contents()
            else:
                # If it has inner tags like <br> or <strong> inside a <p>
                # Only tag it if the direct text is substantial, else leave for manual or skip
                # Actually, let's just tag the whole inner HTML
                key = f"staycrs-auto-{counter}"
                counter += 1
                tag['data-i18n'] = key
                tag['data-i18n-html'] = "true"
                extracted_strings[key] = tag.decode_contents()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
with open('staycrs_missing_strings.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_strings, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(extracted_strings)} strings.")
