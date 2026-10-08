import re

def fix_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # TASK 1: PRICE (homepage)
    html = html.replace('start at USD 55 per month', 'USD 110/month, no setup fee')
    html = html.replace('starting at just $55/month', 'USD 110/month, no setup fee')
    html = html.replace('from USD 55/month', 'USD 110/month, no setup fee')
    html = html.replace('Enterprise-grade hotel software', 'Cloud PMS and real-time channel manager for independent hotels')
    # Link this card to /staycrs.html
    html = re.sub(r'<a href="services\.html#service-3" class="service-card"[^>]*>', 
                  '<a href="staycrs.html" class="service-card" data-i18n-target="href">', html)
    # Rename service card title
    html = html.replace('Enterprise-grade PMS &amp; Channel Manager', 'PMS &amp; Channel Manager by StayCRS')
    html = html.replace('Enterprise-grade PMS & Channel Manager', 'PMS & Channel Manager by StayCRS')
    # FAQ charges for PMS & Channel Manager
    html = html.replace('Our Property Management System (PMS) and Channel Manager services USD 110/month, no setup fee.', 'USD 110 per month, with no setup fee.')
    # Actually, previous replace might have made it 'Our Property Management System (PMS) and Channel Manager services USD 110/month, no setup fee.'
    # Let's clean it up:
    html = re.sub(r'Our Property Management System \(PMS\) and Channel Manager services.*?\.', 'USD 110 per month, with no setup fee.', html)

    # TASK 2: REVENUE MANAGEMENT FAQs (homepage)
    html = re.sub(r'We offer tailored pricing based on the size of your property, your specific needs, and the scope of services required\. Contact us for a customized proposal\.', 
                  'A fixed monthly fee based on the size of your hotel. We send a quote for each property. The fee is the same whether or not you use StayCRS.', html)
    html = re.sub(r'No, our revenue management service operates on a fixed monthly retainer\. We do not take a percentage of your revenue, ensuring your costs remain predictable\.', 
                  'No. It is a fixed monthly fee with no commission.', html)

    # TASK 3: CONTRACT FAQs (homepage)
    # Merge two contract FAQs into one: "Is there a minimum contract period, or can I cancel anytime?"
    # Find the FAQ block for "Is there a minimum contract period?"
    html = re.sub(r'We typically work with a minimum 6-month contract to ensure we have enough time to implement strategies and deliver measurable results\.', 
                  'Initial 3-month term, then cancel anytime with 30 days\' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing.', html)
    # Delete the old "structured lock-in period" wording / "can I cancel anytime" FAQ.
    # We need to find the specific FAQ block and remove it.
    html = re.sub(r'<div class="faq-item">.*?<h3[^>]*>Can I cancel the service if I\'m not satisfied\?</h3>.*?</div>\s*</div>', '</div>', html, flags=re.DOTALL)
    # Update question text:
    html = html.replace('Is there a minimum contract period?', 'Is there a minimum contract period, or can I cancel anytime?')

    # TASK 4: LOCATION WORDING (homepage)
    html = html.replace('Based in Bangkok', 'Registered in Hyderabad, India, with a Bangkok base to meet clients across the region.')
    html = re.sub(r'With on-ground teams in key markets, we understand local dynamics while applying global best practices\.', 
                  'Registered in Hyderabad, India, with a Bangkok base to meet clients across the region. Expertise across Thailand, Laos, India, Nepal, Malaysia and Vietnam.', html)

    # TASK 5: MARKET ORDER
    # The order: Thailand, Laos, India, Nepal, Malaysia, Vietnam
    html = re.sub(r'Thailand, India, Nepal, Malaysia, Laos, and Vietnam', 'Thailand, Laos, India, Nepal, Malaysia and Vietnam', html)
    html = re.sub(r'Thailand, India, Nepal, Malaysia, Laos and Vietnam', 'Thailand, Laos, India, Nepal, Malaysia and Vietnam', html)
    html = re.sub(r'Thailand, India, Nepal, Malaysia, Laos, Vietnam', 'Thailand, Laos, India, Nepal, Malaysia, Vietnam', html)
    # Let's check footer market order
    
    # TASK 6: HOURS
    html = re.sub(r'Available live from 8 a\.m\. to 11 p\.m\.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.', html)
    html = re.sub(r'Our core team is available Monday to Friday, 9:00 AM to 6:00 PM \(ICT\)\. However, we provide extended support for urgent issues and ongoing monitoring as needed\.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.', html)

    # TASK 7: NO FREE TRIAL
    html = html.replace('Request a demo or free trial', 'Request a demo')
    html = html.replace('Request a Demo or Free Trial', 'Request a demo')
    html = html.replace('or free trial', '')
    html = html.replace('or Free Trial', '')

    # TASK 11: PILLARS (homepage)
    html = html.replace('Reduced Costs', 'Results')
    html = re.sub(r'Outsourcing to CRS Central is significantly more cost-effective than hiring a full-time, in-house revenue manager—without compromising on expertise\.', 'Reduced costs: replace two full-time salaries with one expert team at a fraction of the price.', html)

    # TASK 12: SECTION LABELS (homepage)
    html = re.sub(r'<div class="eyebrow"[^>]*>Value Proposition Pillars</div>', '<div class="eyebrow" data-i18n="Why It Works">Why It Works</div>', html)
    html = re.sub(r'<div class="eyebrow"[^>]*>Revenue Calculator &amp; Audit</div>', '<div class="eyebrow" data-i18n="Revenue Calculator">Revenue Calculator</div>', html)
    html = re.sub(r'<div class="eyebrow"[^>]*>About Section</div>', '<div class="eyebrow" data-i18n="About Us">About Us</div>', html)
    html = re.sub(r'<div class="eyebrow"[^>]*>Service Highlights</div>', '<div class="eyebrow" data-i18n="Our Services">Our Services</div>', html)
    html = re.sub(r'<div class="eyebrow"[^>]*>Client Testimonial</div>', '<div class="eyebrow" data-i18n="Client Feedback">Client Feedback</div>', html)
    html = re.sub(r'<div class="eyebrow"[^>]*>Help Center</div>', '<div class="eyebrow" data-i18n="FAQs">FAQs</div>', html)
    html = re.sub(r'>Free Revenue Audit<', '>Free Audit<', html) # Wait, CTA button

    # TASK 13: FORMS
    # Will do below in common function

    # TASK 16: HOMEPAGE META DESCRIPTION
    html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Hotel revenue management for independent hotels across Thailand, Laos, India, Nepal, Malaysia and Vietnam. Dynamic pricing, OTA management and a free revenue audit.">', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

