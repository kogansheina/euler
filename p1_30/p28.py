import os
import sys

"""
Number spiral diagonals
"""
RIGHT = 0
LEFT  = 1
DOWN  = 2
UP    = 3
def printspiral(t,s):
    print t
    for l in s:
        print l
        
def goRight(orgcounter, crtcounter, colnumber):
    direction = RIGHT
    orig = orgcounter[DOWN]
    crt = crtcounter[RIGHT]
    if crt > 0:
        crt -= 1 
        colnumber += 1
    if crt == 0:
        direction = DOWN
        orig += 2
        
    origtuple = (orgcounter[RIGHT],orgcounter[LEFT],orig,orgcounter[UP]) 
    crttuple = (crt,crtcounter[LEFT],orig,crtcounter[UP])
          
    return (colnumber,direction,crttuple,origtuple) 
            
def goDown(orgcounter, crtcounter, rownumber):
    direction = DOWN
    orig = orgcounter[LEFT]
    crt = crtcounter[DOWN]
    if crt > 0:
        crt -= 1 
        rownumber += 1
    if crt == 0:
        direction = LEFT
        orig += 2

    origtuple = (orgcounter[RIGHT],orig,orgcounter[DOWN],orgcounter[UP]) 
    crttuple = (crtcounter[RIGHT],orig,crt,crtcounter[UP])
    
    return (rownumber,direction,crttuple,origtuple) 

def goLeft(orgcounter, crtcounter, colnumber):
    direction = LEFT
    orig = orgcounter[UP]
    crt = crtcounter[LEFT]
    if crt > 0:
        crt -= 1 
        colnumber -= 1
    if crt == 0:
        direction = UP
        orig += 2

    origtuple = (orgcounter[RIGHT],orgcounter[LEFT],orgcounter[DOWN],orig) 
    crttuple = (crtcounter[RIGHT],crt,crtcounter[DOWN],orig)

    return (colnumber,direction,crttuple,origtuple) 

def goUp(orgcounter, crtcounter, rownumber):
    direction = UP
    orig = orgcounter[RIGHT]
    crt = crtcounter[UP]
    if crt > 0:
        crt -= 1 
        rownumber -= 1
    if crt == 0:
        direction = RIGHT
        orig += 2

    origtuple = (orig,orgcounter[LEFT],orgcounter[DOWN],orgcounter[UP]) 
    crttuple = (orig,crtcounter[LEFT],crtcounter[DOWN],crt)

    return (rownumber,direction,crttuple,origtuple) 

if __name__ == '__main__':
    from sys import argv
    
    DIRECTION = {RIGHT:"RIGHT",DOWN:"DOWN",LEFT:"LEFT",UP:"UP"}
    debug = False
    if len(argv) == 1:
        number = 1001
    else:
        number = int(argv[1])
        if number%2 == 0:
            print "number must be odd"
            sys.exit(0)
        if len(argv) > 2:
            debug = True
    endnumber = number*number
    spiral = [None]*number
    for i in range(0,number):
        spiral[i]=[0]*number
    begin = number/2    
    row = spiral[begin]
    lastnumber = 1 
    row[begin] = lastnumber
    rownumber = begin
    colnumber = begin
    direction = RIGHT
    # right left down up
    orgcounter = (1,0,-1,0)
    crtcounter = orgcounter
    rettp = (0,direction,crtcounter,orgcounter)
    #if debug:
    #    printspiral("first",spiral) 
    while lastnumber < endnumber:
        if direction == RIGHT:
            rettp = goRight(orgcounter, crtcounter, colnumber)
            colnumber = rettp[0]
            if colnumber == number:
                print "goRight col error : row=%d col=%d last=%d" % (rownumber,colnumber,lastnumber)
                sys.exit(0)
        elif direction == DOWN:
            rettp = goDown(orgcounter, crtcounter, rownumber)
            rownumber = rettp[0]
            if rownumber == number:
                print "goDown row error : row=%d col=%d last=%d" % (rownumber,colnumber,lastnumber)
                sys.exit(0) 
        elif direction == LEFT:
            rettp = goLeft(orgcounter, crtcounter, colnumber)
            colnumber = rettp[0]
            if colnumber == number:
                print "goLeft col error : row=%d col=%d last=%d" % (rownumber,colnumber,lastnumber)
                sys.exit(0)
        else:
            rettp = goUp(orgcounter, crtcounter, rownumber)
            rownumber = rettp[0]
            if rownumber == number:
                print "goUp row error : row=%d col=%d last=%d" % (rownumber,colnumber,lastnumber)
                sys.exit(0) 
        direction = rettp[1]
        crtcounter = rettp[2]
        orgcounter = rettp[3]
        lastnumber += 1 
        row = spiral[rownumber]    
        row[colnumber] = lastnumber
        #if debug:
        #    printspiral("in loop",spiral) 
    if debug:
        printspiral("final",spiral) 
    sum1 = 0
    for i in range(0,number):
        sum1 += spiral[i][i]
    sum2 = 0
    for i in range(0,number):
        sum2 += spiral[i][number-i-1]
    sum = sum1+sum2-1
    print "sum=%d" % sum
        
                    
        
            
        
        
