import random
import time
from termcolor import colored
newstate = dict()
print '''Sticker positions:

        16 15
        14 13
  19 17 01 02 10 12
  20 18 03 04 09 11
        05 06
        07 08
        21 22
        23 24
'''
option = raw_input('''Please choose an option:
1: Enter cube state
2 or <Enter>: Solved cube state
''')
solved = ['state',colored(u"\u25a0", 'white'),colored(u"\u25a0", 'white'),colored(u"\u25a0", 'white'),colored(u"\u25a0", 'white'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'yellow'),colored(u"\u25a0", 'yellow'),colored(u"\u25a0", 'yellow'),colored(u"\u25a0", 'yellow')]
cube = ['state',colored(u"\u25a0", 'white'),colored(u"\u25a0", 'white'),colored(u"\u25a0", 'white'),colored(u"\u25a0", 'white'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'red'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'blue'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'magenta'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'green'),colored(u"\u25a0", 'yellow'),colored(u"\u25a0", 'yellow'),colored(u"\u25a0", 'yellow'),colored(u"\u25a0", 'yellow')]
cubestate = ['state','','','','','','','','','','','','','','','','','','','','','','','','']
if option == '1':
    for i in range(1,25):
        cubestate[i] = raw_input("What is the state of sticker %i?: " %(i))
        if cubestate[i] == 'r' or cubestate[i] == '~':
          cubestate[i] = colored(u"\u25a0", 'red')
        if cubestate[i] == 'b' or cubestate[i] == '.':
          cubestate[i] = colored(u"\u25a0", 'blue')
        if cubestate[i] == 'o' or cubestate[i] == ',':
          cubestate[i] = colored(u"\u25a0", 'magenta')
        if cubestate[i] == 'g' or cubestate[i] == '0':
          cubestate[i] = colored(u"\u25a0", 'green')
        if cubestate[i] == 'w' or cubestate[i] == '^':
          cubestate[i] = colored(u"\u25a0", 'white')
        if cubestate[i] == 'y' or cubestate[i] == '#':
          cubestate[i] = colored(u"\u25a0", 'yellow')
if option == '2' or option == '':
    for i in range(1,25):
        cubestate[i] = solved[i]
for i in range(1,25):
    cube[i] = cubestate[i]
first = raw_input("What color would you like to solve first?: ")
if first == '':
    first = cubestate[1]
def graphic(x):
    print '''
      %s %s
      %s %s
  %s %s %s %s %s %s
  %s %s %s %s %s %s
      %s %s
      %s %s
      %s %s
      %s %s
    '''%(x[16],x[15],x[14],x[13],x[19],x[17],x[1],x[2],x[10],x[12],x[20],x[18],x[3],x[4],x[9],x[11],x[5],x[6],x[7],x[8],x[21],x[22],x[23],x[24])
def mainr(cube):
    newstate = cube
    oldcube = (cube[0:len(cube)])
    newstate[2] = oldcube[6]
    newstate[4] = oldcube[8]
    newstate[6] = oldcube[22]
    newstate[8] = oldcube[24]
    newstate[22] = oldcube[15]
    newstate[24] = oldcube[13]
    newstate[15] = oldcube[2]
    newstate[13] = oldcube[4]
    newstate[9] = oldcube[11]
    newstate[10] = oldcube[9]
    newstate[11] = oldcube[12]
    newstate[12] = oldcube[10]
    cube = newstate
def r():
    mainr(cube)
def R():
    r()
    r()
    r()
def mainl(cube):
    newstate = cube
    oldcube = (cube[0:len(cube)])
    newstate[1] = oldcube[16]
    newstate[3] = oldcube[14]
    newstate[5] = oldcube[1]
    newstate[7] = oldcube[3]
    newstate[21] = oldcube[5]
    newstate[23] = oldcube[7]
    newstate[16] = oldcube[21]
    newstate[14] = oldcube[23]
    newstate[17] = oldcube[19]
    newstate[18] = oldcube[17]
    newstate[19] = oldcube[20]
    newstate[20] = oldcube[18]
    cube = newstate
