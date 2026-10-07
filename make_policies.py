import re

terms_text = """
Terms and Conditions
StayCRS  |  PMS, Channel Manager and Booking Engine
Last updated: 7 October 2026
Applies to: stay.crscentral.com and crscentral.com/staycrs.html
Operated by: CRS CHAUHAN Private Limited, trading as StayCRS and CRS Central (CIN U70200TS2025PTC206971), No. 4-59/1/308 BLK-A, SS Anurag New Town Pearl, Thumkunta, Hyderabad 500078, Telangana, India. Email: info@crscentral.com
1.  ABOUT THESE TERMS
1.1	These Terms and Conditions ("Terms") govern your use of the StayCRS website and your relationship with StayCRS before you sign a service agreement. StayCRS is a brand of CRS CHAUHAN Private Limited ("StayCRS", "we", "us"). By using the website you accept these Terms. If you do not accept them, please do not use the website.
1.2	StayCRS offers a cloud PMS, Channel Manager and Booking Engine for hotels. The Platform is licensed to us by a third-party technology provider and resold under the StayCRS brand. We do not claim to own or to have developed the underlying software.
2.  SERVICES AND CLIENT AGREEMENTS
2.1	The website describes our services. It is not an offer capable of acceptance. We provide services only under a signed Hotel Technology Services Agreement (the "Client Agreement") with the hotel. If these Terms conflict with a signed Client Agreement, the Client Agreement prevails.
2.2	Services are available only for hotels and similar properties located in India, Nepal, Vietnam, Laos, Malaysia or Thailand. We may decline any request for any lawful reason.
2.3	Features, availability and integrations vary. Descriptions on the website are general and are not a guarantee of any feature, uptime, OTA connection, revenue, occupancy or booking result. Only the Client Agreement creates binding commitments.
3.  PRICING
3.1	Prices shown on the website (including USD 110 per month for PMS plus Channel Manager, and 8% of the booking value of completed stays booked through the Booking Engine) are guides. They exclude GST, VAT and similar taxes, bank and currency charges, and any third-party fees (for example for connecting to a third-party PMS). The Order Form in your Client Agreement states the fees that apply.
3.2	The OTA commission comparison on the website is illustrative. Actual commissions vary by channel and agreement.
4.  DEMO REQUESTS AND CONTACT
4.1	When you send a demo or quote request, you must give accurate information and be authorised to act for your hotel. We use your details as described in our Privacy and Data Protection Policy. A demo request does not create a contract or any obligation to pay.
5.  ACCEPTABLE USE
5.1	You must not: misuse or attempt to gain unauthorised access to the website or any system; copy, scrape or reproduce the website or any demonstration of the Platform; send malicious code; use the website unlawfully; or use any demo or documentation to build or train a competing product or AI model.
6.  INTELLECTUAL PROPERTY
6.1	The StayCRS and CRS Central names, logos, text, graphics and website design belong to CRS CHAUHAN Private Limited. The Platform and its documentation belong to the technology provider and its licensors. You receive no rights in them except to view the website for your own business evaluation.
7.  THIRD-PARTY SERVICES AND LINKS
7.1	The website may link to third-party sites, including OTAs, WhatsApp, LINE and social media. We do not control them and are not responsible for their content, availability or policies.
8.  DISCLAIMERS AND LIABILITY
8.1	The website is provided "as is". We do not warrant that it will be uninterrupted or error-free, or that its content is complete or current.
8.2	To the fullest extent the law allows, we are not liable for any indirect or consequential loss, or any loss of profit, revenue, bookings, goodwill or data, arising from use of the website. Our total liability for any claim arising from use of the website is limited to INR 5,000. Nothing limits liability that cannot lawfully be limited.
9.  RELATED POLICIES
9.1	Please also read our Privacy and Data Protection Policy, Refund Policy and Cancellation Policy, which form part of these Terms.
10.  CHANGES
10.1	We may update these Terms by posting a new version with a new "last updated" date. Continued use of the website means you accept the update. Changes do not alter a signed Client Agreement.
11.  GOVERNING LAW AND DISPUTES
11.1	These Terms are governed by the laws of India. Disputes go first to good-faith discussion for 30 days, then to the courts at Hyderabad, Telangana, which have exclusive jurisdiction. We may seek urgent relief in any court. Mandatory consumer or other laws of your country that cannot be excluded still apply.
12.  CONTACT
12.1	CRS CHAUHAN Private Limited (StayCRS), No. 4-59/1/308 BLK-A, SS Anurag New Town Pearl, Thumkunta, Hyderabad 500078, Telangana, India. Email: info@crscentral.com. WhatsApp: +66 99 014 3142.
"""

