import os
import re

replacements = {
    "Laos, India, Nepal, Malaysia, Thailand and Vietnam": "Thailand, Laos, India, Nepal, Malaysia and Vietnam",
    "Laos, India, Nepal, Malaysia, Thailand, and Vietnam": "Thailand, Laos, India, Nepal, Malaysia, and Vietnam",
    "Laos, India, Nepal, Malaysia, <br>Thailand and Vietnam": "Thailand, Laos, India, Nepal, Malaysia, <br>and Vietnam",
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

print("Done replacing sequences.")
