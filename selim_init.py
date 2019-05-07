#!/usr/bin/python3
# files
import upcomingConcerts as uc
import config 
import tts 
import similarArtists as sa
import upcomingAlbums as ua

# external imports
import time

tts.speak('Saylem initialized. Say my name when you would like to start')
print('Saylem initialized. Say my name when you would like to start')
print('---------------------')

start = input()

# if(query in similar_artist_keyword):

def main_flow():
    similar_artist_keyword = ['similar', 'like', 'artist', 'artists']
    upcoming_shows_keyword = ['concert', 'concerts', 'shows', 'gig', 'gigs', 'show', 'event']
    upcoming_albums_keyword = ['albums', 'new', 'album', 'release', 'releases', 'records']

    tts.speak('Saylem activated')
    print('Saylem activated')
    tts.speak("What would you like?")
    print('What would you like?')
    print('---------------------')
    query = input()
    
    for i in query.split(' '):
        if(i in similar_artist_keyword):
            # similar artists
            tts.speak('what artist')
            print('what artist?')
            print('---------------------')
            artist = input()
            tts.speak('how many results would you like')
            print('how many results would you like')
            print('---------------------')
            limit = input()
            tts.speak('artists that are similar to ' + artist + ' are...')
            print('artists that are similar to ' + artist + ' are...')
            print('---------------------')
            sa.call(artist, limit)
        elif(i in upcoming_shows_keyword):
        # upcoming concerts
            tts.speak('would you like all concerts or a specific artist')
            print('would you like all concerts or a specific artist')
            print('---------------------')
            concertType = input()
            if('all' in concertType):
            # getting all upcoming concerts
                tts.speak('Specify a location')
                print('specify a location')
                print('---------------------')
                city = input()
                tts.speak('Is there a limit you would like to set on the results')
                print('Is there a limit you would like to set on the results')
                print('---------------------')
                limit = input()
                if('no' in limit):
                    uc.concertCall('all', city, '40')
                else:
                    uc.concertCall('all', city, limit)
                # uc.concertCall('all', city, limit)
            else:
            # getting artist specific concerts
                tts.speak('what artist would you like?')
                print('what artist would you like')
                print('---------------------')
                artistCall = input()
                uc.concertCall(artistCall, None, None)
        elif(i in upcoming_albums_keyword):
        # getting new albums
            tts.speak("Albums being released soon are")
            print('albums being released soon are')
            print('---------------------')
            time.sleep(1)
            ua.upcoming()
        else:
            tts.speak('query not found')

if('Selim' or 'Saylem' in start):
    main_flow()

        