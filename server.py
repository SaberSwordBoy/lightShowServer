import os
import sys
import time
import board
import random
import neopixel
from flask import request, Flask
from flask_restful import Api, Resource

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FLASK AND NEOPIXEL SETUP
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

LEDCOUNT = 300
pixels = neopixel.NeoPixel(board.D18,LEDCOUNT)
app = Flask(__name__)
api = Api(app)

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# COLORS AND VARIABLES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

red     = (255,0,0)
blue    = (0,0,255)
green   = (0,255,0)
yellow  = (255,255,0)
magenta = (255,0,255)
white   = (255,255,255)
black   = (0,0,0)

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FUNCTIONS AND LIGHT SEQUENCES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def allWhite(): pixels.fill(white)
def allRed(): pixels.fill(red)
def allBlue(): pixels.fill(blue)
def allGreen(): pixels.fill(green)
def allOff(): pixels.fill(black)
def allMagenta(): pixels.fill(magenta)
def allYellow(): pixels.fill(yellow)

def redGreenToCenter():
    start=0
    end=LEDCOUNT
    middle=LEDCOUNT//2
    loc=end-1
    for i in range(start,middle):
        pixels[i] = red
        pixels[loc] = green
        loc -= 1
        
def greenRedToCenter():
    start=0
    end=LEDCOUNT
    middle=LEDCOUNT//2
    loc=end-1
    for i in range(start,middle):
        pixels[i] = green
        pixels[loc] = red
        loc -= 1

def blueMagentaToCenter():
    start = 0
    end = LEDCOUNT
    middle = LEDCOUNT//2
    loc = end-1
    for i in range(start, middle):
        pixels[i] = blue
        pixels[loc] = magenta
        loc -= 1

def magentaBlueToCenter():
    start = 0
    end = LEDCOUNT
    middle = LEDCOUNT//2
    loc = end-1
    for i in range(start, middle):
        pixels[i] = magenta
        pixels[loc] = blue
        loc -= 1
        
# Map functions to names so we can call them using the API
mappings = { 
    "allRed": allRed,
    "allWhite": allWhite,
    "allBlue": allBlue,
    "allGreen": allGreen,
    "allOff": allOff,
    "allBlack": allOff,
    "allYellow": allYellow,
    "allMagenta": allMagenta,
    "redGreenToCenter": redGreenToCenter,
    "greenRedToCenter": greenRedToCenter,
    "magentaBlueToCenter": magentaBlueToCenter,
    "blueMagentaToCenter": blueMagentaToCenter
    
}

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# API RESOURCES AND PAGES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Index(Resource):
    """Index page. Nothing usefull here!"""
    def get(self):
        return "Hello, world! This page won't help you!"

class ExecFunc(Resource):
    """Execute function based on supplied argument"""
    def get(self):
        return "Submit a POST request"
    def post(self):
        func_name = request.form['func']
        try:
            mappings[func_name]()
            return f"Success! Function '{func_name}' executed! ✅"
        except KeyError:
            return f"That function '{func_name}' does not exists. ☠️", 500

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# SET RESOURCES AND RUN RUN APP
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

api.add_resource(Index, "/")
api.add_resource(ExecFunc, '/exec')
if __name__ == "__main__":
    app.run("0.0.0.0", 80)