from characterAttrib import *
import worldObjManager


class HammerOrk(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.8
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 6
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.bloodFrame = 0.0
        self.hp = 150
        self.offensePower = 15
        self.isBaseAttack = False
        self.isOnceAttack = False
        self.isBleeding = False
        self.right = self.x + self.size / 2
        self.left = self.x - self.size / 2
        self.top = self.y + self.size / 2
        self.bottom = self.y - self.size / 2
        if self.hpBarImage is None:
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


class SwordOrk(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.8
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 6
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.bloodFrame = 0.0
        self.hp = 180
        self.offensePower = 25
        self.isBaseAttack = False
        self.isOnceAttack = False
        self.isBleeding = False
        self.right = self.x + self.size / 2
        self.left = self.x - self.size / 2
        self.top = self.y + self.size / 2
        self.bottom = self.y - self.size / 2
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\enemyHpBar.png")

    def draw(self):
        self.state.draw(self, 'enemy', EnemyCharacterIndex.ork2.value)

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


class AxeOrk(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.8
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 6
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.bloodFrame = 0.0
        self.hp = 200
        self.offensePower = 40
        self.isBaseAttack = False
        self.isOnceAttack = False
        self.isBleeding = False
        self.right = self.x + self.size / 2
        self.left = self.x - self.size / 2
        self.top = self.y + self.size / 2
        self.bottom = self.y - self.size / 2
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\enemyHpBar.png")

    def draw(self):
        self.state.draw(self, 'enemy', EnemyCharacterIndex.ork3.value)

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
