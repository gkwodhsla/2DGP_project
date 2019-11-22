from pico2d import *
import gameFramework
import titleState

victoryImage = None
defeatImage = None
isVictory = None
showTime = 0.0


def enter():
    global victoryImage, defeatImage
    victoryImage = load_image('effectImages\\victory.png')
    defeatImage = load_image("effectImages\\defeat.png")


def exit():
    global victoryImage, defeatImage
    del victoryImage
    del defeatImage


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    global showTime
    showTime += gameFramework.frameTime
    if showTime >= 4.0:
        gameFramework.change_state(titleState)


def draw():
    global victoryImage, defeatImage
    clear_canvas()
    if isVictory:
        victoryImage.draw_to_origin(250, 100, 800, 400)
    else:
        defeatImage.draw_to_origin(250, 100, 800, 400)
    update_canvas()
