files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

import re

new_css = """/* Final StayCRS Fixes */
.nav.wrap { max-width: 1440px !important; gap: 2rem; padding: 0 20px; }
.logo { direction: ltr; flex-shrink: 0 !important; }
header .nav > a { flex-shrink: 0; }
@media (max-width: 1300px) {
  .links { gap: 14px !important; }
  .links a { font-size: 0.85rem !important; }
}
@media (max-width: 900px) {
  .links { gap: 8px !important; }
  .links a { font-size: 0.75rem !important; }
  .links .btn { padding: 6px 12px !important; }
}
@media (max-width: 620px) {
  .nav.wrap { padding: 0 10px !important; gap: 10px !important; }
  .logo { height: 32px !important; }
  .links { gap: 8px !important; }
  .links .btn { padding: 6px 10px !important; font-size: 0.8rem !important; }
  .lang-btn { font-size: 0.8rem !important; padding: 4px 6px !important; }
}
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the old patch block if it exists
    html = re.sub(r'/\* Fix Logo Squishing and Nav Width \*/.*?(?=</style>)', '', html, flags=re.DOTALL)
    # Remove any previous Final StayCRS Fixes to be safe
    html = re.sub(r'/\* Final StayCRS Fixes \*/.*?(?=</style>)', '', html, flags=re.DOTALL)
    
    html = html.replace('</style>', new_css + '\n</style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied final robust CSS.")
