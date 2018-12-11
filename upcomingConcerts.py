import os
import json
import requests

apiKey = os.environ.get('TICKETMASTER_API')

url = "https://app.ticketmaster.com/discovery/v2/events.json?"

params = (url + 'apikey=' + apiKey + '&countryCode=IE')

response = requests.get(params).json()

with open('bin/UpcomingConcerts/one.json', 'w') as outfile:
    json.dump(response, outfile)