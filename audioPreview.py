#!/usr/bin/python3
import urllib.request
import urllib.parse
import re
from pytube import YouTube
import subprocess

# https://www.youtube.com/watch?v=oHg5SJYRHA0

def getUrl(artistName):
    scriptStart = "ffmpeg -y $(youtube-dl -g --extract-audio '"
    scriptEnd = "' | sed \"s/.*/-ss 00:10 -i &/\") -t 0:30 -c copy bin/AudioPreview/clip.mp4\ncvlc --play-and-exit bin/AudioPreview/clip.mp4"
    query = urllib.parse.urlencode({"search_query": artistName})
    page = urllib.request.urlopen("http://www.youtube.com/results?" + query)
    results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
    bashResp = "http://www.youtube.com/watch?v=" + results[1]
    with open('youtube.sh', 'w') as f:
        f.writelines("#!/bin/sh\n" + scriptStart + bashResp + scriptEnd)
    subprocess.call(['./youtube.sh'])
    # return('http://www.youtube.com/watch?v=' + results[1])

# def getMp3(url):
#     yt = YouTube(url)
#     stream = yt.streams.filter(only_audio=True).first()
#     stream.download()    

# def returnUrl(artistName):
#     url = getUrl(artistName)
#     getMp3(url)

getUrl('black cilice')