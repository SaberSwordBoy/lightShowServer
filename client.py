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
<<<<<<< HEAD
        audio = pygame.mixer.Sound(song_mappings[song_name] + "song.ogg")
=======
        audio = pygame.mixer.Sound(song_mappings[song_name] + "song.ogg")
>>>>>>> efd3fe53bc3b1740e31fc240d0f987b9b2a1e4c2
        audio.play()
    except Exception as e:
        print(e)
        
play_song("MindFreak")