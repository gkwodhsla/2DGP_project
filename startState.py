from pico2d import *
import characterAttrib
import gameFramework
import titleState
font = None
backGroundImage = None
percentage = 0
i = 0

def enter():
    global font, backGroundImage
    font = load_font('textfile\\Sofija.TTF', 60)
    backGroundImage = load_image("effectImages\\start.png")


def exit():
    global font, backGroundImage
    del font
    del backGroundImage


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    global percentage, i
    if i == 0:
        i += 1
    elif i == 1:
        characterAttrib.loadOrkImage()
        percentage = 50
        i+=1
    elif i == 2:
        characterAttrib.loadKnightImage()
        i += 1
    elif i == 3:
        gameFramework.change_state(titleState)


def draw():
    global font, backGroundImage
    clear_canvas()
    backGroundImage.draw_to_origin(0,0,800,600)
    font.draw(150, 300, 'Now    loading......    %d' %percentage, (0, 0, 0))
    update_canvas()
