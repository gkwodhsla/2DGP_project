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
        if self.updateTime>=2.0:
            self.updateTime=0.0
            self.currentMoney+=3

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)
        self.font.draw(self.x - 20, self.y - 50, '%d' % self.currentMoney, (255, 255, 255))


class SpearmanRespawnButton:
    clickButtonImage = None
    onButtonImage = None
    outButtonImage = None
    waitButtonImage = None

    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class AxemanRespawnButton:
    pass


class SwordmanRespawnButton:
    pass
