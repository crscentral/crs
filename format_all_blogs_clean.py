import re
import glob
import os

skip_files = [
    'affordable-pms-channel-manager-for-independent-hotels.html',
    'hotel-website-development-direct-bookings.html',
    'hotel-digital-marketing-social-media.html',
    'what-is-hotel-revenue-management.html'
]

def format_html(content):
    match = re.search(r'(<div class="blog-post-body"[^>]*>)(.*?)(</div>\s*(?:</article>|<!--))', content, flags=re.DOTALL)
    if not match:
        return content
    
    body = match.group(2)
    
    # Strip data-i18n
    body = re.sub(r'\sdata-i18n="[^"]*"', '', body)
    body = re.sub(r'\sdata-i18n-html="[^"]*"', '', body)
    
    tags = re.findall(r'<p[^>]*>.*?</p>|<h[1-6][^>]*>.*?</h[1-6]>|<ul>.*?</ul>', body, flags=re.DOTALL)
    
    new_tags = []
    
    for tag in tags:
        if tag.startswith('<p'):
            inner_text = re.sub(r'<[^>]+>', '', tag).strip()
            
            # Check if this paragraph should actually be a heading
            # Conditions for a heading:
            # 1. Short (length between 10 and 80)
            # 2. Does not end in period, comma, or colon
            # 3. Not starting with lowercase (often a continuation)
            # 4. Doesn't contain common paragraph phrases
            
            is_heading_candidate = (
                10 < len(inner_text) < 80 and
                not inner_text.endswith('.') and
                not inner_text.endswith(':') and
                not inner_text.endswith(',') and
                not inner_text.endswith('?') and
                inner_text[0].isupper() and
                "?" not in inner_text and
                not inner_text.startswith("By ") and
                not inner_text.startswith("At a glance")
            )
            
            # Some specific exceptions
            if is_heading_candidate and not "This means" in inner_text and not "For example" in inner_text:
                new_tags.append(f'<h3 style="margin-top: 2.5rem; margin-bottom: 1rem; font-size: 1.5rem; font-family: var(--font-heading); color: var(--text-dark);">{inner_text}</h3>')
            else:
                # Keep as <p>, but if it's very short and ends in ':', let's bold it
                if inner_text.endswith(':'):
                    # Replace the <p...> with bolded inner text inside
                    tag = re.sub(r'(<p[^>]*>)(.*?)(</p>)', r'\1<strong>\2</strong>\3', tag)
                new_tags.append(tag)
        else:
            new_tags.append(tag)
            
    formatted_body = "\n".join(new_tags)
    
    # Group short paragraphs that look like bullet points into a list.
    # If a <p> tag starts with a capital letter, does not end in a period, and is less than 100 chars, and immediately follows a colon or another bullet.
    # Actually, let's just do a regex replace to bold key terms.
    
    formatted_body = re.sub(r'(?<!>)(Hotel Revenue Management)(?!<)', r'<strong>\1</strong>', formatted_body, flags=re.IGNORECASE)
    formatted_body = re.sub(r'(?<!>)(CRS Central)(?!<)', r'<strong>\1</strong>', formatted_body)
    formatted_body = formatted_body.replace('<strong><strong>', '<strong>').replace('</strong></strong>', '</strong>')
    
    seo_block = """
    <div style="margin-top: 3rem; padding: 2rem; background: #f8fafc; border-radius: var(--radius-lg); border-left: 4px solid var(--primary-color);">
      <h3 style="font-size: 1.4rem; font-family: var(--font-heading); color: var(--text-dark); margin-bottom: 0.75rem;">Optimize Your Strategy with CRS Central</h3>
      <p style="margin-bottom: 0; color: var(--text-body); line-height: 1.8;"><strong>CRS Central</strong> specializes in comprehensive <strong>Hotel Revenue Management</strong> for independent properties. We leverage dynamic pricing strategies, OTAs optimization, and deep market data to help hotels maximize their Average Daily Rate (ADR) and increase direct bookings. <a href="../audit.html" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Request a Free Revenue Audit today</a> to discover your hidden revenue potential.</p>
    </div>
    """
    if "Optimize Your Strategy with CRS Central" not in formatted_body:
        formatted_body += seo_block
    
    new_content = content[:match.start(2)] + formatted_body + content[match.end(2):]
    return new_content

count = 0
for filepath in glob.glob('blog/*.html'):
    basename = os.path.basename(filepath)
    if basename in skip_files:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        orig = f.read()
        
    res = format_html(orig)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(res)
    count += 1

print(f"Successfully cleaned and formatted {count} blogs.")
