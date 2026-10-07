import re

files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the FIRST occurrence of /* WhatsApp Float CSS */ or /* WhatsApp & Cookie Banner dynamic CSS
    # and strip everything from there to </style>
    
    # Let's just find the original </style> and replace all our injected stuff.
    # Actually, we can just use regex to remove anything between the first injected comment and </style>
    
    html = re.sub(r'/\* WhatsApp Float CSS \*/.*?</style>', '</style>', html, flags=re.DOTALL)
    html = re.sub(r'/\* WhatsApp & Cookie Banner dynamic CSS.*?</style>', '</style>', html, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Cleaned up injected CSS.")
