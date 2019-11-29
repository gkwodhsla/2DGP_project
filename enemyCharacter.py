from characterAttrib import *
import worldObjManager


class HammerOrk(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.5  # 초당 0.5번의 행동을한다.
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 6
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.hp = 200
        self.offensePower = 3
        self.isBaseAttack = False
        self.right = self.x + self.size / 2
        self.left = self.x - self.size / 2
        self.top = self.y + self.size / 2
        self.bottom = self.y - self.size / 2
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\enemyHpBar.png")

    def draw(self):
        self.state.draw(self, 'enemy', EnemyCharacterIndex.ork1.value)

    def update(self):
        self.right = self.x + self.size / 2
        self.left = self.x - self.size / 2
        self.top = self.y + self.size / 2
        self.bottom = self.y - self.size / 2
        self.state.update(self, 'enemy')
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
            self.state = WalkState

    def checkCollisionWithBase(self):
        if self.x < worldObjManager.baseList[0].x + worldObjManager.baseList[0].size / 2:
            self.state = AttackState
            self.isBaseAttack = True
        else:
            self.state = WalkState

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
