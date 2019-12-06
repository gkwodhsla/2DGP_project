import camera
import endState
import gameFramework


class AllyBase:
    def __init__(self, imageDir, baseXpos, baseYpos):
        self.image = camera.load_image(imageDir)
        self.x = baseXpos
        self.y = baseYpos
        self.size = 300
        self.hp = 500
        self.hpBarHeigth = 10
        self.hpBarImage = camera.load_image("effectImages\\hpBar.png")

    def draw(self):
        self.hpBarImage.draw(self.x - camera.cameraXCoord, self.y + self.size / 2, self.hp / 2, self.hpBarHeigth)
        self.image.composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y, self.size, self.size)

    def calcHp(self, _hp):
        self.hp -= _hp
        if self.hp <= 0:
            endState.isVictory = False
            gameFramework.change_state(endState)


class EnemyBase:
    def __init__(self, imageDir, baseXpos, baseYpos):
        self.image = camera.load_image(imageDir)
        self.x = baseXpos
        self.y = baseYpos
        self.size = 300
        self.hp = 500
        self.hpBarHeigth = 10
        self.hpBarImage = camera.load_image("effectImages\\enemyHpBar.png")
        self.enemyRespawnTime = 0.0

    def draw(self):
        self.hpBarImage.draw(self.x - camera.cameraXCoord, self.y + self.size / 2, self.hp / 2, self.hpBarHeigth)
        self.image.draw(self.x - camera.cameraXCoord, self.y, self.size, self.size)

    def calcHp(self, _hp):
        self.hp -= _hp
        if self.hp <= 0:
            endState.isVictory = True
            gameFramework.change_state(endState)

    def update(self):
        self.enemyRespawnTime += gameFramework.frameTime
        if self.enemyRespawnTime >= 7.0:
            self.enemyRespawnTime = 0.0
            return True
