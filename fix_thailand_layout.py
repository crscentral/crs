import re
import os

with open('thailand.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Expand Hero Width and fix button wrapping
content = re.sub(
    r'<div class="hero-content" style="text-align: center; max-width: 850px; margin: 0 auto;">',
    r'<div class="hero-content" style="text-align: center; max-width: 1100px; margin: 0 auto;">',
    content
)

content = re.sub(
    r'<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin-top: 1rem;">',
    r'<style>\n  @media (min-width: 768px) {\n    .market-buttons { flex-wrap: nowrap !important; }\n  }\n  .float-img-right { float: right; width: 45%; max-width: 450px; margin: 0 0 1.5rem 2rem; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); }\n  .float-img-left { float: left; width: 45%; max-width: 450px; margin: 0 2rem 1.5rem 0; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); }\n  @media (max-width: 768px) {\n    .float-img-right, .float-img-left { float: none; width: 100%; max-width: 100%; margin: 1rem 0; }\n  }\n</style>\n<div class="market-buttons" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin-top: 1rem;">',
    content
)

# 2. Refactor Sections to use floating images
def create_floating_section(section_id, title_id, title_text, img_src, img_alt, is_light, is_reverse, content_html, extra_img_src=None):
    bg_class = " section-light" if is_light else ""
    
    img_tag_1 = f'<img src="{img_src}" alt="{img_alt}" class="float-img-{"left" if is_reverse else "right"}" loading="lazy" onerror="this.style.display=\'none\'">'
    img_tag_2 = f'<img src="{extra_img_src}" alt="Secondary image" class="float-img-left" loading="lazy" onerror="this.style.display=\'none\'">' if extra_img_src else ''
    
    return f"""<section id="{section_id}" class="section{bg_class}">
    <div class="section-container" style="display: block; overflow: hidden;">
      {img_tag_1}
      {img_tag_2}
      <h2 class="section-title" style="font-size: 1.8rem; margin-top: 0;" data-i18n="{title_id}">{title_text}</h2>
{content_html}
    </div>
  </section>"""

# Replace Bangkok
bkk_content = """      <p>Bangkok is a year-round hotel market. Business travellers, meetings and events, medical visitors, transit stays and city-break tourists all fill rooms, from Sukhumvit and Silom to the riverside and Old City. With thousands of rooms competing in every price band, the hotels that win are the ones that price with discipline.</p>
      <h3 style="margin-top: 1.5rem;">Why Bangkok Hotels Need Revenue Management Now</h3>
      <ul class="bullet-list" style="margin-bottom: 1.5rem;">
        <li><strong>Flat Weekday and Weekend Pricing:</strong> Rates do not reflect the very different demand on corporate weekdays and leisure weekends.</li>
        <li><strong>Crowded Competitive Sets:</strong> Hundreds of similar properties within a few streets make rate position and OTA ranking critical.</li>
        <li><strong>OTA Dependency:</strong> Most bookings arrive through a handful of OTAs, creating heavy commission costs and little direct revenue.</li>
        <li><strong>Untapped Segments:</strong> Corporate accounts, long-stay guests, event and meeting groups and medical visitors are present in Bangkok but rarely targeted strategically.</li>
      </ul>
      <h3 style="margin-top: 1.5rem;">What CRS Central Does for Bangkok Hotels</h3>
      <ul class="bullet-list">
        <li><strong>Dynamic Pricing by Day and Segment:</strong> Rate structures that respond to weekday corporate demand, weekend leisure, events and competitor moves.</li>
        <li><strong>Competitive Set Monitoring:</strong> Clear rate positioning against the properties your guests actually compare you with.</li>
        <li><strong>OTA Performance Improvement:</strong> Better content, smarter promotions and stronger conversion on Agoda, Booking.com, Trip.com and Expedia.</li>
        <li><strong>Corporate and Long-Stay Strategy:</strong> Pricing and packages for negotiated accounts, extended stays and small groups.</li>
        <li><strong>Direct Booking Growth:</strong> Reducing OTA commission dependency through your website, phone, LINE and WhatsApp enquiries.</li>
      </ul>"""

# Replace Hua Hin
hh_content = """      <p>Hua Hin is a classic seaside resort town within easy reach of Bangkok. Its demand is shaped by weekend and holiday visitors from the capital, golf, family travel and wellness stays, plus guests who spend extended periods in the cool season. That makes demand highly uneven across the week and the year.</p>
      <h3 style="margin-top: 1.5rem;">Why Hua Hin Hotels Need Revenue Management Now</h3>
      <ul class="bullet-list" style="margin-bottom: 1.5rem;">
        <li><strong>Weekend Peaks and Midweek Gaps:</strong> Rooms sell out at weekends and public holidays while midweek stays empty, often leading to broad discounting.</li>
        <li><strong>Last-Minute Booking Behaviour:</strong> Short-notice bookings from the Bangkok market make pricing and availability decisions time-sensitive.</li>
        <li><strong>Seasonal Long-Stay Demand:</strong> Longer stays in the cool season are often priced without a clear structure.</li>
        <li><strong>Limited Direct Distribution:</strong> Many properties depend on OTAs for guests who would book direct if the offer were clear.</li>
      </ul>
      <h3 style="margin-top: 1.5rem;">What CRS Central Does for Hua Hin Hotels</h3>
      <ul class="bullet-list">
        <li><strong>Peak and Holiday Yield Protection:</strong> Rate tiers that capture full value on weekends and Thai public holidays.</li>
        <li><strong>Midweek Demand Building:</strong> Offers and packages for golf, wellness, family and long-weekend stays that fill quiet nights without cutting rates across the board.</li>
        <li><strong>Long-Stay Rate Structure:</strong> Clear weekly and monthly pricing for seasonal visitors.</li>
        <li><strong>OTA Optimization:</strong> Content, ranking and promotion improvements on the channels your Bangkok and international guests use.</li>
        <li><strong>Direct Booking Development:</strong> A booking path through your website, LINE and WhatsApp for repeat weekend guests.</li>
      </ul>"""

# Replace Pattaya
pty_content = """      <p>Pattaya combines drive-in weekend demand from Bangkok and the eastern region with regional and international leisure travellers, groups, weddings and events. Its large supply of rooms and strong OTA presence make rate discipline and channel mix especially important.</p>
      <h3 style="margin-top: 1.5rem;">Why Pattaya Hotels Need Revenue Management Now</h3>
      <ul class="bullet-list" style="margin-bottom: 1.5rem;">
        <li><strong>Heavy OTA Dependency:</strong> Bookings flow mostly through a few channels, creating large commission costs.</li>
        <li><strong>Rate Competition:</strong> Dense supply across every price level pushes hotels into price-led selling.</li>
        <li><strong>Group and Event Pricing:</strong> Groups, weddings and events are often quoted without a yield-based approach.</li>
        <li><strong>Weak Weekend and Holiday Capture:</strong> Peak nights are sold too cheaply and too early.</li>
      </ul>
      <h3 style="margin-top: 1.5rem;">What CRS Central Does for Pattaya Hotels</h3>
      <ul class="bullet-list">
        <li><strong>Rate Integrity and Parity:</strong> Consistent rates across every channel, with controls that stop uncontrolled discounting.</li>
        <li><strong>Group and Event Strategy:</strong> Pricing frameworks that account for displaced transient demand and group value.</li>
        <li><strong>OTA Visibility and Conversion:</strong> Better listings, smarter promotions and the right mix of channels.</li>
        <li><strong>Weekend and Holiday Yield:</strong> Rate tiers and minimum-stay rules for peak periods.</li>
        <li><strong>Commission Reduction:</strong> A direct booking strategy supported by the StayCRS Booking Engine.</li>
      </ul>"""

# Replace Phuket
hkt_content = """      <p>Phuket is Thailand's best-known island destination, with beach resorts, boutique hotels and private villas serving international guests across Patong, Kata, Karon, Kamala, Bang Tao and Phuket Town. Demand swings sharply between the high season and the quieter monsoon months, and many guests book far in advance.</p>
      <h3 style="margin-top: 1.5rem;">Why Phuket Hotels Need Revenue Management Now</h3>
      <ul class="bullet-list" style="margin-bottom: 1.5rem;">
        <li><strong>Sharp Season Swings:</strong> High-season rates are often under-priced, while low-season rooms are discounted too deeply.</li>
        <li><strong>Booking Window Pressure:</strong> Long-haul guests book early, so early-season pricing decisions affect the whole year.</li>
        <li><strong>Villa and Resort Complexity:</strong> Villas, suites and room types need separate pricing logic, minimum stays and seasonal rules.</li>
        <li><strong>High OTA Commissions:</strong> Premium rates mean every point of commission has a large impact.</li>
      </ul>
      <h3 style="margin-top: 1.5rem;">What CRS Central Does for Phuket Hotels</h3>
      <ul class="bullet-list">
        <li><strong>High-Season Yield Protection:</strong> Structured rate tiers and minimum-stay rules that capture full value at peak.</li>
        <li><strong>Low-Season Strategy:</strong> Demand-building offers and packages that protect rate integrity rather than discounting broadly.</li>
        <li><strong>Villa and Room-Type Pricing:</strong> Clear logic across villas, suites and room categories, including long-stay rates.</li>
        <li><strong>International OTA Optimization:</strong> Content and ranking improvements on Booking.com, Agoda, Trip.com and Expedia.</li>
        <li><strong>Direct Booking Development:</strong> Reducing commission dependency for a market where high rates make direct conversion especially valuable.</li>
      </ul>"""

new_bangkok = create_floating_section("bangkok", "thailand-bkk-title", "Bangkok: Thailand's Business and City-Break Capital", "assets/images/thailand_bangkok.webp", "Bangkok skyline and Chao Phraya river at dusk", False, False, bkk_content, "assets/images/thailand_bangkok_2.webp")
new_huahin = create_floating_section("hua-hin", "thailand-hh-title", "Hua Hin: The Royal Seaside Escape", "assets/images/thailand_huahin.webp", "Hua Hin beach with hotel and golf course nearby", True, True, hh_content)
new_pattaya = create_floating_section("pattaya", "thailand-pty-title", "Pattaya: High-Volume Leisure Next to the Capital", "assets/images/thailand_pattaya.webp", "Pattaya bay and beachfront hotels", False, False, pty_content)
new_phuket = create_floating_section("phuket", "thailand-hkt-title", "Phuket: International Beach and Villa Travel", "assets/images/thailand_phuket.webp", "Phuket beach, resort and private villa overlooking the sea", True, True, hkt_content)

# We need to replace from <section id="bangkok"> to before <!-- Achieve Together & Advantage Section -->
match = re.search(r'<!-- Bangkok Section -->.*?<!-- Achieve Together & Advantage Section -->', content, re.DOTALL)
if match:
    replacement = "<!-- Bangkok Section -->\n" + new_bangkok + "\n\n  <!-- Hua Hin Section -->\n" + new_huahin + "\n\n  <!-- Pattaya Section -->\n" + new_pattaya + "\n\n  <!-- Phuket Section -->\n" + new_phuket + "\n\n  <!-- Achieve Together & Advantage Section -->"
    content = content[:match.start()] + replacement + content[match.end()-40:]
else:
    print("Could not find section markers")
    
# Finally, update the Advantage section to include the 5th image (floating right)
advantage_match = re.search(r'<h2 class="section-title" style="font-size: 1.8rem;">The CRS Central Advantage in Thailand</h2>', content)
if advantage_match:
    img_advantage = '<img src="assets/images/thailand_advantage.webp" alt="Thailand historical park" class="float-img-right" loading="lazy" onerror="this.style.display=\'none\'">\n          '
    content = content[:advantage_match.start()] + img_advantage + content[advantage_match.start():]
else:
    print("Could not find Advantage marker")

# Also need to make the Advantage section a floating container. Currently it's inside split-layout.
# Let's remove split-layout for Advantage.
adv_container_match = re.search(r'<div class="split-layout">\s*<div class="split-content" style="width: 100%;">\s*<img src="assets/images/thailand_advantage', content)
if adv_container_match:
    content = content.replace(
        '<div class="split-layout">\n        <div class="split-content" style="width: 100%;">',
        '<div style="display: block; overflow: hidden;">'
    )
    # We have to close it properly too... actually the easiest is regex.
    # We replaced the opening. The closing </div></div> needs to be </div>.
    # Let's just do a simpler replacement:
    
with open('thailand.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sections")
