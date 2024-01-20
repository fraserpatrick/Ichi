import pygame, sys, sqlite3, datetime, random, time
pygame.init()

conn = sqlite3.connect('ichidatabase.db')
cursor = conn.cursor()
def create():
    cursor.execute("""CREATE TABLE user (
    username VARCHAR(20) PRIMARY KEY,
    wins VARCHAR,
    losses VARCHAR,
    games VARCHAR,
    lastselected DATETIME);""")

def adddata():
    cursor.execute("""INSERT INTO user VALUES ("User1",0,0,0, CURRENT_TIMESTAMP);""")
    conn.commit()
    cursor.execute("""INSERT INTO user VALUES ("User2",0,0,0, CURRENT_TIMESTAMP);""")
    conn.commit()
    cursor.execute("""INSERT INTO user VALUES ("User3",0,0,0, CURRENT_TIMESTAMP);""")
    conn.commit()
    cursor.execute("""INSERT INTO user VALUES ("User4",0,0,0, CURRENT_TIMESTAMP);""")
    conn.commit()
    
if cursor.execute(
  """SELECT Name FROM sqlite_master WHERE type='table'
  AND Name='user'; """).fetchall() == []:
  create()
  adddata()

conn.close()

def startpage():
    global selecteduser
    getlastusers()
    userselectedtext = font30.render('User selected: ' + selecteduser, True, black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 525 <= mouse[0] <= 865 and 270 <= mouse[1] <= 345:
                    noplayerspage()
                if 410 <= mouse[0] <= 980 and 355 <= mouse[1] <= 430:
                    leaderboardpage()
                if 497.5 <= mouse[0] <= 902.5 and 440 <= mouse[1] <= 515:
                    changeuserpage()
                if 610 <= mouse[0] <= 790 and 525 <= mouse[1] <= 600:
                    rulespage()
                if 627.5 <= mouse[0] <= 772.5 and 610 <= mouse[1] <= 685:
                    pygame.quit()
                    sys.exit()
                    

        mouse = pygame.mouse.get_pos()

        screen.blit(background,(0,0))

        pygame.draw.rect(screen,color_light,[530, 270, 340, 75])
        pygame.draw.rect(screen,color_light,[415, 355, 570, 75])
        pygame.draw.rect(screen,color_light,[497.5, 440, 405, 75])
        pygame.draw.rect(screen,color_light,[610, 525, 180, 75])
        pygame.draw.rect(screen,color_light,(627.5, 610, 145, 75))

        screen.blit(title2 , (482.5,-27.5))
        screen.blit(title1 , (490,-20))
        screen.blit(playgamebuttontext, (535, 260))
        screen.blit(viewleaderboardbuttontext, (420, 345))
        screen.blit(changeuserbuttontext, (502.5, 430))
        screen.blit(rulesbuttontext, (615, 515))
        screen.blit(quitbuttontext, (632.5, 600))
        screen.blit(ichicharacter, (0, 0))
        screen.blit(ichicharacter, (1100, 0))
        screen.blit(userselectedtext, (10, 660))

        pygame.display.update()

def noplayerspage():
    global noplayers
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 545 <= mouse[0] <= 600 and 355 <= mouse[1] <= 430:
                    noplayers = 1
                    startgame()
                if 672.5 <= mouse[0] <= 727.5 and 55 <= mouse[1] <= 430:
                    noplayers = 2
                    startgame()
                if 800 <= mouse[0] <= 855 and 355 <= mouse[1] <= 430:
                    noplayers = 3
                    startgame()
                if 0 <= mouse[0] <= 110 and 650 <= mouse[1] <= 725:
                    startpage()

        mouse = pygame.mouse.get_pos()

        screen.blit(background,(0,0))
        pygame.draw.rect(screen,color_light,(545,355,55,75))
        pygame.draw.rect(screen,color_light,(672.5,355,55,75))
        pygame.draw.rect(screen,color_light,(800,355,55,75))
        pygame.draw.rect(screen,color_light,(0,650,110,75))

        screen.blit(ichicharacter, (0, 0))
        screen.blit(ichicharacter, (1100, 0))
        screen.blit(onebuttontext,(555, 350))
        screen.blit(twobuttontext,(682.5, 350))
        screen.blit(threebuttontext,(810, 350))
        screen.blit(backbuttontext,(5, 645))
        screen.blit(noplayerstext,(355, 200))

        pygame.display.update()

def leaderboardpage():
    getmostwins()
    getmostlosses()
    getmostgames()
    x=1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 110 and 650 <= mouse[1] <= 725:
                    startpage()
                if 60 <= mouse[1] <= 115:
                    if 490 <= mouse[0] <= 605:
                        x=1
                    if 627.5 <= mouse[0] <= 772.5:
                        x=2
                    if 795 <= mouse[0] <= 940:
                        x=3

        mouse = pygame.mouse.get_pos()

        updateleaderboard(x)

        pygame.display.update()

def changeuserpage():
    global usertextposition
    usertextposition = 150
    getlastusers()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 110 and 650 <= mouse[1] <= 725:
                    startpage()
                if 535 <= mouse[0] <= 865 and 70 <= mouse[1] <= 120:
                    newuser()
                if 500 <= mouse[0] <= 900 and 150 <= mouse[1] <= 650:
                    if usertextposition <= mouse[1] <= usertextposition+50:
                        changeuser(0)
                    if usertextposition+50 <= mouse[1] <= usertextposition+100:
                        changeuser(1)
                    if usertextposition+100 <= mouse[1] <= usertextposition+150:
                        changeuser(2)
                    if usertextposition+150 <= mouse[1] <= usertextposition+200:
                        changeuser(3)
                    if usertextposition+200 <= mouse[1] <= usertextposition+250:
                        changeuser(4)
                    if usertextposition+250 <= mouse[1] <= usertextposition+300:
                        changeuser(5)
                    if usertextposition+300 <= mouse[1] <= usertextposition+350:
                        changeuser(6)
                    if usertextposition+350 <= mouse[1] <= usertextposition+400:
                        changeuser(7)
                    if usertextposition+400 <= mouse[1] <= usertextposition+450:
                        changeuser(8)
                    if usertextposition+450 <= mouse[1] <= usertextposition+500:
                        changeuser(9)
                    if usertextposition+500 <= mouse[1] <= usertextposition+550:
                        changeuser(10)
                    if usertextposition+550 <= mouse[1] <= usertextposition+600:
                        changeuser(11)
                    if usertextposition+600 <= mouse[1] <= usertextposition+650:
                        changeuser(12)
                    if usertextposition+650 <= mouse[1] <= usertextposition+700:
                        changeuser(13)
                    if usertextposition+700 <= mouse[1] <= usertextposition+750:
                        changeuser(14)
                    if usertextposition+750 <= mouse[1] <= usertextposition+800:
                        changeuser(15)
                    if usertextposition+800 <= mouse[1] <= usertextposition+850:
                        changeuser(16)
                    if usertextposition+850 <= mouse[1] <= usertextposition+900:
                        changeuser(17)
                    if usertextposition+900 <= mouse[1] <= usertextposition+950:
                        changeuser(18)
                    if usertextposition+950 <= mouse[1] <= usertextposition+1000:
                        changeuser(19)
                    if usertextposition+1000 <= mouse[1] <= usertextposition+1050:
                        changeuser(20)

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and usertextposition != 150:
            usertextposition += 5
            updateusertext()

        if keys[pygame.K_DOWN] and usertextposition != -350:
            usertextposition -= 5
            updateusertext()

        updateusertext()

        pygame.display.update()

def rulespage():
    global rulestextposition
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 110 and 650 <= mouse[1] <= 725:
                    startpage()

        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and rulestextposition != 60:
            rulestextposition += 5
            updaterulestext()

        if keys[pygame.K_DOWN] and rulestextposition != -320:
            rulestextposition -= 5
            updaterulestext()

        updaterulestext()

        pygame.display.update()

def updaterulestext():
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,color_light,(295,50,810,600))

    y=100
    for i in range(3):
        rulestext = font25.render(rules[i], True, black)
        screen.blit(rulestext,(310, rulestextposition+y))
        y +=30
    y=230
    for i in range(3,14):
        rulestext = font25.render(rules[i], True, black)
        screen.blit(rulestext,(310, rulestextposition+y))
        y +=30
    y=610
    for i in range(14,17):
        rulestext = font25.render(rules[i], True, black)
        screen.blit(rulestext,(310, rulestextposition+y))
        y +=30
    y=740
    for i in range(17,20):
        rulestext = font25.render(rules[i], True, black)
        screen.blit(rulestext,(310, rulestextposition+y))
        y +=30
    y=870
    for i in range(20,23):
        rulestext = font25.render(rules[i], True, black)
        screen.blit(rulestext,(310, rulestextposition+y))
        y +=30

    screen.blit(rulestitletext,(562.5, rulestextposition))
    screen.blit(rulestext1,(655, rulestextposition+60))
    screen.blit(rulestext2,(617.5, rulestextposition+190))
    screen.blit(rulestext3,(585, rulestextposition+570))
    screen.blit(rulestext4,(310, rulestextposition+710))
    screen.blit(rulestext5,(310, rulestextposition+840))
    screen.blit(rulesupperbackground,(0,0))
    screen.blit(ruleslowerbackground,(0,650))

    pygame.draw.rect(screen,color_light,(0,650,110,75))
    screen.blit(backbuttontext,(5, 645))

