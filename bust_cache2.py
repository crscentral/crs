import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'assets/css/style.min.css' in html:
        # replace any old ?v=... or add ?v=12
        html = re.sub(r'assets/css/style\.min\.css(?:\?v=\d+)?', 'assets/css/style.min.css?v=12', html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")
