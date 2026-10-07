import os

files_to_update = [
    'staycrs-terms.html',
    'staycrs-cancellation.html',
    'staycrs-privacy.html',
    'staycrs-refund.html'
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('<a href="#top" aria-label="StayCRS home">', '<a href="staycrs.html" aria-label="StayCRS home">')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated logo link in {filename}")

