#!/bin/sh
ffmpeg -y $(youtube-dl -g --extract-audio 'http://www.youtube.com/watch?v=M_5kdIhx_to' | sed "s/.*/-ss 00:10 -i &/") -t 0:30 -c copy bin/AudioPreview/clip.mp4
cvlc --play-and-exit bin/AudioPreview/clip.mp4