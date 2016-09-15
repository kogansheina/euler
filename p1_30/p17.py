#!/usr/bin/env python
import os
# number letter counts
# write numbers by words and count the letters 1 - 1000 (inclusive)
s99 = 0
digit1_9 = ['one','two','three','four','five','six','seven','eight','nine']

def upto99():
    digit10_19 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    digit_tens = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    sum = 0
    for i in digit1_9:
        sum += len(i) # 1-9
    s1_9 = sum
    for i in digit10_19:
        sum += len(i) # 10-19
    for j in digit_tens:
        s=0
        l=len(j)
        sum += l*10 + s1_9
    return sum
    
def cent(c):
    res = len(c+'hundred')
    l = len(c+'hundredand')
    res += l*99+s99
    return res
        
if __name__ == '__main__':
    s99 = upto99()
    print "s99="+str(s99)
    res = 0 
    for i in digit1_9:
        res += cent(i)
    sum = s99 + res + len('onethousand')
    print "sum=%d" % sum
        
