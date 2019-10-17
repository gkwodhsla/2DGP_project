# tpye0 = base , type1 = allyCharacter , type2 = enemyCharacter
import camera
from pico2d import *
from base import *
import worldObjManager
import allyCharacter
import enemyCharacter


def eventLoop():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            camera.handleEvent(event.x)


running = True

allyBase = base("base\\allyBase.png", 150, 150, True)
enemyBase = base("base\\enemyBase.png", camera.backgroundImage.w - 150, 150, False)

knight1 = allyCharacter.Knight1(300, 100)
knight2 = allyCharacter.Knight1(300, 100)

ork1 = enemyCharacter.Ork1(1600, 100)
ork2 = enemyCharacter.Ork1(1600,100)

worldObjManager.addObject(allyBase, 0)
worldObjManager.addObject(enemyBase, 0)
worldObjManager.addObject(knight1, 1)
worldObjManager.addObject(knight2,1)
worldObjManager.addObject(ork1, 2)
worldObjManager.addObject(ork2,2)
while running:
    eventLoop()

    camera.update()
    worldObjManager.update()

    clear_canvas()
    camera.draw()
    worldObjManager.drawObject()
    #knight2.draw()#충돌체크를 위해서 남겨놓은것 나중에 지울것.
    #ork2.draw()

    #knight1.checkCollision(knight2.x)#이또한 마찬가지....
    #ork1.checkCollision(ork2.x)

    update_canvas()
