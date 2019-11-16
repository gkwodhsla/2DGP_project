import camera
import gameFramework
import allyCharacter


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

    def handleEvent(self, mouseXpos, mouseYpos, isClick):
        if (not isClick and self.x - self.size / 2 <= mouseXpos <= self.x + self.size / 2
                and self.y - self.size / 2 <= mouseYpos <= self.y + self.size / 2):
            self.state = MOUSE_ON
        else:
            self.state = MOUSE_OUT
        if (isClick and self.x - self.size / 2 <= mouseXpos <= self.x + self.size / 2
                and self.y - self.size / 2 <= mouseYpos <= self.y + self.size / 2):
            self.state = MOUSE_CLICK
        if not isClick and self.state == MOUSE_CLICK:
            self.state = WAIT

    def makeObjectAndReturn(self):
        # 오브젝트의 현재 돈을 알아낸뒤 캐릭터를 생성할수있으면 돈을 차감하고 캐릭터 객체를 생성한다.
        return allyCharacter.Knight1(300, 100)


class AxemanRespawnButton:
    pass


class SwordmanRespawnButton:
    pass
