import os
import json
import requests

apiKey = os.environ.get('TICKETMASTER_API')

url = "https://app.ticketmaster.com/discovery/v2/events.json?"

params = (url + 'apikey=' + apiKey + '&countryCode=IE')

response = requests.get(params).json()
file = open('bin/UpcomingConcerts/one.txt', 'w')

for event in response["_embedded"]["events"]:
	# events = event["name"]
	
	file.writelines('%s\n' % event["name"])
	print(event["name"])
	print(event["dates"]["start"]["dateTime"])
	
file.close()