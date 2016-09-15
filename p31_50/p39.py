import os
import sys

"""
Integer right triangles
"""
if __name__ == '__main__':
    
    number = 1000 
    sol = (0,3)     
    for p in range(3,number+1): # MAX+1
        solutions = []
        for a in range(1,p):
            for b in range (1,p):
                c = p-a-b
                if c**2 == a**2+b**2:
                    solutions.append((a,b,c,p))
        if sol[0] < len(solutions):
            print "solution for %d: " % (p)
            print solutions
            sol =(len(solutions),p)
            
    print sol            
      
        
