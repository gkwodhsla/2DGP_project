import gameFramework
import camera
import random
import math


class Cannon:
    image = None
    pixelPerMeter = (10.0 / 0.2)  # 10pixel 20cm
    shootSpeedKmph = 35
    shootSpeedMpm = (shootSpeedKmph * 1000.0 / 60.0)
    shootSpeedMps = (shootSpeedMpm / 60.0)
    shootSpeedPps = (shootSpeedMps * pixelPerMeter)

    gravitationalAccelerationKmph = -9.8
    gravitationalAccelerationMph = (gravitationalAccelerationKmph * 1000.0 / 60.0)
    gravitationalAccelerationMps = (gravitationalAccelerationMph / 60.0)
    gravitationalAccelerationPps = (gravitationalAccelerationMps * pixelPerMeter)

    def __init__(self):
        self.size = 70
        self.x = 0.0
        self.y = 0.0  # float(random.randint(150, 250))
        self.offensePower = 9999

        self.initVelocity = self.shootSpeedPps
        self.launchAngle = 30
        self.xVelocity = self.initVelocity * math.cos(math.radians(self.launchAngle))
        self.yVelocity = self.initVelocity * math.sin(math.radians(self.launchAngle))
        self.yVelocityBefore = self.yVelocity
        self.xVelocityBefore = self.xVelocity

        # pyhisics values
        if self.image == None:
            self.image = camera.load_image("effectImages\\cannonBall.png")

    def update(self):
        accelation = self.gravitationalAccelerationPps
        self.yVelocity = self.yVelocity + gameFramework.frameTime * accelation
        self.x = self.x + ((self.xVelocity + self.xVelocityBefore) / 2) * gameFramework.frameTime
        self.y = self.y + ((self.yVelocity + self.yVelocityBefore) / 2) * gameFramework.frameTime
        self.xVelocityBefore = self.xVelocity
        self.yVelocityBefore = self.yVelocity

    def draw(self):
        self.image.draw(self.x - camera.cameraXCoord, self.y, self.size, self.size)

    def checkCollsion(self):
        pass


if __name__ == '__main__':
    ball1 = Cannon()
    while ball1.y >= 0:
        ball1.update()
