with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

addition = """
/* Fix for dark mode auto-inversion breaking the logo filters */
img.logo-img, img.hero-logo-img, img.calc-header-logo, .footer img.logo-img {
    color-scheme: light !important;
    isolation: isolate !important;
}
"""

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css + "\n" + addition)
print("Added fix to style.css")
