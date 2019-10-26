#최초에 이 파이썬 파일에서 캔버스를 엽니다.

from pico2d import *
import random

windowWIDTH = 800
windowHEIGHT = 600


backgroundImage = None

x = 0
y = 0

cameraXCoord = 0

moveRight = False

moveLeft = False

def enter():
    global backgroundImage
    backgroundImage = load_image("background\\" + str(random.randint(1, 4)) + ".png")

def draw():
    global cameraXCoord
    backgroundImage.clip_draw_to_origin(x + cameraXCoord, 0, windowWIDTH, windowHEIGHT, 0, 0)


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
    if moveRight and cameraXCoord < backgroundImage.w - windowWIDTH:
        cameraXCoord += 2
    elif moveLeft and cameraXCoord > 0:
        cameraXCoord -= 2

def exit():
    global backgroundImage
    del(backgroundImage)