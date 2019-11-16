# tpye0 = base , type1 = allyCharacter , type2 = enemyCharacter
import camera
from pico2d import *
from base import *
import worldObjManager
import allyCharacter
import enemyCharacter
import gameFramework
import characterAttrib
import cannon
import GUI

allyBase = None
enemyBase = None
coin = None
spearRespawnButton = None

def enter():
    global allyBase, enemyBase
    global coin, spearRespawnButton
    camera.enter()
    allyCharacter.loadKnightImage()
    enemyCharacter.loadOrkImage()
    # fourth type is base type True: ally
    allyBase = base("base\\allyBase.png", 200, 150, True)
    enemyBase = base("base\\enemyBase.png", camera.backgroundImage.w - 200, 150, False)

    coin = GUI.Coin()
    spearRespawnButton=GUI.SpearmanRespawnButton()

    worldObjManager.addObject(allyBase, 0)
    worldObjManager.addObject(enemyBase, 0)


def exit():
    global allyBase, enemyBase, coin
    del allyBase
    del enemyBase
    del coin
    camera.exit()
    characterAttrib.exit()
    worldObjManager.deleteAllObjects()

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
            camera.handleEvent(event.x)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                worldObjManager.addObject(allyCharacter.Knight1(300, 100), 1)
            elif event.key == SDLK_1:
                worldObjManager.addObject(enemyCharacter.Ork1(1600, 100), 2)
            elif event.key  == SDLK_SPACE:
                worldObjManager.addObject(cannon.Cannon(),3)


def update():
    global coin
    worldObjManager.update()
    camera.update()
    coin.update()

def draw():
    global coin
    clear_canvas()
    camera.draw()
    coin.draw()
    spearRespawnButton.draw()
    worldObjManager.drawObject()
    update_canvas()
