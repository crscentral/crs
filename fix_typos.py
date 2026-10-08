import re

for filename in ['index.html', 'staycrs.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('Issue invoices and receipts from the system..', 'Issue invoices and receipts from the system.')
    html = html.replace('No setup fee..', 'No setup fee.')
    
    html = html.replace('Registered in Hyderabad, India, with a Bangkok base to meet clients across the region., with on-ground teams and local expertise across Thailand, Laos, India, Nepal, Malaysia, and Vietnam.', 'Registered in Hyderabad, India, with a Bangkok base to meet clients across the region. Expertise across Thailand, Laos, India, Nepal, Malaysia and Vietnam.')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
