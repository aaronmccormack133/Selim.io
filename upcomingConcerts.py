#!/usr/bin/python3
# external imports
import os
import json
import requests
import re

# files
import config
import tts

# query = input('Query: ')

ticketmaster = "https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&"
ticketMasterKey = config.TICKETMASTER_API
bandsintown = 'https://rest.bandsintown.com/artists/'
bandsintownKey = config.BIT_API
file = open('bin/UpcomingConcerts/one.txt', 'w')

# Cleaning up the output for events
# Input: event json
# Output: date format = DD MM YYYY
def cleanEvent(eventResp):
	eventDate = eventResp["datetime"].split('T')
	eventDateTotal = eventDate[0].replace('-', ' ')
	dateNonSplit = eventDateTotal.split(' ')
	date = dateNonSplit[2] + ' ' + dateNonSplit[1] + ' ' + dateNonSplit[0]
	return date

def ticketMasterCall(city, results):
	if(' ' in city):
		city = city.replace(' ', '+')
	params = (ticketmaster + 'apikey=' + ticketMasterKey + '&sort=date,asc&city=' + city + '&size=' + results)
	response = requests.get(params).json()
	print(params)
	for event in response["_embedded"]["events"]:
		tts.speak(event['name'])
		print(event['name'])
		file.writelines('%s\n' % event["name"])

	file.close()

def bandsintownCall(artist):
	# Call the LRU here, checking to see if its in the list
	# if not add it
	tts.speak(artist)

	if(' ' in artist):
		artistParam = artist
		artistParam = artistParam.replace(' ', '%20')
		artistParam = artistParam.strip()
		params = (bandsintown + artistParam + '/events?' +
		          'app_id=' + bandsintownKey + '&date=upcoming')
	else:
		artistParam = artist
		params = (bandsintown + artistParam + '/events?' + 
					'app_id=' + bandsintownKey + '&date=upcoming')

	print(params)
	response = requests.get(params).json()
	for event in response:
		date = cleanEvent(event)
		file.writelines('\n%s\n' % date + artist)
		file.writelines('\n%s' % event["venue"]["city"])
		total = event['venue']['city'] + date
		tts.speak(total)
		print(total)
		
	file.close()

# Getting the input from user
def getInput(input):
    return re.compile(r'\b({0})\b'.format(input), flags=re.IGNORECASE).search

# Api Call
# Input: User input, band
# Output: User output, Event name, location, date
def concertCall(input, city, limit):
    # The query for ticketmaster
	if(getInput('all')(input)):
		ticketMasterCall(city, limit)
	# The query for bandsintown
	else:
		bandsintownCall(input)

# concertCall(query)