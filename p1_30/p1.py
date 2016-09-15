Enter file contents here#!/usr/bin/env python
import os
"""
    sum of multiplies of 3 and 5 below 1000
"""
def main(limit):
    list3 = []
    list5 = []
    
    for i in range(1,limit):
        if (i%3 == 0):
            list3.append(i)
    for i in range(1,limit):
        if (i%5 == 0) and not i in list3:
            list5.append(i)
    sum = 0
    for i in range(0,len(list3)):
        sum += list3[i]
    for i in range(0,len(list5)):
        sum += list5[i]
    print "sum = %d" % (sum) 
       
if __name__ == '__main__':
    from sys import argv
    
    if len(argv) == 1:
        main(1000)
    else :
        main(int(argv[1]))
