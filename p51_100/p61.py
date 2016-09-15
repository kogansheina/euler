#!/usr/bin/env python
import os
import sys

""""
Cyclical figurate numbers
"""
def calc_p3(n):
    return n*(n+1)/2
def calc_p4(n):
    return n*n
def calc_p5(n):
    return n*(3*n-1)/2
def calc_p6(n):
    return n*(2*n-1)
def calc_p7(n):
    return n*(5*n-3)/2
def calc_p8(n):
    return n*(3*n-2)
    
def build_entry(limit,typ,mydict):
    for t in range(limit[0],limit[1]+1):
        cb = "calc_p"+str(typ)
        p = cb(t)
        if len(str(p)) < 4:
            continue
        elif len(str(p)) > 4:
            break
        else:
            try:
                mylist = mydict[(typ,p)]
            except KeyError:
                mydict[(typ,p)] = []
                
    return mydict
              
if __name__ == "__main__":
    # calculates the limits for each formula to give a 4-digit number
    p3 = (10,200) 
    p4 = (10,100)
    p5 = (10,100) 
    p6 = (10,100) 
    p7 = (10,100)
    p8 = (10,100)
   
    l8 = []
    for t in range(p8[0],p8[1]):
        p = str(calc_p8(t))
        if len(p) < 4:
            continue
        elif len(p) > 4:
            break
        else:
            l8.append(p)
    last = {} 
    for p in l8:
        gr = p[-2:] # this must be the beginning of p3 numbers
        for t in range(p3[0],p3[1]+1):
            r = calc_p3(t)
            strr = str(r)
            if len(strr) < 4:
                continue
            elif len(strr) > 4:
                break
            elif strr.startswith(gr): 
                last[p] = {r:{}}
    for el in last: # el is a dict, key = legal p6
        entry1 = last[el]
        print entry1
        for el3 in entry1: # el3 is a key
            gr = str(el3)[-2:] # this must be the beginning of the next
            for t in range(p4[0],p4[1]+1):
                r = calc_p4(t)
                strr = str(r)
                if len(strr) < 4:
                    continue
                elif len(strr) > 4:
                    break
                elif strr.startswith(gr): 
                    entry1[p] = {r:{}}
    for k in last.keys():
        print k,last[k]
    # l3 contains all 4-digit numbers which begins with the last 2 digits of p8
                 
