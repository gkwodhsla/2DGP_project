from characterAttrib import *
import worldObjManager


class Ork1(CharacterABC):
    state = WalkState
    hpBarImage = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.hp = 200
        self.offensePower = 1
        self.isBaseAttack = False
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\enemyHpBar.png")

    def draw(self):
        self.state.draw(self, 1, 0)


    def update(self):
        self.state.update(self, 1)
        if self.hp <= 0:
            return True

        return False

    def checkCollisionWithAlly(self, frontCharacterXpos):
        if self.x < frontCharacterXpos + self.size:
            self.state = IdleState
        else:
            self.state = WalkState

    def checkCollisionWithEnemy(self, enemyXpos):
        if self.x < enemyXpos + self.size:
            if self.state != AttackState and worldObjManager.allyCharacterList[0].hp > 0:
                self.state = AttackState
                self.frame = 0
        else:
            self.state=WalkState

    def checkCollisionWithBase(self):
        if self.x < worldObjManager.baseList[0].x + worldObjManager.baseList[0].size / 2:
            self.state = AttackState
            self.isBaseAttack = True

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
