#!/usr/bin/python3
import urllib.request
import urllib.parse
import re
from pytube import YouTube
import subprocess
import fnmatch
import os

# Input: Artist Name
# Output: A 30 second audio clip from the artist
# Description: The user submits a band of their choice which is then inserted into a query that will filter youtube responses and find a url of a clip
# the url is then used to download a 30 second audio clip from the shell file. It's then returned and played via VLC media player which is in every distro
# on Linux
def getUrl(artistName):
    if(' ' in artistName):
        tempArtist = artistName.replace(' ', '-')
        tempArtist = tempArtist.strip()
    else:
        tempArtist = artistName.strip()
    for file in os.listdir('bin/AudioPreview/'):
        # Check if the file is already downloaded. If it is play it instead of making a new query.
        if fnmatch.fnmatch(file, tempArtist+'.mkv'):
            print('found')
            artistName = artistName.replace(' ', '-')
            script = "#!/bin/sh\ncvlc --play-and-exit bin/AudioPreview/" + artistName + ".mkv"
            with open('youtube.sh', 'w') as f:
                f.writelines(script)
        else:
            query = urllib.parse.urlencode({"search_query": artistName})
            page = urllib.request.urlopen("http://www.youtube.com/results?" + query)
            results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
            bashResp = "http://www.youtube.com/watch?v=" + results[1]
            if (' ' in artistName):
                # Check for a space in the name, if there is, change the query.
                artistName = artistName.replace(' ', '-')
                artistName = artistName.strip()
                scriptStart = "ffmpeg -y $(youtube-dl -g --extract-audio '"
                scriptEnd = "' | sed \"s/.*/-ss 00:10 -i &/\") -t 0:30 -c copy bin/AudioPreview/" + artistName + ".mkv\ncvlc --play-and-exit bin/AudioPreview/" + artistName + ".mkv"
            else:
                scriptStart = "ffmpeg -y $(youtube-dl -g --extract-audio '"
                scriptEnd = "' | sed \"s/.*/-ss 00:10 -i &/\") -t 0:30 -c copy bin/AudioPreview/" + artistName + ".mkv\ncvlc --play-and-exit bin/AudioPreview/" + artistName + ".mkv"
            with open('youtube.sh', 'w') as f:
                f.writelines("#!/bin/sh\nrm -f bin/AudioPreview/*\n" + scriptStart + bashResp + scriptEnd)
    # Executes the ./youtube.sh shell file where the command is written to. This will play the audio file.
    subprocess.call(['./youtube.sh'])