import re

for filename in ['assets/js/script-v2.js', 'assets/js/script-v2.min.js']:
    with open(filename, 'r', encoding='utf-8') as f:
        js = f.read()
    
    js = js.replace('.json?v=9', '.json?v=10')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(js)

for filename in ['index.html', 'staycrs.html', 'about.html', 'services.html', 'contact.html', 'blog.html', 'audit.html', 'privacy.html', 'terms.html', 'thailand.html', 'vietnam.html', 'malaysia.html', 'laos.html', 'india.html']:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
            
        html = re.sub(r'script-v2\.min\.js\?v=\d+', 'script-v2.min.js?v=20261008', html)
        html = re.sub(r'translations-v2\.min\.js\?v=\d+', 'translations-v2.min.js?v=20261008', html)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
    except FileNotFoundError:
        pass

print("Bumped cache busters")
