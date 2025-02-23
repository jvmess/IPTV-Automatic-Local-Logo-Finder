Me and my friend ChatGPT created a tool to automatically pull a logo from Wikipedia (higher quality images) for local channels. When I was going through IPTVEditor, I was struggling because of the time it took to go to each Wikipedia page and get the photo and copy it, so I decided to make a little Python script for it.

The way it works is you just type in the 3-4 letter call sign, and it will copy the logo onto your clipboard, ready for you to paste. If it is unable to find a logo for a certain page (Wikipedia has multiple pages with the same name, so you have to specify more), it will automatically try to search for it with -TV, -CD, and -LD in the name. This is shown in the video with the KLAF example not being found in KLAF, KLAF-TV, KLAF-CD, but was found in KLAF-LD.

I found that this sped the process up immensely, so I figured I would share it with you guys.

What is required:

Python, newest version is probably the best.

Prior to running:

  pip install requests

  pip install pyperclip (used to copy it to your clipboard)

  pip install bs4 (web scraper to get logo)

  Call sign for the channel

What this doesn't work with:

  Any normal channel

    The reason for this is that it was created to automatically capitalize all letters so that Wikipedia could recognize the call sign. However, with normal channels, not all the letters are capitalized. Plus, you need to replace spaces with underscores.

    You could hypothetically remove .upper() from the the_page variable, but you would also have to know the exact name of the page. It's very easy with local channels because its just the call sign.

  Channels you do not have the call sign for

    If you don't have the call sign, Wikipedia won't be able to find it for you. Your best bet is to just google the station name (Ex: NBC 15 Lafayette) and find it there.
