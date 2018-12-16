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

file = open('bin/UpcomingAlbums/upcomingRelease.txt', 'w')

for tr in calender.find_all('tr'):
    if tr.find('a') is None:
        if tr.find('td') is None:
            continue
        else:
            artistName = tr.find('td', {'class': 'artistName'}).text.strip()
            albumName = tr.find('td', {'class': 'albumTitle'}).text.strip()
            
    else:
        artistName = tr.find('a').text.strip()
        albumName = tr.find('td', {'class': 'albumTitle'}).text.strip()
        
        
    print(artistName)
    file.writelines('%s\n' % artistName.encode('utf-8'))
    print(albumName)
    file.writelines('%s\n' % albumName.encode('utf-8'))

file.close()

# print(soup.encode('utf-8'))
