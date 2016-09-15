#!/usr/bin/env python
import os
import sys
""""
XOR decryption
"""

# Top 20 common english words (lowercased) 
COMMON_ENGLISH_WORDS = [ 
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 
    'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at']
 
def is_ascii(c):
    if c == 127 or (c >= 0 and c <= 31):
        return False
    return True
    
def main():
    lowletters = []
    for i in range(0,26):
        lowletters.append(ord('a')+i)
    try:
        filename = "p059_cipher.txt"
        #filename = "y.txt"
        fd = open(filename,'r')
        linelist = fd.read().split(",")
        fd.close()
        llen = len(linelist)    
        bestkey = (lowletters[0],lowletters[0],lowletters[0]) 
        bestkeycounter = 0 
        for a in lowletters:
            for b in lowletters:
                for c in lowletters: 
                    result = []
                    stop = False
                    for l in range(0,llen):
                        if l==0 or l%3==0:
                            key=a
                        elif l%3==1:
                            key=b 
                        else:
                            key=c
                        e = int(linelist[l])
                        res = e^key
                        if is_ascii(res):
                            result.append(res) 
                        else:
                            stop = True
                            break
                    if not stop:
                        buff = chr(result[0])
                        if len(result)>1:
                            try:
                                for cc in result[1:]:
                                    buff += chr(cc)
                            except IndexError:
                                print "index error %d" % cc
                                print result
                        bf = buff.split()
                        counter = 0
                        for w in bf:
                            if w in COMMON_ENGLISH_WORDS:
                                counter += 1
                        if counter > bestkeycounter:
                            bestkeycounter = counter
                            bestkey = (a,b,c)
        print "best key", bestkey 
        result = []
        for l in range(0,llen):
            if l==0 or l%3==0:
                key=bestkey[0]
            elif l%3==1:
                key=bestkey[1] 
            else:
                key=bestkey[2]
            e = int(linelist[l])
            res = e^key
            result.append(res)
        sum = result[0] 
        buff = chr(result[0])
        if len(result)>1:
            try:
                for cc in result[1:]:
                    buff += chr(cc)
                    sum += cc
            except IndexError:
                print "index error %d" % cc
                print result
        print buff
        print "......... "+str(sum)
    except IOError:
        print 'File p059_cipher.txt cannot be open'
        
if __name__ == "__main__":
    main()


