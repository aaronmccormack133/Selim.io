import upcomingConcerts as uc
import config 
import tts 
import similarArtists as sa
# import scraper

tts.speak('Saylem activated')
tts.speak("What would you like?")
query = input()

if((query == "similar artist") or (query == "similar artists")):
    tts.speak('what artist')
    artist = input()
    tts.speak('how many results would you like')
    limit = input()
    tts.speak('artists that are similar to ' + artist + ' are...')
    sa.call(artist, limit)
elif((query == "upcoming concerts") or (query == "upcoming shows") or (query == "upcoming gigs")):
    tts.speak('would you like all concerts or a specific artist')
    concertType = input()
    if((concertType == "all") or (concertType == "all concerts")):
        uc.concertCall('all')
    else:
        tts.speak('what artist would you like?')
        artistCall = input()
        uc.concertCall(artistCall)