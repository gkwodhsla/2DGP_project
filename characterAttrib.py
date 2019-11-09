from abc import *
import camera
import worldObjManager
from pico2d import *
import enum
import gameFramework
import random

numOfAllyWalkImage = 6
numOfAllyAttackImage = 7
numOfAllyDieImage = 6
numOfAllyIdleImage = 7

allyhpBarPos = 20
allyhpBarHeigth = 10

knightIdleImageList = [[] for i in range(0, 3)]
knightWalkImageList = [[] for i in range(0, 3)]
knightAttackImageList = [[] for i in range(0, 3)]
knightDieImageList = [[] for i in range(0, 3)]

class AllyCharacterIndex(enum.Enum):
    knight1 = 0
    knight2 = 1
    knight3 = 2

numOfEnemyIdleImage = 6
numOfEnemyWalkImage = 6
numOfEnemyAttackImage = 6
numOfEnemyDieImage = 6

enemyhpBarPos = 10
enemyhpBarHeigt = 10

orkIdleImageList = [[] for i in range(0, 3)]
orkWalkImageList = [[] for i in range(0, 3)]
orkAttackImageList = [[] for i in range(0, 3)]
orkDieImageList = [[] for i in range(0, 3)]



pixelPerMeter = (10.0/0.2) #10pixel 20cm
runSpeedKmph = 7
runSpeedMpm = (runSpeedKmph*1000.0/60.0)
runSpeedMps = (runSpeedMpm/60.0)
runSpeedPps = (runSpeedMps*pixelPerMeter)
velocity = runSpeedPps


class EnemyCharacterIndex(enum.Enum):
    ork1 = 0
    ork2 = 1
    ork3 = 2
# 기사 걷는 이미지가 담긴 리스트.

def loadKnightImage():
    for i in range(0, numOfAllyWalkImage + 1):
        knightWalkImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
        # knightWalkImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
        # knightWalkImageList[2].append(load_image("Ally\\Knight\\3_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))
    for i in range(0, numOfAllyAttackImage + 1):
        knightAttackImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_ATTACK\\ATTACK_00" + str(i) + ".png"))
        # knightAttackImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_ATTACK\\ATTACK_00" + str(i) + ".png"))
        # knightAttackImageList[2].append(load_image("Ally\\Knight\\3_KNIGHT\\_ATTACK\\ATTACK_00" + str(i) + ".png"))
    for i in range(0, numOfAllyDieImage + 1):
        knightDieImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_DIE\\_DIE_00" + str(i) + ".png"))
        # knightDieImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_DIE\\_DIE_00" + str(i) + ".png"))
        # knightDieImageList[2].append(load_image("Ally\\Knight\\2_KNIGHT\\_DIE\\_DIE_00" + str(i) + ".png"))
    for i in range(0, numOfAllyDieImage + 1):
        knightIdleImageList[0].append(load_image("Ally\\Knight\\1_KNIGHT\\_IDLE\\_IDLE_00" + str(i) + ".png"))
        # knightIdleImageList[1].append(load_image("Ally\\Knight\\2_KNIGHT\\_IDLE\\_IDLE_00" + str(i) + ".png"))
        # knightIdleImageList[2].append(load_image("Ally\\Knight\\2_KNIGHT\\_IDLE\\_IDLE_00" + str(i) + ".png"))

def loadOrkImage():
    for i in range(0, numOfEnemyWalkImage + 1):
        orkWalkImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\WALK\\WALK_00" + str(i) + ".png"))
        # orkWalkImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\WALK\\WALK_00" + str(i) + ".png"))
        # orkWalkImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\WALK\\WALK_00" + str(i) + ".png"))
    for i in range(0, numOfEnemyAttackImage + 1):
        orkAttackImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\ATTAK\\ATTAK_00" + str(i) + ".png"))
        # orkWalkImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\ATTAK\\ATTAK_00" + str(i) + ".png"))
        # orkWalkImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\ATTAK\\ATTAK_00" + str(i) + ".png""))
    for i in range(0, numOfEnemyDieImage + 1):
        orkDieImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\DIE\\DIE_00" + str(i) + ".png"))
        # orkWalkImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\DIE\\DIE_00" + str(i) + ".png"))
        # orkWalkImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\DIE\\DIE_00" + str(i) + ".png""))
    for i in range(0, numOfEnemyIdleImage + 1):
        orkIdleImageList[0].append(load_image("Enemy\\Orks\\1_ORK\\IDLE\\IDLE_00" + str(i) + ".png"))
        # orkIdleImageList[1].append(load_image("Enemy\\Orks\\2_ORK\\IDLE\\IDLE_00" + str(i) + ".png"))
        # orkIdleImageList[2].append(load_image("Enemy\\Orks\\3_ORK\\IDLE\\IDLE_00" + str(i) + ".png""))


