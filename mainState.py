# tpye0 = base , type1 = allyCharacter , type2 = enemyCharacter
import camera
from pico2d import *
from base import *
import worldObjManager
import allyCharacter
import enemyCharacter
import gameFramework

allyBase=None
enemyBase=None

def enter():
    global allyBase , enemyBase
    camera.enter()
    allyCharacter.loadKnightImage()
    enemyCharacter.loadOrkImage()
    allyBase = base("base\\allyBase.png", 200, 150, True)
    enemyBase = base("base\\enemyBase.png", camera.backgroundImage.w - 200, 150, False)

    worldObjManager.addObject(allyBase, 0)
    worldObjManager.addObject(enemyBase, 0)

def exit():
    global allyBase,enemyBase
    del(allyBase)
    del(enemyBase)
    allyCharacter.exit()
    enemyCharacter.exit()
    camera.exit()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            gameFramework.running=False
        elif event.type == SDL_MOUSEMOTION:
            camera.handleEvent(event.x)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                worldObjManager.addObject(allyCharacter.Knight1(300,100),1)
            elif event.key==SDLK_1:
                worldObjManager.addObject(enemyCharacter.Ork1(1600,100),2)


def update():
    worldObjManager.update()
    camera.update()


def draw():
    clear_canvas()
    camera.draw()
    worldObjManager.drawObject()
    update_canvas()