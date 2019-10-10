from pico2d import *
import random

windowWIDTH=800
windowHEIGHT=600

open_canvas(windowWIDTH,windowHEIGHT)
#background=load_image("background\\"+str(random.randint(1,5))+".png")
background=load_image("background\\1.png")
x = 0
y = 0

cameraXCoord = 0

def draw():
    background.clip_draw_to_origin(x,0,windowWIDTH,windowHEIGHT,0,0)