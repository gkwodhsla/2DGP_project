# 이 객체에서 worldObject들을 관리합니다.

# type0 = base , type1 = allyCharacter , type2 = enemyCharacter
# objects in each deathList will be destroy when its done its job.
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
    # The general game logic update loop return value is boolean and if this value is TRUE then this object moved to deathlist
    for i in range(0, len(allyCharacterList)):
        if (allyCharacterList[i].update()):
            allyCharacterList[i].frame = 0
            allyDeathList.append(allyCharacterList.pop(i))
            break

    if (len(allyCharacterList) > 0):
        allyCharacterList[0].checkCollisionWithBase()

    # Checking Collision with enemy unit
    if (len(allyCharacterList) > 0 and len(enemyCharacterList) > 0):
        allyCharacterList[0].checkCollisionWithEnemy(enemyCharacterList[0].x)

    # Checking Collision with ally unit
    for i in range(1, len(allyCharacterList)):
        allyCharacterList[i].checkCollisionWithAlly(allyCharacterList[i - 1].x)

    #so far allyCharacter updating code.
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    #same as allyCharacter updating code but just using diffent list.
    for i in range(0, len(enemyCharacterList)):
        if (enemyCharacterList[i].update()):
            enemyCharacterList[i].frame = 0
            enemyDeathList.append(enemyCharacterList.pop(i))
            break

    if (len(enemyCharacterList) > 0):
        enemyCharacterList[0].checkCollisionWithBase()

    if (len(allyCharacterList) > 0 and len(enemyCharacterList) > 0):
        enemyCharacterList[0].checkCollisionWithEnemy(allyCharacterList[0].x)

    for i in range(1, len(enemyCharacterList)):
        enemyCharacterList[i].checkCollisionWithAlly(enemyCharacterList[i - 1].x)

    #for updating dying animation.
    for i in range(0, len(allyDeathList)):
        allyDeathList[i].update()

    for i in range(0, len(enemyDeathList)):
        enemyDeathList[i].update()


def deleteObject(type, object):
    if type == 'ally':
        allyDeathList.remove(object)
    elif type == 'enemy':
        enemyDeathList.remove(object)
    del object


# draw all object in each list
def drawObject():
    # draw bases
    for obj in baseList:
        obj.draw()

    # draw allyCharacters
    for obj in allyCharacterList:
        obj.draw()

    # draw enemyCharacters
    for obj in enemyCharacterList:
        obj.draw()

    # draw dying characters images first ally next enemy

    for i in range(0, len(allyDeathList)):
        allyDeathList[i].draw()
    for i in range(0, len(enemyDeathList)):
        enemyDeathList[i].draw()


# delete all objects when game is over.
def deleteAllObjects():
    for i in range(0, len(allyCharacterList)):
        del (allyCharacterList[i])

    for i in range(0, len(enemyCharacterList)):
        del (enemyCharacterList[i])
