import re

def fix_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. PRICE (homepage)
    # Service card
    html = html.replace('Enterprise-grade PMS &amp; Channel Manager', 'PMS &amp; Channel Manager by StayCRS')
    html = html.replace('Enterprise-grade hotel software starting at just $55/month. Cloud PMS and real-time channel manager with no setup fee.', 'Cloud PMS and real-time channel manager for independent hotels. USD 110/month, no setup fee.')
    # Link
    html = re.sub(r'<a class="service-card" href="services\.html#service-3"', '<a class="service-card" href="staycrs.html"', html)
    
    # FAQ charges for PMS
    html = html.replace('Our Property Management System (PMS) and Channel Manager services start at USD 55 per month.', 'USD 110 per month, with no setup fee.')

    # 2. REVENUE MANAGEMENT FAQs (homepage)
    html = html.replace('We offer tailored pricing based on the size of your property, your specific needs, and the scope of services required. Contact us for a customized proposal.', 'A fixed monthly fee based on the size of your hotel. We send a quote for each property. The fee is the same whether or not you use StayCRS.')
    html = html.replace('No, our revenue management service operates on a fixed monthly retainer. We do not take a percentage of your revenue, ensuring your costs remain predictable.', 'No. It is a fixed monthly fee with no commission.')

    # 3. CONTRACT FAQs (homepage)
    # Target "Is there a minimum contract period?" question text
    html = html.replace('Is there a minimum contract period?', 'Is there a minimum contract period, or can I cancel anytime?')
    # Replace the answer
    html = html.replace('Our engagement terms are discussed individually based on your property\'s needs and goals. We offer flexible arrangements with a structured lock-in period as outlined in our service agreements.', 'Initial 3-month term, then cancel anytime with 30 days\' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing.')
    # Remove the second FAQ block (Can I cancel anytime)
    # It looks like:
    # <div class="faq-item">
    # <div class="faq-question" data-i18n="Can I cancel the service if I'm not satisfied?">Can I cancel the service if I'm not satisfied?</div>
    # ...
    # </div>
    html = re.sub(r'<div class="faq-item">\s*<div class="faq-question"[^>]*>Can I cancel the service if I\'m not satisfied\?</div>.*?</div>\s*</div>', '</div>', html, flags=re.DOTALL)

    # 4. LOCATION WORDING (homepage)
    html = html.replace('Based in Bangkok, with on-ground teams and local expertise across Thailand, Laos, India, Nepal, Malaysia, and Vietnam.', 'Registered in Hyderabad, India, with a Bangkok base to meet clients across the region. Expertise across Thailand, Laos, India, Nepal, Malaysia and Vietnam.')
    
    # Check if 'Based in Bangkok' exists elsewhere
    html = html.replace('Based in Bangkok', 'Registered in Hyderabad, India, with a Bangkok base to meet clients across the region.')

    # 5. MARKET ORDER (common later)
    
    # 6. HOURS
    html = html.replace('Available live from 8 a.m. to 11 p.m.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.')
    html = html.replace('Our core team is available Monday to Friday, 9:00 AM to 6:00 PM (ICT). However, we provide extended support for urgent issues and ongoing monitoring as needed.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.')

    # 7. NO FREE TRIAL
    html = html.replace('Request a Demo or Free Trial', 'Request a demo')
    html = html.replace('Request a demo or free trial', 'Request a demo')
    # Let's replace lowercase too just in case
    html = re.sub(r'(?i)or free trial', '', html)

    # 11. PILLARS (homepage)
    html = html.replace('>Reduced Costs<', '>Results<')
    html = html.replace('Outsourcing to CRS Central is significantly more cost-effective than hiring a full-time, in-house revenue manager—without compromising on expertise.', 'Reduced costs: replace two full-time salaries with one expert team at a fraction of the price.')

    # 12. SECTION LABELS (homepage)
    html = html.replace('>Value Proposition Pillars<', '>Why It Works<')
    html = html.replace('>Revenue Calculator &amp; Audit<', '>Revenue Calculator<')
    html = html.replace('>Revenue Calculator & Audit<', '>Revenue Calculator<')
    html = html.replace('>About Section<', '>About Us<')
    html = html.replace('>Service Highlights<', '>Our Services<')
    html = html.replace('>Client Testimonial<', '>Client Feedback<')
    html = html.replace('>Help Center<', '>FAQs<')
    html = html.replace('>Free Revenue Audit CTA<', '>Free Audit<')
    html = html.replace('>Free Revenue Audit<', '>Free Audit<') # the CTA button if labeled that way? Wait, "Free Revenue Audit CTA" eyebrow.
    
    # Note on 12: "Free Revenue Audit CTA -> Free Audit" might be an eyebrow. Let's make sure it's the eyebrow.
    # We will do a generic replacement for the eyebrow
    
    # 16. HOMEPAGE META DESCRIPTION
    html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Hotel revenue management for independent hotels across Thailand, Laos, India, Nepal, Malaysia and Vietnam. Dynamic pricing, OTA management and a free revenue audit.">', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def fix_staycrs():
    with open('staycrs.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 3. Add contract sentence under pricing section
    if 'Initial 3-month term' not in html:
        html = html.replace('<!-- Pricing Cards -->', '<p style="text-align: center; color: var(--text-white); opacity: 0.8; font-size: 0.9rem; margin-bottom: 2rem;">Initial 3-month term, then cancel anytime with 30 days\' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing.</p>\n<!-- Pricing Cards -->')

    # 6. HOURS
    html = html.replace('Mon-Sun, 8:00 a.m.-7:00 p.m.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.')

    # 7. NO FREE TRIAL
    html = html.replace('Request a Demo or Free Trial', 'Request a demo')
    html = html.replace('Request a demo or free trial', 'Request a demo')
    html = re.sub(r'(?i)or free trial', '', html)

    # 8. EXPERIENCE WORDING
    html = html.replace('more than 17 years in luxury hospitality', 'decades in luxury hospitality')

    # 9. TAX RECEIPTS
    html = html.replace('Issue invoices, receipts and tax receipts from the system', 'Issue invoices and receipts from the system.')

    # 10. BOOKING ENGINE FEES
    html = html.replace('We only charge the flat 8% fee on direct bookings.', 'We only charge the flat 8% fee on direct bookings. Payment gateway fees are charged separately by your bank or payment provider.')
    html = html.replace('No setup surprises', 'No setup fee.')

    # Add Gateway fee under Booking engine card
    be_card_pattern = r'(<div class="pricing-card">.*?<h3>Booking Engine</h3>.*?</div>)'
    be_replacement = r'\1\n<p style="font-size: 0.8rem; opacity: 0.7; text-align: center; margin-top: 10px;">Payment gateway fees are charged separately by your bank or payment provider.</p>'
    html = re.sub(be_card_pattern, be_replacement, html, flags=re.DOTALL)

    # Add third pricing card
    if 'Revenue Management' not in html[html.find('<!-- Pricing Cards -->'):html.find('<!-- Comparison Table -->')]:
        new_card = """
        <div class="pricing-card">
            <h3>Revenue Management</h3>
            <div class="price">Quote</div>
            <p>Fixed monthly fee based on your hotel's size. No commission.</p>
            <a href="#demo" class="btn light">Request a quote</a>
        </div>
        """
        html = html.replace('</div>\n</div>\n\n<!-- Comparison Table -->', f'{new_card}\n</div>\n</div>\n\n<!-- Comparison Table -->')

    # 13. FORMS - "Interested in" dropdown: add "Revenue Management"
    if 'value="Revenue Management"' not in html:
        html = html.replace('<option value="Booking Engine">Booking Engine</option>', '<option value="Booking Engine">Booking Engine</option>\n<option value="Revenue Management">Revenue Management</option>')

    # 14. STAYCRS COPYRIGHT
    html = html.replace('© 2025 CRS Chauhan Private Limited.', '© 2026 StayCRS.')

    # 15. CANONICAL
    if '<link rel="canonical"' not in html:
        html = html.replace('</head>', '<link rel="canonical" href="https://crscentral.com/staycrs.html">\n</head>')
    else:
        html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://crscentral.com/staycrs.html">', html)
    
    html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://crscentral.com/staycrs.html">', html)

    with open('staycrs.html', 'w', encoding='utf-8') as f:
        f.write(html)

def common_fixes():
    for filename in ['index.html', 'staycrs.html']:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        # 5. MARKET ORDER
        old_markets = ['Thailand, India, Nepal, Malaysia, Laos, and Vietnam',
                       'Thailand, India, Nepal, Malaysia, Laos and Vietnam',
                       'Thailand, India, Nepal, Malaysia, Laos, Vietnam']
        for om in old_markets:
            html = html.replace(om, 'Thailand, Laos, India, Nepal, Malaysia and Vietnam')

        # Dropdowns and footers:
        # We need to correctly reorder the existing <li> items for countries.
        # Find all country lists and manually replace.
        nav_pattern = r'(<li><a href="thailand\.html".*?</li>)\s*(<li><a href="india\.html".*?</li>)\s*(<li><a href="nepal\.html".*?</li>)\s*(<li><a href="malaysia\.html".*?</li>)\s*(<li><a href="laos\.html".*?</li>)\s*(<li><a href="vietnam\.html".*?</li>)'
        nav_repl = r'\1\n\5\n\2\n\3\n\4\n\6'
        html = re.sub(nav_pattern, nav_repl, html, flags=re.DOTALL)

        # 13. FORMS
        # Find the form and inject Country dropdown
        country_dropdown = """
<div class="form-group">
  <label>Country</label>
  <select name="Country" class="form-input" required>
    <option value="" disabled selected>Select Country</option>
    <option value="Thailand">Thailand</option>
    <option value="Laos">Laos</option>
    <option value="India">India</option>
    <option value="Nepal">Nepal</option>
    <option value="Malaysia">Malaysia</option>
    <option value="Vietnam">Vietnam</option>
    <option value="Other">Other</option>
  </select>
</div>
"""
        # Inject before Hotel Name
        if 'name="Country"' not in html:
            html = re.sub(r'(<div class="form-group">\s*<label[^>]*>Hotel Name)', rf'{country_dropdown}\n\1', html)

        # Inject consent before submit button
        consent_html = """
<div class="form-group" style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
  <input type="checkbox" name="Privacy_Consent" id="privacyConsent" required style="width: auto;">
  <label for="privacyConsent" style="margin: 0; font-size: 0.9rem;">I agree to the <a href="privacy.html" style="color: var(--c1); text-decoration: underline;" target="_blank">Privacy Policy</a></label>
</div>
"""
        if 'name="Privacy_Consent"' not in html:
            html = re.sub(r'(<button type="submit"[^>]*>)', rf'{consent_html}\n\1', html)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

fix_index()
fix_staycrs()
common_fixes()
print("Applied precise fixes.")
