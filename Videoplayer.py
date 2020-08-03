import pygame
import os
import time
from moviepy.editor import *

def play_video(name):
    pygame.init()
    # video = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption(name)

    pack = "E3P"
    current_dir = os.path.dirname(__file__)

    # clip = VideoFileClip(f'{os.path.dirname(__file__)}\\YouTube\\Videos\\{name}.mp4')
    clip = VideoFileClip(os.path.join(current_dir, pack, "YouTube", "Videos", f"{name}.mp4"))
    time.sleep(3)
    clip.preview()

    screen = pygame.display.set_mode((1280 + 500, 720))
    pygame.display.set_caption("Ellie")

# play_video("INVISIBLE by Chocolat3")