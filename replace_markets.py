import os
import re

replacements = {
    "Laos, India, Nepal, Malaysia and Vietnam": "Laos, India, Nepal, Malaysia, Thailand and Vietnam",
    "Laos, India, Nepal, Malaysia, and Vietnam": "Laos, India, Nepal, Malaysia, Thailand, and Vietnam",
    "Laos, India, Nepal, <br>Malaysia and Vietnam": "Laos, India, Nepal, Malaysia, <br>Thailand and Vietnam",
    
    # Chinese
    "老挝、印度、尼泊尔、<br>马来西亚和越南。": "老挝、印度、尼泊尔、马来西亚、<br>泰国和越南。",
    
    # Khmer
    "ឡាវ ឥណ្ឌា នេប៉ាល់ <br>ម៉ាឡេស៊ី និងវៀតណាម។": "ឡាវ ឥណ្ឌា នេប៉ាល់ ម៉ាឡេស៊ី <br>ថៃ និងវៀតណាម។",
    
    # Vietnamese
    "Lào, Ấn Độ, Nepal, <br>Malaysia và Việt Nam.": "Lào, Ấn Độ, Nepal, Malaysia, <br>Thái Lan và Việt Nam.",
    
    # Thai
    "ลาว, อินเดีย, เนปาล, <br>มาเลเซีย และเวียดนาม": "ลาว, อินเดีย, เนปาล, มาเลเซีย, <br>ไทย และเวียดนาม",
    
    # Arabic
    "لاوس والهند ونيبال و <br>ماليزيا وفيتنام.": "لاوس والهند ونيبال وماليزيا و <br>تايلاند وفيتنام.",
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = content
    for old, new in replacements.items():
        modified = modified.replace(old, new)

    if modified != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.xml'):
            process_file(os.path.join(root, file))

print("Done replacing.")
