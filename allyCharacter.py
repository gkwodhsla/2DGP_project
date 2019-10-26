from characterAttrib import *
import worldObjManager

numOfWalkImage = 6
numOfAttackImage = 7
numOfDieImage = 6
knightWalkImageList = [[] for i in range(0, 3)]
knightAttackImageList = [[] for i in range(0, 3)]
knightDieImageList = [[] for i in range(0,3)]

# 기사 걷는 이미지가 담긴 리스트.

def loadKnightImage():
    for i in range(0, numOfWalkImage + 1):
        knightWalkImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
        # knightWalkImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
        # knightWalkImageList[2].append(load_image("Ally\\Knight\\3_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
    for i in range(0, numOfAttackImage + 1):
        knightAttackImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_ATTACK\\ATTACK_00" + str(i) + ".png"))
        # knightAttackImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_ATTACK\\ATTACK_00" + str(i) + ".png"))
        # knightAttackImageList[2].append(load_image("Ally\\Knight\\3_KNIGHT\\_ATTACK\\ATTACK_00" + str(i) + ".png"))
    for i in range(0, numOfDieImage + 1):
        knightDieImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_DIE\\_DIE_00" + str(i) + ".png"))
        #knightDieImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_DIE\\_DIE_00" + str(i) + ".png"))
        #knightDieImageList[2].append(load_image("Ally\\Knight\\2_KNIGHT\\_DIE\\_DIE_00" + str(i) + ".png"))

# 이미지 로드.


class Knight1(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 100
        self.offensePower = 1

    def draw(self):
        if self.state == CharacterState.WALK:
            knightWalkImageList[0][self.frame % numOfWalkImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                     self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[0][self.frame % numOfWalkImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                     self.size)
        elif self.state == CharacterState.ATTACK:
            knightAttackImageList[0][self.frame % numOfAttackImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                         self.size)
        elif self.state == CharacterState.DIE:
            knightDieImageList[0][self.frame & numOfDieImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                   self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x += 1

        elif self.state == CharacterState.ATTACK:
            self.frame += 1
            if self.frame % numOfAttackImage == 0:
                worldObjManager.enemyCharacterList[0].hp -= self.offensePower
                if worldObjManager.enemyCharacterList[0].hp <=0:
                    self.state = CharacterState.WALK
                    worldObjManager.enemyCharacterList[0].state = CharacterState.DIE

                    #상대캐릭터가 죽으면 나는 WALK상태가되고 상대는 DIE상태가된다.
        elif self.state == CharacterState.DIE:
            self.frame+=1
            if self.frame == numOfDieImage:
                if (len(worldObjManager.allyDeathList) > 0):
                    worldObjManager.deleteObject(1,self)
                    if (len(worldObjManager.allyCharacterList) > 0):
                        worldObjManager.allyCharacterList[0].state = CharacterState.WALK
        if self.hp<=0:
            return True

        return False

    def checkCollision(self, frontCharacterXpos):
        if self.x + self.size > frontCharacterXpos:
            self.state = CharacterState.IDLE
        else:
            self.state = CharacterState.WALK

    def checkEnemyMeet(self, enemyXpos):
        if self.x + self.size > enemyXpos:
            if self.state != CharacterState.ATTACK and worldObjManager.enemyCharacterList[0].hp>0:
                self.state = CharacterState.ATTACK
                self.frame = 0

    def changeState(self):
        pass


"""
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
            knightWalkImageList[1][self.frame % numOfWalkImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                     self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[1][self.frame % numOfWalkImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
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
            self.state = CharacterState.WALK

    def checkEnemyMeet(self, enemyXpos):
        if self.x + self.size > enemyXpos:
            self.state = CharacterState.IDLE  # 일단 IDLE로 나중에 ATTACK으로 수정할것.

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
            knightWalkImageList[2][self.frame % numOfWalkImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
                                                                     self.size)
        elif self.state == CharacterState.IDLE:
            knightWalkImageList[2][self.frame % numOfWalkImage].draw(self.x - camera.cameraXCoord, self.y, self.size,
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
            self.state = CharacterState.WALK

    def checkEnemyMeet(self, enemyXpos):
        if self.x + self.size > enemyXpos:
            self.state = CharacterState.IDLE  # 일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass
    
"""
