import re

with open('staycrs.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Payment gateway text
if 'Payment gateway fees are charged separately' not in html:
    html = re.sub(r'(<div class="card"><h3[^>]*>Booking Engine</h3>.*?</div>)', 
                  r'\1\n<p style="font-size: 0.8rem; opacity: 0.7; text-align: center; margin-top: 10px;">Payment gateway fees are charged separately by your bank or payment provider.</p>', html, flags=re.DOTALL)
    
    html = html.replace('We only charge the flat 8% fee on direct bookings.', 'We only charge the flat 8% fee on direct bookings. Payment gateway fees are charged separately by your bank or payment provider.')

# Add 3rd Pricing Card "Revenue Management"
if 'Quote' not in html:
    new_card = """
<div class="card">
  <h3>Revenue Management</h3>
  <div class="big8">Quote</div>
  <p style="margin-top:8px">Fixed monthly fee based on your hotel's size. No commission.</p>
  <a href="#demo" class="btn light" style="margin-top: 15px; display: inline-block;">Request a quote</a>
</div>
"""
    # Replace grid g3 layout to include new card
    grid_end = '</div>\n\n<!-- Comparison Table -->'
    html = html.replace('</div>\n</div>\n\n<!-- Comparison Table -->', f'{new_card}\n</div>\n</div>\n\n<!-- Comparison Table -->')
    html = html.replace('</div>\n\n<!-- Comparison Table -->', f'{new_card}\n</div>\n\n<!-- Comparison Table -->')

# Add 3-month contract sentence
if 'Initial 3-month term' not in html:
    html = html.replace('<div class="grid g3" style="grid-template-columns:1fr 1fr">', 
                        '<p style="text-align: center; color: var(--text-white); opacity: 0.8; font-size: 0.9rem; margin-bottom: 2rem;">Initial 3-month term, then cancel anytime with 30 days\' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing.</p>\n<div class="grid g3" style="grid-template-columns:1fr 1fr">')

with open('staycrs.html', 'w', encoding='utf-8') as f:
    f.write(html)
