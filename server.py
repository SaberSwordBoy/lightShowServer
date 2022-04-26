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
# FUNCTIONS AND LIGHT SEQUENCES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def allWhite(): pixels.fill((255,255,255))
def allRed(): pixels.fill((255,0,0))
def allBlue(): pixels.fill((0,0,255))
def allGreen(): pixels.fill((0,255,0))
def allOff(): pixels.fill((0,0,0))

mappings = {
    "allRed": allRed,
    "allWhite": allWhite,
    "allBlue": allBlue,
    "allGreen": allGreen,
    "allOff": allOff,
    "allBlack": allOff
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
            return f"That function '{func_name}' does not exists. ☠️"

api.add_resource(Index, "/")
api.add_resource(ExecFunc, '/exec')
if __name__ == "__main__":
    app.run("0.0.0.0", 80)