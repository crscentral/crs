import re

with open('staycrs-terms.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace the content section with a placeholder
placeholder_content = """<h1 style='margin-bottom: 20px;'>{title}</h1>
<p style='margin-bottom: 10px;'>This policy document could not be loaded from the previous upload. Please provide the text for this policy.</p>"""

privacy_html = re.sub(r'<section class="wrap".*?</section>', 
                      f'<section class="wrap" style="padding: 40px 22px; max-width: 900px; min-height: 60vh;">\n{placeholder_content.format(title="Privacy Policy")}\n</section>', 
                      template, flags=re.DOTALL)

refund_html = re.sub(r'<section class="wrap".*?</section>', 
                     f'<section class="wrap" style="padding: 40px 22px; max-width: 900px; min-height: 60vh;">\n{placeholder_content.format(title="Refund Policy")}\n</section>', 
                     template, flags=re.DOTALL)

with open('staycrs-privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_html)
    
with open('staycrs-refund.html', 'w', encoding='utf-8') as f:
    f.write(refund_html)

print("Created placeholders.")
