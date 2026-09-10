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
    # Isolate the body
    match = re.search(r'(<div class="blog-post-body"[^>]*>)(.*?)(</div>\s*(?:</article>|<!--))', content, flags=re.DOTALL)
    if not match:
        return content
    
    prefix = match.group(1)
    body = match.group(2)
    suffix = match.group(3)
    
    # Strip data-i18n
    body = re.sub(r'\sdata-i18n="[^"]*"', '', body)
    body = re.sub(r'\sdata-i18n-html="[^"]*"', '', body)
    
    # Identify lists
    tags = re.findall(r'<p[^>]*>.*?</p>|<h[1-6][^>]*>.*?</h[1-6]>|<ul>.*?</ul>', body, flags=re.DOTALL)
    
    new_tags = []
    in_list = False
    list_items = []
    
    def close_list():
        nonlocal in_list, list_items, new_tags
        if in_list:
            if len(list_items) > 1:
                ul = '<ul style="margin: 1rem 0 1.5rem 1.5rem; list-style-type: disc; line-height: 1.8;">\n'
                for li in list_items:
                    inner = re.sub(r'<p[^>]*>(.*?)</p>', r'\1', li, flags=re.DOTALL)
                    ul += f"  <li>{inner}</li>\n"
                ul += '</ul>'
                new_tags.append(ul)
            else:
                new_tags.extend(list_items)
            in_list = False
            list_items = []

    for tag in tags:
        if tag.startswith('<p'):
            inner_text = re.sub(r'<[^>]+>', '', tag).strip()
            is_short = len(inner_text) > 0 and len(inner_text) < 180
            ends_with_period = inner_text.endswith('.')
            ends_with_colon = inner_text.endswith(':')
            
            if new_tags and new_tags[-1].strip().endswith(':</p>'):
                in_list = True
                list_items.append(tag)
            elif in_list and (not ends_with_period or is_short or inner_text.startswith('- ')) and len(inner_text) < 200:
                list_items.append(tag)
            else:
                close_list()
                new_tags.append(tag)
        else:
            close_list()
            new_tags.append(tag)
            
    close_list()
    formatted_body = "\n".join(new_tags)
    
    # Bold key SEO terms
    formatted_body = re.sub(r'(?<!>)(Hotel Revenue Management)(?!<)', r'<strong>\1</strong>', formatted_body, flags=re.IGNORECASE)
    formatted_body = re.sub(r'(?<!>)(CRS Central)(?!<)', r'<strong>\1</strong>', formatted_body)
    
    # Fix double bold
    formatted_body = formatted_body.replace('<strong><strong>', '<strong>').replace('</strong></strong>', '</strong>')
    
    # Add SEO footer block
    seo_block = """
    <div style="margin-top: 3rem; padding: 1.5rem; background: var(--bg-light); border-radius: var(--radius-md); border-left: 4px solid var(--primary-color);">
      <h3 style="font-size: 1.25rem; font-family: var(--font-heading); color: var(--text-dark); margin-bottom: 0.5rem;">Maximize Your Profit with CRS Central</h3>
      <p style="margin-bottom: 0;"><strong>CRS Central</strong> is a leading provider of <strong>Hotel Revenue Management</strong> and OTA optimization services across Southeast Asia and beyond. We help independent hotels, resorts, and boutiques leverage dynamic pricing, channel distribution, and data-driven strategies to increase direct bookings and overall profitability. <a href="../audit.html" style="color: var(--primary-color); font-weight: 600; text-decoration: none;">Request a Free Revenue Audit today.</a></p>
    </div>
    """
    if "Maximize Your Profit with CRS Central" not in formatted_body:
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

print(f"Successfully formatted {count} blogs.")
