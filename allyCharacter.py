from characterAttrib import *

numOfImage = 6
knightWalkImageList = [[] for i in range(0, 3)]


def loadKnightImage():
    for i in range(0, 6 + 1):
        knightWalkImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))

loadKnightImage()

class Knight1(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0

    def draw(self):
        if self.state == CharacterState.WALK:
            knightWalkImageList[0][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[0][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x += 0.1

    def checkCollision(self, frontCharacterXpos):
        if self.x + self.size > frontCharacterXpos:
            self.state = CharacterState.IDLE

    def changeState(self):
        pass
