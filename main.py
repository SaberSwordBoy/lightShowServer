import neopixel
import board
import time
import random
from flask import Flask, request
from flask_restful import Resource, Api

NUM_PIXELS = 300
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)

def _randColor():
    return random.randint(0,255)

def randomColor(): pixels.fill((_randColor(),_randColor(),_randColor()))
def allRed():      pixels.fill((255,0,0))
def allBlue():     pixels.fill((0,0,255))
def allGreen():    pixels.fill((0,255,0))
def turnOff():     pixels.fill((0,0,0))

def explodeFromCenter():
    center_px = NUM_PIXELS//2
    start=0
    end=NUM_PIXELS-1
    pixels.fill((255,0,255))
    
def explodeToCenter():
    center_px = NUM_PIXELS//2
    start=0
    end=NUM_PIXELS-1
    for i in range(start,center_px+1):
        pixels[i]  = (255,0,0)
        pixels.show()
        pixels[end]=(0,255,0)
        pixels.show()
        end-=1
        
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
        
def rainbow_cycle(wait=0):
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show() 
        time.sleep(wait)

app = Flask(__name__)
api = Api(app)

class Index(Resource):
	def get(self):
		return {'hello':'world'}

class LightSequence(Resource):
    def get(self):
        return "Submit a post request"
    def post(self):
        func_name = request.form['func']
        print(f"[!] EXECUTING - {func_name}")
        exec(f"{func_name}()")
        return f":thumbsup: Executing {func_name}()"

class SetColor(Resource):
    def post(self):
        color=[]
        for i in request.form["color"].split(","): color.append(int(i))
        pixels.fill(color)
        
api.add_resource(Index,"/")
api.add_resource(LightSequence, "/lights")
api.add_resource(SetColor, '/color')
if __name__ == "__main__":
	app.run("0.0.0.0", 80)
