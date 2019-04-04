import os
import json
import requests

import config
import tts

# apiKey = os.environ.get('LAST.FM_API')
apiKey = config.LASTFM_API
# sharedSecret = os.environ.get('LAST.FM_SS')
sharedSecret = config.LASTFM_SS

url = "http://ws.audioscrobbler.com/2.0/?"

artistName = input('Artist: ')
if (' ' in artistName):
    artistName = artistName.replace(' ', '+')
    artistName = artistName.strip()

limit = input('Limit: ')
params = ('method=artist.getSimilar&artist=' 
    + artistName 
    + '&api_key=' 
    + apiKey 
    + '&format=json&limit=' 
    + limit)

def apiCall (apiUrl, params):
    response = requests.get(apiUrl + params).json()

    file = open('bin/SimilarArtist/artistOne.txt', 'w')

    for artist in response["similarartists"]["artist"]:
        print(artist['name'])
        tts.speak(artist['name'])
        file.writelines('%s\n' % artist['name'])

    file.close()
            
apiCall(url, params)
