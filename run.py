import time
import os
import pickle
from main import Image2ASCii
from time import sleep
import pygame
from threading import Thread
from moviepy.editor import *


videoPath = "noot.mp4"
audioPath = "noot.mp3"
obj = Image2ASCii(videoPath, 12)
obj.video_ascii()


def audio():
    pygame.mixer.music.play()

audio = Thread(target=audio)

def read():
    pickle_off = open("output.txt", "rb")
    datas = pickle.load(pickle_off)
    video = VideoFileClip(videoPath)
    video.audio.write_audiofile(audioPath)
    pygame.mixer.init()
    pygame.mixer.music.load(audioPath)
    audio.start()
    for data in datas:
        print(data)
        sleep(0.025)

read()

obj = Image2ASCii("img.jpg", 2)
obj.image_ascii()