def updateusertext():
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,color_light,(500,150,400,500))

    y=0
    for i in lastusers:
        if i != "NULL":
            usernametext = font40.render(i, True, black)
            screen.blit(usernametext, (505, usertextposition+y))

            pygame.draw.rect(screen,black,(500,usertextposition+50+y,400,2))
            y += 50

    screen.blit(userupperbackground,(0,0))
    screen.blit(userlowerbackground,(0,650))

    pygame.draw.rect(screen,color_light,(500,70,400,60))
    screen.blit(newuserbuttontext, (505, 65))

    screen.blit(ichicharacter, (0, 0))
    screen.blit(ichicharacter, (1100, 0))

    pygame.draw.rect(screen,color_light,(0,650,110,75))
    screen.blit(backbuttontext,(5, 645))

def changeuser(x):
    time = datetime.datetime.now()
    global selecteduser
    if lastusers[x] != "NULL":
        selecteduser = lastusers[x]

        conn = sqlite3.connect('ichidatabase.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE USER SET lastselected = ? WHERE username = ?;',(time, lastusers[x]))
        conn.commit()
        conn.close()
    startpage()

def getlastusers():
    global selecteduser
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM USER ORDER BY lastselected DESC")
    usernamedata = cursor.fetchall()
    conn.close()

    lastusers.clear()
    i = 0
    for x in usernamedata:
        z = ''
        for item in x:
            z = z + item
        lastusers.append(z)
        i += 1
    while i != 20:
        lastusers.append("NULL")
        i += 1
    selecteduser = lastusers[0]

def newuser():
    global uservalid
    newuser = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 110 and 650 <= mouse[1] <= 725:
                    changeuserpage()
                if 580 <= mouse[0] <= 820 and 450 <= mouse[1] <= 510 and uservalid == True:
                    createnewuser(newuser)

            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    newuser = newuser[:-1]
                    checkuservalid(newuser)
                    updatenewuserpage(newuser)
                else:
                    newuser += event.unicode
                    checkuservalid(newuser)
                    updatenewuserpage(newuser)

            updatenewuserpage(newuser)

        pygame.display.update()

