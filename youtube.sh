#!/bin/sh
ffmpeg -y $(youtube-dl -g --extract-audio 'http://www.youtube.com/watch?v=i6h4b-Jm8iU' | sed "s/.*/-ss 00:10 -i &/") -t 0:30 -c copy bin/AudioPreview/darkthrone.mp4
cvlc --play-and-exit bin/AudioPreview/darkthrone.mp4