def l():
    mainl(cube)
def L():
    l()
    l()
    l()
def mainu(cube):
    newstate = cube
    oldcube = (cube[0:len(cube)])
    newstate[5] = oldcube[9]
    newstate[6] = oldcube[10]
    newstate[9] = oldcube[13]
    newstate[10] = oldcube[14]
    newstate[13] = oldcube[17]
    newstate[14] = oldcube[18]
    newstate[17] = oldcube[5]
    newstate[18] = oldcube[6]
    newstate[1] = oldcube[3]
    newstate[2] = oldcube[1]
    newstate[3] = oldcube[4]
    newstate[4] = oldcube[2]
    cube = newstate
def u():
    mainu(cube)
def U():
    u()
    u()
    u()
def maind(cube):
    newstate = cube
    oldcube = (cube[0:len(cube)])
    newstate[7] = oldcube[19]
    newstate[8] = oldcube[20]
    newstate[11] = oldcube[7]
    newstate[12] = oldcube[8]
    newstate[15] = oldcube[11]
    newstate[16] = oldcube[12]
    newstate[19] = oldcube[15]
    newstate[20] = oldcube[16]
    newstate[21] = oldcube[23]
    newstate[22] = oldcube[21]
    newstate[23] = oldcube[24]
    newstate[24] = oldcube[22]
    cube = newstate
def d():
    maind(cube)
def D():
    d()
    d()
    d()
def mainf(cube):
    newstate = cube
    oldcube = (cube[0:len(cube)])
    newstate[3] = oldcube[20]
    newstate[4] = oldcube[18]
    newstate[9] = oldcube[3]
    newstate[11] = oldcube[4]
    newstate[22] = oldcube[9]
    newstate[21] = oldcube[11]
    newstate[20] = oldcube[22]
    newstate[18] = oldcube[21]
    newstate[5] = oldcube[7]
    newstate[6] = oldcube[5]
    newstate[7] = oldcube[8]
    newstate[8] = oldcube[6]
    cube = newstate
def f():
    mainf(cube)
def F():
    f()
    f()
    f()
def mainb(cube):
    newstate = cube
    oldcube = (cube[0:len(cube)])
    newstate[1] = oldcube[10]
    newstate[2] = oldcube[12]
    newstate[10] = oldcube[24]
    newstate[12] = oldcube[23]
    newstate[24] = oldcube[19]
    newstate[23] = oldcube[17]
    newstate[19] = oldcube[1]
    newstate[17] = oldcube[2]
    newstate[13] = oldcube[15]
    newstate[14] = oldcube[13]
    newstate[15] = oldcube[16]
    newstate[16] = oldcube[14]
    cube = newstate
def b():
    mainb(cube)
def B():
    b()
    b()
    b()
def x():
    L()
    r()
def X():
    x()
    x()
    x()
def y():
    d()
    U()
def Y():
    y()
    y()
    y()
def z():
    B()
    f()
def Z():
    b()
    F()
