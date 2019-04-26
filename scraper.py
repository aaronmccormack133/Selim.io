# https://www.youtube.com/watch?v=F1kZ39SvuGE
# external imports
from bs4 import BeautifulSoup
import requests
import os
import config

# files
import tts

url = config.SELIM_SCRAPE_URL
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
        
        
    file.writelines('%s, ' % artistName)
    file.writelines('%s\n' % albumName)

    # fullTitle = artistName + ', ' + albumName
    # tts.speak(fullTitle)

file.close()