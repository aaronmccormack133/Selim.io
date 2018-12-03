import os
import json
import requests

apiKey = os.environ.get('LAST.FM_API')
sharedSecret = os.environ.get('LAST.FM_SS')

url = "http://ws.audioscrobbler.com/2.0/?"
artistName = 'Iron Maiden'
limit = '5'
params = ('method=artist.getSimilar&artist=' 
    + artistName 
    + '&api_key=' 
    + apiKey 
    + '&format=json&limit=' 
    + limit)

def apiCall (apiUrl, params):
    urlReq = requests.get(apiUrl + params)
    response = urlReq.text

    print(response)
            
apiCall(url, params)