cancellation_text = """
Cancellation Policy
StayCRS  |  PMS, Channel Manager and Booking Engine
Last updated: 7 October 2026
Applies to: stay.crscentral.com and crscentral.com/staycrs.html
Operated by: CRS CHAUHAN Private Limited, trading as StayCRS and CRS Central (CIN U70200TS2025PTC206971), No. 4-59/1/308 BLK-A, SS Anurag New Town Pearl, Thumkunta, Hyderabad 500078, Telangana, India. Email: info@crscentral.com
1.  ABOUT THIS POLICY
1.1	This policy explains how a hotel can cancel its StayCRS services, and what happens to hotel guest bookings made through the Booking Engine. It applies together with the signed Hotel Technology Services Agreement ("Client Agreement"), which prevails if they conflict.
2.  CANCELLING YOUR SERVICE
2.1	Initial term. The Client Agreement has an initial term (stated in your Order Form, normally 12 months) that starts on the date your account is created. It renews automatically for successive 12-month periods unless either party gives at least 75 days' written notice before the current term ends.
2.2	Notice. To cancel, email info@crscentral.com with the subject "Cancellation" and the hotel name, giving at least 60 days' written notice. The cancellation takes effect no earlier than the end of the initial term. We will confirm receipt within 2 Business Days.
2.3	Fees during notice. Fees continue to be charged until the end of the notice period. There is no pro-rata refund for unused time.
2.4	Early termination. If the hotel ends the service before the end of the initial term, other than because of our uncured material breach, it pays its average monthly fees over the previous 3 months multiplied by the months remaining in the initial term.
2.5	Property closed or sold. Closure or sale of the property is a cancellation and requires notice. The hotel remains responsible until the end of the initial term, unless the buyer takes over the Client Agreement and we agree in writing.
3.  CANCELLATION BY STAYCRS
3.1	We may suspend or cancel the service where the Client Agreement allows, including for non-payment (suspension after 7 days overdue on 5 days' notice, termination at 30 days overdue), breach, unlawful use, security or compliance concerns, or where an OTA, bank, our technology provider or the law requires it.
3.2	If our arrangement with our technology provider ends, we will give as much notice as we can. Service may continue for a transition period of up to 90 days, and we will help the hotel migrate. If service ends with no replacement available, prepaid fees for the period afterwards are refunded (see the Refund Policy).
4.  WHAT HAPPENS WHEN SERVICE ENDS
4.1	Access to the Platform ends on the effective date, and unpaid fees become due at once.
4.2	Data. If the hotel asks within 15 days after termination, and all amounts due are paid, we will arrange export of its data in CSV or Excel format. After that the data may be deleted, subject to the retention periods in our Privacy and Data Protection Policy. Card data is deleted one month after check-out and is not available for export.
4.3	The hotel should switch off OTA connections and update its own website, and should close or reassign any inventory before the end date. We are not responsible for bookings made after the service ends.
5.  HOTEL GUEST BOOKINGS MADE THROUGH THE BOOKING ENGINE
5.1	Each hotel sets its own rate plans and cancellation terms, which are shown to guests at booking. StayCRS is not a party to the stay.
5.2	Amendments and cancellations. Guests amend or cancel through the Booking Engine site. If a hotel receives an amendment or cancellation request for a Booking Engine reservation in any other way, it must notify StayCRS in writing within 24 hours. The Booking Engine fee applies only to completed stays, so cancelled bookings and no-shows are not charged. Amendments affecting commission need approval and the hotel's internal records alone are not proof.
5.3	Refunds to guests are the hotel's responsibility. Deposits collected online for cancelled bookings are handled under the Platform rules.
6.  WITHDRAWING BEFORE SIGNING
6.1	Before a Client Agreement is signed, a hotel may stop at any time at no cost. A demo or enquiry does not oblige you to continue.
7.  CONTACT
7.1	CRS CHAUHAN Private Limited (StayCRS), Hyderabad, India. Email: info@crscentral.com.
"""

def text_to_html(text):
    lines = text.strip().split('\n')
    title = lines[0]
    html_lines = []
    html_lines.append(f"<h1 style='margin-bottom: 20px;'>{title}</h1>")
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        # Check if it's a heading (like "1. ABOUT THESE TERMS")
        if re.match(r'^\d+\.\s+[A-Z\s]+$', line):
            html_lines.append(f"<h3 style='margin-top: 30px; margin-bottom: 15px;'>{line}</h3>")
        else:
            html_lines.append(f"<p style='margin-bottom: 10px;'>{line}</p>")
    
    return "\n".join(html_lines)

# Read the layout from staycrs.html
with open('staycrs.html', 'r', encoding='utf-8') as f:
    staycrs = f.read()

# Extract header (up to </header>) and footer (from <footer>)
header_match = re.search(r'(.*?</header>)', staycrs, re.DOTALL)
footer_match = re.search(r'(<footer.*)', staycrs, re.DOTALL)

header = header_match.group(1)
footer = footer_match.group(1)

# Generate HTML pages
pages = {
    'staycrs-terms.html': terms_text,
    'staycrs-cancellation.html': cancellation_text,
}

for filename, text in pages.items():
    content = text_to_html(text)
    
    # Assemble
    full_html = f"""{header}
<section class="wrap" style="padding: 40px 22px; max-width: 900px; min-height: 60vh;">
{content}
</section>
{footer}"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {filename}")

# Update links in staycrs.html
staycrs = staycrs.replace(
    '<a style="display:inline;margin-right:16px" href="https://crscentral.com" target="_blank" rel="noopener">Terms &amp; Conditions</a>',
    '<a style="display:inline;margin-right:16px" href="staycrs-terms.html">Terms &amp; Conditions</a>'
)
staycrs = staycrs.replace(
    '<a style="display:inline;margin-right:16px" href="https://crscentral.com" target="_blank" rel="noopener">Privacy Policy</a>',
    '<a style="display:inline;margin-right:16px" href="staycrs-privacy.html">Privacy Policy</a>'
)
staycrs = staycrs.replace(
    '<a style="display:inline;margin-right:16px" href="https://crscentral.com" target="_blank" rel="noopener">Refund Policy</a>',
    '<a style="display:inline;margin-right:16px" href="staycrs-refund.html">Refund Policy</a>'
)
staycrs = staycrs.replace(
    '<a style="display:inline" href="https://crscentral.com" target="_blank" rel="noopener">Cancellation Policy</a>',
    '<a style="display:inline" href="staycrs-cancellation.html">Cancellation Policy</a>'
)

with open('staycrs.html', 'w', encoding='utf-8') as f:
    f.write(staycrs)
print("Updated staycrs.html links")
