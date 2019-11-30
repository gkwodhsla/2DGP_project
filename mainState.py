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
axeRespawnButton = None
swordRespawnButton = None
font = None
oldScroll = None
cannonPrepareTime = 7.0
curCannonPrepareTime = 0.0


def enter():
    global allyBase, enemyBase
    global coin, spearRespawnButton, axeRespawnButton, swordRespawnButton
    global font
    global oldScroll
    camera.enter()

    # fourth type is base type True: ally
    allyBase = base("base\\allyBase.png", 200, 150, True)
    enemyBase = base("base\\enemyBase.png", camera.backgroundImage.w - 200, 150, False)

    coin = GUI.Coin()
    spearRespawnButton = GUI.SpearmanRespawnButton()
    axeRespawnButton = GUI.AxemanRespawnButton()
    swordRespawnButton = GUI.SwordmanRespawnButton()
    worldObjManager.addObject(allyBase, 0)
    worldObjManager.addObject(enemyBase, 0)
    oldScroll = GUI.OldScroll()
    font = load_font('textfile\\Sofija.TTF', 25)


def exit():
    global allyBase, enemyBase, coin, spearRespawnButton, swordRespawnButton
    del allyBase
    del enemyBase
    # del coin
    # del spearRespawnButton
    camera.exit()
    #characterAttrib.exit()
    worldObjManager.deleteAllObjects()


def pause():
    pass


def resume():
    pass


def handle_events():
    global curCannonPrepareTime
    events = get_events()
    for event in events:
        spearRespawnButton.handleEvent(event, coin)
        axeRespawnButton.handleEvent(event, coin)
        swordRespawnButton.handleEvent(event,coin)
        if event.type == SDL_QUIT:
            gameFramework.running = False
        elif event.type == SDL_MOUSEMOTION:
            camera.handleEvent(event.x)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                worldObjManager.addObject(allyCharacter.SwordMan(300, 100), 1)
            elif event.key == SDLK_1:
                worldObjManager.addObject(enemyCharacter.AxeOrk(1600, 100), 2)
            elif event.key == SDLK_SPACE:
                if curCannonPrepareTime <= 0.0:
                    for i in range(4):
                        worldObjManager.addObject(cannon.Cannon(), 3)
                    curCannonPrepareTime = cannonPrepareTime


def update():
    global curCannonPrepareTime
    worldObjManager.update()
    camera.update()
    coin.update()
    spearRespawnButton.update()
    axeRespawnButton.update()
    swordRespawnButton.update()
    if curCannonPrepareTime >= 0.0:
        curCannonPrepareTime -= gameFramework.frameTime


def draw():
    clear_canvas()
    camera.draw()
    coin.draw()
    oldScroll.draw()
    spearRespawnButton.draw()
    axeRespawnButton.draw()
    swordRespawnButton.draw()
    worldObjManager.drawObject()
    if curCannonPrepareTime <= 0:
        font.draw(300, 50, 'cannon is ready press spacebar!!!', (255, 255, 255))
    else:
        font.draw(300, 50, 'cannon is preparing plz wait...', (255, 255, 255))
    update_canvas()
