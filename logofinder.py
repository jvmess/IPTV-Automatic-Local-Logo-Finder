import requests
import pyperclip
from bs4 import BeautifulSoup

# Wikipedia page URL
base_url = 'https://en.wikipedia.org/wiki/'

# Identify yourself to Wikipedia so they don't block you
headers = {
    'User-Agent': 'LogoFinderBot/1.0 (Contact: your@email.com) Python-requests'
}

def scrape_image_url(partial_url):
    try:
        page_url = base_url + partial_url
        # Added headers=headers here
        res = requests.get(page_url, headers=headers)
        
        if res.status_code == 404:
            return None
        
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        infobox = soup.find('table', class_='infobox')
        
        if infobox:
            img_tag = infobox.find('img')
            if img_tag:
                # Ensure we get the full URL
                src = img_tag['src']
                if src.startswith('//'):
                    return 'https:' + src
                return src
    except Exception as exc:
        # Silencing common 404s to keep the terminal clean
        pass
    return None

while True:
    the_page = input("Enter Wikipedia page title (or press Enter to exit): ").strip().upper()
    if not the_page:
        break
    
    # List of suffixes to try in order
    suffixes = ['', '-TV', '-CD', '-LD', '_(TV)']
    the_url = None

    for suffix in suffixes:
        current_attempt = the_page + suffix
        the_url = scrape_image_url(current_attempt)
        if the_url:
            break
        else:
            print(f"Not found at {current_attempt}...")

    if the_url:
        print(f"Success! Image URL: {the_url}")
        pyperclip.copy(the_url)
        print("URL copied to clipboard!")
    else:
        print(f"Error: Could not find an image for {the_page} with any common suffix.")
