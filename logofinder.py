import requests
import pyperclip
from bs4 import BeautifulSoup
import re

# Wikipedia page URL
base_url = 'https://en.wikipedia.org/wiki/'

# Custom headers to avoid 403 Forbidden errors
headers = {
    'User-Agent': 'TVStationLogoFinder/3.0 (Contact: your@email.com) Python-requests'
}

def scrape_image_url(partial_url, index=0):
    try:
        page_url = base_url + partial_url
        res = requests.get(page_url, headers=headers, allow_redirects=True)
        
        if res.status_code != 200:
            return None

        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Find the infobox
        infobox = soup.find('table', class_='infobox')
        if not infobox:
            return None

        # Find all images within the infobox
        all_imgs = infobox.find_all('img')
        
        if all_imgs and len(all_imgs) > index:
            img_tag = all_imgs[index]
            src = img_tag['src']
            if src.startswith('//'):
                return 'https:' + src
            return src
                
    except Exception:
        pass
    return None

print("--- Wikipedia Logo Finder (Multi-Image Edition) ---")
print("Format: 'CALLSIGN' for 1st image, 'CALLSIGN 2' for 2nd image.")

while True:
    user_input = input("\nEnter Station (e.g., KJRH or KJRH 2): ").strip()
    if not user_input:
        break
    
    # Split input to check for a trailing number
    parts = user_input.split()
    target_index = 0 # Default to 1st image
    
    if len(parts) > 1 and parts[-1].isdigit():
        target_index = int(parts[-1]) - 1 # Convert "2" to index 1
        callsign = " ".join(parts[:-1]).upper()
    else:
        callsign = user_input.upper()

    suffixes = ['', '-TV', '-CD', '-LD', '_(TV)']
    the_url = None

    for suffix in suffixes:
        attempt = callsign + suffix
        the_url = scrape_image_url(attempt, index=target_index)
        if the_url:
            break
    
    if the_url:
        print(f"✅ Success! Found image #{target_index + 1} for {callsign}")
        print(f"URL: {the_url}")
        pyperclip.copy(the_url)
        print("Copied to clipboard!")
    else:
        print(f"❌ Error: Could not find image #{target_index + 1} for {callsign}.")
