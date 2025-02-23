import requests
import pyperclip
from bs4 import BeautifulSoup

# Wikipedia page URL
base_url = 'https://en.wikipedia.org/wiki/'

# Scrape Wikipedia page for main image
def scrape_image_url(partial_url):
    try:
        page_url = base_url + partial_url
        res = requests.get(page_url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        infobox = soup.find('table', class_='infobox')
        if infobox:
            img_tag = infobox.find('img')
            if img_tag:
                return 'https:' + img_tag['src']
    except Exception as exc:
        print(exc)
    return None

# Loop to continuously ask for input and fetch image URLs
while True:
    the_page = input("Enter Wikipedia page title (or press Enter to exit): ").strip().upper()
    if not the_page:
        break
    
    the_url = scrape_image_url(the_page)
    
    # If no image is found, try appending '-TV' and search again
    if not the_url:
        print(f"No image file found for {the_page}, trying {the_page}-TV...")
        the_url = scrape_image_url(the_page + '-TV')
    
    # If '-TV' doesn't work, try '-CD'
    if not the_url:
        print(f"No image file found for {the_page}-TV, trying {the_page}-CD...")
        the_url = scrape_image_url(the_page + '-CD')
    
    # If '-CD' doesn't work, try '-LD'
    if not the_url:
        print(f"No image file found for {the_page}-CD, trying {the_page}-LD...")
        the_url = scrape_image_url(the_page + '-LD')
    
    if the_url:
        print(f"Image URL for {the_page}: {the_url}")
        pyperclip.copy(the_url)  # Copy each URL immediately
        print("Image URL copied to clipboard!")
    else:
        print(f"No image file found for {the_page}, {the_page}-TV, {the_page}-CD, or {the_page}-LD")
