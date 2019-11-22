import camera
import endState
import gameFramework

class base:

    def __init__(self, imageDir, baseXpos, baseYpos, isAllyBase):
        self.image = camera.load_image(imageDir)
        self.x = baseXpos
        self.y = baseYpos
        self.size = 300
        self.isAllyBase = isAllyBase
        self.hp = 500
        self.hpBarHeigth = 10
        if(isAllyBase):
            self.hpBarImage=camera.load_image("effectImages\\hpBar.png")
        else:
            self.hpBarImage=camera.load_image("effectImages\\enemyHpBar.png")

    def draw(self):
        if self.isAllyBase:
            self.hpBarImage.draw(self.x-camera.cameraXCoord,self.y + self.size/2,self.hp/2,self.hpBarHeigth)
            self.image.composite_draw(0, 'h', self.x-camera.cameraXCoord, self.y,self.size,self.size)
        else:
            self.hpBarImage.draw(self.x - camera.cameraXCoord, self.y + self.size / 2, self.hp / 2, self.hpBarHeigth)
            self.image.draw(self.x-camera.cameraXCoord, self.y,self.size,self.size)

    def calcHp(self,_hp):
        self.hp -= _hp
        if self.hp <= 0:
            if self.isAllyBase:
                endState.isVictory = False
                gameFramework.change_state(endState)
            else:
                endState.isVictory = True
                gameFramework.change_state(endState)
