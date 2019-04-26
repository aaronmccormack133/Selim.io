import os
import tts

file = open('bin/UpcomingAlbums/upcomingRelease.txt', 'r')

f = file.readlines()
for x in f:
    tts.speak(x)
    print(x.strip())