moves = ['r','l','f','b','u','d']
finalalg = ''
finalalg2 = ''
def use(alg):
    global finalalg
    global finalalg2
    if alg == 'tperm':
        alg = 'ruRURfrrURUruRF'
    if alg == 'yperm':
        alg = 'frURUruRFruRURfrF'
    if alg == 'sune':
        alg = 'ruRuruuR'
    if alg == 'antisune':
        alg = 'RUrURuur'
    if alg == 'headlights':
        alg = 'fruRUF'
    if alg == 'racecar':
        alg = 'fruRUruRUF'
    if alg == 'superman':
        alg = 'fruRUruRUruRUF'
    if alg == 'chameleon':
        alg = 'ruRURfrF'
    if alg == 'bowtie':
        alg = 'RfrBRFrb'
    if alg == 'yperm':
        alg = 'fruRUruRFruRURfrF'
    finalalg = finalalg + alg
    finalalg = str.replace(finalalg,"uuuu", "")
    finalalg = str.replace(finalalg,"brBbrBbrB", "bRB")
    finalalg = str.replace(finalalg,"brBbrB", "brrB")
    finalalg = str.replace(finalalg,"brBbrrB","bRB")
    finalalg = str.replace(finalalg,"brrBbrB","bRB")
    finalalg = str.replace(finalalg,'uuu','U')
    finalalg = str.replace(finalalg,'zzzz','')
    finalalg = str.replace(finalalg,'ZZZZ','')
    finalalg = str.replace(finalalg,'YYYY','')
    finalalg = str.replace(finalalg,'yyyy','')
    finalalg = str.replace(finalalg,'XXXX','')
    finalalg = str.replace(finalalg,'xxxx','')
    finalalg = str.replace(finalalg,'y','dU')
    finalalg = str.replace(finalalg,'Y','Du')
    finalalg = str.replace(finalalg,'x','rL')
    finalalg = str.replace(finalalg,'X','Rl')
    finalalg = str.replace(finalalg,'z','fB')
    finalalg = str.replace(finalalg,'Z','Fb')

    for move in range(0,len(alg)):
        turn = alg[move]
        if turn == "r":
            r()
        elif turn == "R":
            R()
        elif turn == "l":
            l()
        elif turn == "L":
            L()
        elif turn == "f":
            f()
        elif turn == "F":
            F()
        elif turn == "u":
            u()
        elif turn == "U":
            U()
        elif turn == "b":
            b()
        elif turn == "B":
            B()
        elif turn == "d":
            d()
        elif turn == "D":
            D()
        elif turn == "x":
            x()
        elif turn == "X":
            X()
        elif turn == "z":
            z()
        elif turn == "Z":
            Z()
        elif turn == "y":
            y()
        elif turn == "Y":
            Y()
        else:
            print "Unknown move:", turn
def use1(alg):
    if alg == 'tperm':
        alg = 'ruRURfrrURUruRF'
    if alg == 'yperm':
        alg = 'frURUruRFruRURfrF'
    if alg == 'sune':
        alg = 'ruRuruuR'
    if alg == 'antisune':
        alg = 'RUrURuur'
    if alg == 'headlights':
        alg = 'fruRUF'
    if alg == 'racecar':
        alg = 'fruRUruRUF'
    if alg == 'superman':
        alg = 'fruRUruRUruRUF'
    if alg == 'chameleon':
        alg = 'ruRURfrF'
    if alg == 'bowtie':
        alg = 'RfrBRFrb'
    if alg == 'yperm':
        alg = 'fruRUruRFruRURfrF'
    print alg
    for move in range(0,len(alg)):
        turn = alg[move]
        if turn == "r":
            r()
        elif turn == "R":
            R()
        elif turn == "l":
            l()
        elif turn == "L":
            L()
        elif turn == "f":
            f()
        elif turn == "F":
            F()
        elif turn == "u":
            u()
        elif turn == "U":
            U()
        elif turn == "b":
            b()
        elif turn == "B":
            B()
        elif turn == "d":
            d()
        elif turn == "D":
            D()
        elif turn == "x":
            x()
        elif turn == "X":
            X()
        elif turn == "z":
            z()
        elif turn == "Z":
            Z()
        elif turn == "y":
            y()
        elif turn == "Y":
            Y()
        else:
            print "Unknown move:", turn
top = cube[1:5]
front = cube[5:9]
right = cube[9:13]
back = cube[13:17]
left = cube[17:21]
bottom = cube[21:len(cube)]
def bottomcheck():
    if cube[21] == cube[22] == cube[23] == cube[24]:
        return True
    else:
        return False
def rightcheck():
    if cube[9] == cube[10] == cube[11] == cube[12]:
        return True
    else:
        return False
