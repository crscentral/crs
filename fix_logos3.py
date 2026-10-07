import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = content
    # Replace calc-header-logo (with or without loading="lazy")
    modified = modified.replace(
        '<img src="assets/images/logo_globe_transparent.webp" alt="CRS Central Logo" class="calc-header-logo" width="350" height="181" loading="lazy">',
        '<div class="calc-header-logo" aria-label="CRS Central Logo"></div>'
    )
    modified = modified.replace(
        '<img src="assets/images/logo_globe_transparent.webp" alt="CRS Central Logo" class="calc-header-logo" width="350" height="181">',
        '<div class="calc-header-logo" aria-label="CRS Central Logo"></div>'
    )

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

print("Done replacing calc-header-logos.")
