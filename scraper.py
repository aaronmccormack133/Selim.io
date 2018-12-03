# https://www.youtube.com/watch?v=F1kZ39SvuGE
from bs4 import BeautifulSoup
import requests
import os

url = os.environ.get('SELIM_SCRAPE_URL')
print(url)
pageRequest = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
pageResp = pageRequest.content.decode('ISO-8859-1', 'replace')

soup = BeautifulSoup(pageResp, 'html.parser')
calender = soup.find('table', {'class': 'musicTable'})

for tr in calender.find_all('tr'):
    if tr.find('a') is None:
        if tr.find('td') is None:
            continue
        else:
            artistName = tr.find('td', {'class': 'artistName'})
            artistName.encode('utf-8')
            albumName = tr.find('td', {'class': 'albumTitle'})
            albumName.encode('utf-8')
    else:
        artistName = tr.find('a')
        artistName.encode('utf-8')
        albumName = tr.find('td', {'class': 'albumTitle'})
        albumName.encode('utf-8')
        
    print(artistName)
    print(albumName)

# print(soup.encode('utf-8'))