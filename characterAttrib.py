from abc import *
from enum import Enum
import camera
import worldObjManager
from pico2d import *

numOfAllyWalkImage = 6
numOfAllyAttackImage = 7
numOfAllyDieImage = 6
numOfAllyIdleImage = 7

AllyhpBarPos = 20
AllyhpBarHeigth = 10

knightIdleImageList = [[] for i in range(0 , 3)]
knightWalkImageList = [[] for i in range(0, 3)]
knightAttackImageList = [[] for i in range(0, 3)]
knightDieImageList = [[] for i in range(0, 3)]


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

def exit():
    for i in range(0, numOfAllyWalkImage + 1):
        del(knightWalkImageList[0])
        #del(knightWalkImageList[1])
        #del(knightWalkImageList[2])
    for i in range(0, numOfAllyAttackImage + 1):
        del(knightAttackImageList[0])
        #del(knightAttackImageList[1])
        #del(knightAttackImageList[2])
    for i in range(0, numOfAllyDieImage + 1):
        del(knightDieImageList[0])
        #del(knightDieImageList[0])
        #del(knightDieImageList[0])
# 이미지 로드.

class CharacterABC(metaclass=ABCMeta):
    size = 100

    def draw(self):
        pass

    def move(self):
        pass

    def update(self):
        pass

    def checkCollision(self,frontCharacterXpos):
        # 충돌처리는 월드 오브젝트 리스트의 맨앞에 있는 애들은 적군을 만났는지 아닌지 충돌체크하고 만나면 상태를 ATTACK으로 바꾼다.
        # 나머지뒤에 오브젝트들은 앞에 아군과 충돌인지 아닌지 검사한다. 만일 아군과 충돌이면 상태를 IDLE하게 해준다.
        # 아군 self.x+self.size<frontobject's Xpos
        # 적군 self.xpos>frontobject's Xpos + self.size로 충돌체크해주면됨.
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
        object.frame = 0
    @staticmethod
    def update(object,type):
        object.frame += 1
    @staticmethod
    def draw(object,type,characterType):
        # type0 = ally type1 = enemy
        # characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 0 and characterType == 0:
            object.hpBarImage.draw(object.x - AllyhpBarPos - camera.cameraXCoord, object.y + object.size / 2, object.hp / 2, AllyhpBarHeigth)
            knightIdleImageList[0][object.frame % numOfAllyIdleImage].draw(object.x - camera.cameraXCoord, object.y, object.size,
                                                                     object.size)
        else:
            pass
    @staticmethod
    def exit(object):
        pass


class WalkState:
    @staticmethod
    def enter(object):
        object.frame = 0
    @staticmethod
    def update(object,type):
        object.frame += 1
        if type == 0:
            object.x += 0.4
        else:
            pass
    @staticmethod
    def draw(object,type,characterType):
        #type0 = ally type1 = enemy
        #characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 0 and characterType == 0:
            object.hpBarImage.draw(object.x - AllyhpBarPos - camera.cameraXCoord, object.y + object.size / 2, object.hp / 2, AllyhpBarHeigth)
            knightWalkImageList[0][object.frame % numOfAllyWalkImage].draw(object.x - camera.cameraXCoord, object.y, object.size,
                                                                     object.size)
    @staticmethod
    def exit(object):
        pass


class AttackState:
    @staticmethod
    def enter(object):
        object.frame = 0
    @staticmethod
    def update(object,type):
        object.frame += 1
        if type == 0:
            if object.frame % numOfAllyAttackImage == 0:
                if not object.isBaseAttack:
                    worldObjManager.enemyCharacterList[0].hp -= object.offensePower
                    if worldObjManager.enemyCharacterList[0].hp <= 0:
                        #object.state = WalkState
                        worldObjManager.enemyCharacterList[0].state = DeathState
                        # 상대캐릭터가 죽으면 나는 WALK상태가되고 상대는 DIE상태가된다.
                else:
                    worldObjManager.baseList[1].hp -= object.offensePower
        else:
            pass
    @staticmethod
    def draw(object,type,characterType):
        #type0 = ally type1 = enemy
        #characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 0 and characterType == 0:
            object.hpBarImage.draw(object.x - AllyhpBarPos - camera.cameraXCoord, object.y + object.size / 2, object.hp / 2, AllyhpBarHeigth)
            knightAttackImageList[0][object.frame % numOfAllyAttackImage].draw(object.x - camera.cameraXCoord, object.y, object.size,
                                                                     object.size)
    @staticmethod
    def exit(object):
        pass

class DeathState:
    @staticmethod
    def enter(object):
        object.frame = 0

    @staticmethod
    def update(object, type):
        object.frame += 1
        if type == 0:
            if object.frame == numOfAllyDieImage:
                if (len(worldObjManager.allyDeathList) > 0):
                    worldObjManager.deleteObject(1, object)
                if (len(worldObjManager.allyCharacterList) > 0):
                    worldObjManager.allyCharacterList[0].state = CharacterState.WALK
        else:
            pass

    @staticmethod
    def draw(object, type, characterType):
        # type0 = ally type1 = enemy
        # characterType==0 knight1 , 1 knight2, 2 knight 3
        if type == 0 and characterType == 0:
            object.hpBarImage.draw(object.x - AllyhpBarPos - camera.cameraXCoord, object.y + object.size / 2,
                                   object.hp / 2, AllyhpBarHeigth)
            knightDieImageList[0][object.frame % numOfAllyDieImage].draw(object.x - camera.cameraXCoord, object.y,
                                                                           object.size,
                                                                           object.size)

    @staticmethod
    def exit(object):
        pass
