from characterAttrib import *
import worldObjManager


class SpearMan(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.8  # 초당 0.8번의 행동을한다.
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 7
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.hp = 100
        self.offensePower = 1
        self.isBaseAttack = False
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\hpBar.png")

    def draw(self):
        self.state.draw(self, 'ally', AllyCharacterIndex.knight1.value)


    def update(self):
        self.state.update(self, 'ally')
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
        else:
            self.state = WalkState
    def changeState(self):
        pass


class AxeMan(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.8  # 초당 0.8번의 행동을한다.
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 6
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.hp = 120
        self.offensePower = 2
        self.isBaseAttack = False
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\hpBar.png")

    def draw(self):
        self.state.draw(self, 'ally', AllyCharacterIndex.knight2.value)


    def update(self):
        self.state.update(self, 'ally')
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
        else:
            self.state = WalkState
    def changeState(self):
        pass


class SwordMan(CharacterABC):
    state = WalkState
    hpBarImage = None
    timePerAction = 0.8  # 초당 0.8번의 행동을한다.
    actionPerTime = 1.0 / timePerAction
    framesPerActionIdle = 6
    framesPerActionWalk = 6
    framesPerActionAttack = 6
    framesPerActionDeath = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0
        self.hp = 150
        self.offensePower = 3
        self.isBaseAttack = False
        if self.hpBarImage == None:
            self.hpBarImage = load_image("effectImages\\hpBar.png")

    def draw(self):
        self.state.draw(self, 'ally', AllyCharacterIndex.knight3.value)


    def update(self):
        self.state.update(self, 'ally')
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
        else:
            self.state = WalkState
    def changeState(self):
        pass
