import os
import sys

"""
Names scores

alphabetical value of a character = ord(char)
letter position into alphabet

"""
def char_position(letter):
    return ord(letter.lower()) - ord('a') + 1

if __name__ == '__main__':
    from sys import argv
    
    names = []
    try:
        fd = open("names.txt",'r')
        for line in fd:
            a = [x.strip() for x in line.split('","')]
            names = names + a
        names[0] = names[0][1:] 
        a = names[len(names)-1]       
        names[len(names)-1] = a[1:len(a)-1] 
        names.sort()       
    except IOError:
        print 'File names.txt cannot be open'
    score = 0
    for n in range(0,len(names)):
        s = 0
        name = names[n]
        for letter in name:
            s += char_position(letter) 
        score += s*(n+1)
    print score   
    
        
        
        
