import os
import sys

"""
Distinct powers
"""
if __name__ == '__main__':
    from sys import argv
    
    debug = False
    if len(argv) == 1:
        number = 100
    else:
        number = int(argv[1])
        if len(argv) > 2:
            debug = True
    final = []
    for a in range(2,number+1): 
        for b in range(2,number+1):
            t = pow(a,b)
            if t not in final:
                final.append(t)
    print len(final)       
                    
        
            
        
        
