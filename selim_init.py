#!/usr/bin/python3
# files
# Upcoming Concert calls
import upcomingConcerts as uc
# Import API keys
import config 
# import text to speech
import tts 
# import similar artist calls
import similarArtists as sa
# import upcoming album calls
import upcomingAlbums as ua
# import reminder calls
import reminder
# import clip preview calls
import audioPreview as ap
# import speech recognition
import speech

# external imports
import time

"""
    This is the main file for operations for Selim.io. This file is executed to run all of the functions that interact with the user.
    In order to use the application via Speech, all of the speech.speech() calls must be uncommented
    In order to use the application via command line, all of the input() calls must be uncommented.
"""
        
# Input: Artist, Limit(number of responses)
# Output: Calls the similarArtist function in the file. Output results in Text-to-Speech
# Description: This flow gets the user to interact witht the bot to get them to input an artist 
# they would like to receive information on regarding similar artists to the ones they specify
def similarArtist():
    tts.speak('what artist')
    print('what artist?')
    print('---------------------')
    # artist = input()
    artist = speech.speech()
    tts.speak('how many results would you like')
    print('how many results would you like')
    print('---------------------')
    # limit = input()
    limit = speech.speech()
    tts.speak('artists that are similar to ' + artist + ' are...')
    print('artists that are similar to ' + artist + ' are...')
    print('---------------------')
    sa.call(artist, limit)

# Input: ConcertType (to check which concert query), location, limit, artist
# Output: Return of text-to-Speech of Specific band concerts or All Concerts in an area
# Description: The user can get information on concerts of specific artists or all concerts
# in a specific area.
def upcomingShows():
    tts.speak('would you like all concerts or a specific artist')
    print('would you like all concerts or a specific artist')
    print('---------------------')
    # concertType = input()
    concertType = speech.speech()
    print(concertType)
    if('concert' in concertType):
    # getting all upcoming concerts
        tts.speak('Specify a location')
        print('specify a location')
        print('---------------------')
        # city = input()
        city = speech.speech()
        tts.speak('Is there a limit you would like to set on the results')
        print('Is there a limit you would like to set on the results')
        print('---------------------')
        # limit = input()
        limit = speech.speech()
        if('no' in limit):
            uc.concertCall('all', city, '40')
        else:
            uc.concertCall('all', city, limit)
    else:
    # getting artist specific concerts
        tts.speak('what artist would you like?')
        print('what artist would you like')
        print('---------------------')
        # artistCall = input()
        artistCall = speech.speech()
        uc.concertCall(artistCall, None, None)

# Input: None
# Output: Text-to-Speech of albums scraped
# Description: Gives the user an output of upcoming albums
def upcomingAlbums():
    tts.speak("Albums being released soon are")
    print('albums being released soon are')
    print('---------------------')
    time.sleep(1)
    ua.upcoming()

# Input: Artist, Venue, Date
# Output: None
# Description: Lets the user set a notification that will be outputted when the date is reached
def reminders():
    tts.speak('What artist would you like to set a reminder for')
    print('What artist would you like to set a reminder for')
    # remindArtist = input()
    remindArtist = speech.speech()
    tts.speak('What is the venue')
    print('What is the venue')
    # remindVenue = input()
    remindVenue = speech.speech()
    tts.speak('What is the date. Specify in date month format')
    print('What is the date. Specify in date month format')
    # remindDate = input()
    remindDate = speech.speech()
    reminder.setReminder(remindDate, remindArtist, remindVenue)
    tts.speak('Your reminder has been set')

# Input: Artist
# Output: Audio preview of that artist
# Description: User inputs an artist that they would like to have previewed. The clip returned is a thirty second sample
def audioClip():
    tts.speak('what artist would you like to hear a clip of?')
    print('what artist')
    # audioClipArtist = input()
    audioClipArtist = speech.speech()
    tts.speak('Audio preview of ' + audioClipArtist + ' starting now.')
    tts.speak('Please wait a moment while it loads')
    ap.getUrl(audioClipArtist)

# Input: Keyword for the specified path
# Output: None
# Description: The main flow of the application. All of the methods are called from here. The user specifies a keyword
# and using that keyword, the path is chosen and the functions are called.
def main_flow():
    similar_artist_keyword = ['similar', 'like', 'artist', 'artists']
    upcoming_shows_keyword = ['concert', 'concerts', 'shows', 'gig', 'gigs', 'show', 'event']
    upcoming_albums_keyword = ['albums', 'new', 'album', 'release', 'releases', 'records']
    reminder_keyword = ['reminder', 'notification', 'notify']
    audioclip_keyword = ['preview', 'clip', 'track', 'sample']

    tts.speak('Saylem activated')
    print('Saylem activated')
    tts.speak("What would you like?")
    print('What would you like?')
    print('---------------------')
    # query = input()
    query = speech.speech()
    while query not in similar_artist_keyword + upcoming_albums_keyword + upcoming_shows_keyword + reminder_keyword + audioclip_keyword:
        tts.speak('query not found. Please try again')
        # query = input
        query = speech.speech()
    print(query)
    
    # take the input apart and look for keywords
    for i in query.split(' '):
        if(i in similar_artist_keyword):
            # similar artists keyword found
            similarArtist()
            tts.speak('Query Finished. Submit another query if you would like.')
        elif(i in upcoming_shows_keyword):
            # upcoming concerts keyword found
            upcomingShows()
            tts.speak('Query Finished. Submit another query if you would like.')
        elif(i in upcoming_albums_keyword):
            # getting new albums keyword found
            upcomingAlbums()
            tts.speak('Query Finished. Submit another query if you would like.')
        elif(i in reminder_keyword):
            # reminders keyword found
            reminders()
            tts.speak('Query Finished. Submit another query if you would like.')
        elif(i in audioclip_keyword):
            # audio clip keyword found
            audioClip()
            tts.speak('Query Finished. Submit another query if you would like.')
        else:
            # no keyword found
            tts.speak('query not found')

def main():
    tts.speak('Saylem initialized. Say my name when you would like to start')
    print('Saylem initialized. Say my name when you would like to start')
    print('---------------------')

    start = speech.speech()
    # start = input()
    print(start)
    reminder.checkForReminder()

    if('Sale' or 'Salem' in start):
        main_flow()

if __name__ == '__main__': main()