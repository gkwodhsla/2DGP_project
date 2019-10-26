from characterAttrib import *

numOfImage = 6
knightWalkImageList = [[] for i in range(0, 3)]


# 기사 걷는 이미지가 담긴 리스트.

def loadKnightImage():
    for i in range(0, 6 + 1):
        knightWalkImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
        #knightWalkImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
        #knightWalkImageList[2].append(load_image("Ally\\Knight\\3_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))


# 이미지 로드.



class Knight1(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 100
        self.offensePower = 10

    def draw(self):
        if self.state == CharacterState.WALK:
            knightWalkImageList[0][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                 self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[0][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                 self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x += 0.1

    def checkCollision(self, frontCharacterXpos):
        if self.x + self.size > frontCharacterXpos:
            self.state = CharacterState.IDLE
        else:
            self.state=CharacterState.WALK

    def checkEnemyMeet(self,enemyXpos):
        if self.x + self.size > enemyXpos:
            self.state=CharacterState.IDLE#일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass


class Knight2(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 200
        self.offensePower = 20

    def draw(self):
        if self.state == CharacterState.WALK:
            knightWalkImageList[1][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                 self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[1][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                 self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x += 0.1

    def checkCollision(self, frontCharacterXpos):
        if self.x + self.size > frontCharacterXpos:
            self.state = CharacterState.IDLE
        else:
            self.state=CharacterState.WALK

    def checkEnemyMeet(self,enemyXpos):
        if self.x + self.size > enemyXpos:
            self.state=CharacterState.IDLE#일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass


class Knight3(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 300
        self.offensePower = 30

    def draw(self):
        if self.state == CharacterState.WALK:
            knightWalkImageList[2][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                 self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[2][self.frame % numOfImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                 self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x += 0.1

    def checkCollision(self, frontCharacterXpos):
        if self.x + self.size > frontCharacterXpos:
            self.state = CharacterState.IDLE
        else:
            self.state=CharacterState.WALK

    def checkEnemyMeet(self,enemyXpos):
        if self.x + self.size > enemyXpos:
            self.state=CharacterState.IDLE#일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass
