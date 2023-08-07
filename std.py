#! /home/linus/src/python/project/env01/bin/python3
#

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=0hUtMciwzwE")
print("ready to download...")

yt.streams.first().download()
print("finished download.")


