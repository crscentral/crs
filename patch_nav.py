files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

nav_css = """
/* Nav Fixes */
.links a, .lang-btn, .lang-option {
  white-space: nowrap !important;
}
@media (max-width: 1300px) {
  .links { gap: 12px !important; }
  .links a { font-size: 0.8rem !important; }
  .lang-btn { font-size: 0.8rem !important; padding: 4px 8px !important; }
}
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '/* Nav Fixes */' not in html:
        html = html.replace('</style>', nav_css + '\n</style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Injected nav CSS.")
