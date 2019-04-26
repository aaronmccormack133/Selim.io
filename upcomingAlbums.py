import os
import tts

def upcoming():
    file = open('bin/UpcomingAlbums/upcomingRelease.txt', 'r')

    f = file.readlines()
    for x in f:
        tts.speak(x)