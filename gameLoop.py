# tpye0 = base , type1 = allyCharacter , type2 = enemyCharacter
import camera
from pico2d import *
from base import *
import worldObjManager

def eventLoop():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            camera.handleEvent(event.x)


running = True

allyBase=base("base\\allyBase.png",150,150,True)
enemyBase=base("base\\enemyBase.png",camera.backgroundImage.w-150,150,False)

worldObjManager.addObject(allyBase,0)
worldObjManager.addObject(enemyBase,0)

while running:
    eventLoop()

    camera.update()

    clear_canvas()
    camera.draw()
    worldObjManager.drawObject()
    #allyBase.draw()
    #enemyBase.draw()
    update_canvas()
