import re

with open('thailand.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Hero text alignment and width
# We will explicitly add style="max-width: 900px; margin: 0 auto; text-align: center;" to the two paragraphs.
content = content.replace(
    '<p class="hero-desc" data-i18n="thailand-intro1">',
    '<p class="hero-desc" style="max-width: 1000px; margin: 0 auto 1.5rem auto; text-align: center;" data-i18n="thailand-intro1">'
)
content = content.replace(
    '<p class="hero-desc" data-i18n="thailand-intro2">',
    '<p class="hero-desc" style="max-width: 1000px; margin: 0 auto 1.5rem auto; text-align: center;" data-i18n="thailand-intro2">'
)
content = content.replace(
    '<p class="hero-desc" style="font-weight: 600; margin-top: 1.5rem;" data-i18n="thailand-choose">',
    '<p class="hero-desc" style="font-weight: 600; margin: 1.5rem auto 1rem auto; text-align: center;" data-i18n="thailand-choose">'
)
# Also fix subtitle
content = content.replace(
    '<p class="hero-desc" style="font-weight: 600; color: var(--accent-color);" data-i18n="thailand-subtitle">',
    '<p class="hero-desc" style="font-weight: 600; color: var(--accent-color); max-width: 1000px; margin: 0 auto 1.5rem auto; text-align: center;" data-i18n="thailand-subtitle">'
)

# 2. Fix Bangkok section
# Current structure:
# <img src="assets/images/thailand_bangkok.webp" alt="Bangkok skyline and Chao Phraya river at dusk" class="float-img-right" loading="lazy" onerror="this.style.display='none'">
# <img src="assets/images/thailand_bangkok_2.webp" alt="Secondary image" class="float-img-left" loading="lazy" onerror="this.style.display='none'">
# We want to replace these two lines with a stacked container on the right.

old_bangkok_imgs = """<img src="assets/images/thailand_bangkok.webp" alt="Bangkok skyline and Chao Phraya river at dusk" class="float-img-right" loading="lazy" onerror="this.style.display='none'">
      <img src="assets/images/thailand_bangkok_2.webp" alt="Secondary image" class="float-img-left" loading="lazy" onerror="this.style.display='none'">"""

new_bangkok_imgs = """<div class="float-img-right" style="display: flex; flex-direction: column; gap: 1.5rem; background: transparent; box-shadow: none; margin-bottom: 2rem;">
        <img src="assets/images/thailand_bangkok.webp" alt="Bangkok skyline and Chao Phraya river at dusk" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--shadow-sm);" loading="lazy" onerror="this.style.display='none'">
        <img src="assets/images/thailand_bangkok_2.webp" alt="Secondary image" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--shadow-sm);" loading="lazy" onerror="this.style.display='none'">
      </div>"""

if old_bangkok_imgs in content:
    content = content.replace(old_bangkok_imgs, new_bangkok_imgs)
else:
    print("Could not find Bangkok images exactly, trying regex...")
    # Just in case whitespace is slightly off
    content = re.sub(
        r'<img src="assets/images/thailand_bangkok\.webp".*?class="float-img-right".*?>\s*<img src="assets/images/thailand_bangkok_2\.webp".*?class="float-img-left".*?>',
        new_bangkok_imgs,
        content,
        flags=re.DOTALL
    )

with open('thailand.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated thailand.html")
