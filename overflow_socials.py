import re
import glob

html_files = glob.glob('*.html') + glob.glob('blog/*.html')

# We'll just modify index.html first and then sync to all
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Currently in index.html, it looks like this:
# <h4 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--text-white); font-size: 1.1rem;" data-i18n="footer-social-title">Connect With Us</h4>
# <div class="footer-social" style="display: flex; gap: 0.8rem; flex-wrap: nowrap; margin-top: 1rem;">
# ... icons ...
# </div>

pattern = re.compile(
    r'(<h4[^>]*>Connect With Us</h4>\s*<div class="footer-social"[^>]*>.*?</div>)',
    re.DOTALL
)

match = pattern.search(idx)
if not match:
    print("Could not find social block in index.html")
    exit()
    
social_html = match.group(1)

# Modify the gap and width
social_html = re.sub(
    r'gap:\s*0\.8rem;',
    'gap: 2rem;',
    social_html
)

# Wrap it in a fixed width div so it overflows
new_block = f"""
        <div style="width: 650px; position: relative; z-index: 10;">
          {social_html}
        </div>"""
        
# Replace in index
idx = idx.replace(match.group(1), new_block.strip())

# We also should probably ensure mobile responsiveness. If screen is small, 650px will cause horizontal scroll.
# Actually, it's safer to just let it be `width: max-content; gap: 2.5rem;`
# Let's change the wrapper to `width: max-content;`
idx = idx.replace('width: 650px;', 'width: max-content; max-width: 90vw;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)

print("Updated index.html")