def getmostwins():
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM USER")
    usernamedata = cursor.fetchall()
    cursor.execute("SELECT wins FROM USER")
    winsdata = cursor.fetchall()
    conn.close()

    mostwinsuser.clear()
    mostwins.clear()
    for i in usernamedata:
        x = ''
        for item in i:
            x = x + item
        mostwinsuser.append(x)
    for i in winsdata:
        x = ''
        for item in i:
            x = x + item
        mostwins.append(x)

    bubblesort(mostwinsuser, mostwins)

def getmostlosses():
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM USER")
    usernamedata = cursor.fetchall()
    cursor.execute("SELECT losses FROM USER")
    lossesdata = cursor.fetchall()
    conn.close()

    mostlossesuser.clear()
    mostlosses.clear()
    for i in usernamedata:
        x = ''
        for item in i:
            x = x + item
        mostlossesuser.append(x)
    for i in lossesdata:
        x = ''
        for item in i:
            x = x + item
        mostlosses.append(x)

    bubblesort(mostlossesuser, mostlosses)

def getmostgames():
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM USER")
    usernamedata = cursor.fetchall()
    cursor.execute("SELECT games FROM USER")
    gamesdata = cursor.fetchall()
    conn.close()

    mostgamesuser.clear()
    mostgames.clear()
    for i in usernamedata:
        x = ''
        for item in i:
            x = x + item
        mostgamesuser.append(x)
    for i in gamesdata:
        x = ''
        for item in i:
            x = x + item
        mostgames.append(x)

    bubblesort(mostgamesuser, mostgames)

def bubblesort(x, y):
    length = len(y)
    for i in range(length-1):
        for j in range(0,length-i-1):
            if int(y[j]) < int(y[j+1]):
                y[j], y[j+1] = y[j+1], y[j]
                x[j], x[j+1] = x[j+1], x[j]

def updateleaderboard(value):
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,color_light,(0,650,110,75))
    screen.blit(backbuttontext,(5, 645))
    screen.blit(ichicharacter, (0, 0))
    screen.blit(ichicharacter, (1100, 0))
    if value == 1:
        pygame.draw.rect(screen,color_light,(460,150,480,500))
        pygame.draw.rect(screen,black,(699,150,2,500))
        pygame.draw.rect(screen,color_dark,(460,60,145,55))
        screen.blit(winstext,(480,60))
        pygame.draw.rect(screen,color_light,(627.5,60,145,55))
        screen.blit(lossestext,(632.5,60))
        pygame.draw.rect(screen,color_light,(795,60,145,55))
        screen.blit(gamestext,(800,60))

        y=150
        i = 0
        while i != 10:
            leaderboardtext = font40.render(mostwinsuser[i], True, black)
            screen.blit(leaderboardtext, (465, y))
            pygame.draw.rect(screen,black,(460,y+50,480,2))
            y +=50
            i +=1
            if i == len(mostwinsuser):
                break
        y=150
        i = 0
        while i != 10:
            leaderboardnum = font40.render(mostwins[i], True, black)
            screen.blit(leaderboardnum, (705, y))
            y +=50
            i +=1
            if i == len(mostwinsuser):
                break

    elif value == 2:
        pygame.draw.rect(screen,color_light,(460,150,480,500))
        pygame.draw.rect(screen,black,(699,150,2,500))
        pygame.draw.rect(screen,color_light,(460,60,145,55))
        screen.blit(winstext,(480,60))
        pygame.draw.rect(screen,color_dark,(627.5,60,145,55))
        screen.blit(lossestext,(632.5,60))
        pygame.draw.rect(screen,color_light,(795,60,145,55))
        screen.blit(gamestext,(800,60))

        y=150
        i = 0
        while i != 10:
            leaderboardtext = font40.render(mostlossesuser[i], True, black)
            screen.blit(leaderboardtext, (465, y))
            pygame.draw.rect(screen,black,(460,y+50,480,2))
            y +=50
            i +=1
            if i == len(mostlossesuser):
                break
        y=150
        i = 0
        while i != 10:
            leaderboardnum = font40.render(mostlosses[i], True, black)
            screen.blit(leaderboardnum, (705, y))
            y +=50
            i +=1
            if i == len(mostlossesuser):
                break

    elif value == 3:
        pygame.draw.rect(screen,color_light,(460,150,480,500))
        pygame.draw.rect(screen,black,(699,150,2,500))
        pygame.draw.rect(screen,color_light,(460,60,145,55))
        screen.blit(winstext,(480,60))
        pygame.draw.rect(screen,color_light,(627.5,60,145,55))
        screen.blit(lossestext,(632.5,60))
        pygame.draw.rect(screen,color_dark,(795,60,145,55))
        screen.blit(gamestext,(800,60))

        y=150
        i = 0
        while i != 10:
            leaderboardtext = font40.render(mostgamesuser[i], True, black)
            screen.blit(leaderboardtext, (465, y))
            pygame.draw.rect(screen,black,(460,y+50,480,2))
            y +=50
            i +=1
            if i == len(mostgamesuser):
                break
        y=150
        i = 0
        while i != 10:
            leaderboardnum = font40.render(mostgames[i], True, black)
            screen.blit(leaderboardnum, (705, y))
            y +=50
            i +=1
            if i == len(mostgamesuser):
                break

def updatenewuserpage(newuser):
    global uservalid

    screen.blit(background,(0,0))
    screen.blit(ichicharacter, (0, 0))
    screen.blit(ichicharacter, (1100, 0))

    pygame.draw.rect(screen,color_light,(0,650,110,75))
    screen.blit(backbuttontext,(5, 645))

    screen.blit(enterusertext,(417.5,200))

    pygame.draw.rect(screen,color_light,(580,450,240,60))
    screen.blit(createusertext, (585,450))

    pygame.draw.rect(screen,color_light,(450,320,500,60))
    newusertext = font40.render(newuser, True, black)
    screen.blit(newusertext,(455,320))

    validtext = font40.render('Valid: ' + str(uservalid), True, black)
    screen.blit(validtext,(610,390))

