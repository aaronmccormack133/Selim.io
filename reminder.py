#!/usr/bin/python3
import datetime
from datetime import date
import os

import tts

def checkForReminder():
    f = open('bin/Reminder/reminderOne.txt', 'r')
    today = date.today()
    todayDateDay = today.strftime('%d').lstrip('0')
    todayDateMonth = today.strftime('%m').lstrip('0')
    todayDate = todayDateDay + ' ' + todayDateMonth
    for line in f:
        if todayDate in line:
            print('found')
            total = f.readlines()
            artist = total[0].strip()
            venue = total[1].strip()
            tts.speak(artist + ' is on today at ' + venue)
            print(artist + ' is on today at ' + venue)

def setReminder(date, artist, venue):
    file = open('bin/Reminder/reminderOne.txt', 'a')

    day, month = date[:len(date)//2], date[len(date)//2:]
    day = day.lstrip('0')
    month = month.lstrip('0')
    date = day + ' ' + month

    file.writelines('%s\n%s\n%s\n' % (date, artist, venue))

    file.close()