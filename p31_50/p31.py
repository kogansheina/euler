import os
import sys

"""
Coin sums
1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p

2p : 1+1, 2*1 ==> 2
5p : 2p*2 + 1 ==> 3
10p : 5p*2 => 9
20p : 10p*2 => 81

"""
coins = [1,2,5,10,20,50,100,200]
def a(i,n):
    s = i
    t = [i]
    while s < n:
        s += i
        if s <= n:
            t.append(i)
    if s == n:
        return t 
    return None  
     
def b(basic,number,group):
    t = []
    if len(basic) >= group:
        c = 0
        j = 0
        g = group
        while group > 0:
            c += basic[j]
            j += 1
            group -= 1
        if c <= number and c in coins:
             t.append(c)
             t += basic[g:]
             t.sort()
    return t
    
def d(basic,grouplist):
         
    tmp = []
    for y in basic:
        if y not in grouplist:
            tmp.append(y) 
    return tmp
              
def c(basic,grouplist,g):
    t = []
    tmp = d(basic,grouplist)
    for gg in range(1,g):
        while tmp != []:
            tmp = b(tmp,number,coins[gg])
            if tmp != []:
                t.append(tmp+grouplist)
        tmp = d(basic,grouplist)
        
    return t 
    
def e(lim1,number,basic,bcoins):
    for g in range(1,lim1):
        group = coins[g]
        if group >= number:
            break
        while basic != []:
            basic = b(basic,number,group)
            if basic not in bcoins and basic != []:
                bcoins.append(basic)
                if g > 1:
                    bcoins += c(basic,[group],g)
        basic = bcoins[0] 
    return bcoins
       
if __name__ == '__main__':
    
    from sys import argv
    
    number = 200
    if len(argv) == 2:
        number = int(argv[1]) 
    bcoins = []
    basic = a(coins[0],number)
    if basic != None:
        bcoins.append(basic)
    bcoins = e(len(coins)-1,number,basic,bcoins)    
               
    if  number in coins and [number] not in bcoins:
        bcoins.append([number])
        
    print "final"
    print len(bcoins)
    for t in bcoins:
        print len(t)
        print t
                            
        
            
        
        
