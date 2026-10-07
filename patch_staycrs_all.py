import re

files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

css_to_add = """
/* WhatsApp & Cookie Banner dynamic CSS injected for script-v2.js compatibility */
.whatsapp-float { position: fixed; bottom: 30px; right: 30px; width: 60px; height: 60px; background-color: #25d366; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3); z-index: 9999; border: 2px solid #ffffff; }
.whatsapp-icon { width: 34px; height: 34px; }
.whatsapp-float:hover { transform: translateY(-5px) scale(1.05); background-color: #20ba5a; }
.whatsapp-badge { position: absolute; right: 75px; background-color: #ffffff; color: #128c7e; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.85rem; font-weight: 700; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); border: 1px solid rgba(37, 211, 102, 0.3); white-space: nowrap; }
.whatsapp-badge::after { content: ""; position: absolute; right: -6px; top: 50%; transform: translateY(-50%); border-width: 6px 0 6px 6px; border-style: solid; border-color: transparent transparent transparent #ffffff; display: block; width: 0; }
@media (max-width: 480px) { .whatsapp-float { bottom: 20px; right: 20px; width: 55px; height: 55px; } .whatsapp-icon { width: 30px; height: 30px; } .whatsapp-badge { display: none; } }

.cookie-banner { position: fixed; bottom: 30px; left: 30px; width: 380px; background: rgba(10, 25, 47, 0.95); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 1.5rem; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); z-index: 10000; color: #fff; transition: all 0.4s; transform: translateY(100px); opacity: 0; visibility: hidden; }
.cookie-banner.show { transform: translateY(0); opacity: 1; visibility: visible; }
.cookie-content { display: flex; flex-direction: column; gap: 1rem; }
.cookie-header { display: flex; align-items: center; gap: 0.75rem; }
.cookie-icon { width: 24px; height: 24px; color: #C9A24A; }
.cookie-header h4 { margin: 0; font-size: 1.15rem; font-weight: 700; }
.cookie-text { margin: 0; font-size: 0.9rem; color: rgba(255, 255, 255, 0.7); line-height: 1.5; }
.cookie-actions { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; }
.cookie-btn { padding: 0.6rem 1rem; border-radius: 8px; font-size: 0.85rem; font-weight: 600; cursor: pointer; border: none; text-align: center; }
.cookie-btn-accept { background-color: #C9A24A; color: #18344A; }
.cookie-btn-reject { background-color: rgba(255, 255, 255, 0.1); color: #fff; border: 1px solid rgba(255, 255, 255, 0.2); }
.cookie-btn-manage { grid-column: span 2; background-color: transparent; color: rgba(255, 255, 255, 0.6); text-decoration: underline; padding: 0.25rem; font-size: 0.8rem; }
.cookie-preferences { border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 1rem; margin-top: 0.5rem; display: flex; flex-direction: column; gap: 1rem; }
.cookie-pref-item { display: flex; justify-content: space-between; align-items: center; gap: 1rem; }
.cookie-pref-info { display: flex; flex-direction: column; }
.cookie-pref-name { font-size: 0.85rem; font-weight: 600; color: #fff; }
.cookie-pref-desc { font-size: 0.75rem; color: rgba(255, 255, 255, 0.5); line-height: 1.3; }
.cookie-switch { position: relative; display: inline-block; width: 44px; height: 22px; }
.cookie-switch input { opacity: 0; width: 0; height: 0; }
.cookie-slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: rgba(255, 255, 255, 0.2); transition: .3s; border-radius: 34px; }
.cookie-slider:before { position: absolute; content: ""; height: 16px; width: 16px; left: 3px; bottom: 3px; background-color: white; transition: .3s; border-radius: 50%; }
.cookie-switch input:checked + .cookie-slider { background-color: #C9A24A; }
.cookie-switch input:checked + .cookie-slider:before { transform: translateX(22px); }
.cookie-btn-save { background-color: #18344A; color: #fff; border: 1px solid rgba(255, 255, 255, 0.1); margin-top: 0.5rem; width: 100%; }
@media (max-width: 480px) { .cookie-banner { bottom: 0; left: 0; right: 0; width: 100%; border-radius: 12px 12px 0 0; padding: 1.25rem; } }
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # ensure the previous patch is there, and append cookie css.
    if '/* WhatsApp & Cookie Banner dynamic CSS' not in html:
        html = html.replace('</style>', css_to_add + '\n</style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied full CSS patch.")
