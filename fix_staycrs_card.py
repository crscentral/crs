import re

with open('staycrs.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_card = """
<div class="card">
  <h3>Revenue Management</h3>
  <div class="big8">Quote</div>
  <p style="margin-top:8px">Fixed monthly fee based on your hotel's size. No commission.</p>
  <a href="#demo" class="btn light" style="margin-top: 15px; display: inline-block;">Request a quote</a>
</div>
"""
if 'Quote</div>' not in html:
    html = html.replace('Pay only when you earn.</p></div>\n</div>\n<a class="btn"', f'Pay only when you earn.</p></div>\n{new_card}\n</div>\n<a class="btn"')

with open('staycrs.html', 'w', encoding='utf-8') as f:
    f.write(html)
