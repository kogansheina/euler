#!/usr/bin/env python
import os
    
"""
the greatest product of 4 adjacent numbers in one direction
"""
def right(row,column):
    prod = 1
    if column > len(row)-4:
        return -1
    try:    
        for j in range(column,column+4):
            prod *= row[j]
    except IndexError:
        print "IndexError right: column=%d index=%d" % (column,j)
    return prod

def left(row,column):
    prod = 1
    if column < 3:
        return -1
    try:
        for j in range(column,column-4,-1):
            prod *= row[j]
    except IndexError:
        print "IndexError left: column=%d index=%d" % (column,j)
    return prod
    
def up(row,column,rows):
    if row < 3:
        return -1
    prod = 1
    try:
        for j in range(row,row-4,-1):
            rowl = rows[j]
            prod *= rowl[column]
    except IndexError:
        print "IndexError up: row=%d column=%d index=%d" % (row,column,j)
    return prod

def down(row,column,rows):
    if row > len(rows)-4:
        return -1
    prod = 1
    try:
        for j in range(row,row+4,1):
            rowl = rows[j]
            prod *= rowl[column]
    except IndexError:
        print "IndexError down: row=%d column=%d index=%d" % (row,column,j)
    return prod

def diagonal_right_down(row,column,rows):
    l = len(rows[row])
    if row > len(rows)-4 or column > l-4:
        return -1
    prod = 1
    try:
        for j in range(row,row+4,1):
            rowl = rows[j]
            prod *= rowl[column+j-row]
    except IndexError:
        print "IndexError diagonal_right_down: row=%d column=%d index=%d" % (row,column,j)
    return prod
    
def diagonal_left_down(row,column,rows):
    if row > len(rows)-4 or column < 3:
        return -1
    prod = 1
    try:
        for j in range(row,row+4,1):
            rowl = rows[j]
            prod *= rowl[column-j+row]
    except IndexError:
        print "IndexError diagonal_left_down: row=%d column=%d index=%d" % (row,column,j)
    return prod

def diagonal_right_up(row,column,rows):
    l = len(rows[row])
    if row < 3 or column > l-4:
        return -1
    prod = 1
    try:
        for j in range(row,row-4,-1):
            rowl = rows[j]
            prod *= rowl[column-j+row]
    except IndexError:
        print "IndexError diagonal_right_up: row=%d column=%d index=%d" % (row,column,j)
    return prod


def diagonal_left_up(row,column,rows):
    if row < 3 or column < 3:
        return -1
    prod = 1
    try:
        for j in range(row,row-4,-1):
            rowl = rows[j]
            prod *= rowl[column+j-row]
    except IndexError:
        print "IndexError diagonal_left_up: row=%d column=%d index=%d" % (row,column,j)
    return prod
if __name__ == '__main__':
    
    row1 = [8,02,22,97,38,15,00,40,00,75,04,05,07,78,52,12,50,77,91,8]
    row2 = [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,04,56,62,00]
    row3 = [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,03,49,13,36,65]
    row4 = [52,70,95,23,04,60,11,42,69,24,68,56,01,32,56,71,37,02,36,91]
    row5 = [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80]
    row6 = [24,47,32,60,99,03,45,02,44,75,33,53,78,36,84,20,35,17,12,50]
    row7 = [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70]
    row8 = [67,26,20,68,02,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21]
    row9 = [24,55,58,05,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72]
    row10 = [21,36,23,9,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95]
    row11 = [78,17,53,28,22,75,31,67,15,94,03,80,04,62,16,14,9,53,56,92]
    row12 = [16,39,05,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57]
    row13 = [86,56,00,48,35,71,89,07,05,44,44,37,44,60,21,58,51,54,17,58]
    row14 = [19,80,81,68,05,94,47,69,28,73,92,13,86,52,17,77,04,89,55,40]
    row15 = [04,52,8,83,97,35,99,16,07,97,57,32,16,26,26,79,33,27,98,66]
    row16 = [88,36,68,87,57,62,20,72,03,46,33,67,46,55,12,32,63,93,53,69]
    row17 = [04,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36]
    row18 = [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,04,36,16]
    row19 = [20,73,35,29,78,31,90,01,74,31,49,71,48,86,81,16,23,57,05,54]
    row20 = [01,70,54,71,83,51,54,69,16,92,33,48,61,43,52,01,89,19,67,48]
    myarray = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,
               row13,row14,row15,row16,row17,row18,row19,row20]

    from sys import argv
    
    if len(argv) == 1:
        maxprod = -1
        for i in range(0,len(myarray)):
            for j in range(0,len(row1)):
                pright = right(myarray[i],j)
                if maxprod < pright:
                    maxprod = pright
                pleft = left(myarray[i],j)
                if maxprod < pleft:
                    maxprod = pleft
                pdown = down(i,j,myarray)
                if maxprod < pdown:
                    maxprod = pdown
                pup = up(i,j,myarray)
                if maxprod < pup:
                    maxprod = pup
                pdlu = diagonal_left_up(i,j,myarray)
                if maxprod < pdlu:
                    maxprod = pdlu
                pdld = diagonal_left_down(i,j,myarray)
                if maxprod < pdld:
                    maxprod = pdld
                pdru = diagonal_right_up(i,j,myarray)
                if maxprod < pdru:
                    maxprod = pdru
                pdrd = diagonal_right_down(i,j,myarray)
                if maxprod < pdrd:
                    maxprod = pdrd
                #print "(%d,%d) : right=%d left=%d up=%d down=%d diagonal left up=%d "\
                #    "diagonal left down=%d diagonal right up=%d diagonal right down=%d" % (i,j,pright,pleft,pup,pdown,pdlu,pdld,pdru,pdrd)
    else:
        i = int(argv[1])
        j = int(argv[2])
        pright = right(myarray[i],j)
        maxprod = pright
        pleft = left(myarray[i],j)
        if maxprod < pleft:
            maxprod = pleft
        pdown = down(i,j,myarray)
        if maxprod < pdown:
            maxprod = pdown
        pup = up(i,j,myarray)
        if maxprod < pup:
            maxprod = pup
        pdlu = diagonal_left_up(i,j,myarray)
        if maxprod < pdlu:
            maxprod = pdlu
        pdld = diagonal_left_down(i,j,myarray)
        if maxprod < pdld:
            maxprod = pdld
        pdru = diagonal_right_up(i,j,myarray)
        if maxprod < pdru:
            maxprod = pdru
        pdrd = diagonal_right_down(i,j,myarray)
        if maxprod < pdrd:
            maxprod = pdrd
        print "(%d,%d) : right=%d left=%d up=%d down=%d diagonal left up=%d "\
            "diagonal left down=%d diagonal right up=%d diagonal right down=%d" % (i,j,pright,pleft,pup,pdown,pdlu,pdld,pdru,pdrd)
    print maxprod
