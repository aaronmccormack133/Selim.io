#!/usr/bin/python3
import urllib.request
import urllib.parse
import re
from pytube import YouTube

# https://www.youtube.com/watch?v=oHg5SJYRHA0

def getUrl(artistName):
    scriptStart = "ffmpeg $(youtube-dl -g --extract-audio '"
    scriptEnd = "' | sed \"s/.*/-ss 00:05 -i &/\") -t 0:30 -c copy out.mp4"
    query = urllib.parse.urlencode({"search_query": artistName})
    page = urllib.request.urlopen("http://www.youtube.com/results?" + query)
    results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
    bashResp = "http://www.youtube.com/watch?v=" + results[1]
    with open('youtube.sh', 'w') as f:
        f.writelines(scriptStart + bashResp + scriptEnd)
    # return('http://www.youtube.com/watch?v=' + results[1])

# def getMp3(url):
#     yt = YouTube(url)
#     stream = yt.streams.filter(only_audio=True).first()
#     stream.download()    

# def returnUrl(artistName):
#     url = getUrl(artistName)
#     getMp3(url)

getUrl('black cilice')