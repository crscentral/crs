import json
import re

# 1. Update HTML
with open('thailand.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "Which Thai cities do you cover?": "thailand-faq-q1",
    "Do we need to change our PMS or channel manager?": "thailand-faq-q2",
    "How much does it cost?": "thailand-faq-q3",
    "What size of hotel do you work with?": "thailand-faq-q4",
    "What does the free audit include?": "thailand-faq-q5"
}

for text, key in replacements.items():
    html = html.replace(f">{text}</summary>", f' data-i18n="{key}">{text}</summary>')

with open('thailand.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update JSON dicts
translations = {
    "en": {
        "thailand-faq-q1": "Which Thai cities do you cover?",
        "thailand-faq-q2": "Do we need to change our PMS or channel manager?",
        "thailand-faq-q3": "How much does it cost?",
        "thailand-faq-q4": "What size of hotel do you work with?",
        "thailand-faq-q5": "What does the free audit include?"
    },
    "th": {
        "thailand-faq-q1": "คุณครอบคลุมเมืองใดบ้างในประเทศไทย?",
        "thailand-faq-q2": "เราจำเป็นต้องเปลี่ยน PMS หรือ channel manager หรือไม่?",
        "thailand-faq-q3": "มีค่าใช้จ่ายเท่าไร?",
        "thailand-faq-q4": "คุณทำงานกับโรงแรมขนาดใด?",
        "thailand-faq-q5": "การตรวจสอบฟรีรวมอะไรบ้าง?"
    },
    "zh-CN": {
        "thailand-faq-q1": "您覆盖泰国的哪些城市？",
        "thailand-faq-q2": "我们需要更换我们的 PMS 或渠道管理器吗？",
        "thailand-faq-q3": "费用是多少？",
        "thailand-faq-q4": "你们与什么规模的酒店合作？",
        "thailand-faq-q5": "免费审计包括什么？"
    },
    "ar": {
        "thailand-faq-q1": "ما هي المدن التايلاندية التي تغطيها؟",
        "thailand-faq-q2": "هل نحتاج إلى تغيير نظام إدارة الممتلكات (PMS) أو مدير القنوات؟",
        "thailand-faq-q3": "كم هي التكلفة؟",
        "thailand-faq-q4": "ما هو حجم الفندق الذي تعمل معه؟",
        "thailand-faq-q5": "ما الذي تتضمنه المراجعة المجانية؟"
    },
    "vi": {
        "thailand-faq-q1": "Bạn bao phủ những thành phố nào của Thái Lan?",
        "thailand-faq-q2": "Chúng tôi có cần thay đổi PMS hoặc công cụ quản lý kênh của mình không?",
        "thailand-faq-q3": "Chi phí là bao nhiêu?",
        "thailand-faq-q4": "Bạn làm việc với khách sạn quy mô nào?",
        "thailand-faq-q5": "Đánh giá miễn phí bao gồm những gì?"
    },
    "km": {
        "thailand-faq-q1": "តើអ្នកគ្របដណ្តប់ទីក្រុងថៃណាខ្លះ?",
        "thailand-faq-q2": "តើពួកយើងចាំបាច់ត្រូវផ្លាស់ប្តូរ PMS ឬកម្មវិធីគ្រប់គ្រងប៉ុស្តិ៍របស់យើងទេ?",
        "thailand-faq-q3": "តើវាមានតម្លៃប៉ុន្មាន?",
        "thailand-faq-q4": "តើអ្នកធ្វើការជាមួយសណ្ឋាគារទំហំប៉ុនណា?",
        "thailand-faq-q5": "តើការត្រួតពិនិត្យដោយឥតគិតថ្លៃរួមបញ្ចូលអ្វីខ្លះ?"
    }
}

for lang, data in translations.items():
    filepath = f"assets/locales/{lang}.json"
    with open(filepath, 'r', encoding='utf-8') as f:
        locale = json.load(f)
        
    for k, v in data.items():
        locale[k] = v
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(locale, f, ensure_ascii=False, indent=2)

print("Updated HTML and JSON translations.")

# Bump cache version in JS
with open('assets/js/script-v2.js', 'r', encoding='utf-8') as f:
    js = f.read()
js = js.replace('.json?v=7', '.json?v=8')
with open('assets/js/script-v2.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('assets/js/script-v2.min.js', 'r', encoding='utf-8') as f:
    js_min = f.read()
js_min = js_min.replace('.json?v=7', '.json?v=8')
with open('assets/js/script-v2.min.js', 'w', encoding='utf-8') as f:
    f.write(js_min)

