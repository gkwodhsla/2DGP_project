import camera
import gameFramework
import allyCharacter
import worldObjManager

class Coin:
    image = None
    currentMoney = 0
    def __init__(self):
        self.x = camera.windowWIDTH - 100
        self.y = camera.windowHEIGHT - 70
        self.size = 70
        self.updateTime = 0.0
        self.font = camera.load_font('textfile\\Sofija.TTF', 35)
        if self.image is None:
            self.image = camera.load_image('effectImages\\coin.png')

    def update(self):
        self.updateTime += gameFramework.frameTime
        if self.updateTime >= 1.5:
            self.updateTime = 0.0
            self.currentMoney += 7

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.currentMoney, (255, 255, 255))


MOUSE_ON, MOUSE_OUT, MOUSE_CLICK, WAIT = range(4)


class OldScroll:
    scrollImage = None
    def __init__(self):
        self.x = 25
        self.y = camera.windowHEIGHT - 160
        self.width = 450
        self.height = 150
        if self.scrollImage is None:
            self.scrollImage = camera.load_image("effectImages\\oldScroll.png")

    def draw(self):
        self.scrollImage.draw_to_origin(self.x, self.y, self.width, self.height)

class SpearmanRespawnButton:
    clickButtonImage = None
    onButtonImage = None
    outButtonImage = None
    waitButtonImage = None

    def __init__(self):
        self.x = 150
        self.y = camera.windowHEIGHT - 80
        self.size = 80
        self.font = camera.load_font('textfile\\Sofija.TTF', 25)
        self.cost = 10
        self.currentRespawnTime = 0.0
        self.maxRespawnTime = 2.0
        self.state = MOUSE_OUT
        if self.clickButtonImage is None:
            self.clickButtonImage = camera.load_image('button\\knight1Click.png')
        if self.onButtonImage is None:
            self.onButtonImage = camera.load_image('button\\knight1On.png')
        if self.outButtonImage is None:
            self.outButtonImage = camera.load_image('button\\knight1Out.png')
        if self.waitButtonImage is None:
            self.waitButtonImage = camera.load_image('button\\knight1Wait.png')

    def update(self):
        if self.state is WAIT:
            self.currentRespawnTime -= gameFramework.frameTime
            if self.currentRespawnTime <= 0:
                self.state = MOUSE_OUT

    def draw(self):
        if self.state == MOUSE_OUT:
            self.outButtonImage.draw(self.x, self.y, self.size, self.size)
        elif self.state == MOUSE_ON:
            self.onButtonImage.draw(self.x, self.y, self.size, self.size)
        elif self.state == MOUSE_CLICK:
            self.clickButtonImage.draw(self.x, self.y, self.size, self.size)
        else:
            self.waitButtonImage.draw(self.x, self.y, self.size, self.size)
            self.font.draw(self.x - 20, self.y, '(%3.1f)' % self.currentRespawnTime, (255, 0, 0))
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.cost, (255, 255, 255))

    def handleEvent(self, event, coin):
        if self.state is not WAIT:
            if event.type == camera.SDL_MOUSEMOTION:
                if (self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    self.state = MOUSE_ON
                else:
                    self.state = MOUSE_OUT
            elif event.type == camera.SDL_MOUSEBUTTONDOWN:
                if (self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    self.state = MOUSE_CLICK
            elif event.type == camera.SDL_MOUSEBUTTONUP:
                if (self.state is MOUSE_CLICK and self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    if self.makeObjectAndReturn(coin):
                        self.state = WAIT
                        self.currentRespawnTime = self.maxRespawnTime
                    else:
                        self.state = MOUSE_OUT

    def makeObjectAndReturn(self,coin):
        if coin.currentMoney-self.cost >= 0:
            coin.currentMoney -= self.cost
            worldObjManager.addObject(allyCharacter.SpearMan(300, 100), 1)
            return True
        return False


class AxemanRespawnButton:
    clickButtonImage = None
    onButtonImage = None
    outButtonImage = None
    waitButtonImage = None

    def __init__(self):
        self.x = 150 + 100
        self.y = camera.windowHEIGHT - 80
        self.size = 80
        self.font = camera.load_font('textfile\\Sofija.TTF', 25)
        self.cost = 20
        self.currentRespawnTime = 0.0
        self.maxRespawnTime = 3.5
        self.state = MOUSE_OUT
        if self.clickButtonImage is None:
            self.clickButtonImage = camera.load_image('button\\knight2Click.png')
        if self.onButtonImage is None:
            self.onButtonImage = camera.load_image('button\\knight2On.png')
        if self.outButtonImage is None:
            self.outButtonImage = camera.load_image('button\\knight2Out.png')
        if self.waitButtonImage is None:
            self.waitButtonImage = camera.load_image('button\\knight2Wait.png')

    def update(self):
        if self.state is WAIT:
            self.currentRespawnTime -= gameFramework.frameTime
            if self.currentRespawnTime <= 0:
                self.state = MOUSE_OUT

    def draw(self):
        if self.state == MOUSE_OUT:
            self.outButtonImage.draw(self.x, self.y, self.size, self.size)
        elif self.state == MOUSE_ON:
            self.onButtonImage.draw(self.x, self.y, self.size, self.size)
        elif self.state == MOUSE_CLICK:
            self.clickButtonImage.draw(self.x, self.y, self.size, self.size)
        else:
            self.waitButtonImage.draw(self.x, self.y, self.size, self.size)
            self.font.draw(self.x - 20, self.y, '(%3.1f)' % self.currentRespawnTime, (255, 0, 0))
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.cost, (255, 255, 255))

    def handleEvent(self, event, coin):
        if self.state is not WAIT:
            if event.type == camera.SDL_MOUSEMOTION:
                if (self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    self.state = MOUSE_ON
                else:
                    self.state = MOUSE_OUT
            elif event.type == camera.SDL_MOUSEBUTTONDOWN:
                if (self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    self.state = MOUSE_CLICK
            elif event.type == camera.SDL_MOUSEBUTTONUP:
                if (self.state is MOUSE_CLICK and self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    if self.makeObjectAndReturn(coin):
                        self.state = WAIT
                        self.currentRespawnTime = self.maxRespawnTime
                    else:
                        self.state = MOUSE_OUT

    def makeObjectAndReturn(self,coin):
        if coin.currentMoney-self.cost >= 0:
            coin.currentMoney -= self.cost
            worldObjManager.addObject(allyCharacter.AxeMan(300, 100), 1)
            return True
        return False


class SwordmanRespawnButton:
    clickButtonImage = None
    onButtonImage = None
    outButtonImage = None
    waitButtonImage = None

    def __init__(self):
        self.x = 150 + 100 + 100
        self.y = camera.windowHEIGHT - 80
        self.size = 80
        self.font = camera.load_font('textfile\\Sofija.TTF', 25)
        self.cost = 30
        self.currentRespawnTime = 0.0
        self.maxRespawnTime = 5.0
        self.state = MOUSE_OUT
        if self.clickButtonImage is None:
            self.clickButtonImage = camera.load_image('button\\knight3Click.png')
        if self.onButtonImage is None:
            self.onButtonImage = camera.load_image('button\\knight3On.png')
        if self.outButtonImage is None:
            self.outButtonImage = camera.load_image('button\\knight3Out.png')
        if self.waitButtonImage is None:
            self.waitButtonImage = camera.load_image('button\\knight3Wait.png')

    def update(self):
        if self.state is WAIT:
            self.currentRespawnTime -= gameFramework.frameTime
            if self.currentRespawnTime <= 0:
                self.state = MOUSE_OUT

    def draw(self):
        if self.state == MOUSE_OUT:
            self.outButtonImage.draw(self.x, self.y, self.size, self.size)
        elif self.state == MOUSE_ON:
            self.onButtonImage.draw(self.x, self.y, self.size, self.size)
        elif self.state == MOUSE_CLICK:
            self.clickButtonImage.draw(self.x, self.y, self.size, self.size)
        else:
            self.waitButtonImage.draw(self.x, self.y, self.size, self.size)
            self.font.draw(self.x - 20, self.y, '(%3.1f)' % self.currentRespawnTime, (255, 0, 0))
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.cost, (255, 255, 255))

    def handleEvent(self, event, coin):
        if self.state is not WAIT:
            if event.type == camera.SDL_MOUSEMOTION:
                if (self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    self.state = MOUSE_ON
                else:
                    self.state = MOUSE_OUT
            elif event.type == camera.SDL_MOUSEBUTTONDOWN:
                if (self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    self.state = MOUSE_CLICK
            elif event.type == camera.SDL_MOUSEBUTTONUP:
                if (self.state is MOUSE_CLICK and self.x - self.size / 2 <= event.x <= self.x + self.size / 2
                        and self.y - self.size / 2 <= camera.windowHEIGHT - event.y - 1 <= self.y + self.size / 2):
                    if self.makeObjectAndReturn(coin):
                        self.state = WAIT
                        self.currentRespawnTime = self.maxRespawnTime
                    else:
                        self.state = MOUSE_OUT

    def makeObjectAndReturn(self, coin):
        if coin.currentMoney - self.cost >= 0:
            coin.currentMoney -= self.cost
            worldObjManager.addObject(allyCharacter.SwordMan(300, 100), 1)
            return True
        return False
