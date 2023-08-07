from pytube import YouTube
import os
from tqdm import trange
from time import sleep

def LowResolution(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(progressive=True, file_extension="mp4").get_lowest_resolution()
    
    try:
        youtubeObject.download()
        for i in trange(0, 10, desc="Progress: "):
            sleep(.1)
    except Exception as ex:
        print(ex)
    print("Video has been downloaded in the lowest resolution")
    input("")

def HighResolution(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(progressive=True, file_extension="mp4").get_by_itag(22)
    
    try:
        youtubeObject.download()
        for i in trange(0, 10, desc="Progress: "):
            sleep(.1)
    except Exception as ex:
        print(ex)
    print("Video has been downloaded in the highest resolution")
    input("")

def AudioOnly(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).get_by_itag(140)
    
    try:
        youtubeObject.download()
        for i in trange(0, 10, desc="Progress: "):
            sleep(.1)
    except Exception as ex:
        print(ex)
    print("Audio has been downloaded")
    input("")

os.system("cls")

option = input('''
[1] Low Resolution (.mp4)
[2] High Resolution (.mp4)
[3] Audio Only (.mp4)

[#] Choose: ''')

link = input("Enter the YouTube video URL: ")

if option == "1":
    LowResolution(link)
elif option == "2":
    HighResolution(link)
elif option == "3":
    AudioOnly(link)