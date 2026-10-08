files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('text-align: left;', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed text align")
