#!/usr/bin/env python
import os
import sys
from copy import deepcopy

DOWN = 0
RIGHT = 1

"""
Lattice paths
"""
def printlist(s,l,number):
    if len(s) > 0:
        print s
    if len(l) == 0:
        print "empty" 
        return   
    for i in range(0,number+1):
        for j in range(0,number+1):
            point = l[i*(number+1)+j] # list of tuples
            for p in point: # p is 'to' tuple 
                print "(%d, %d) -> (%d, %d) : %d" % (i,j,p[0],p[1],p[2])
        print "\n"
            
def firstLine(number,G):
    i = 0
    for j in range(0,number+1):
        point = []
        point.append((i+1,j,number)) # down
        if j == number:
            point.append((-1,-1,0)) # no right
        else:
            point.append((i,j+1,number-j)) # right
        G.append(point) 
        
    return G
        
def Line(i,number,G):
    for j in range(0,number+1):
        point = []
        point.append((i+1,j,(i+j)*(number-i+1))) #down
        if j == number:
            point.append((-1,-1,0)) # no right
        elif j == 0:
            point.append((i,j+1,number-j)) 
        else:
            point.append((i,j+1,(i+j)*(number-j+1))) 
        G.append(point) 
    
    return G
    
def lastLine(number,G):
    i = number
    for j in range(0,number+1):
        point = []
        point.append((-1,-1,0)) # no down
        if j == number:
            point.append((-1,-1,0)) # no right
        elif j == 0:
            point.append((i,j+1,number-j)) 
        else:
            point.append((i,j+1,(i+j)*(number-j+1))) 
        G.append(point) 

    return G

def goDown(line,col,way,G,number,cc):
    if cc == 1:
        location = line*(number+1)+col
        point = G[location]
        down = point[DOWN]
        next = (down[0],down[1])
        counter = down[2]
        if counter > 0:
            way.append(next)
            point[DOWN] = (down[0],down[1],counter-1)
            G[location] = point
            if next == (number,number):
                return (way,0)
            ret = goDown(next[0],next[1],way,G,number,cc)
            way = ret[0]
            cc = ret[1]
        else:
            cc = -1
    return (way,cc)
    
def goRight(line,col,way,G,number,cc):
    if cc == 1:
        location = line*(number+1)+col
        point = G[location]
        right = point[RIGHT]
        next = (right[0],right[1])
        counter = right[2]
        if counter > 0:
            way.append(next)
            point[RIGHT] = (right[0],right[1],counter-1)
            G[location] = point
            if next == (number,number):
                return (way,0)
            location = next[0]*(number+1)+next[1]
            point = G[location]
            ret = goRight(next[0],next[1],way,G,number,cc)
            way = ret[0]
            cc = ret[1]
        else:
            cc = -1
    return (way,cc)
    
def firstWay(G,number):
    ret = goRight(0,0,[(0,0)],G,number,1)
    way = ret[0]
    cc = ret[1]
    if cc != 0: # need to change direction
        ret = goDown(way[-1][0],way[-1][1],way,G,number,1)
        way = ret[0]
        cc = ret[1]
    return (way,cc)
        
def RightDown(G,number,prev):
    cc = prev[1]
    way = prev[0]
    n = 0
    while cc == 0: 
        print way
        n += 1
        next = (0,0)
        # look for the first point which has another direction free
        for i in range(len(way)-2,-1,-1):
            location = way[i][0]*(number+1)+way[i][1]
            point = G[location]
            right = (point[RIGHT][0],point[RIGHT][1])
            rightcount = point[RIGHT][2]
            down = (point[DOWN][0],point[DOWN][1])
            downcount = point[DOWN][2]
            if rightcount == 0 and downcount == 0: # done
                continue
            if downcount > 0:
                nn = down
            else:
                nn = right
            if nn != way[i+1]:
                next = (nn[0],nn[1])
                break
        if next != (0,0):
            way = way[:i+1]
            way.append(next)
            if next != (number,number):
                # add from here - if you can
                ret = goRight(next[0],next[1],way,G,number,1)
                way = ret[0]
                cc = ret[1]
                if cc != 0: # need to change direction
                    ret = goDown(way[-1][0],way[-1][1],way,G,number,1)
                    way = ret[0]
                    cc = ret[1]
                    if cc != 0:
                        #printlist("GRID-F",G,number)
                        print "...cc=%d " % (cc)
                        print way
            else:
                print "%d FINISH !!!!!!!!!!!" % n
                return True
        else:
            print "%d FINISH ?????????" % n
            return True
    else:
        print "%d Ufffffffff" % n
    return False
        
if __name__ == '__main__':
    from sys import argv
    
    number = 20
    if len(argv) > 1:
        number = int(argv[1]) 
    # (number+1)**2 points in lattice
    # each point is a list of 2 tuples (down and right)
    # each tuple is the 'to' coordianates
    G = firstLine(number,[])  
    # lines
    for i in range(1,number):
        G = Line(i,number,G)
    # last line
    G = lastLine(number,G)  
    #printlist("GRID",G,number)
    ret = firstWay(G,number)
    RightDown(G,number,ret)
