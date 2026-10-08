files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

import re

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the current Final StayCRS Fixes - Aligned Version
    # We will modify it to add gap: 3rem to .nav.wrap and aggressive shrink
    
    new_css = """/* Final StayCRS Fixes - Aligned Version */
.logo { direction: ltr; flex-shrink: 0 !important; }
header .nav > a { flex-shrink: 0; margin-inline-end: auto; }
header .nav { gap: 2rem; }

/* Ensure items fit within the 1120px wrap without squishing the logo */
.links { gap: 16px !important; flex-shrink: 1; }
.links a { font-size: 0.9rem !important; }

@media (max-width: 1200px) {
  .links { gap: 10px !important; }
  .links a { font-size: 0.8rem !important; }
  .links .btn { padding: 6px 12px !important; }
}
@media (max-width: 900px) {
  .links { gap: 8px !important; }
  .links a { font-size: 0.75rem !important; }
  .links .btn { padding: 6px 10px !important; font-size: 0.75rem !important; }
  .lang-btn { font-size: 0.75rem !important; padding: 4px 6px !important; }
}
"""

    html = re.sub(r'/\* Final StayCRS Fixes - Aligned Version \*/.*?(?=@media \(max-width: 900px\))', new_css.split('@media (max-width: 900px)')[0], html, flags=re.DOTALL)
    
    # Also replace the 900px block to include the new smaller sizes
    html = re.sub(r'@media \(max-width: 900px\).*?\}', '@media (max-width: 900px) {\n  .links { gap: 8px !important; }\n  .links a { font-size: 0.75rem !important; }\n  .links .btn { padding: 6px 10px !important; font-size: 0.75rem !important; }\n  .lang-btn { font-size: 0.75rem !important; padding: 4px 6px !important; }\n}', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied aligned CSS v3.")
