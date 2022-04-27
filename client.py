from imp import source_from_cache
import os
from re import S
import time
import json
import pygame
import requests
import threading
import pyglet

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# INITIALIZE MIXER AND SETTINGS VARIABLES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

pygame.mixer.init()
URL = "http://192.168.1.4/exec"

song_mappings = {
    "MindFreak": "music/MindFreak/",
    "Believer": "music/Believer/"
}

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FUNCTIONS AND OTHER STUFF
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def play_song(song_name):
    mappings = json.load(open(song_mappings[song_name] + "mappings.json"))["mapping"]
    
    #sound = pyglet.resource.media(song_mappings[song_name] + "song.mp3", streaming=False)
    #sound.play()
    pygame.mixer.music.load(song_mappings[song_name] + "song.ogg")
    pygame.mixer.music.play()
    
    start_time = time.time()
    running = True
    while running:
        try:
            current_time = round(time.time()-start_time, 1)
            func = mappings.get(str(current_time))
            
            print(current_time, pygame.mixer.music.get_pos(), func)
            
            if func:
                req = requests.post(URL, data={"func": func})
                print(req.json(), req.status_code)
                
        except KeyboardInterrupt:
            requests.post(URL, data={"func": "allOff"})
            return
        
        time.sleep(0.1)
        
    print(round(time.time() - start_time, 2))

play_song("MindFreak")
