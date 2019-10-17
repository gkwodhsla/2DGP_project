from characterAttrib import *

numOfImage = 6
orkWalkImageList = [[] for i in range(0, 3)]


def loadOrkImage():
    for i in range(0, 6 + 1):
        orkWalkImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\WALK\\WALK_00" + str(i) + ".png"))


loadOrkImage()


class Ork1(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0

    def draw(self):
        if self.state == CharacterState.WALK:
            orkWalkImageList[0][self.frame % numOfImage].composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y,
                                                                        self.size, self.size)
        elif self.state == CharacterState.IDLE:
            orkWalkImageList[0][self.frame % numOfImage].composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y,
                                                                        self.size, self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x -= 0.2

    def checkCollision(self, frontCharacterXpos):
        if self.x < frontCharacterXpos+self.size:
            self.state = CharacterState.IDLE
        else:
            self.state=CharacterState.WALK
    def checkEnemyMeet(self,enemyXpos):
        if self.x < enemyXpos + self.size:
            self.state=CharacterState.IDLE#일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass
