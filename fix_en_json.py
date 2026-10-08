import json

with open('assets/locales/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

# Apply rules to values
for key, val in en.items():
    if isinstance(val, str):
        # 1. Price
        val = val.replace('$55', 'USD 110')
        val = val.replace('USD 55', 'USD 110')
        val = val.replace('Enterprise-grade hotel software starting at just USD 110/month. Cloud PMS and real-time channel manager with no setup fee.', 'Cloud PMS and real-time channel manager for independent hotels. USD 110/month, no setup fee.')
        val = val.replace('Our Property Management System (PMS) and Channel Manager services start at USD 110 per month.', 'USD 110 per month, with no setup fee.')
        
        # 2. Revenue Management FAQ
        if key == "What are the charges for Hotel Revenue Management?":
            pass # The key is the question, value is answer. We don't change the key here unless it's in the value too.
        val = val.replace('Our engagement terms are discussed individually based on your property\'s needs and goals. We offer flexible arrangements with a structured lock-in period as outlined in our service agreements.', "Initial 3-month term, then cancel anytime with 30 days' written notice. This applies to all services: Revenue Management, StayCRS and Digital Marketing.")
        val = val.replace('Our revenue management services are customized based on the size, complexity, and specific needs of your property. Contact us for a personalized proposal.', 'A fixed monthly fee based on the size of your hotel. We send a quote for each property. The fee is the same whether or not you use StayCRS.')
        val = val.replace('In addition to our management fee, standard commissions apply for bookings made through third-party channels (OTAs). However, we focus heavily on driving direct bookings to minimize these costs and maximize your net revenue.', 'No. It is a fixed monthly fee with no commission.')
        
        # Location
        val = val.replace('Based in Bangkok, with on-ground teams and local expertise', 'Registered in Hyderabad, India, with a Bangkok base to meet clients across the region. Expertise')
        val = val.replace('Based in Bangkok', 'Registered in Hyderabad, India, with a Bangkok base')
        val = val.replace("We're Based in Bangkok, Close to Our Clients", "Registered in Hyderabad, India, with a Bangkok base to meet clients across the region.")
        val = val.replace('We are based in Bangkok solely for convenient travel', 'We are registered in Hyderabad, India, with a Bangkok base solely for convenient travel')
        val = val.replace('Being based in Bangkok gives us', 'Being registered in Hyderabad, India, with a Bangkok base gives us')
        
        # Nav and Headers
        val = val.replace('Free Revenue Audit CTA', 'Free Audit')
        val = val.replace('Value Proposition Pillars', 'Why It Works')
        val = val.replace('Revenue Calculator & Audit', 'Revenue Calculator')
        val = val.replace('About Section', 'About Us')
        val = val.replace('Service Highlights', 'Our Services')
        val = val.replace('Client Testimonial', 'Client Feedback')
        val = val.replace('Help Center', 'FAQs')
        if val == 'Free Revenue Audit':
            val = 'Free Audit'
        
        # Hours
        val = val.replace('Available live from 8 a.m. to 11 p.m.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.')
        val = val.replace('Mon-Sun, 8:00 a.m.-7:00 p.m.', 'Daily 8am–7pm ICT (UTC+7). WhatsApp support until 11pm ICT.')
        
        # Free trial
        val = val.replace('Request a demo or free trial', 'Request a demo')
        
        # StayCRS
        val = val.replace('more than 17 years', 'decades')
        val = val.replace('Issue invoices, receipts and tax receipts from the system.', 'Issue invoices and receipts from the system.')
        val = val.replace('No setup surprises. Pick what you need.', 'No setup fee. Pick what you need.')

        # Market Order
        val = val.replace('Thailand, Laos, Vietnam, Malaysia and India', 'Thailand, Laos, India, Nepal, Malaysia and Vietnam')
        
        en[key] = val

# Also, since I changed the `data-i18n` attributes in HTML, those NEW keys are now queried!
# I must add the NEW keys into en.json so it finds them, or just let them fallback. 
# But wait, if they fallback to the HTML, that's fine. But for existing keys, we must update them.

with open('assets/locales/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, indent=2, ensure_ascii=False)

print("Updated en.json")