def frontcheck():
    if cube[5] == cube[6] == cube[7] == cube[8]:
        return True
    else:
        return False
def topcheck():
    if cube[1] == cube[2] == cube[3] == cube[4]:
        return True
    else:
        return False
def leftcheck():
    if cube[17] == cube[18] == cube[19] == cube[20]:
        return True
    else:
        return False
def backcheck():
    if cube[13] == cube[14] == cube[15] == cube[16]:
        return True
    else:
        return False
def bottomlayercheck():
    if cube[21] == cube[22] == cube[23] == cube[24] and cube[7] == cube[8] and cube[11] == cube[12] and cube[15] == cube[16] and cube[19] == cube[20]:
        return True
    else:
        return False
def rightlayercheck():
    if cube[9] == cube[10] == cube[11] == cube[12] and cube[4] == cube[2] and cube[13] == cube[15] and cube[24] == cube[22] and cube[6] == cube[8]:
        return True
    else:
        return False
def frontlayercheck():
    if cube[5] == cube[6] == cube[7] == cube[8] and cube[3] == cube[4] and cube[9] == cube[11] and cube[21] == cube[22] and cube[20] == cube[18]:
        return True
    else:
        return False
def toplayercheck():
    if cube[1] == cube[2] == cube[3] == cube[4] and cube[5] == cube[6] and cube[9] == cube[10] and cube[13] == cube[14] and cube[17] == cube[18]:
        return True
    else:
        return False
def leftlayercheck():
    if cube[17] == cube[18] == cube[19] == cube[20] and cube[1] == cube[3] and cube[5] == cube[7] and cube[21] == cube[23] and cube[16] == cube[14]:
        return True
    else:
        return False
def backlayercheck():
    if cube[13] == cube[14] == cube[15] == cube[16] and cube[1] == cube[3] and cube[10] == cube[12] and cube[23] == cube[24] and cube[19] == cube[17]:
        return True
    else:
        return False
def solvedcheck():
    if backlayercheck() == frontlayercheck() == toplayercheck() == bottomlayercheck() == rightlayercheck() == leftlayercheck() == True:
        return True
def solveddown():
    while True:
        if bottomlayercheck() == True:
            break
        elif toplayercheck() == True:
            use('fbfb')
            break
        elif rightlayercheck() == True:
            use('z')
            break
        elif leftlayercheck() == True:
            use('Z')
            break
        elif frontlayercheck() == True:
            use('X')
            break
        elif backlayercheck() == True:
            use('x')
            break
def solvedsidedown():
    while True:
        if bottomcheck() == True:
            break
        elif topcheck() == True:
            use('fbfb')
            break
        elif rightcheck() == True:
            use('z')
            break
        elif leftcheck() == True:
            use('Z')
            break
        elif frontcheck() == True:
            use('X')
            break
        elif backcheck() == True:
            use('x')
            break
def oll():
    while True:
        if topcheck() == True:
            break
        else:
            for i in range(4):
                use('u')
                if cube[1] == cube[4] == cube[5] == cube[10]:
                    use('bowtie')
                    break
                elif cube[3] == cube[6] == cube[10] == cube[14]:
                    use('sune')
                    break
                elif cube[1] == cube[5] == cube[9] == cube[13]:
                    use('antisune')
                    break
                elif cube[1] == cube[2] == cube[5] == cube[6]:
                    use('u')
                    use('headlights')
                    break
                elif cube[2] == cube[4] == cube[5] == cube[14]:
                    use('chameleon')
                    break
                elif cube[6] == cube[13] == cube[17] == cube[18]:
                    use('racecar')
                    break
                elif cube[5] == cube[6] == cube[13] == cube[14]:
                    use('superman')
                    break

