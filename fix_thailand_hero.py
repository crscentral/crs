import re

with open('thailand.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Thai mix in hero
content = content.replace('ความเชี่ยวชาญด้านตลาดThailand', 'Thailand Market Expertise')
content = content.replace("Thailandเป็นหนึ่งในตลาดโรงแรมที่มีผู้เยี่ยมชมมากที่สุดและแข่งขันสูงที่สุดของเอเชีย กรุงเทพฯ หัวหิน พัทยา และภูเก็ต ต่างขับเคลื่อนด้วยกลุ่มลูกค้า ฤดูกาล และพฤติกรรมการจองที่แตกต่างกัน", "Thailand is one of Asia's most visited hotel markets, and one of its most competitive. Bangkok, Hua Hin, Pattaya and Phuket each run on a different demand engine, with their own guests, seasons and booking habits.")
content = content.replace('จองการตรวจสอบรายได้ฟรีสำหรับโรงแรมในThailand &rarr;', 'Book a Free Revenue Audit in Thailand &rarr;')

# Fix advantage section image
# Look for <h2 class="section-title" style="font-size: 1.8rem;">The CRS Central Advantage in Thailand</h2>
adv_title = '<h2 class="section-title" style="font-size: 1.8rem;">The CRS Central Advantage in Thailand</h2>'
img_adv = '<img src="assets/images/thailand_advantage.webp" alt="Thailand historical park" class="float-img-right" loading="lazy" onerror="this.style.display=\'none\'">'

if adv_title in content and img_adv not in content:
    content = content.replace(adv_title, img_adv + '\n          ' + adv_title)
    
# Remove split-layout from Advantage section so it wraps properly
# Find the start of The CRS Central Advantage in Thailand block
# It's currently in a split-layout.
#   <div class="split-layout">
#     <div class="split-content" style="width: 100%;">
#       <img src="assets/images/thailand_advantage...
# Let's replace the <div class="split-layout"> wrapper right before Advantage.
content = content.replace('<div class="split-layout">\n        <div class="split-content" style="width: 100%;">\n          <img src="assets/images/thailand_advantage.webp"',
                          '<div style="display: block; overflow: hidden; margin-top: 3rem;">\n          <img src="assets/images/thailand_advantage.webp"')
content = content.replace('<div class="split-layout">\n        <div class="split-content" style="width: 100%;">\n          <h2 class="section-title" style="font-size: 1.8rem;">The CRS Central Advantage in Thailand</h2>',
                          '<div style="display: block; overflow: hidden; margin-top: 3rem;">\n          <h2 class="section-title" style="font-size: 1.8rem;">The CRS Central Advantage in Thailand</h2>')

with open('thailand.html', 'w', encoding='utf-8') as f:
    f.write(content)
