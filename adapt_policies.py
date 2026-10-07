import re

def extract_main_policy(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract everything inside <div class="static-page-content">
    match = re.search(r'<div class="static-page-content">(.*?)</div>\s*<!--', html, re.DOTALL)
    if not match:
        match = re.search(r'<div class="static-page-content">(.*?)</div>\s*</main>', html, re.DOTALL)
    if not match:
        match = re.search(r'<div class="static-page-content">(.*?)</div>\s*(?:</main>|<!--)', html, re.DOTALL)
        
    if match:
        content = match.group(1).strip()
        # Remove any container divs
        return content
    return "<p>Content not found.</p>"

privacy_content = extract_main_policy('privacy.html')
refund_content = extract_main_policy('refund.html')

# We need to wrap them in the StayCRS layout
with open('staycrs-terms.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace the inner section
def replace_inner(template, title, inner_html):
    replacement = f"<h1 style='margin-bottom: 20px;'>{title}</h1>\n{inner_html}"
    # The staycrs-terms.html has <section class="wrap" ...> ... </section>
    new_html = re.sub(r'(<section class="wrap" style="padding: 40px 22px; max-width: 900px; min-height: 60vh;">).*?(</section>)', 
                      fr'\1\n{replacement}\n\2', template, flags=re.DOTALL)
    return new_html

# Style adjustments to match StayCRS (h2 -> h3, etc if needed, but actually standard tags are fine)
# Wait, the main site has <h2> and <h3>. The staycrs layout uses h2 and h3 natively.
# Let's just inject them directly.

privacy_html = replace_inner(template, "Privacy Policy", privacy_content)
refund_html = replace_inner(template, "Refund Policy", refund_content)

with open('staycrs-privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_html)
with open('staycrs-refund.html', 'w', encoding='utf-8') as f:
    f.write(refund_html)

print("Adapted policies successfully.")
