import re

def patch_about():
    with open('about.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('Based in Bangkok', 'Registered in Hyderabad, India, with a Bangkok base')
    
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(html)

def patch_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace("We're Based in Bangkok, Close to Our Clients", "Registered in Hyderabad, India, with a Bangkok base to meet clients across the region.")
    html = html.replace("We are based in Bangkok solely for convenient travel", "We are registered in Hyderabad, India, with a Bangkok base solely for convenient travel")
    
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(html)

def patch_laos():
    with open('laos.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace("Being based in Bangkok gives us easy access", "Being registered in Hyderabad, India, with a Bangkok base gives us easy access")
    
    with open('laos.html', 'w', encoding='utf-8') as f:
        f.write(html)

patch_about()
patch_contact()
patch_laos()
print("Patched about.html, contact.html, laos.html")
