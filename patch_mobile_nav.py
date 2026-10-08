files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

import re

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add the hamburger button to the header
    if 'menu-toggle-btn' not in html:
        html = html.replace('<nav class="links">', '<button class="menu-toggle-btn" style="display:none; background:transparent; border:none; font-size:1.8rem; cursor:pointer; color:var(--navy); padding:0 10px;">☰</button>\n<nav class="links">')

    # 2. Add the mobile CSS
    mobile_css = """
/* Mobile Hamburger Nav for StayCRS */
@media (max-width: 900px) {
  .menu-toggle-btn { display: block !important; }
  header .wrap.nav { justify-content: space-between; position: relative; }
  .links {
    position: absolute;
    top: 68px;
    left: 0;
    right: 0;
    background: #fff;
    flex-direction: column;
    align-items: stretch !important;
    padding: 20px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    display: none !important;
    z-index: 1000;
  }
  .links.mobile-open {
    display: flex !important;
  }
  .links a:not(.btn) {
    display: block !important;
    padding: 12px 0 !important;
    border-bottom: 1px solid #eee;
    font-size: 1.1rem !important;
  }
  .links .btn {
    margin-top: 15px;
    text-align: center;
    width: 100%;
  }
  .lang-selector {
    margin-top: 15px;
    width: 100%;
  }
  .lang-btn {
    width: 100%;
    text-align: left;
    font-size: 1.1rem !important;
  }
}
"""
    if '/* Mobile Hamburger Nav for StayCRS */' not in html:
        html = html.replace('</style>', mobile_css + '\n</style>')

    # 3. Add the JS toggle
    js_code = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.menu-toggle-btn');
    const linksNav = document.querySelector('.links');
    if (toggleBtn && linksNav) {
        toggleBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            linksNav.classList.toggle('mobile-open');
            toggleBtn.innerHTML = linksNav.classList.contains('mobile-open') ? '✕' : '☰';
        });
        document.addEventListener('click', function(e) {
            if (!linksNav.contains(e.target) && e.target !== toggleBtn) {
                linksNav.classList.remove('mobile-open');
                toggleBtn.innerHTML = '☰';
            }
        });
    }
});
</script>
</body>
"""
    if 'const toggleBtn = document.querySelector' not in html:
        html = html.replace('</body>', js_code)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied mobile hamburger nav patch to all staycrs files.")
