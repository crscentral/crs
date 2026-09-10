import glob
import re

for filepath in glob.glob('blog/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # look inside <div class="blog-post-body" ... </div>
    match = re.search(r'<div class="blog-post-body"[^>]*>(.*?)</div>\s*(?:</article>|<!--)', content, flags=re.DOTALL)
    if match:
        body = match.group(1)
        # count number of <p> tags vs <ul> tags
        p_count = len(re.findall(r'<p[^>]*>', body))
        ul_count = len(re.findall(r'<ul[^>]*>', body))
        print(f"{filepath}: {p_count} <p> tags, {ul_count} <ul> tags")

