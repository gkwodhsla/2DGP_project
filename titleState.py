from pico2d import *
import characterAttrib
import gameFramework
import camera

startButtonImages = None
quitButtonImages = None

ButtonOn, ButtonDown, ButtonUP = 0, 1, 2

startButtonState = ButtonUP
quitButtonState = ButtonUP

startButtonXpos = 250
startButtonYpos = 350

quitButtonXpos = 250
quitButtonYpos = 150


def enter():
    global startButtonImages, quitButtonImages
    startButtonImages = load_image("button\\startButton.png")
    quitButtonImages = load_image("button\\quitButton.png")


def exit():
    global startButtonImages, quitButtonImages
    del startButtonImages
    del quitButtonImages


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gameFramework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = camera.windowHEIGHT - event.y
            if startButtonXpos <= mouseX <= startButtonXpos + 150 and startButtonYpos<=mouseY<=startButtonYpos+150:
                startButtonState=


        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                worldObjManager.addObject(allyCharacter.Knight1(300, 100), 1)
            elif event.key == SDLK_1:
                worldObjManager.addObject(enemyCharacter.Ork1(1600, 100), 2)
            elif event.key == SDLK_SPACE:
                for i in range(2):
                    worldObjManager.addObject(cannon.Cannon(), 3)


def update():
    pass


def draw():
    global startButtonImages, quitButtonImages
    clear_canvas()
    startButtonImages.clip_draw_to_origin(0, 150 * startButtonState, 300, 150, startButtonXpos, startButtonYpos)
    quitButtonImages.clip_draw_to_origin(0, 150 * quitButtonState, 300, 150, startButtonXpos, startButtonYpos)
    update_canvas()
