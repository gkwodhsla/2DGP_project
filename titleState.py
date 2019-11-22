from pico2d import *
import characterAttrib
import gameFramework
import camera
import mainState

startButtonImages = None
quitButtonImages = None
backGroundImages = None

ButtonDown, ButtonOn, ButtonUP = 0, 1, 2

startButtonState = ButtonUP
quitButtonState = ButtonUP

startButtonXpos = 250
startButtonYpos = 350

quitButtonXpos = 250
quitButtonYpos = 150


def enter():
    global startButtonImages, quitButtonImages, backGroundImages
    startButtonImages = load_image("button\\startButton.png")
    quitButtonImages = load_image("button\\quitButton.png")
    backGroundImages = load_image("background\\1.png")


def exit():
    global startButtonImages, quitButtonImages, backGroundImages
    del startButtonImages
    del quitButtonImages
    del backGroundImages


def pause():
    pass


def resume():
    pass


def handle_events():
    global startButtonState, quitButtonState
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gameFramework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = camera.windowHEIGHT - event.y
            if startButtonXpos <= mouseX <= startButtonXpos + 300 and startButtonYpos <= mouseY <= startButtonYpos + 150:
                startButtonState = ButtonOn
            else:
                startButtonState = ButtonUP
            if quitButtonXpos <= mouseX <= quitButtonXpos + 300 and quitButtonYpos <= mouseY <= quitButtonYpos + 150:
                quitButtonState = ButtonOn
            else:
                quitButtonState = ButtonUP
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouseX = event.x
            mouseY = camera.windowHEIGHT - event.y
            if startButtonXpos <= mouseX <= startButtonXpos + 300 and startButtonYpos <= mouseY <= startButtonYpos + 150:
                startButtonState = ButtonDown
            else:
                startButtonState = ButtonUP
            if quitButtonXpos <= mouseX <= quitButtonXpos + 300 and quitButtonYpos <= mouseY <= quitButtonYpos + 150:
                quitButtonState = ButtonDown
            else:
                quitButtonState = ButtonUP
        elif event.type == SDL_MOUSEBUTTONUP:
            mouseX = event.x
            mouseY = camera.windowHEIGHT - event.y
            if startButtonXpos <= mouseX <= startButtonXpos + 300 and startButtonYpos <= mouseY <= startButtonYpos + 150:
                gameFramework.change_state(mainState)
            else:
                startButtonState = ButtonUP
            if quitButtonXpos <= mouseX <= quitButtonXpos + 300 and quitButtonYpos <= mouseY <= quitButtonYpos + 150:
                gameFramework.running = False
            else:
                quitButtonState = ButtonUP

def update():
    pass


def draw():
    global startButtonImages, quitButtonImages
    clear_canvas()
    backGroundImages.draw_to_origin(0, 0, 800, 600)
    startButtonImages.clip_draw_to_origin(0, 150 * startButtonState, 300, 150, startButtonXpos, startButtonYpos)

    quitButtonImages.clip_draw_to_origin(0, 150 * quitButtonState, 300, 150, quitButtonXpos, quitButtonYpos)
    update_canvas()
