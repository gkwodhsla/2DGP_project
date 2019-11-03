from characterAttrib import *
import worldObjManager


class Knight1(CharacterABC):
    state = WalkState
    hpBarImage = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 100
        self.offensePower = 1
        self.isBaseAttack = False
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\hpBar.png")

    def draw(self):
        self.state.draw(self, 0, 0)


    def update(self):
        self.state.update(self, 0)
        if self.hp <= 0:
            return True

        return False

    def checkCollisionWithAlly(self, frontCharacterXpos):
        if self.x + self.size > frontCharacterXpos:
            self.state = IdleState
        else:
            self.state = WalkState

    def checkCollisionWithEnemy(self, enemyXpos):
        if self.x + self.size > enemyXpos:
            if self.state != AttackState and worldObjManager.enemyCharacterList[0].hp > 0:
                self.state = AttackState
                self.frame = 0
        else:
            self.state = WalkState

    def checkCollisionWithBase(self):
        if self.x + self.size > worldObjManager.baseList[1].x:
            self.state = AttackState
            self.isBaseAttack = True

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