def checkuservalid(newuser):
    global uservalid
    global lastusers
    for i in lastusers:
        if i == newuser or len(newuser) > 20 or len(newuser) < 1:
            uservalid = False
            break
        else:
            uservalid = True

def createnewuser(newuser):
    global selecteduser
    selecteduser = newuser
    time = datetime.datetime.now()
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO user VALUES (?,0,0,0,?);""",(selecteduser, time))
    conn.commit()
    conn.close()

    lastusers.append(newuser)

    startpage()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= mouse[1] <= 460:
                    if 410 <= mouse[0] <= 650:
                        gamepage()
                    if 750 <= mouse[0] <= 990:
                        startpage()

        mouse = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        screen.blit(background,(0,0))

        screen.blit(ichicharacter, (0, 0))
        screen.blit(ichicharacter, (0, 550))
        screen.blit(ichicharacter, (1100, 0))
        screen.blit(ichicharacter, (1100, 550))

        pygame.draw.rect(screen,color_light,(410,400,240,60))
        screen.blit(playagaintext,(425,400))
        pygame.draw.rect(screen,color_light,(750,400,240,60))
        screen.blit(mainmenutext,(755,400))

        if win == True:
            screen.blit(resulttext,(480,150))
        else:
            screen.blit(resulttext,(475,150))

        pygame.display.update()

def updateuserstats(result):
    global userwins, userlosses, usergames, selecteduser
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    usergames += 1
    usergames = str(usergames)
    if result == True:
        userwins += 1
        userwins = str(userwins)
        cursor.execute("UPDATE USER SET wins = ?, games = ? WHERE username = ?;",(userwins, usergames, selecteduser))
    elif result == False:
        userlosses +=1
        userlosses = str(userlosses)
        cursor.execute("UPDATE USER SET losses = ?, games = ? WHERE username = ?;",(userlosses, usergames, selecteduser))
    conn.commit()
    conn.close()

def startgame():
    global gamecomplete, ichipress, gamepause, direction, position, position, winner, loopbreak, deck, cardlist, users, botlist
    gamecomplete = ichipress = gamepause = False
    direction = True
    position = winner = loopbreak = 0
    deck.clear()
    cardlist.clear()
    users.clear()
    botlist.clear()

    createdeck()
    createhands()
    sorthands()
    getbotnames()
    gamepage()

def gamepage():
    global gamecomplete, gamepause, ichipress, direction, loopbreak, winner, position
    gamecomplete = False
    while gamecomplete == False and gamepause == False:
        updategamepage(0)

        if direction == True and loopbreak == 0:
            for i in range(noplayers+1):
                time.sleep(1)
                getinput(i)
                checkwin(i)
                checkichi(i)
                updategamepage(i)
                if loopbreak != 0 or gamecomplete == True or gamepause == True:
                    break

        elif direction == True and loopbreak == 1:
            for i in range((position+1),(noplayers+1)):
                time.sleep(1)
                getinput(i)
                checkwin(i)
                checkichi(i)
                updategamepage(i)
            loopbreak = 0

        elif direction == False and loopbreak == 0:
            for i in reversed(range(noplayers+1)):
                time.sleep(1)
                getinput(i)
                checkwin(i)
                checkichi(i)
                updategamepage(i)
                if loopbreak != 0 or gamecomplete == True or gamepause == True:
                    break


        elif direction == False and loopbreak == 1:
            for i in reversed(range(0,(position))):
                time.sleep(1)
                getinput(i)
                checkwin(i)
                checkichi(i)
                updategamepage(i)
            loopbreak = 0

        elif direction == True and loopbreak == 2:
            for i in range((position+2),(noplayers+1)):
                time.sleep(1)
                getinput(i)
                checkwin(i)
                checkichi(i)
                updategamepage(i)
            loopbreak = 0

        elif direction == False and loopbreak == 2:
            for i in reversed(range(0,(position-1))):
                time.sleep(1)
                getinput(i)
                checkwin(i)
                checkichi(i)
                updategamepage(i)
            loopbreak = 0

    if gamecomplete == True:
        if winner == 0:
            resultspage(True)
        else:
            resultspage(False)
    elif gamepause == True:
        pausepage()

class player:
    def __init__(self, nocards, hand=None):
        self.nocards = nocards
        self.hand = hand if hand else list()

    def addcard(self, card):
        self.hand.append(card)

class card:
    def __init__(self, color, value, indeck):
        self.color = color
        self.value = value
        self.indeck = indeck

def resultspage(win):
    getuserstats()
    if win == True:
        resulttext = font120.render('You win!', True, black)
        updateuserstats(True)
    elif win == False:
        resulttext = font120.render('You lose!', True, black)
        updateuserstats(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= mouse[1] <= 460:
                    if 410 <= mouse[0] <= 650:
                        startgame()
                        gamepage()
                    if 750 <= mouse[0] <= 990:
                        startpage()

        mouse = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        screen.blit(background,(0,0))

        screen.blit(ichicharacter, (0, 0))
        screen.blit(ichicharacter, (0, 550))
        screen.blit(ichicharacter, (1100, 0))
        screen.blit(ichicharacter, (1100, 550))

        pygame.draw.rect(screen,color_light,(410,400,240,60))
        screen.blit(playagaintext,(425,400))
        pygame.draw.rect(screen,color_light,(750,400,240,60))
        screen.blit(mainmenutext,(755,400))

        if win == True:
            screen.blit(resulttext,(480,150))
        else:
            screen.blit(resulttext,(475,150))

        pygame.display.update()

def getuserstats():
    global userwins, userlosses, usergames, selecteduser
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT wins FROM USER WHERE username = ?",(selecteduser,))
    winsdata = cursor.fetchall()
    cursor.execute("SELECT losses FROM USER WHERE username = ?",(selecteduser,))
    lossesdata = cursor.fetchall()
    cursor.execute("SELECT games FROM USER WHERE username = ?",(selecteduser,))
    gamesdata = cursor.fetchall()
    conn.close()

    userwins = userlosses = usergames = 0
    userwins = str(userwins)
    userlosses = str(userlosses)
    usergames = str(usergames)

    for x in winsdata:
        for item in x:
            userwins = userwins + item
    for x in lossesdata:
        for item in x:
            userlosses = userlosses + item
    for x in gamesdata:
        for item in x:
            usergames = usergames + item

    userwins = int(userwins)
    userlosses = int(userlosses)
    usergames = int(usergames)

def updateuserstats(result):
    global userwins, userlosses, usergames, selecteduser
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    usergames += 1
    usergames = str(usergames)
    if result == True:
        userwins += 1
        userwins = str(userwins)
        cursor.execute("UPDATE USER SET wins = ?, games = ? WHERE username = ?;",(userwins, usergames, selecteduser))
    elif result == False:
        userlosses +=1
        userlosses = str(userlosses)
        cursor.execute("UPDATE USER SET losses = ?, games = ? WHERE username = ?;",(userlosses, usergames, selecteduser))
    conn.commit()
    conn.close()

def createdeck():
    global deck
    for color in range(1,5):
        for value1 in values:
            cardlist.append(card(color,value1,1))
    for value2 in range(13,15):
        for i in range(4):
            cardlist.append(card(5,value2,1))
    deck = cardlist
    random.shuffle(deck)

def createhands():
    global lastplayedcard
    for i in range(noplayers + 1):
        users.append(player(0))
        for x in range(7):
            for card in deck:
                if card.indeck == 1:
                    users[i].addcard(card)
                    card.indeck = 2
                    break
    for i in deck:
        if i.indeck == 1:
            lastplayedcard = i
            i.indeck = 2
            break

def sorthands():
    redcards = []
    bluecards = []
    greencards = []
    yellowcards = []
    blackcards = []
    hand = []
    for i in range(noplayers + 1):
        hand.clear()
        redcards.clear()
        bluecards.clear()
        greencards.clear()
        yellowcards.clear()
        blackcards.clear()
        for x in users[i].hand:
            if x.color == 1:
                redcards.append(x)
            elif x.color == 2:
                bluecards.append(x)
            elif x.color == 3:
                greencards.append(x)
            elif x.color == 4:
                yellowcards.append(x)
            elif x.color == 5:
                blackcards.append(x)

        bubblesort2(redcards)
        bubblesort2(bluecards)
        bubblesort2(greencards)
        bubblesort2(yellowcards)
        bubblesort2(blackcards)

        hand = redcards + bluecards + greencards + yellowcards + blackcards
        users[i].hand.clear()
        for z in hand:
            users[i].addcard(z)

def bubblesort2(y):
    length = len(y)
    for i in range(length-1):
        for j in range(0,length-i-1):
            if int(y[j].value) > int(y[j+1].value):
                y[j], y[j+1] = y[j+1], y[j]
    return y

def playcard(color,value,x):
    global lastplayedcard
    if color != 99 and value != 99:
        hand = users[x].hand
        for i in hand:
            if i.color == color and i.value == value:
                lastplayedcard = i
                for z in deck:
                    if z == i:
                        z.indeck = 3
                users[x].hand.remove(i)
                break
    elif color == 99 and value == 99:
        pickupcard(x)

    checkcardpower(color,value,x)

def checkcardpower(color,value,x):
    global lastplayedcard, direction, loopbreak, position
    if value == 10:
        position = x
        if x == 3 and direction == True:
            position = -1
        elif x == 0 and direction == False:
            position = 4
        loopbreak = 2

    if value == 11:
        position = x
        loopbreak = 1
        if direction == True:
            direction = False
        elif direction == False:
            direction = True

    if value == 12:
        if direction == True:
            if x == noplayers:
                pickupcard(0)
                pickupcard(0)
            else:
                pickupcard(x+1)
                pickupcard(x+1)
        elif direction == False:
            if x == 0:
                pickupcard(noplayers)
                pickupcard(noplayers)
            else:
                pickupcard(x-1)
                pickupcard(x-1)
        position = x
        if x == 3 and direction == True:
            position = -1
        elif x == 0 and direction == False:
            position = 4
        loopbreak = 2

    if value == 13:
        changecolor(x)

    if value == 14:
        changecolor(x)
        if direction == True:
            if x == noplayers:
                pickupcard(0)
                pickupcard(0)
                pickupcard(0)
                pickupcard(0)
            else:
                pickupcard(x+1)
                pickupcard(x+1)
                pickupcard(x+1)
                pickupcard(x+1)
        elif direction == False:
            if x == 0:
                pickupcard(noplayers)
                pickupcard(noplayers)
                pickupcard(noplayers)
                pickupcard(noplayers)
            else:
                pickupcard(x-1)
                pickupcard(x-1)
                pickupcard(x-1)
                pickupcard(x-1)
        position = x
        if x == 3 and direction == True:
            position = -1
        elif x == 0 and direction == False:
            position = 4
        loopbreak = 2

def changecolor(i):
    if i == 0:
        waiting = True
        while waiting == True:
            pygame.draw.rect(screen,black,(340,190,720,320))
            pygame.draw.rect(screen,white,(345,195,710,310))
            pygame.draw.rect(screen,red,(350,200,350,150))
            pygame.draw.rect(screen,green,(700,200,350,150))
            pygame.draw.rect(screen,blue,(350,350,350,150))
            pygame.draw.rect(screen,yellow,(700,350,350,150))
            screen.blit(changeredtext,(420,210))
            screen.blit(changegreentext,(730,210))
            screen.blit(changebluetext,(400,350))
            screen.blit(changeyellowtext,(705,350))
            pygame.display.update()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 350 < mouse[0] < 700 and 200 < mouse[1] < 350:
                        lastplayedcard.color = 1
                        waiting = False
                    elif 700 < mouse[0] < 1050 and 200 < mouse[1] < 350:
                        lastplayedcard.color = 2
                        waiting = False
                    elif 350 < mouse[0] < 700 and 350 < mouse[1] < 700:
                        lastplayedcard.color = 3
                        waiting = False
                    elif 700 < mouse[0] < 1050 and 350 < mouse[1] < 700:
                        lastplayedcard.color = 4
                        waiting = False
        updategamepage(i)

    else:
        colorvalue = [0,0,0,0]
        for x in users[i].hand:
            if x.color == 1:
                colorvalue[0] += 1
            elif x.color == 2:
                colorvalue[1] +=1
            elif x.color == 3:
                colorvalue[2] +=1
            elif x.color == 4:
                colorvalue[3] +=1

        for x in range(len(colorvalue)):
            if colorvalue[x] == max(colorvalue):
                newcolor = x+1
        lastplayedcard.color = newcolor

def getinput(i):
    global ichipress, gamepause
    updategamepage(i)
    if i == 0:
        valid = False
        while valid == False:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    pausepage()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 5 < mouse[0] < 215 and 585 < mouse[1] < 695:
                        playcard(99,99,i)
                        valid = True
                        break
                    if 5 < mouse[0] < 215 and 470 < mouse[1] < 580:
                        ichipress = True
                    if 0 < mouse[0] < 130 and 0 < mouse[1] < 60:
                        gamepause = True
                        valid = True
                    pos = 235
                    poss = 410
                    if len(users[0].hand) < 12:
                        for x in range(len(users[0].hand)):
                            if pos < mouse[0] < pos+80 and poss < mouse[1] < poss+140:
                                card = users[0].hand[x]
                                if lastplayedcard.color == card.color or lastplayedcard.value == card.value or card.color == 5:
                                    valid = True
                                    playcard(card.color,card.value,i)
                                    break
                            pos += 85
                    else:
                        for x in range(11):
                            if pos < mouse[0] < pos+80 and poss < mouse[1] < poss+140:
                                card = users[0].hand[x]
                                if lastplayedcard.color == card.color or lastplayedcard.value == card.value or card.color == 5:
                                    valid = True
                                    playcard(card.color,card.value,i)
                                    break
                            pos += 85
                        pos = 235
                        poss = 555
                        for x in range(len(users[0].hand)-11):
                            if pos < mouse[0] < pos+80 and poss < mouse[1] < poss+140:
                                card = users[0].hand[x+11]
                                if lastplayedcard.color == card.color or lastplayedcard.value == card.value or card.color == 5:
                                    valid = True
                                    playcard(card.color,card.value,i)
                                    break
                            pos += 85

    else:
        for x in range(len(users[i].hand)):
            if lastplayedcard.color == users[i].hand[x].color or lastplayedcard.value == users[i].hand[x].value or users[i].hand[x].color == 5:
                color = int(users[i].hand[x].color)
                value = int(users[i].hand[x].value)
                break
            else:
                color = value = 99
        playcard(color,value,i)

def pickupcard(x):
    for i in deck:
        if i.indeck == 1:
            users[x].addcard(i)
            i.indeck = 2
            break

    checkdeck()
    sorthands()

def checkdeck():
    global deck
    no = 0
    for i in deck:
        if i.indeck == 1:
            no +=1
    if no == 0:
        for x in deck:
            if x.indeck == 3:
                x.indeck = 1
        random.shuffle(deck)

def checkichi(i):
    global ichipress
    randomchance = [1,2,3,4,5]
    if i != 0:
        random.shuffle(randomchance)
        if randomchance[1] != 1 and len(users[i].hand) == 1:
            ichipress = True
    if ichipress == False and len(users[i].hand) == 1:
        pickupcard(i)
        pickupcard(i)
    elif ichipress == True and len(users[i].hand) != 1:
        pickupcard(i)
        pickupcard(i)
    ichipress = False

def checkwin(i):
    global winner, gamecomplete
    if len(users[i].hand) == 0:
        winner = i
        gamecomplete = True

def updategamepage(x):
    if lastplayedcard.color == 1:
        last_color = red
    elif lastplayedcard.color == 2:
        last_color = green
    elif lastplayedcard.color == 3:
        last_color = blue
    elif lastplayedcard.color == 4:
        last_color = yellow
    elif lastplayedcard.color == 5:
        last_color = black

    screen.blit(background,(0,0))

    if direction == True:
        screen.blit(directionTrue,(510,150))
    elif direction == False:
        screen.blit(directionFalse,(490,150))

    pygame.draw.rect(screen,white,(5,470,210,110))
    pygame.draw.rect(screen,black,(10,475,200,100))
    screen.blit(ichibuttontext,(15,475))

    pygame.draw.rect(screen,color_light,(0,0,130,60))
    screen.blit(pausebuttontext,(5,0))

    pygame.draw.rect(screen,black,(620,170,160,230))
    pygame.draw.rect(screen,last_color,(625,175,150,220))

    if last_color == black:
        pygame.draw.rect(screen,white,(620,170,160,230))
        pygame.draw.rect(screen,last_color,(625,175,150,220))

    pygame.draw.rect(screen,white,(5,585,210,110))
    pygame.draw.rect(screen,black,(10,590,200,100))
    screen.blit(deckbuttontext,(15,590))

    cardposition = [235,410]
    cardvalueposition = [240,450]
    for i in range(len(users[0].hand)):
        if x == 0:
            if users[0].hand[i].color == 1:
                new_color = red
            elif users[0].hand[i].color == 2:
                new_color = green
            elif users[0].hand[i].color == 3:
                new_color = blue
            elif users[0].hand[i].color == 4:
                new_color = yellow
            elif users[0].hand[i].color == 5:
                new_color = black
        elif x !=0:
            if users[0].hand[i].color == 1:
                new_color = darkred
            elif users[0].hand[i].color == 2:
                new_color = darkgreen
            elif users[0].hand[i].color == 3:
                new_color = darkblue
            elif users[0].hand[i].color == 4:
                new_color = darkyellow
            elif users[0].hand[i].color == 5:
                new_color = darkblack


        pygame.draw.rect(screen,black,(cardposition[0],cardposition[1],80,140))
        pygame.draw.rect(screen,new_color,((cardposition[0]+5),cardposition[1]+5,70,130))

        if new_color == black or new_color == darkblack:
            pygame.draw.rect(screen,white,(cardposition[0],cardposition[1],80,140))
            pygame.draw.rect(screen,new_color,((cardposition[0]+5),cardposition[1]+5,70,130))

        if users[0].hand[i].value < 10:
            new_value = font60.render(str(users[0].hand[i].value),True,black)
            screen.blit(new_value,(cardvalueposition[0]+20,cardvalueposition[1]))
        elif users[0].hand[i].value == 10:
            new_value = font35.render('Skip',True,black)
            screen.blit(new_value,(cardvalueposition[0]+2.5,cardvalueposition[1]+10))
        elif users[0].hand[i].value == 11:
            new_value = font20.render('Reverse',True,black)
            screen.blit(new_value,(cardvalueposition[0]+2.5,cardvalueposition[1]+20))
        elif users[0].hand[i].value == 12:
            new_value = font60.render('+2',True,black)
            screen.blit(new_value,(cardvalueposition[0],cardvalueposition[1]))
        elif users[0].hand[i].value == 13:
            new_value = font35.render('Wild',True,white)
            screen.blit(new_value,(cardvalueposition[0],cardvalueposition[1]+15))
        elif users[0].hand[i].value == 14:
            new_value = font60.render('+4',True,white)
            screen.blit(new_value,(cardvalueposition[0],cardvalueposition[1]))

        cardposition[0] +=85
        cardvalueposition[0] +=85

        if cardposition[0] == 1170:
            cardposition[0] = 235
            cardposition[1] +=145

        if cardvalueposition[0] == 1175:
            cardvalueposition[0] = 240
            cardvalueposition[1] +=145

    if lastplayedcard.value < 10:
        last_value = font120.render(str(lastplayedcard.value),True,black)
        screen.blit(last_value,(670,220))
    elif lastplayedcard.value == 10:
        last_value = font70.render('Skip',True,black)
        screen.blit(last_value,(635,240))
    elif lastplayedcard.value == 11:
        last_value = font40.render('Reverse',True,black)
        screen.blit(last_value,(635,260))
    elif lastplayedcard.value == 12:
        last_value = font120.render('+2',True,black)
        screen.blit(last_value,(630,220))
    elif lastplayedcard.value == 13:
        last_value = font70.render('Wild',True,black)
        screen.blit(last_value,(630,240))
    elif lastplayedcard.value == 14:
        last_value = font120.render('+4',True,black)
        screen.blit(last_value,(630,220))

    if noplayers == 1:
        gameuser1 = font60.render(botlist[0],True,black)
        screen.blit(gameuser1,(560,0))
        gameuser1cards = font40.render('Number of cards: '+str(len(users[1].hand)),True,black)
        screen.blit(gameuser1cards,(560,75))
    elif noplayers == 2:
        gameuser1 = font60.render(botlist[0],True,black)
        gameuser2 = font60.render(botlist[1],True,black)
        screen.blit(gameuser1,(25,125))
        screen.blit(gameuser2,(1050,125))
        gameuser1cards = font40.render('Number of cards: '+str(len(users[1].hand)),True,black)
        gameuser2cards = font40.render('Number of cards: '+str(len(users[2].hand)),True,black)
        screen.blit(gameuser1cards,(25,200))
        screen.blit(gameuser2cards,(1050,200))
    elif noplayers == 3:
        gameuser1 = font60.render(botlist[0],True,black)
        gameuser2 = font60.render(botlist[1],True,black)
        gameuser3 = font60.render(botlist[2],True,black)
        screen.blit(gameuser1,(25,125))
        screen.blit(gameuser2,(560,0))
        screen.blit(gameuser3,(1050,125))
        gameuser1cards = font40.render('Number of cards: '+str(len(users[1].hand)),True,black)
        gameuser2cards = font40.render('Number of cards: '+str(len(users[2].hand)),True,black)
        gameuser3cards = font40.render('Number of cards: '+str(len(users[3].hand)),True,black)
        screen.blit(gameuser1cards,(25,200))
        screen.blit(gameuser2cards,(560,75))
        screen.blit(gameuser3cards,(1050,200))

    pygame.display.update()

def getbotnames():
    global selecteduser
    conn = sqlite3.connect('ichidatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM USER WHERE username != ?",(selecteduser,))
    botnamedata = cursor.fetchall()
    conn.close()

    for i in botnamedata:
        botname = ''
        for item in i:
            botname = botname + item
        botlist.append(botname)

    random.shuffle(botlist)

def pausepage():
    global gamepause
    gamepause = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= mouse[1] <= 460:
                    if 410 <= mouse[0] <= 650:
                        gamepage()
                    if 750 <= mouse[0] <= 990:
                        startpage()

        mouse = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))
        screen.blit(background,(0,0))

        screen.blit(ichicharacter, (0, 0))
        screen.blit(ichicharacter, (0, 550))
        screen.blit(ichicharacter, (1100, 0))
        screen.blit(ichicharacter, (1100, 550))

        pygame.draw.rect(screen,color_light,(410,400,240,60))
        screen.blit(resumetext,(445,400))
        pygame.draw.rect(screen,color_light,(750,400,240,60))
        screen.blit(mainmenutext,(755,400))

        screen.blit(pausedtext,(380,150))

        pygame.display.update()


screen = pygame.display.set_mode((1400, 700))
pygame.display.set_caption('Ichi')
white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (140, 140, 140)
black = (0, 0, 0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
darkred = (155,0,0)
darkgreen = (0,155,0)
darkblue = (0,0,155)
darkyellow = (155,155,0)
darkblack = (100,100,100)
selecteduser = "No user"
direction = win = True
rulestextposition = 60
usertextposition = 150
lastusers = list()
mostwinsuser = list()
mostwins = list()
mostgamesuser = list()
mostgames = list()
mostlossesuser = list()
mostlosses = list()
userwins = userlosses = usergames = ''
deck = []
cardlist = []
users = []
botlist = []
values = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]
gamecomplete = ichipress = gamepause = uservalid = False
position = winner = loopbreak = noplayers = 0

ichicharacter = pygame.image.load(r'Ichicharacter.png')
ichicharacter = pygame.transform.scale(ichicharacter, (300 ,150))
ichicharacter.set_colorkey((255, 255, 255))

background = pygame.image.load(r'background.png')
background = pygame.transform.scale(background, (1400, 700))

directionTrue = pygame.image.load(r'directionTrue.png')
directionTrue = pygame.transform.scale(directionTrue,(400,200))
directionFalse = pygame.image.load(r'directionFalse.png')
directionFalse = pygame.transform.scale(directionFalse,(400,200))

font280 = pygame.font.SysFont('Times new roman', 280)
font270 = pygame.font.SysFont('Times new roman', 270)
font120 = pygame.font.SysFont('Times new roman', 120)
font90 = pygame.font.SysFont('Times new roman', 90)
font80 = pygame.font.SysFont('Times new roman', 80)
font75 = pygame.font.SysFont('Times new roman', 75)
font70 = pygame.font.SysFont('Times new roman', 70)
font60 = pygame.font.SysFont('Times new roman', 60)
font50 = pygame.font.SysFont('Times new roman', 50)
font40 = pygame.font.SysFont('Times new roman', 40)
font35 = pygame.font.SysFont('Times new roman', 35)
font30 = pygame.font.SysFont('Times new roman', 30)
font25 = pygame.font.SysFont('Times new roman', 25)
font20 = pygame.font.SysFont('Times new roman', 20)

title1 = font270.render('Ichi', True, white)
title2 = font280.render('Ichi', True, black)
playgamebuttontext = font75.render('Play Game', True, black)
viewleaderboardbuttontext = font75.render('View Leaderboard', True, black)
changeuserbuttontext = font75.render('Change User', True, black)
rulesbuttontext = font75.render('Rules', True, black)
quitbuttontext = font75.render('Quit', True, black)

noplayerstext = font90.render('How many players?', True, black)
onebuttontext = font75.render('1', True, black)
twobuttontext = font75.render('2', True, black)
threebuttontext = font75.render('3', True, black)

backbuttontext = font50.render('Back', True, black)

rulesupperbackground = pygame.image.load(r'rulesupperbackground.png')
rulesupperbackground = pygame.transform.scale(rulesupperbackground, (1400,50))
ruleslowerbackground = pygame.image.load(r'lowerbackground.png')
ruleslowerbackground = pygame.transform.scale(ruleslowerbackground, (1400,50))
rulestitletext = font50.render("ICHI RULES", True, black)
rulestext1 = font30.render("SETUP", True, black)
rulestext2 = font30.render("GAMEPLAY", True, black)
rulestext3 = font30.render("SPECIAL CARDS", True, black)
rulestext4 = font25.render("COLOUR CARDS:", True, black)
rulestext5 = font25.render("WILD CARDS:", True, black)
rules = ["Every player starts with seven cards. The rest of the cards are placed in a Draw","Pile. The top card will be placed in the center and used as the starter card.","Then the game begins!","The user will start then the game will continue in a clockwise direction. Each","player has to try match the colour, number or symbol of the previous card, or","the player can use a wild card If the player cannot play a card or chooses not","to, then a card must be picked up from the Draw Pile and added to the player's","hand.","The game continues until a player has only one card left. Before the","player places their second last card, they must press the 'ICHI!' button. If a","player fails to do this, another player may press the 'ICHI!' button and cause","a penalty to the player with only one card left. The penalty is to pick two cards","from the Draw Pile and add them to the player's hand.","The aim of the game is to be the first player to place down all of your cards.","There are 2 types of specical cards; colour and wild. The colour cards must be","played like any other card, on a matching colour or symbol. The wild cards","can be played on any card. ","Reverse – If going clockwise, switch to counterclockwise or vice versa.","Skip – The next player has to skip their turn.","+2 – The next player will have to pick up two cards.","Change Colour – The player can choose a colour to set the game to","+4 – Acts in the same way as the Change Colour with the difference that it","         will also cause the next player to pick up 4 cards."]

newuserbuttontext = font60.render('Create new user', True, black)
userupperbackground = pygame.image.load(r'userupperbackground.png')
userupperbackground = pygame.transform.scale(userupperbackground, (1400,150))
userlowerbackground = pygame.image.load(r'lowerbackground.png')
userlowerbackground = pygame.transform.scale(userlowerbackground, (1400,50))

winstext = font50.render('Wins', True, black)
lossestext = font50.render('Losses', True, black)
gamestext = font50.render('Games', True, black)

enterusertext = font90.render('Enter username', True, black)
createusertext = font50.render('Create user', True, black)

playagaintext = font50.render('Play again', True, black)
mainmenutext = font50.render('Main menu', True, black)
pausedtext = font120.render('Game paused', True, black)
resumetext = font50.render('Resume', True, black)

playagaintext = font50.render('Play again', True, black)
mainmenutext = font50.render('Main menu', True, black)
pausedtext = font120.render('Game paused', True, black)
resumetext = font50.render('Resume', True, black)
changeredtext = font120.render('Red',True,black)
changegreentext = font120.render('Green',True,black)
changebluetext = font120.render('Blue',True,black)
changeyellowtext = font120.render('Yellow',True,black)
ichibuttontext = font90.render('ICHI',True,white)
pausebuttontext = font50.render('Pause',True,black)
deckbuttontext = font90.render('Deck',True,white)

startpage()
