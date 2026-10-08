import os
import glob

# The favicon HTML to insert before </head>
favicon_html = '    <link rel="icon" type="image/webp" href="assets/images/logo_globe_transparent.webp">\n'

html_files = glob.glob('*.html')
for file in html_files:
    if file == "staycrs.html": 
        # staycrs.html already has its own specific favicon (the house SVG), so we skip it to preserve its branding.
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check if we already injected it
    if '<link rel="icon"' not in html:
        # Insert before </head>
        html = html.replace('</head>', favicon_html + '</head>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Injected favicon into HTML files")
