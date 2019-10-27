# 이 객체에서 worldObject들을 관리합니다.

# type0 = base , type1 = allyCharacter , type2 = enemyCharacter
baseList = []
allyCharacterList = []
enemyCharacterList = []
allyDeathList = []
enemyDeathList = []

# add object according to its own type
def addObject(object, type):
    if type == 0:
        baseList.append(object)
    elif type == 1:
        allyCharacterList.append(object)
    elif type == 2:
        enemyCharacterList.append(object)


def update():
    #일반적인 로직업데이트 루프. 반환값은BOOL이며 TRUE시 객체가 곧 파괴.
    for i in range(0, len(allyCharacterList)):
        if(allyCharacterList[i].update()):
            allyCharacterList[i].frame = 0
            allyDeathList.append(allyCharacterList.pop(i))
            break

    #적군과 충돌체크
    if (len(allyCharacterList) > 0 and len(enemyCharacterList) > 0):
        allyCharacterList[0].checkEnemyMeet(enemyCharacterList[0].x)

    #앞에 있는 아군과의 충돌체크.
    if (len(allyCharacterList) > 0):
        for i in range(1, len(allyCharacterList)):
            allyCharacterList[i].checkCollision(allyCharacterList[i - 1].x)



    for i in range(0, len(enemyCharacterList)):
        if(enemyCharacterList[i].update()):
            enemyCharacterList[i].frame = 0
            enemyDeathList.append(enemyCharacterList.pop(i))
            break

    if (len(allyCharacterList) > 0 and len(enemyCharacterList) > 0):
        enemyCharacterList[0].checkEnemyMeet(allyCharacterList[0].x)

    if (len(enemyCharacterList) > 0):
        for i in range(1, len(enemyCharacterList)):
            enemyCharacterList[i].checkCollision(enemyCharacterList[i - 1].x)


    #죽은상태......(DIE애니메이션을위한 update)
    if(len(allyDeathList)>0):
        for i in range(0,len(allyDeathList)):
            allyDeathList[i].update()

    if (len(enemyDeathList) > 0):
        for i in range(0, len(enemyDeathList)):
            enemyDeathList[i].update()


def deleteObject(type,object):
    if type == 1:
        allyDeathList.remove(object)
    elif type == 2:
        enemyDeathList.remove(object)
    del object


# draw all object in each list
def drawObject():
    for obj in baseList:
        obj.draw()

    for obj in allyCharacterList:
        obj.draw()

    for obj in enemyCharacterList:
        obj.draw()
    #죽는 이미지를 그리기위한 코드.
    if (len(allyDeathList) > 0):
        for i in range(0, len(allyDeathList)):
            allyDeathList[i].draw()
    if (len(enemyDeathList) > 0):
        for i in range(0, len(enemyDeathList)):
            enemyDeathList[i].draw()


# delete all objects when game is over.
def deleteAllObjects():
    for i in range(0, len(allyCharacterList)):
        del (allyCharacterList[i])

    for i in range(0, len(enemyCharacterList)):
        del (enemyCharacterList[i])
