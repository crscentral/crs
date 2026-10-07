import re
import json

files = [
    'staycrs.html',
    'staycrs-privacy.html',
    'staycrs-terms.html',
    'staycrs-refund.html',
    'staycrs-cancellation.html'
]

# A basic regex-based text node extractor (simplified)
# We will just use BeautifulSoup to do it cleanly.
