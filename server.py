import os
import sys
import time
import board
import random
import neopixel
from flask import request, Flask
from flask_restful import Api, Resource

LEDCOUNT = 300

pixels = neopixel.NeoPixel(board.D18,LEDCOUNT)
app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return "Hello, world! This page won't help you!"

api.add_resource(Index, "/")
if __name__ == "__main__":
    app.run("0.0.0.0", 80)