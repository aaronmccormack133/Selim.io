# files
import upcomingConcerts as uc
import config 
import tts 
import similarArtists as sa
import upcomingAlbums as ua

# external imports
import time

tts.speak('Saylem activated')
tts.speak("What would you like?")
query = input()

similar_artist_keyword = ['similar', 'like', 'artist', 'artists']
upcoming_shows_keyword = ['concert', 'shows', 'gig', 'gigs', 'show', 'event']
upcoming_albums_keyword = ['albums', 'new', 'album', 'release', 'releases', 'records']

# if(query in similar_artist_keyword):


for i in query.split(' '):
    if(i in similar_artist_keyword):
        # similar artists
        tts.speak('what artist')
        artist = input()
        tts.speak('how many results would you like')
        limit = input()
        tts.speak('artists that are similar to ' + artist + ' are...')
        sa.call(artist, limit)
    elif(i in upcoming_shows_keyword):
    # upcoming concerts
        tts.speak('would you like all concerts or a specific artist')
        concertType = input()
        if('all' in concertType):
        # getting all upcoming concerts
            uc.concertCall('all')
        else:
        # getting artist specific concerts
            tts.speak('what artist would you like?')
            artistCall = input()
            uc.concertCall(artistCall)
    elif(i in upcoming_albums_keyword):
    # getting new albums
        tts.speak("Albums being released soon are")
        time.sleep(1)
        ua.upcoming()
    else:
        tts.speak('query not found')
        