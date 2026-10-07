import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    replacements = {
        '>Thailand Market Expertise<': '>Thailand Expertise<',
        '>Laos Market Expertise<': '>Laos Expertise<',
        '>Malaysia Market Expertise<': '>Malaysia Expertise<',
        '>Vietnam Market Expertise<': '>Vietnam Expertise<',
        '>India Market Expertise<': '>India Expertise<',
        '>Nepal Market Expertise<': '>Nepal Expertise<'
    }

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
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

