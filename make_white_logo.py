from PIL import Image
import os

filepath = 'assets/images/logo_globe_transparent.webp'
outpath = 'assets/images/logo_globe_white.webp'

if os.path.exists(filepath):
    img = Image.open(filepath).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # item is (R, G, B, A)
        # If it's a dark pixel, make it white. Let's just make ALL non-transparent pixels white to be safe, 
        # since the logo is supposed to be solid white.
        if item[3] > 0:
            # Keep the original alpha, but change RGB to 255, 255, 255
            new_data.append((255, 255, 255, item[3]))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(outpath, 'WEBP')
    print("Created logo_globe_white.webp")
else:
    print("Source logo not found.")
