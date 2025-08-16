from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    page = browser.new_page()
    page.goto('https://tokchart.com/dashboard/tiktok-trending-sounds/BD')
    
    test = page.inner_html('#content')
    
    soup = BeautifulSoup(test, 'html.parser')
    
    sound = soup.find_all('a', class_='inline-block hover:underline font-medium text-gray-800 truncate')
    sound_artist = soup.find_all('span',class_='max-w-[200px] overflow-hidden text-ellipsis')
            
    # for s in sound:
    #     print(s.get_text(strip=True))
        
    for sa in sound_artist:
        print(sa.get_text(strip=True))
    


    
    