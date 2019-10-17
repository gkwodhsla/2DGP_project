from characterAttrib import *

loadKnightImage()

class Knight1(CharacterABC):
    state=CharacterState.WALK
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.frame=0
    def draw(self):
        if(self.state==CharacterState.WALK):
            walkImageList[self.frame%len(walkImageList)].draw(self.x-camera.cameraXCoord,self.y,self.size,self.size)
        elif(self.state==CharacterState.IDLE):
            walkImageList[self.frame % len(walkImageList)].draw(self.x - camera.cameraXCoord, self.y, self.size,self.size)

    def move(self):
        pass

    def update(self):
        if(self.state==CharacterState.WALK):
            self.frame+=1
            self.x+=0.1

    def checkCollision(self,frontCharacterXpos):
        if(self.x+self.size>frontCharacterXpos):
            self.state=CharacterState.IDLE

    def changeState(self):
        pass