import os

files_to_update = [
    'staycrs-terms.html',
    'staycrs-cancellation.html',
    'staycrs-privacy.html',
    'staycrs-refund.html'
]

replacements = {
    '<a href="#pms">PMS</a>': '<a href="staycrs.html#pms">PMS</a>',
    '<a href="#channel-manager">Channel Manager</a>': '<a href="staycrs.html#channel-manager">Channel Manager</a>',
    '<a href="#booking-engine">Booking Engine</a>': '<a href="staycrs.html#booking-engine">Booking Engine</a>',
    '<a href="#revenue-management">Revenue Management</a>': '<a href="staycrs.html#revenue-management">Revenue Management</a>',
    '<a class="btn" href="#demo">Get a Demo</a>': '<a class="btn" href="staycrs.html#demo">Get a Demo</a>',
    '<a href="#demo" class="btn outl" style="padding:14px 28px;font-size:1.05rem">Get a Demo</a>': '<a href="staycrs.html#demo" class="btn outl" style="padding:14px 28px;font-size:1.05rem">Get a Demo</a>'
}

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated nav links in {filename}")

