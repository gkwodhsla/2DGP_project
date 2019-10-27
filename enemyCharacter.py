from characterAttrib import *
import worldObjManager

numOfWalkImage = 6
numOfAttackImage = 6
numOfDieImage = 6
orkWalkImageList = [[] for i in range(0, 3)]
orkAttackImageList = [[] for i in range(0, 3)]
orkDieImageList = [[] for i in range(0, 3)]

hpBarImage = None

hpBarPos = 10
hpBarHeigt = 10

def loadOrkImage():
    global hpBarImage
    for i in range(0, numOfWalkImage + 1):
        orkWalkImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\WALK\\WALK_00" + str(i) + ".png"))
        # orkWalkImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\WALK\\WALK_00" + str(i) + ".png"))
        # orkWalkImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\WALK\\WALK_00" + str(i) + ".png"))
    for i in range(0, numOfAttackImage + 1):
        orkAttackImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\ATTAK\\ATTAK_00" + str(i) + ".png"))
        # orkWalkImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\ATTAK\\ATTAK_00" + str(i) + ".png"))
        # orkWalkImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\ATTAK\\ATTAK_00" + str(i) + ".png""))
    for i in range(0, numOfDieImage + 1):
        orkDieImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\DIE\\DIE_00" + str(i) + ".png"))
        # orkWalkImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\DIE\\DIE_00" + str(i) + ".png"))
        # orkWalkImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\DIE\\DIE_00" + str(i) + ".png""))
    hpBarImage = load_image("enemyHpBar.png")

def exit():
    del hpBarImage
    for i in range(0, numOfWalkImage + 1):
        del(orkWalkImageList[0])
        #del(orkWalkImageList[1])
        #del(orkWalkImageList[2])
    for i in range(0, numOfAttackImage + 1):
        del(orkAttackImageList[0])
        #del(orkAttackImageList[1])
        #del(orkAttackImageList[2])

    for i in range(0, numOfDieImage + 1):
        del(orkDieImageList[0])
        #del(orkDieImageList[1])
        #del(orkDieImageList[2])


class Ork1(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 200
        self.offensePower = 2

    def draw(self):
        if self.state == CharacterState.WALK:
            hpBarImage.draw(self.x + hpBarPos - camera.cameraXCoord, self.y + self.size / 2, self.hp / 2, hpBarHeigt)
            orkWalkImageList[0][self.frame % numOfWalkImage].composite_draw(0, 'h', self.x - camera.cameraXCoord,
                                                                            self.y,
                                                                            self.size, self.size)
        elif self.state == CharacterState.IDLE:
            hpBarImage.draw(self.x + hpBarPos - camera.cameraXCoord, self.y + self.size / 2, self.hp / 2, hpBarHeigt)
            orkWalkImageList[0][self.frame % numOfWalkImage].composite_draw(0, 'h', self.x - camera.cameraXCoord,
                                                                            self.y,
                                                                            self.size, self.size)
        elif self.state == CharacterState.ATTACK:
            hpBarImage.draw(self.x + hpBarPos - camera.cameraXCoord, self.y + self.size / 2, self.hp / 2, hpBarHeigt)
            orkAttackImageList[0][self.frame % numOfAttackImage].composite_draw(0, 'h', self.x - camera.cameraXCoord,
                                                                                self.y,
                                                                                self.size, self.size)
        elif self.state == CharacterState.DIE:
            orkDieImageList[0][self.frame % numOfAttackImage].composite_draw(0, 'h', self.x - camera.cameraXCoord,
                                                                             self.y,
                                                                             self.size, self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x -= 0.2

        elif self.state == CharacterState.ATTACK:
            self.frame += 1
            if self.frame % numOfAttackImage == 0:
                worldObjManager.allyCharacterList[0].hp -= self.offensePower
                if worldObjManager.allyCharacterList[0].hp <= 0:
                    self.state = CharacterState.WALK
                    worldObjManager.allyCharacterList[0].state = CharacterState.DIE
                    # 상대캐릭터가 죽으면 나는 WALK상태가되고 상대는 DIE상태가된다.

        elif self.state == CharacterState.DIE:
            self.frame += 1
            if self.frame == numOfDieImage:
                if (len(worldObjManager.enemyDeathList) > 0):
                    worldObjManager.deleteObject(2, self)
                if (len(worldObjManager.enemyCharacterList) > 0):
                    worldObjManager.enemyCharacterList[0].state = CharacterState.WALK
        if self.hp <= 0:
            return True

    def checkCollision(self, frontCharacterXpos):
        if self.x < frontCharacterXpos + self.size:
            self.state = CharacterState.IDLE
        else:
            self.state = CharacterState.WALK

    def checkEnemyMeet(self, enemyXpos):
        if self.x < enemyXpos + self.size:
            if self.state != CharacterState.ATTACK and worldObjManager.allyCharacterList[0].hp>0:
                self.state = CharacterState.ATTACK
                self.frame = 0

    def changeState(self):
        pass


"""
class Ork2(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 200
        self.offensePower = 20

    def draw(self):
        if self.state == CharacterState.WALK:
            orkWalkImageList[1][self.frame % numOfImage].composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y,
                                                                        self.size, self.size)
        elif self.state == CharacterState.IDLE:
            orkWalkImageList[1][self.frame % numOfImage].composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y,
                                                                        self.size, self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x -= 0.2

    def checkCollision(self, frontCharacterXpos):
        if self.x < frontCharacterXpos + self.size:
            self.state = CharacterState.IDLE
        else:
            self.state = CharacterState.WALK

    def checkEnemyMeet(self, enemyXpos):
        if self.x < enemyXpos + self.size:
            self.state = CharacterState.IDLE  # 일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass


class Ork3(CharacterABC):
    state = CharacterState.WALK

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 400
        self.offensePower = 30

    def draw(self):
        if self.state == CharacterState.WALK:
            orkWalkImageList[2][self.frame % numOfImage].composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y,
                                                                        self.size, self.size)
        elif self.state == CharacterState.IDLE:
            orkWalkImageList[2][self.frame % numOfImage].composite_draw(0, 'h', self.x - camera.cameraXCoord, self.y,
                                                                        self.size, self.size)

    def move(self):
        pass

    def update(self):
        if self.state == CharacterState.WALK:
            self.frame += 1
            self.x -= 0.2

    def checkCollision(self, frontCharacterXpos):
        if self.x < frontCharacterXpos + self.size:
            self.state = CharacterState.IDLE
        else:
            self.state = CharacterState.WALK

    def checkEnemyMeet(self, enemyXpos):
        if self.x < enemyXpos + self.size:
            self.state = CharacterState.IDLE  # 일단 IDLE로 나중에 ATTACK으로 수정할것.

    def changeState(self):
        pass

"""
