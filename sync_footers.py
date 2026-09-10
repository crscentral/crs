import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html')

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
    
footer_match = re.search(r'(<footer class="footer">.*?</footer>)', idx_content, re.DOTALL)
ideal_footer = footer_match.group(1)

for file in html_files:
    if file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    is_blog = 'blog/' in file
    
    if is_blog:
        file_footer = ideal_footer.replace('src="assets/', 'src="../assets/')
        file_footer = file_footer.replace('href="./"', 'href="../"')
        for page in ['about.html', 'audit.html', 'blog.html', 'contact.html', 'laos.html', 'malaysia.html', 'vietnam.html', 'india.html', 'nepal.html', 'services.html', 'cancellation.html', 'privacy.html', 'refund.html', 'terms.html']:
            file_footer = file_footer.replace(f'href="{page}', f'href="../{page}')
    else:
        file_footer = ideal_footer
        
    content = re.sub(r'<footer class="footer">.*?</footer>', lambda _: file_footer, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
