import os
import time
import pygame
import requests
from music.Believer import script as  BV
from music.MindFreak import script as MF 

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# INITIALIZE MIXER AND SETTINGS VARIABLES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

pygame.mixer.init()
URL = "http://192.168.1.31/exec"

BV.URL = URL
MF.URL = URL

song_mappings = {
    "Believer": BV,
    "MindFreak": MF
}

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FUNCTIONS AND OTHER STUFF
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def play_song(song_name):
    try:
        song_mappings[song_name].start()
        return "Started!"
    except KeyError:
        return "That song doesn't exist!"
