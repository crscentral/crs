files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

css_patch = """
/* Fix Logo Squishing and Nav Width */
.nav.wrap { max-width: 1440px !important; padding-left: 30px; padding-right: 30px; }
.logo, .logo-link { flex-shrink: 0 !important; }
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '/* Fix Logo Squishing and Nav Width */' not in html:
        html = html.replace('</style>', css_patch + '\n</style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied logo fix.")
