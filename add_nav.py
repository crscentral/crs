import glob
import re

for file in glob.glob("*.html") + glob.glob("blog/*.html") + glob.glob("staycrs/*.html"):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We look for the nav link for services and append StayCRS right after it
        # Note: Depending on spacing, we might need a robust regex
        
        # Example match: <a href="services.html" class="nav-link" data-i18n="nav-services">Services</a>
        # Sometimes it might be <a href="../services.html" ...
        
        # Pattern: find the </a> for services and add the StayCRS link
        pattern = r'(<a\s+href="(?:\.\./)?services\.html"[^>]*>Services</a>)'
        
        # Determine depth to make correct relative links
        if file.startswith("blog/") or file.startswith("staycrs/"):
            staycrs_link = '\n        <a href="../staycrs.html" class="nav-link">StayCRS</a>'
        else:
            staycrs_link = '\n        <a href="staycrs.html" class="nav-link">StayCRS</a>'
            
        if "StayCRS" not in content and 'class="nav-link"' in content:
            new_content = re.sub(pattern, r'\1' + staycrs_link, content)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        pass

print("Added StayCRS to navigation.")
