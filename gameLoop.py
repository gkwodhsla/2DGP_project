import background
from pico2d import *

def eventLoop():
    global running
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running = False



running = True

while running:
    eventLoop()
    clear_canvas()
    background.draw()
    update_canvas()