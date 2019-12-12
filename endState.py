from pico2d import *
import gameFramework
import camera
import characterAttrib
import titleState

victoryImage = None
defeatImage = None
isVictory = None
showTime = 0.0
victorySound = None
defeatSound = None


def enter():
    global showTime
    showTime = 0.0
    camera.backgroundMusic.stop()
    global victoryImage, defeatImage, victorySound, defeatSound
    victoryImage = load_image('effectImages\\victory.png')
    defeatImage = load_image("effectImages\\defeat.png")
    victorySound = load_wav("sound\\win.wav")
    defeatSound = load_wav("sound\\lose.wav")
    victorySound.set_volume(128)
    defeatSound.set_volume(128)
    if isVictory:
        victorySound.play()
    else:
        defeatSound.play()


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
