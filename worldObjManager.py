#이 객체에서 worldObject들을 관리합니다.

# tpye0 = base , type1 = allyCharacter , type2 = enemyCharacter
baseList=[]
allyCharacterList=[]
enemyCharacterList=[]

#add object according to its own type
def addObject(object,type):
    if type==0:
        baseList.append(object)
    elif type==1:
        allyCharacterList.append(object)
    elif type==2:
        enemyCharacterList.append(object)

def update():
    for obj in allyCharacterList:
        obj.update()

    for obj in enemyCharacterList:
        obj.update()

def deleteObject():
    #캐릭터 사망 추가시 구현예정.
    pass

#draw all object in each list
def drawObject():
    for obj in baseList:
        obj.draw()

    for obj in allyCharacterList:
        obj.draw()

    for obj in enemyCharacterList:
        obj.draw()