import json
import os

translations = {
    "th": {
        "thailand-intro2": "โรงแรมอิสระและวิลล่าหลายแห่งยังคงตั้งราคาตามปฏิทินของปีที่แล้ว พึ่งพา OTA ไม่กี่รายมากเกินไป และจ่ายค่าคอมมิชชั่นสูงสำหรับการจองที่พวกเขาสามารถได้มาโดยตรง ช่องว่างนี้นี่เองที่ CRS Central เพิ่มมูลค่าสูงสุด",
        "thailand-choose": "เลือกตลาดของคุณ:",
        "thailand-btn-bkk": "กรุงเทพฯ: ธุรกิจและการท่องเที่ยวในเมือง",
        "thailand-btn-hh": "หัวหิน: วันหยุดสุดสัปดาห์และกอล์ฟ",
        "thailand-btn-pty": "พัทยา: ท่องเที่ยวทางรถยนต์และแบบกลุ่ม",
        "thailand-btn-hkt": "ภูเก็ต: ชายหาดและวิลล่า"
    },
    "zh-CN": {
        "thailand-intro2": "许多独立酒店和别墅仍在按照去年的日历定价，严重依赖少数几个在线旅行社 (OTA)，并为原本可以直接获得的预订支付高昂的佣金。这种差距正是 CRS Central 创造最大价值的地方。",
        "thailand-choose": "选择您的市场：",
        "thailand-btn-bkk": "曼谷：商务与城市休闲",
        "thailand-btn-hh": "华欣：周末与高尔夫",
        "thailand-btn-pty": "芭堤雅：自驾游与团队游",
        "thailand-btn-hkt": "普吉岛：海滩与别墅"
    },
    "ar": {
        "thailand-intro2": "لا تزال العديد من الفنادق والفيلات المستقلة تحدد الأسعار بناءً على تقويم العام الماضي، وتعتمد بشكل كبير على عدد قليل من وكالات السفر عبر الإنترنت (OTAs)، وتدفع عمولات عالية للحجوزات التي كان بإمكانها الفوز بها مباشرة. هذه الفجوة هي بالضبط حيث تضيف CRS Central أكبر قيمة.",
        "thailand-choose": "اختر سوقك:",
        "thailand-btn-bkk": "بانكوك: الأعمال والعطلات في المدينة",
        "thailand-btn-hh": "هوا هين: عطلات نهاية الأسبوع والغولف",
        "thailand-btn-pty": "باتايا: السفر بالسيارة والمجموعات",
        "thailand-btn-hkt": "فوكيت: الشواطئ والفيلات"
    },
    "vi": {
        "thailand-intro2": "Nhiều khách sạn và biệt thự độc lập vẫn định giá từ lịch của năm ngoái, phụ thuộc nhiều vào một số ít OTA và trả hoa hồng cao cho các đặt phòng mà họ có thể giành được trực tiếp. Khoảng trống đó chính là nơi CRS Central mang lại giá trị cao nhất.",
        "thailand-choose": "Chọn thị trường của bạn:",
        "thailand-btn-bkk": "Bangkok: kinh doanh & nghỉ dưỡng thành phố",
        "thailand-btn-hh": "Hua Hin: cuối tuần & chơi golf",
        "thailand-btn-pty": "Pattaya: du lịch ô tô & nhóm",
        "thailand-btn-hkt": "Phuket: bãi biển & biệt thự"
    },
    "km": {
        "thailand-intro2": "សណ្ឋាគារ និងវីឡាឯករាជ្យជាច្រើននៅតែដាក់តម្លៃតាមប្រតិទិនឆ្នាំមុន ពឹងផ្អែកខ្លាំងលើ OTA មួយចំនួនតូច និងបង់កម្រៃជើងសារខ្ពស់សម្រាប់ការកក់ដែលពួកគេអាចទទួលបានដោយផ្ទាល់។ គម្លាតនេះគឺពិតជាកន្លែងដែល CRS Central បន្ថែមតម្លៃបំផុត។",
        "thailand-choose": "ជ្រើសរើសទីផ្សាររបស់អ្នក៖",
        "thailand-btn-bkk": "បាងកក៖ អាជីវកម្ម និងការសម្រាកនៅទីក្រុង",
        "thailand-btn-hh": "ហួហ៊ីន៖ ចុងសប្តាហ៍ និងវាយកូនហ្គោល",
        "thailand-btn-pty": "ប៉ាតាយ៉ា៖ ការធ្វើដំណើរតាមឡាន និងជាក្រុម",
        "thailand-btn-hkt": "ភូកេត៖ ឆ្នេរ និងវីឡា"
    }
}

for lang, data in translations.items():
    filepath = f"assets/locales/{lang}.json"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            locale = json.load(f)
            
        for k, v in data.items():
            locale[k] = v
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(locale, f, ensure_ascii=False, indent=2)
        print(f"Updated {lang}.json")

# Also bump the cache buster in javascript to ?v=7
with open('assets/js/script-v2.js', 'r', encoding='utf-8') as f:
    js = f.read()
js = js.replace('.json?v=6', '.json?v=7')
with open('assets/js/script-v2.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('assets/js/script-v2.min.js', 'r', encoding='utf-8') as f:
    js_min = f.read()
js_min = js_min.replace('.json?v=6', '.json?v=7')
with open('assets/js/script-v2.min.js', 'w', encoding='utf-8') as f:
    f.write(js_min)

