import camera
import gameFramework


class Coin:
    image = None

    def __init__(self):
        self.x = camera.windowWIDTH - 100
        self.y = camera.windowHEIGHT - 70
        self.currentMoney = 0
        self.size = 70
        self.updateTime = 0.0
        self.font = camera.load_font('textfile\\Sofija.TTF', 35)
        if self.image is None:
            self.image = camera.load_image('effectImages\\coin.png')

    def update(self):
        self.updateTime += gameFramework.frameTime
        if self.updateTime >= 2.0:
            self.updateTime = 0.0
            self.currentMoney += 3

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.currentMoney, (255, 255, 255))


MOUSE_ON, MOUSE_OUT, MOUSE_CLICK, WAIT = range(4)


class MouseOnState:

    @staticmethod
    def enter():
        pass

    @staticmethod
    def draw(button):
        button.onButtonImage.draw(button.x, button.y, button.size, button.size)

    @staticmethod
    def update():
        pass

class SpearmanRespawnButton:
    clickButtonImage = None
    onButtonImage = None
    outButtonImage = None
    waitButtonImage = None

    def __init__(self):
        self.x = 80
        self.y = camera.windowHEIGHT - 80
        self.size = 80
        self.font = camera.load_font('textfile\\Sofija.TTF', 25)
        self.cost = 10
        self.respawnTime = 2.0
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
        pass
        # 오브젝트의 현재 돈을 알아낸뒤 캐릭터를 생성할수있으면 돈을 차감하고 캐릭터 객체를 생성한다.

    def draw(self):
        self.outButtonImage.draw(self.x, self.y, self.size, self.size)
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.cost, (255, 255, 255))


class AxemanRespawnButton:
    pass


class SwordmanRespawnButton:
    pass
