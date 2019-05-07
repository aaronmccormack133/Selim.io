#!/usr/bin/python3
import time
import os

import tts

def checkForReminder():
    f = open('/home/aaron/Documents/Selim.io/bin/Reminder/reminderOne.txt', 'r')
    today = time.strftime('%d%m')
    for line in f:
        if today in line:
            line = line.split(' ')
            tts.speak(line[1] + ' is on today at ' + line[2])

def setReminder(date, artist, venue):
    file = open('/home/aaron/Docouments/Selim.io/bin/Reminders/reminderOne.txt', 'a')

    file.writelines('%d\n%s\n%s\n' % (date, artist, venue))

    file.close()
