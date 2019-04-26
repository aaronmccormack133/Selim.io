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

if((query == "similar artist") or (query == "similar artists")):
    # similar artists
    tts.speak('what artist')
    artist = input()
    tts.speak('how many results would you like')
    limit = input()
    tts.speak('artists that are similar to ' + artist + ' are...')
    sa.call(artist, limit)
elif((query == "upcoming concerts") or (query == "upcoming shows") or (query == "upcoming gigs")):
    # upcoming concerts
    tts.speak('would you like all concerts or a specific artist')
    concertType = input()
    if((concertType == "all") or (concertType == "all concerts")):
        # getting all upcoming concerts
        uc.concertCall('all')
    else:
        # getting artist specific concerts
        tts.speak('what artist would you like?')
        artistCall = input()
        uc.concertCall(artistCall)
elif((query == "new albums") or (query == "new album releases") or ("upcoming albums")):
    # getting new albums
    tts.speak("Albums being released soon are")
    time.sleep(1)
    ua.upcoming()