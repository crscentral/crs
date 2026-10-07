with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add color-scheme: light; to the logos
addition = """
/* Fix for dark mode auto-inversion breaking the logo filters */
.logo-img, .hero-logo-img, .footer .logo-img, .calc-header-logo {
    color-scheme: light !important;
    isolation: isolate;
}
"""
with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css + "\n" + addition)
print("Updated style.css")
