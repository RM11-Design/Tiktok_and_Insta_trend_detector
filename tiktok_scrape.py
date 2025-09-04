from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import creds

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True,slow_mo=50)
    page = browser.new_page()
    page.goto(creds.link)
   
    test = page.inner_html('#content')
   
    soup = BeautifulSoup(test, 'html.parser')
   
    sound = soup.find_all('a', class_='inline-block hover:underline font-medium text-gray-800 truncate')
    sound_artist = soup.find_all('span',class_='max-w-[200px] overflow-hidden text-ellipsis')
    song_name = soup.find_all('div',class_='font-medium')
    song_artist = soup.find_all('div',class_='flex gap-x-1 items-center max-w-[200px] text-gray-600 truncate')
    number_of_views = soup.find_all('div',class_='pl-4 text-xs text-gray-500')

   
filename = "trends.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Sound', 'Sound Artist', 'Song Name', 'Song artist','Number of views'])
    writer.writeheader()
    for s,sar,sn,sa,nv in zip(sound,sound_artist,song_name,song_artist,number_of_views):
        writer.writerow({
            'Sound': s.get_text(strip=True),
            'Sound Artist': sar.get_text(strip=True),
            'Song Name': sn.get_text(strip=True),
            'Song artist': sa.get_text(strip=True),
            'Number of views': nv.get_text(strip=True)
        })
   
