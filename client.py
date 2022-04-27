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
    "MindFreak": "music/MindFreak/",
    "Believer": "music/Believer/"
}

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FUNCTIONS AND OTHER STUFF
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def play_song(song_name):
    mappings = json.load(open(song_mappings[song_name] + "mappings.json"))["mapping"]
    audio = pygame.mixer.Sound(song_mappings[song_name] + "song.ogg")
    start_time = time.time()
    audio.play()
    for i in range(1,210*60):
        try:
            current_time = round(time.time() - start_time, 2)
            func = mappings.get(str(round(current_time, 1)))
            print(i, current_time, round(current_time, 1), func)
            if func:
                requests.post(URL, data={"func": func})
            time.sleep(0.1)
        except KeyboardInterrupt:
            requests.post(URL, data={"func": "allOff"})
            return
    print(round(time.time() - start_time, 2))

play_song("Believer")