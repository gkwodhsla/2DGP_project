import gameFramework
import camera
import random
import math

class Cannon:
    image = None
    pixelPerMeter = (10.0 / 0.2)  # 10pixel 20cm
    shootSpeedKmph = 50
    shootSpeedMpm = (shootSpeedKmph * 1000.0 / 60.0)
    shootSpeedMps = (shootSpeedMpm / 60.0)
    shootSpeedPps = (shootSpeedMps * pixelPerMeter)

    gravitationalAccelerationKmph = 9.8
    gravitationalAccelerationMph = (gravitationalAccelerationKmph*1000.0/60.0)
    gravitationalAccelerationMps = (gravitationalAccelerationMph/60.0)
    gravitationalAccelerationPps = (gravitationalAccelerationMps*pixelPerMeter)

    def __init__(self):
        self.size = 70
        self.x = 0.0
        self.y = float(random.randint(200, 350))
        self.offensePower = 9999

        self.initVelocity = self.shootSpeedPps
        self.launchAngle = 45.0
        self.xVelocity = self.initVelocity*math.cos(self.launchAngle)
        self.yVelocity = self.initVelocity*math.sin(self.launchAngle)
        self.weight = 2.0 #2.0kg

        # f = ma
        # pyhisics values
        if self.image == None:
            self.image = camera.load_image("effectImages\\cannonBall.png")

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x - camera.cameraXCoord, self.y, self.size, self.size)

    def checkCollsion(self):
        pass

if __name__=='__main__':
    ball1=Cannon()
    ball1.update()