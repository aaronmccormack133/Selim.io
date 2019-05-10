#!/bin/sh
rm -f bin/AudioPreview/*
ffmpeg -y $(youtube-dl -g --extract-audio 'http://www.youtube.com/watch?v=Xtc2Yn6WJQw' | sed "s/.*/-ss 00:10 -i &/") -t 0:30 -c copy bin/AudioPreview/visigoth.mkv
cvlc --play-and-exit bin/AudioPreview/visigoth.mkv