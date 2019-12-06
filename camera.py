#camera class this file containing backgroundImage.

from pico2d import *
import random

windowWIDTH = 800
windowHEIGHT = 600


backgroundImage = None
backgroundMusic = None

x = 0
y = 0

cameraXCoord = 0

moveRight = False

moveLeft = False

def enter():
    global backgroundImage
    backgroundImage = load_image("background\\" + str(random.randint(1, 4)) + ".png")
    global backgroundMusic
    backgroundMusic = load_music("sound\\Company_of_Heroes_main_theme.mp3")
    backgroundMusic.set_volume(40)
    backgroundMusic.repeat_play()

def draw():
    global cameraXCoord
    backgroundImage.clip_draw_to_origin(x + cameraXCoord, 0, windowWIDTH, windowHEIGHT, 0, 0)


def handleEvent(mouseX):
    global moveLeft, moveRight
    if 0 < mouseX < 100:
        moveLeft = True
    elif windowWIDTH - 100 < mouseX < windowWIDTH:
        moveRight = True
    else:
        moveLeft = False
        moveRight = False


def update():
    global cameraXCoord
    if moveRight and cameraXCoord < backgroundImage.w - windowWIDTH:
        cameraXCoord += 2
    elif moveLeft and cameraXCoord > 0:
        cameraXCoord -= 2

def exit():
    global backgroundImage
    del(backgroundImage)