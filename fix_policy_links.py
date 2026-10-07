import os

for filename in ['staycrs-terms.html', 'staycrs-cancellation.html', 'staycrs-privacy.html', 'staycrs-refund.html']:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(
            '<a style="display:inline;margin-right:16px" href="https://crscentral.com" target="_blank" rel="noopener">Terms &amp; Conditions</a>',
            '<a style="display:inline;margin-right:16px" href="staycrs-terms.html">Terms &amp; Conditions</a>'
        )
        content = content.replace(
            '<a style="display:inline;margin-right:16px" href="https://crscentral.com" target="_blank" rel="noopener">Privacy Policy</a>',
            '<a style="display:inline;margin-right:16px" href="staycrs-privacy.html">Privacy Policy</a>'
        )
        content = content.replace(
            '<a style="display:inline;margin-right:16px" href="https://crscentral.com" target="_blank" rel="noopener">Refund Policy</a>',
            '<a style="display:inline;margin-right:16px" href="staycrs-refund.html">Refund Policy</a>'
        )
        content = content.replace(
            '<a style="display:inline" href="https://crscentral.com" target="_blank" rel="noopener">Cancellation Policy</a>',
            '<a style="display:inline" href="staycrs-cancellation.html">Cancellation Policy</a>'
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
print("Fixed links in policy pages.")
