# tpye0 = base , type1 = allyCharacter , type2 = enemyCharacter
import camera
from pico2d import *
from base import *
import worldObjManager
import allyCharacter

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



knight1=allyCharacter.knight1(300,100)

worldObjManager.addObject(allyBase,0)
worldObjManager.addObject(enemyBase,0)
worldObjManager.addObject(knight1,1)

while running:
    eventLoop()

    camera.update()

    clear_canvas()
    camera.draw()
    worldObjManager.drawObject()
    worldObjManager.update()

    update_canvas()