def exit():
    for i in range(0, numOfAllyWalkImage + 1):
        del (knightWalkImageList[0])
        # del(knightWalkImageList[1])
        # del(knightWalkImageList[2])
    for i in range(0, numOfAllyAttackImage + 1):
        del (knightAttackImageList[0])
        # del(knightAttackImageList[1])
        # del(knightAttackImageList[2])
    for i in range(0, numOfAllyDieImage + 1):
        del (knightDieImageList[0])
        # del(knightDieImageList[0])
        # del(knightDieImageList[0])
    for i in range(0, numOfAllyIdleImage + 1):
        del (knightIdleImageList[0])
        # del(knightIdleImageList[1])
        # del(knightIdleImageList[2])

    for i in range(0, numOfEnemyWalkImage + 1):
        del (orkWalkImageList[0])
        # del(orkWalkImageList[1])
        # del(orkWalkImageList[2])
    for i in range(0, numOfEnemyAttackImage + 1):
        del (orkAttackImageList[0])
        # del(orkAttackImageList[1])
        # del(orkAttackImageList[2])

    for i in range(0, numOfEnemyDieImage + 1):
        del (orkDieImageList[0])
        # del(orkDieImageList[1])
        # del(orkDieImageList[2])

    for i in range(0, numOfEnemyIdleImage + 1):
        del (orkIdleImageList[0])
        # del(knightIdleImageList[1])
        # del(knightIdleImageList[2])


class CharacterABC(metaclass=ABCMeta):
    size = 100

    def draw(self):
        pass

    def update(self):
        pass

    def checkCollision(self, frontCharacterXpos):
        # 충돌처리는 월드 오브젝트 리스트의 맨앞에 있는 애들은 적군을 만났는지 아닌지 충돌체크하고 만나면 상태를 ATTACK으로 바꾼다.
        # 나머지뒤에 오브젝트들은 앞에 아군과 충돌인지 아닌지 검사한다. 만일 아군과 충돌이면 상태를 IDLE하게 해준다.
        # ally self.x+self.size<frontobject's Xpos
        # enemy self.xpos>frontobject's Xpos + self.size
        pass

    def checkEnemyMeet(self, enemyXpos):
        pass

    def checkBaseCollision(self):
        pass

    def changeState(self):
        pass


class IdleState:
    @staticmethod
    def enter(object):
        object.frame = random.randint(0,3)

    @staticmethod
    def update(object, type):
        object.frame = (object.frame+object.framesPerActionIdle*object.actionPerTime*gameFramework.frameTime)%object.framesPerActionIdle

    @staticmethod
    def draw(object, type, characterType):
        # type0 = ally type1 = enemy
        # characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 'ally':
            object.hpBarImage.draw(object.x - allyhpBarPos - camera.cameraXCoord, object.y + object.size / 2,
                                   object.hp / 2, allyhpBarHeigth)
            knightIdleImageList[characterType][int(object.frame) % object.framesPerActionIdle].draw(object.x - camera.cameraXCoord, object.y,
                                                                           object.size,
                                                                           object.size)
        else:
            object.hpBarImage.draw(object.x + enemyhpBarPos - camera.cameraXCoord, object.y + object.size / 2, object.hp / 2, enemyhpBarHeigt)
            orkIdleImageList[characterType][int(object.frame) % object.framesPerActionIdle].composite_draw(0, 'h', object.x - camera.cameraXCoord,
                                                                            object.y,
                                                                            object.size, object.size)

    @staticmethod
    def exit(object):
        pass


