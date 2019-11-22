import gameFramework
import camera
import random
import math
import worldObjManager
import characterAttrib

class Cannon:
    cannonBallImage = None
    cannonExplosionImage = None
    pixelPerMeter = (10.0 / 0.2)  # 10pixel 20cm
    shootSpeedKmph = 70
    shootSpeedMpm = (shootSpeedKmph * 1000.0 / 60.0)
    shootSpeedMps = (shootSpeedMpm / 60.0)
    shootSpeedPps = (shootSpeedMps * pixelPerMeter)

    gravitationalAccelerationMps = -9.8
    gravitationalAccelerationPps = (gravitationalAccelerationMps * pixelPerMeter)

    def __init__(self):
        self.size = 60
        self.x = 0.0
        self.y = 80.0
        self.offensePower = 9999
        self.isExplosion = False
        self.frame = 0.0
        self.timePerAction = 0.9
        self.actionPerTime = 1.0 / self.timePerAction
        self.framesPerAction = 14
        self.right = self.x + self.size / 2
        self.left = self.x - self.size / 2
        self.top = self.y + self.size / 2
        self.bottom = self.y - self.size / 2
        self.degree = 0

        self.initVelocity = self.shootSpeedPps
        self.launchAngle = float(random.randint(5, 25))
        self.xVelocity = self.initVelocity * math.cos(math.radians(self.launchAngle))
        self.yVelocity = self.initVelocity * math.sin(math.radians(self.launchAngle))

        if self.cannonBallImage == None:
            self.cannonBallImage = camera.load_image("effectImages\\cannonBall.png")
        if self.cannonExplosionImage == None:
            self.cannonExplosionImage = camera.load_image("effectImages\\explosion.png")

    def update(self):
        self.right=self.x+self.size/2
        self.left=self.x-self.size/2
        self.top=self.y+self.size/2
        self.bottom=self.y-self.size/2 - 10
        self.degree+=5
        if self.isExplosion:
            self.frame = (self.frame + self.framesPerAction * self.actionPerTime * gameFramework.frameTime) % self.framesPerAction
            if(self.frame>=self.framesPerAction-0.3):
                worldObjManager.deleteObject('cannon', self)

        else:
            self.x = self.x + self.xVelocity * gameFramework.frameTime
            self.y = self.y + self.yVelocity * gameFramework.frameTime
            self.yVelocity = self.yVelocity + self.gravitationalAccelerationPps * gameFramework.frameTime

    def draw(self):
        if self.isExplosion:
            self.cannonExplosionImage.clip_draw_to_origin(int(self.frame) * 125, 0, 125, 125,
                                                          self.x-camera.cameraXCoord - self.size, self.y - self.size)
        else:
            #self.cannonBallImage.draw(self.x - camera.cameraXCoord, self.y, self.size, self.size)
            self.cannonBallImage.composite_draw(math.radians(self.degree),'',self.x - camera.cameraXCoord, self.y, self.size, self.size)

    def checkCollision(self):
        if not self.isExplosion:
            isCollision = True
            for enemy in worldObjManager.enemyCharacterList:
                if self.right < enemy.left:
                    isCollision = False
                if self.left > enemy.right:
                    isCollision = False
                if self.bottom > enemy.top:
                    isCollision = False
                if self.top < enemy.bottom:
                    isCollision = False

                if isCollision:
                    self.isExplosion = True
                    worldObjManager.enemyDeathList.append(enemy)
                    worldObjManager.enemyCharacterList.remove(enemy)
                    enemy.state = characterAttrib.DeathState

            if (self.y - self.size <= 0):
                self.isExplosion = True



if __name__ == '__main__':
    ball1 = Cannon()
    while ball1.y >= 0:
        ball1.update()
