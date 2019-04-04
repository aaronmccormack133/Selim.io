# external imports
import os
import json
import requests
import re

# files
import config
import tts


query = input('Query: ')

def getInput(input):
    return re.compile(r'\b({0})\b'.format(input), flags=re.IGNORECASE).search

def concertCall(input):
	ticketmaster = "https://app.ticketmaster.com/discovery/v2/events.json?"
	bandsintown = 'https://rest.bandsintown.com/artists/'

	file = open('bin/UpcomingConcerts/one.txt', 'w')

	#ticketMasterKey = os.environ.get('TICKETMASTER_API')
	ticketMasterKey = config.TICKETMASTER_API
	# bandsintownKey = os.environ.get('BIT_API')
	bandsintownKey = config.BIT_API
    # The query for ticketmaster
	if(getInput('all')(input)):
		params = (ticketmaster + 'apikey=' + ticketMasterKey + '&countryCode=IE&sort=date,asc&city=Dublin&size=40')
		response = requests.get(params).json()
		print(params)
		for event in response["_embedded"]["events"]:
			tts.speak(event['name'])
			file.writelines('%s\n' % event["name"])

		file.close()
	# The query for bandsintown
	else:
		if(' ' in input):
			input = input.replace(' ', '%20')
			input = input.strip()
			params = (bandsintown + input + '/events?' +
			          'app_id=' + bandsintownKey + '&date=upcoming')
		else:
			params = (bandsintown + input + '/events?' + 
						'app_id=' + bandsintownKey + '&date=upcoming')

		response = requests.get(params).json()
		for event in response:
			file.writelines('\n%s\n' % event["datetime"] + input)
			file.writelines('\n%s' % event["venue"]["city"].encode('UTF-8'))
		

		file.close()


concertCall(query)
