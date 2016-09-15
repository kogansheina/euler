#!/usr/bin/env python
import os
import sys
import copy
# maximum sum of the digits in the path from the top to the right low corner

#top  = [3]
#row1 = [7,4]
#row2 = [2,4,6]
#row3 = [8,5,9,3]
#triangle = [top,row1,row2,row3] ==> 23
top  = [75]
row1 = [95,64]
row2 = [17,47,82]
row3 = [18,35,87,10]
row4 = [20,04,82,47,65]
row5 = [19,01,23,75,03,34]
row6 = [88,02,77,73,07,63,67]
row7 = [99,65,04,28,06,16,70,92]
row8 = [41,41,26,56,83,40,80,70,33]
row9 = [41,48,72,33,47,32,37,16,94,29]
row10 = [53,71,44,65,25,43,91,52,97,51,14]
row11 = [70,11,33,28,77,73,17,78,39,68,17,57]
row12 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
row13 = [63,66,04,68,89,53,67,30,73,16,69,87,40,31]
row14 = [04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]

triangle = [top,row1,row2,row3,row4,row5,row6,row7,row8,row9,
            row10,row11,row12,row13,row14]

class point:
    def __init__(self,r,c,maxr,maxc):
        self.r = r # row
        self.c = c # column
        self.maxr = maxr
        self.maxc = maxc
        self.entries = [] # max 2 elements (first left side)
        self.outputs = [] # max 4 elements
        
    def addEntry(self):
        if self.r == 0:
            return
        if self.c == 0:
            entry = (self.r-1,self.c)
            self.entries.append(entry)
        elif self.c == self.maxc-1:
            entry = (self.r-1,self.c-1)
            self.entries.append(entry)
        else:
            entry = (self.r-1,self.c-1)
            self.entries.append(entry)
            entry = (self.r-1,self.c)
            self.entries.append(entry)
        
    def addOutput(self):
        if self.r == self.maxr-1:
            return
        entry = (self.r+1,self.c)
        self.outputs.append(entry)
        entry = (self.r+1,self.c+1)
        self.outputs.append(entry)
        
    def printPoint(self):
        print "row=%d column=%d" % (self.r,self.c)  
        print "entries : %d" % len(self.entries)
        for i in self.entries:
            print i
        print "outputs : %d" % len(self.outputs)
        for i in self.outputs:
            print i       
    
def printTracks():
    for t in tracks:
        print t
        
def build(temporary,maxtracks,Counter,tracks):
    
    start = copy.deepcopy(tracks)
    for tr in start:
        # look for those tracks which their last tuple is an entry to crt
        Counter += 1
        if Counter >= maxtracks:
            return (Counter,tracks)
        
        temp = buildTrack(tr,temporary)
        tracks.remove(tr)
        tracks = tracks + temp
    return (Counter,tracks)
        
def buildTrack(tr,temporary):
    last = (0,0)
    tcopy = []
    crt = temporary[tr[len(tr)-1]]
    for e in crt.entries:
        # this will be the beginning of new tracks
        for o in crt.outputs:
            last = o
            ty = copy.deepcopy(tr)
            ty.append(o)
            if ty not in tcopy:
                tcopy.append(ty)
    return tcopy
            
if __name__ == '__main__':
    temporary = {}
    maxrows = len(triangle)
    for r in range(0,maxrows):
        maxcol = len(triangle[r])
        for c in range(0,maxcol):
            np = point(r,c,maxrows,maxcol)
            np.addEntry()
            np.addOutput()
            temporary[(r,c)] = np
    maxtracks = 2**(maxrows-1)     
    tracks = []
    Counter = 1 
    # look for those tracks which their last tuple is an entry to crt
    crt = temporary[(0,0)]
    for o in crt.outputs:
        ty = [(0,0)]
        tracks.append(ty)
        ty.append(o)
    while Counter < maxtracks:   
        tp = build(temporary,maxtracks,Counter,tracks)
        Counter = tp[0]
        tracks = tp[1]
    #printTracks()
    maxsum = 0
    for t in tracks: # t is a list of tuples
        sum = 0
        for p in t:  # p is a tuple = coordinates in triangle
            sum += triangle[p[0]][p[1]]
        if maxsum < sum:
            maxsum = sum
    print maxsum
        
