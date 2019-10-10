from pico2d import *
import random

windowWIDTH = 800
windowHEIGHT = 600

open_canvas(windowWIDTH, windowHEIGHT)

background = load_image("background\\" + str(random.randint(1, 5)) + ".png")

x = 0
y = 0

cameraXCoord = 0

moveRight = False

moveLeft = False


def draw():
    global cameraXCoord
    background.clip_draw_to_origin(x + cameraXCoord, 0, windowWIDTH, windowHEIGHT, 0, 0)


def handleEvent(mouseX):
    global moveLeft, moveRight
    if 0 < mouseX < 150:
        moveLeft = True
    elif windowWIDTH - 150 < mouseX < windowWIDTH:
        moveRight = True
    else:
        moveLeft = False
        moveRight = False


def update():
    global cameraXCoord
    if moveRight and cameraXCoord < background.w - windowWIDTH:
        cameraXCoord += 2
    elif moveLeft and cameraXCoord > 0:
        cameraXCoord -= 2