class WalkState:
    @staticmethod
    def enter(object):
        object.frame = 0

    @staticmethod
    def update(object, type):
        object.frame = (object.frame + object.framesPerActionWalk * object.actionPerTime * gameFramework.frameTime) % object.framesPerActionWalk
        if type == 'ally':
            object.x += velocity*gameFramework.frameTime
        else:
            object.x -= velocity*gameFramework.frameTime

    @staticmethod
    def draw(object, type, characterType):
        # type0 = ally type1 = enemy
        # characterType==0 (knight1,ork1) and so forth...
        if type == 'ally':
            object.hpBarImage.draw(object.x - allyhpBarPos - camera.cameraXCoord, object.y + object.size / 2,
                                   object.hp / 2, allyhpBarHeigth)
            knightWalkImageList[characterType][int(object.frame) % object.framesPerActionWalk].draw(object.x - camera.cameraXCoord, object.y,
                                                                           object.size,
                                                                           object.size)
        else:
            object.hpBarImage.draw(object.x + enemyhpBarPos - camera.cameraXCoord, object.y + object.size / 2, object.hp / 2, enemyhpBarHeigt)
            orkWalkImageList[characterType][int(object.frame) % object.framesPerActionWalk].composite_draw(0, 'h', object.x - camera.cameraXCoord,
                                                                            object.y,
                                                                            object.size, object.size)

    @staticmethod
    def exit(object):
        pass


class AttackState:
    @staticmethod
    def enter(object):
        object.frame = 0

    @staticmethod
    def update(object, type):
        object.frame = (object.frame + object.framesPerActionAttack * object.actionPerTime * gameFramework.frameTime) % object.framesPerActionAttack
        if type == 'ally':
            if int(object.frame) % object.framesPerActionAttack == 0:
                if not object.isBaseAttack:
                    worldObjManager.enemyCharacterList[0].hp -= object.offensePower
                    if worldObjManager.enemyCharacterList[0].hp <= 0:
                        object.state = WalkState
                        worldObjManager.enemyCharacterList[0].state = DeathState
                        # 상대캐릭터가 죽으면 나는 WALK상태가되고 상대는 DIE상태가된다.
                else:
                    worldObjManager.baseList[1].hp -= object.offensePower
        else:
            if int(object.frame) % object.framesPerActionAttack == 0:
                if not object.isBaseAttack:
                    worldObjManager.allyCharacterList[0].hp -= object.offensePower
                    if worldObjManager.allyCharacterList[0].hp <= 0:
                        object.state = WalkState
                        worldObjManager.allyCharacterList[0].state = DeathState
                    # 상대캐릭터가 죽으면 나는 WALK상태가되고 상대는 DIE상태가된다.
                else:
                    worldObjManager.baseList[0].hp -= object.offensePower

    @staticmethod
    def draw(object, type, characterType):
        # type0 = ally type1 = enemy
        # characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 'ally':
            object.hpBarImage.draw(object.x - allyhpBarPos - camera.cameraXCoord, object.y + object.size / 2,
                                   object.hp / 2, allyhpBarHeigth)
            knightAttackImageList[characterType][int(object.frame) % object.framesPerActionAttack].draw(object.x - camera.cameraXCoord, object.y,
                                                                               object.size,
                                                                               object.size)
        else:
            object.hpBarImage.draw(object.x + enemyhpBarPos - camera.cameraXCoord, object.y + object.size / 2, object.hp / 2, enemyhpBarHeigt)
            orkAttackImageList[characterType][int(object.frame) % object.framesPerActionAttack].composite_draw(0, 'h', object.x - camera.cameraXCoord,
                                                                                object.y,
                                                                                object.size, object.size)

    @staticmethod
    def exit(object):
        pass


class DeathState:
    @staticmethod
    def enter(object):
        object.frame = 0

    @staticmethod
    def update(object, type):
        object.frame = (object.frame + object.framesPerActionDeath * object.actionPerTime * gameFramework.frameTime) % object.framesPerActionDeath
        if type == 'ally':
            if object.frame >= float(object.framesPerActionDeath) - 0.2:
                if len(worldObjManager.allyDeathList) > 0:
                    worldObjManager.deleteObject('ally', object)
        else:
            if object.frame >= float(object.framesPerActionDeath) - 0.2:
                if (len(worldObjManager.enemyDeathList) > 0):
                    worldObjManager.deleteObject('enemy', object)

    @staticmethod
    def draw(object, type, characterType):
        # type0 = ally type1 = enemy
        # characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 'ally' and characterType == 0:
            object.hpBarImage.draw(object.x - allyhpBarPos - camera.cameraXCoord, object.y + object.size / 2,
                                   object.hp / 2, allyhpBarHeigth)
            knightDieImageList[characterType][int(object.frame) % object.framesPerActionDeath].draw(object.x - camera.cameraXCoord, object.y,
                                                                         object.size,
                                                                         object.size)
        else:
            orkDieImageList[characterType][int(object.frame) % object.framesPerActionDeath].composite_draw(0, 'h', object.x - camera.cameraXCoord,
                                                                             object.y,
                                                                             object.size, object.size)

    @staticmethod
    def exit(object):
        pass
