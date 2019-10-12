from abc import *
from enum import Enum
import camera
from pico2d import*

walkImageList=[]

def loadKnightImage():
    for i in range(0, 6 + 1):
        walkImageList.append(load_image("Ally\\Knight\\1_KNIGHT\\_WALK\\_WALK_00" + str(i) + ".png"))



class characterState(Enum):
    IDLE=0,
    ATTACK=1,
    WALK=2,
    DIE=3

class characterABC(metaclass=ABCMeta):

    def draw(self):
        pass

    def move(self):
        pass

    def update(self):
        pass

    def checkCollision(self):
        #충돌처리는 월드 오브젝트 리스트의 맨앞에 있는 애들은 적군을 만났는지 아닌지 충돌체크하고 만나면 상태를 ATTACK으로 바꾼다.
        #나머지뒤에 오브젝트들은 앞에 아군과 충돌인지 아닌지 검사한다.
        #만일 아군과 충돌이면 상태를 IDLE하게 해준다.
        pass

    def changeState(self):
        pass