from abc import *
from enum import Enum
import camera
from pico2d import *


class CharacterState(Enum):
    IDLE = 0,
    ATTACK = 1,
    WALK = 2,
    DIE = 3


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