def fix_staycrs():
    with open('staycrs.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # TASK 3: Add the contract sentence under pricing section on staycrs.html
    # "Initial 3-month term, then cancel anytime with 30 days' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing."
    if 'Initial 3-month term' not in html:
        html = html.replace('<!-- Pricing Cards -->', '<p style="text-align: center; color: var(--text-white); opacity: 0.8; font-size: 0.9rem; margin-bottom: 2rem;">Initial 3-month term, then cancel anytime with 30 days\' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing.</p>\n<!-- Pricing Cards -->')

    # TASK 6: HOURS
    html = html.replace('Mon-Sun, 8:00 a.m.-7:00 p.m.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.')

    # TASK 8: EXPERIENCE WORDING
    html = html.replace('more than 17 years in luxury hospitality', 'decades in luxury hospitality')

    # TASK 9: TAX RECEIPTS
    html = html.replace('Issue invoices, receipts and tax receipts from the system', 'Issue invoices and receipts from the system.')

    # TASK 10: BOOKING ENGINE FEES
    if 'Payment gateway fees are charged separately by your bank or payment provider.' not in html:
        # Under Booking Engine pricing card
        html = re.sub(r'(<div class="pricing-card">.*?<h3[^>]*>Booking Engine</h3>.*?</div>)', 
                      r'\1\n<p style="font-size: 0.8rem; opacity: 0.7; text-align: center; margin-top: 10px;">Payment gateway fees are charged separately by your bank or payment provider.</p>', html, flags=re.DOTALL)
        # In the small print under the comparison table
        html = html.replace('We only charge the flat 8% fee on direct bookings.', 'We only charge the flat 8% fee on direct bookings. Payment gateway fees are charged separately by your bank or payment provider.')
        html = html.replace('No setup surprises', 'No setup fee.')

    # Add third pricing card: "Revenue Management. Fixed monthly fee based on your hotel's size. No commission. Request a quote." link #demo.
    if 'Revenue Management. Fixed monthly fee' not in html:
        new_card = """
        <div class="pricing-card">
            <h3>Revenue Management</h3>
            <div class="price">Quote</div>
            <p>Fixed monthly fee based on your hotel's size. No commission.</p>
            <a href="#demo" class="btn light">Request a quote</a>
        </div>
        """
        html = html.replace('</div>\n</div>\n\n<!-- Comparison Table -->', f'{new_card}\n</div>\n</div>\n\n<!-- Comparison Table -->')

    # TASK 13: FORMS
    # "Interested in" dropdown: add "Revenue Management"
    if 'value="Revenue Management"' not in html:
        html = html.replace('<option value="Booking Engine">Booking Engine</option>', '<option value="Booking Engine">Booking Engine</option>\n<option value="Revenue Management">Revenue Management</option>')

    # TASK 14: STAYCRS COPYRIGHT
    html = html.replace('© 2025 CRS Chauhan Private Limited.', '© 2026 StayCRS.')

    # TASK 15: CANONICAL
    html = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://crscentral.com/staycrs.html">', html)
    if '<link rel="canonical"' not in html:
        html = html.replace('</head>', '<link rel="canonical" href="https://crscentral.com/staycrs.html">\n</head>')
    
    html = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://crscentral.com/staycrs.html">', html)

    with open('staycrs.html', 'w', encoding='utf-8') as f:
        f.write(html)

def common_fixes():
    for filename in ['index.html', 'staycrs.html']:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        # TASK 5: MARKET ORDER (Nav Dropdown & Footer)
        # Find Nav items for markets
        markets_html = """
        <li><a href="thailand.html" class="dropdown-item" data-i18n="Thailand">Thailand</a></li>
        <li><a href="laos.html" class="dropdown-item" data-i18n="Laos">Laos</a></li>
        <li><a href="india.html" class="dropdown-item" data-i18n="India">India</a></li>
        <li><a href="nepal.html" class="dropdown-item" data-i18n="Nepal">Nepal</a></li>
        <li><a href="malaysia.html" class="dropdown-item" data-i18n="Malaysia">Malaysia</a></li>
        <li><a href="vietnam.html" class="dropdown-item" data-i18n="Vietnam">Vietnam</a></li>
        """
        # Replace existing dropdown list
        html = re.sub(r'<li><a href="thailand\.html".*?<li><a href="vietnam\.html"[^>]*>Vietnam</a></li>', markets_html.strip(), html, flags=re.DOTALL)
        
        # Replace Footer list
        footer_markets = """
        <li><a href="thailand.html" data-i18n="Thailand">Thailand</a></li>
        <li><a href="laos.html" data-i18n="Laos">Laos</a></li>
        <li><a href="india.html" data-i18n="India">India</a></li>
        <li><a href="nepal.html" data-i18n="Nepal">Nepal</a></li>
        <li><a href="malaysia.html" data-i18n="Malaysia">Malaysia</a></li>
        <li><a href="vietnam.html" data-i18n="Vietnam">Vietnam</a></li>
        """
        html = re.sub(r'<li><a href="thailand\.html" data-i18n="Thailand">Thailand</a></li>.*?<li><a href="vietnam\.html" data-i18n="Vietnam">Vietnam</a></li>', footer_markets.strip(), html, flags=re.DOTALL)

        # TASK 13: FORMS
        # Add a required "Country" dropdown
        country_dropdown = """
        <div class="form-group">
            <label data-i18n="Country">Country</label>
            <select name="Country" class="form-input" required>
                <option value="" disabled selected data-i18n="Select Country">Select Country</option>
                <option value="Thailand" data-i18n="Thailand">Thailand</option>
                <option value="Laos" data-i18n="Laos">Laos</option>
                <option value="India" data-i18n="India">India</option>
                <option value="Nepal" data-i18n="Nepal">Nepal</option>
                <option value="Malaysia" data-i18n="Malaysia">Malaysia</option>
                <option value="Vietnam" data-i18n="Vietnam">Vietnam</option>
                <option value="Other" data-i18n="Other">Other</option>
            </select>
        </div>
        """
        
        # Insert Country dropdown before Hotel Name or Message if it doesn't exist
        if 'name="Country"' not in html:
            html = html.replace('<div class="form-group">\n<label data-i18n="Hotel Name">', f'{country_dropdown}\n<div class="form-group">\n<label data-i18n="Hotel Name">')
            html = html.replace('<div class="form-group">\n            <label data-i18n="Hotel Name">', f'{country_dropdown}\n<div class="form-group">\n            <label data-i18n="Hotel Name">')
            html = html.replace('<div class="form-group">\n              <label data-i18n="Hotel Name">', f'{country_dropdown}\n<div class="form-group">\n              <label data-i18n="Hotel Name">')

        # Add a required checkbox above the submit button
        privacy_checkbox = """
        <div class="form-group" style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
            <input type="checkbox" name="Privacy_Consent" id="privacyConsent" required style="width: auto;">
            <label for="privacyConsent" style="margin: 0; font-size: 0.9rem;" data-i18n="I agree to the Privacy Policy">I agree to the <a href="privacy.html" style="color: var(--c1); text-decoration: underline;" target="_blank">Privacy Policy</a></label>
        </div>
        """
        if 'name="Privacy_Consent"' not in html:
            html = re.sub(r'(<button type="submit"[^>]*>)', rf'{privacy_checkbox}\n\1', html)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

fix_index()
fix_staycrs()
common_fixes()
print("Done")
