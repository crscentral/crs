import re
import glob

def format_html(content):
    # 1. Isolate the body
    match = re.search(r'(<div class="blog-post-body"[^>]*>)(.*?)(</div>\s*(?:</article>|<!--))', content, flags=re.DOTALL)
    if not match:
        return content
    
    prefix = match.group(1)
    body = match.group(2)
    suffix = match.group(3)
    
    # 2. Strip data-i18n
    body = re.sub(r'\sdata-i18n="[^"]*"', '', body)
    body = re.sub(r'\sdata-i18n-html="[^"]*"', '', body)
    
    # 3. Find pseudo-lists
    # We will split the body by tags
    tags = re.findall(r'<p[^>]*>.*?</p>|<h[1-6][^>]*>.*?</h[1-6]>|<ul>.*?</ul>', body, flags=re.DOTALL)
    
    new_tags = []
    in_list = False
    list_items = []
    
    def close_list():
        nonlocal in_list, list_items, new_tags
        if in_list:
            if len(list_items) > 1:
                # It's a real list
                ul = '<ul style="margin: 1rem 0 1.5rem 1.5rem; list-style-type: disc; line-height: 1.8;">\n'
                for li in list_items:
                    # Strip <p> tags and wrap in <li>
                    inner = re.sub(r'<p[^>]*>(.*?)</p>', r'\1', li, flags=re.DOTALL)
                    ul += f"  <li>{inner}</li>\n"
                ul += '</ul>'
                new_tags.append(ul)
            else:
                # False alarm, put it back as <p>
                new_tags.extend(list_items)
            in_list = False
            list_items = []

    for tag in tags:
        if tag.startswith('<p'):
            # Check if it looks like a list item
            inner_text = re.sub(r'<[^>]+>', '', tag).strip()
            # If previous tag ended in ':' and this is short, start a list
            # Or if we are already in a list and this doesn't end in '.' and isn't too long
            is_short = len(inner_text) > 0 and len(inner_text) < 150
            ends_with_period = inner_text.endswith('.')
            
            if new_tags and new_tags[-1].strip().endswith(':</p>'):
                # Start list
                in_list = True
                list_items.append(tag)
            elif in_list and (not ends_with_period or is_short) and len(inner_text) < 200:
                list_items.append(tag)
            else:
                close_list()
                new_tags.append(tag)
        else:
            close_list()
            new_tags.append(tag)
            
    close_list()
    
    # 4. Join back
    formatted_body = "\n".join(new_tags)
    
    # 5. Bold key SEO terms
    formatted_body = re.sub(r'(?<!>)(Hotel Revenue Management)(?!<)', r'<strong>\1</strong>', formatted_body, flags=re.IGNORECASE)
    formatted_body = re.sub(r'(?<!>)(CRS Central)(?!<)', r'<strong>\1</strong>', formatted_body)
    
    # Clean up double strongs if they already existed
    formatted_body = formatted_body.replace('<strong><strong>', '<strong>').replace('</strong></strong>', '</strong>')
    
    # 6. Add SEO footer block
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

# Test on one file
with open('blog/danang-hotels-rate-fencing-increase-revenue.html', 'r') as f:
    orig = f.read()
    
res = format_html(orig)
with open('test_output.html', 'w') as f:
    f.write(res)
print("Test completed.")
