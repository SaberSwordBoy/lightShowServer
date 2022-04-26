import os
import time
import json
import pygame
import requests

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# INITIALIZE MIXER AND SETTINGS VARIABLES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

pygame.mixer.init()
URL = "http://192.168.1.31/exec"

song_mappings = {
    "MindFreak": "music/MindFreak/"
}

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FUNCTIONS AND OTHER STUFF
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def play_song(song_name):
    try:
        audio = pygame.mixer.load(song_mappings[song_name] + "music.mp3")
        audio.play()
    except Exception as e:
        print(e)