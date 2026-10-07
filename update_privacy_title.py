import os

files_to_update = [
    'staycrs.html',
    'staycrs-terms.html',
    'staycrs-cancellation.html',
    'staycrs-privacy.html',
    'staycrs-refund.html'
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update footer links
        content = content.replace('>Privacy Policy</a>', '>Privacy and Data Protection Policy</a>')
        
        # Update h1 heading (specifically in staycrs-privacy.html)
        content = content.replace("<h1 style='margin-bottom: 20px;'>Privacy Policy</h1>", "<h1 style='margin-bottom: 20px;'>Privacy and Data Protection Policy</h1>")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

