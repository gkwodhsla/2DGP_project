from characterAttrib import *

loadKnightImage()

class knight1(characterABC):
    state=characterState.WALK

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.frame=0
    def draw(self):
        if(self.state==characterState.WALK):
            walkImageList[self.frame%len(walkImageList)].draw(self.x-camera.cameraXCoord,self.y,100,100)

    def move(self):
        pass

    def update(self):
        if(self.state==characterState.WALK):
            self.frame+=1
            self.x+=1

    def checkCollision(self):
        pass

    def changeState(self):
        pass