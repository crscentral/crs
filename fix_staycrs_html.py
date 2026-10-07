from bs4 import BeautifulSoup
import json

files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

lang_html = """
<div class="lang-selector" style="position: relative; margin-left: auto;">
  <button class="lang-btn" style="background: transparent; border: 1px solid var(--navy); border-radius: 4px; padding: 6px 12px; color: var(--navy); font-size: 0.9rem; cursor: pointer; font-weight: 600;">English ▼</button>
  <div class="lang-dropdown" style="display: none; position: absolute; right: 0; top: 100%; background: #fff; border: 1px solid #ccc; border-radius: 4px; width: 140px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); z-index: 100;">
    <div class="lang-option active" data-lang="en" style="padding: 8px 16px; cursor: pointer; color: var(--navy); font-size: 0.9rem; border-bottom: 1px solid #eee;">English</div>
    <div class="lang-option" data-lang="th" style="padding: 8px 16px; cursor: pointer; color: var(--navy); font-size: 0.9rem; border-bottom: 1px solid #eee;">ภาษาไทย</div>
    <div class="lang-option" data-lang="zh-CN" style="padding: 8px 16px; cursor: pointer; color: var(--navy); font-size: 0.9rem; border-bottom: 1px solid #eee;">中文(简体)</div>
    <div class="lang-option" data-lang="ar" style="padding: 8px 16px; cursor: pointer; color: var(--navy); font-size: 0.9rem; border-bottom: 1px solid #eee;">العربية</div>
    <div class="lang-option" data-lang="vi" style="padding: 8px 16px; cursor: pointer; color: var(--navy); font-size: 0.9rem; border-bottom: 1px solid #eee;">Tiếng Việt</div>
    <div class="lang-option" data-lang="km" style="padding: 8px 16px; cursor: pointer; color: var(--navy); font-size: 0.9rem;">ភាសាខ្មែរ</div>
  </div>
</div>
<style>
.lang-selector:hover .lang-dropdown, .lang-selector.open .lang-dropdown { display: block !important; }
.lang-option:hover { background: var(--tint); }
</style>
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove the bad languageSelect if it exists
    bad_select = soup.select_one('#languageSelect')
    if bad_select:
        bad_select.decompose()
        
    nav_links = soup.select_one('.nav .links')
    if nav_links and not soup.select_one('.lang-selector'):
        dropdown_soup = BeautifulSoup(lang_html, 'html.parser')
        nav_links.append(dropdown_soup)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("Fixed StayCRS HTML injection.")
