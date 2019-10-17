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
    for i in range(0,len(allyCharacterList)):
        allyCharacterList[i].update()

    allyCharacterList[0].checkEnemyMeet(enemyCharacterList[0].x)

    if(len(allyCharacterList)>0):
        for i in range(1,len(allyCharacterList)):
            allyCharacterList[i].checkCollision(allyCharacterList[i-1].x)


    for i in range(0, len(enemyCharacterList)):
        enemyCharacterList[i].update()

    enemyCharacterList[0].checkEnemyMeet(allyCharacterList[0].x)

    if (len(enemyCharacterList) > 0):
        for i in range(1, len(enemyCharacterList)):
            enemyCharacterList[i].checkCollision(enemyCharacterList[i-1].x)


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