def pll():
    while True:
        for i in range(4):
            use('u')
            if toplayercheck() == True:
                break
            elif topcheck() == True and cube[5] == cube[14] == cube[7] == cube[8] and cube[6] == cube[13] == cube[15] == cube[16]:
                use('yperm')
                break
            elif topcheck() == True and cube[6] == cube[13] and cube[9] == cube[14]:
                use('tperm')
                break
        break
def lastmove():
    if cube[5] == cube[19]:
        use('u')
    elif cube[5] == cube[15]:
        use('uu')
    elif cube[5] == cube[11]:
        use('U')
flips = ['x','y','z']
def getnext():
    while True:
        for i in range(3):
            if topcheck() == True:
                break
            use('brB')
            if cube[3] == cube[4] == first:
                use('u')
                break
            elif cube[3] == cube[9] == first:
                use('RdrDRdrDRdrDRdrDu')
                break
            elif cube[3] == cube[6] == first:
                use('RdrDRdrDu')
                break
        if topcheck() == True:
            break
        use('d')
def firstside():
    while True:
        if cube[3] == first:
            break
        elif cube[1] == first:
            use('U')
            break
        elif cube[2] == first:
            use('uu')
            break
        elif cube[4] == first:
            use('u')
            break
        else:
            use(random.choice(flips))
    while True:
        if topcheck() == True:
            break
        getnext()
def simulate():
    graphic(cube)
    global finalalg
    while True:
        alg = raw_input("What algorithm would you like to execute? ")
        if alg == 'oll':
            oll()
            alg = ''
        if alg == 'firstside':
            firstside()
            alg = ''
        if alg == 'scramble':
            print "Scramble:",
            alg = ''
            for i in range(15):
                alg = alg+random.choice(moves)
            use1(alg)
            alg = ''
        if alg == 'lastlayer':
            solveddown()
            oll()
            pll()
            lastmove()
            alg = ''
        if alg == 'solve':
            while True:
                t1 = time.time()
                firstside()
                pll()
                use('fbfb')
                oll()
                pll()
                lastmove()
                if solvedcheck() == True:
                    break
            alg = ''
            print "Solution: ", finalalg
            print "Solved in", time.time()-t1, "seconds"
            finalalg = ''
        if alg == 'newsolve':
            while True:
                listmoves = [R,r,U,u,F,f]
                t1 = time.time()
                for i in range(25):
                    scrambledstate[i] = cubestate[i]

        if alg == 'pll':
            pll()
            alg = ''
        if alg == 'solveddown':
            solveddown()
            alg = ''
        if alg == 'tperm':
            alg = 'ruRURfrrURUruRF'
        if alg == 'yperm':
            alg = 'frURUruRFruRURfrF'
        if alg == 'sune':
            alg = 'ruRuruuR'
        if alg == 'antisune':
            alg = 'RUrURuur'
        if alg == 'headlights':
            alg = 'fruRUF'
        if alg == 'racecar':
            alg = 'fruRUruRUF'
        if alg == 'superman':
            alg = 'rruuruurr'
        if alg == 'chameleon':
            alg = 'ruRURfrF'
        if alg == 'bowtie':
            alg = 'RfrBRFrb'
        for move in range(0,len(alg)):
            turn = alg[move]
            if turn == "r":
                use('r')
            elif turn == "R":
                use('R')
            elif turn == "l":
                use('l')
            elif turn == "L":
                use('L')
            elif turn == "f":
                use('f')
            elif turn == "F":
                use('F')
            elif turn == "u":
                use('u')
            elif turn == "U":
                use('U')
            elif turn == "b":
                use('b')
            elif turn == "B":
                use('B')
            elif turn == "d":
                use('d')
            elif turn == "D":
                use('D')
            elif turn == "x":
                use('x')
            elif turn == "X":
                use('X')
            elif turn == "z":
                use('z')
            elif turn == "Z":
                use('Z')
            elif turn == "y":
                use('y')
            elif turn == "Y":
                use('Y')
            else:
                print "Unknown move:", turn
                break
        graphic(cube)

simulate()