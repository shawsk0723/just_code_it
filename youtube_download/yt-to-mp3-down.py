import os
from pytube import YouTube
link = input("Enter a youtube video's URL:\n") # i.e. https://youtu.be/dQw4w9WgXcQ
yt = YouTube(link)
filePath = yt.streams.filter(only_audio=True).first().download()
mp3FilePath = filePath.replace('mp4', 'mp3')
os.rename(filePath, mp3FilePath)
print(f'mp3 download complete = {mp3FilePath}')