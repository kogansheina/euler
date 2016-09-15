import os
import sys
import math

"""
Coded triangle numbers
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding 
these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number 
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?
"""
def detect_tn(n):
    a = 1+8*n
    delta = math.sqrt(a)
    t = (-1+delta)/2
    if int(t) == t:
        return int(t)
    return 0
    
def position(c):
    return ord(c)-ord('A')+1 
              
def calc_word(w):
    s = 0
    for c in w: 
        s += position(c)
    return s
                     
if __name__ == '__main__':
    
    names = []
    try:
        fd = open("words.txt",'r')
        for line in fd:
            a = [x.strip() for x in line.split('","')]
            names = names + a
        names[0] = names[0][1:] 
        a = names[len(names)-1]       
        names[len(names)-1] = a[1:len(a)-1] 
        #names.sort()
        counter = 0
        for w in names:
            v = calc_word(w)
            if detect_tn(v) > 0:
                counter += 1
        print counter
    except IOError:
        print 'File words.txt cannot be open'
        
      
        
