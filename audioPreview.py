#!/usr/bin/python3
import urllib.request
import urllib.parse
import re
from pytube import YouTube
import subprocess
import fnmatch
import os

def getUrl(artistName):
    artistName = artistName.strip()
    for file in os.listdir('bin/AudioPreview/'):
        if fnmatch.fnmatch(file, artistName+'.mp4'):
            script = "#!/bin/sh\ncvlc --play-and-exit bin/AudioPreview/" + artistName + ".mp4"
            with open('youtube.sh', 'w') as f:
                f.writelines(script)
        else:
            scriptStart = "ffmpeg -y $(youtube-dl -g --extract-audio '"
            scriptEnd = "' | sed \"s/.*/-ss 00:10 -i &/\") -t 0:30 -c copy bin/AudioPreview/" + artistName + ".mp4\ncvlc --play-and-exit bin/AudioPreview/" + artistName + ".mp4"
            query = urllib.parse.urlencode({"search_query": artistName})
            page = urllib.request.urlopen("http://www.youtube.com/results?" + query)
            results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
            bashResp = "http://www.youtube.com/watch?v=" + results[1]
            with open('youtube.sh', 'w') as f:
                f.writelines("#!/bin/sh\n" + scriptStart + bashResp + scriptEnd)
    subprocess.call(['./youtube.sh'])