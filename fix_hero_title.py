import re
import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(
    r'<h1 class="hero-title" data-i18n="home-hero-title">Hotel Revenue <br> Management Consultancy <span>— Laos, India, Nepal, Malaysia, <br>Thailand and Vietnam\.</span></h1>',
    r'<h1 class="hero-title" data-i18n="home-hero-title">Hotel Revenue <br> Management Consultancy <span>— Across South and Southeast Asia.</span></h1>',
    content
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Update JSON files
locales = {
    'en.json': 'Hotel Revenue <br> Management Consultancy <span>— Across South and Southeast Asia.</span>',
    'zh.json': '酒店收益 <br> 管理咨询公司 <span>— 跨越南亚与东南亚。</span>',
    'km.json': 'ការប្រឹក្សាគ្រប់គ្រង <br> ប្រាក់ចំណូលសណ្ឋาគារ <span>— នៅទូទាំងអាស៊ីខាងត្បូង និងអាស៊ីអាគ្នេយ៍។</span>',
    'vi.json': 'Tư vấn Quản lý <br> Doanh thu Khách sạn <span>— Khắp Nam Á và Đông Nam Á.</span>',
    'th.json': 'ที่ปรึกษาการบริหาร <br> รายได้โรงแรม <span>— ทั่วทั้งเอเชียใต้และเอเชียตะวันออกเฉียงใต้</span>',
    'ar.json': 'استشارات إدارة <br> إيرادات الفنادق <span>— عبر جنوب وجنوب شرق آسيا.</span>'
}

for filename, new_title in locales.items():
    filepath = os.path.join('assets', 'locales', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the value for "home-hero-title"
    content = re.sub(
        r'"home-hero-title":\s*".*?"',
        f'"home-hero-title": "{new_title}"',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated home-hero-title everywhere.")
