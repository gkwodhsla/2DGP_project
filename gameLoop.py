import background
from pico2d import *


def eventLoop():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            background.handleEvent(event.x)


running = True

while running:
    eventLoop()

    background.update()

    clear_canvas()
    background.draw()
    update_canvas()
