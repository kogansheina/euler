#!/usr/bin/env python
import os
import sys
import copy
# number of lattice paths from (0,0) to (N,N) N=20 - default
class point:
    def __init__(self,r,c,maxr,maxc):
        self.r = r # row
        self.c = c # column
        self.maxr = maxr
        self.maxc = maxc
        self.entries = [] # max 2 elements (first left side)
        self.outputs = [] # max 4 elements
        
    def addEntry(self):
        if self.r == 0 and self.c == 0:
            return
        if self.r == 0:
            entry = (self.r,self.c-1)
            self.entries.append(entry)
        elif self.c == 0:
            entry = (self.r-1,self.c)
            self.entries.append(entry)
        else:
            entry = (self.r-1,self.c)
            self.entries.append(entry)
            entry = (self.r,self.c-1)
            self.entries.append(entry)
        
    def addOutput(self):
        if self.r == self.maxr-1 and self.c == self.maxc-1:
            return
        if self.r == self.maxr-1:
            entry = (self.r,self.c+1)
            self.outputs.append(entry)
        elif self.c == self.maxc-1:
            entry = (self.r+1,self.c)
            self.outputs.append(entry)
        else:
            entry = (self.r,self.c+1)
            self.outputs.append(entry)
            entry = (self.r+1,self.c)
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
        
def build(temporary,tracks):
    
    start = copy.deepcopy(tracks)
    for tr in start:
        # look for those tracks which their last tuple is an entry to crt
        temp = buildTrack(tr,temporary)
        if temp == None:
            return (temp,tracks)
        tracks.remove(tr)
        tracks = tracks + temp
    return (temp,tracks)
        
def buildTrack(tr,temporary):
    crt = temporary[tr[len(tr)-1]]
    #crt.printPoint()
    if len(crt.outputs) == 0:
        return None
    last = (0,0)
    tcopy = []
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
    from sys import argv
    
    number = 20
    if len(argv) > 1:
        number = int(argv[1]) 
    temporary = {}
    maxrows = number+1
    for r in range(0,maxrows):
        maxcol = maxrows
        for c in range(0,maxcol):
            np = point(r,c,maxrows,maxcol)
            np.addEntry()
            np.addOutput()
            temporary[(r,c)] = np
            #np.printPoint()
    print "table Done"
    tracks = []
    Counter = 1 
    # look for those tracks which their last tuple is an entry to crt
    crt = temporary[(0,0)]
    for o in crt.outputs:
        ty = [(0,0)]
        tracks.append(ty)
        ty.append(o)
    while True:   
        Counter += 1
        tp = build(temporary,tracks)
        tracks = tp[1]
        if tp[0] == None:
            break
        elif Counter % 5 == 0:
            print "Counter %d Len %d" % (Counter,len(tracks))
            #printTracks()
    print "Final Counter %d Len %d" % (Counter,len(tracks))
        
