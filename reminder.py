#!/usr/bin/python3
import time
import os

import tts

def checkForReminder():
    f = open('bin/Reminder/reminderOne.txt', 'r')
    today = time.strftime('%d %m')
    print(today)
    for line in f:
        if today in line:
            print('found')
            total = f.readlines()
            artist = total[0].strip()
            venue = total[1].strip()
            # tts.speak(line[1] + ' is on today at ' + line[2])
            print(artist + ' is on today at ' + venue)

def setReminder(date, artist, venue):
    file = open('bin/Reminder/reminderOne.txt', 'w')

    file.writelines('%s\n%s\n%s\n' % (date, artist, venue))

    file.close()