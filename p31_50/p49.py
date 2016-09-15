import os
import sys
import genprimes

prime = []
"""
Prime permutations
"""
def pertmp(tmp,number,i1,i2,i3):
    tmp+=number[i1]
    tmp+=number[i2]
    tmp+=number[i3]
    return ins(tmp)
    
    """
    input string  - output number
    """
def ins(tmp):
    tmpn = int(tmp)
    if tmpn/1000 > 0:
        if tmpn in prime:
            return tmpn
    return None
    
def good(tmpn):
    if tmpn != None:
        if isinstance(tmpn, int):
            return True 
        else:
            print "error type"
            print type(tmpn)
            print tmpn
    return False
            
def per(number,p,i0,i1,i2,i3):
    tmp = number[i0]
    tmpn = pertmp(tmp,number,i1,i2,i3)
    if good(tmpn): 
        p.add(tmpn) 
    return p
                
    """
    input string  - insert number
    """
def permut(number):
    p = set()
    nr = int(number)
    p.add(nr)  # 1
    tmp = number[:2]
    tmp+=number[3]
    tmp+=number[2]
    tmpn = ins(tmp)
    if good(tmpn):
        p.add(tmpn) # 2
    p = per(number,p,0,2,1,3) #3    
    p = per(number,p,0,2,3,1) #4    
    p = per(number,p,0,3,2,1) #5    
    p = per(number,p,0,3,1,2) #6    
    p = per(number,p,1,0,3,2) #7    
    p = per(number,p,1,0,2,3) #8    
    p = per(number,p,1,3,0,2) #9    
    p = per(number,p,1,3,2,0) #10    
    p = per(number,p,1,2,0,3) #11    
    p = per(number,p,1,2,3,0) #12    
    p = per(number,p,2,0,1,3) #13    
    p = per(number,p,2,0,3,1) #14    
    p = per(number,p,2,1,0,3) #15    
    p = per(number,p,2,1,3,0) #16    
    p = per(number,p,2,3,0,1) #17    
    p = per(number,p,2,3,1,0) #18  
    p = per(number,p,3,0,1,2) #19  
    p = per(number,p,3,0,2,1) #20  
    p = per(number,p,3,1,0,2) #21  
    p = per(number,p,3,1,2,0) #22  
    p = per(number,p,3,2,0,1) #23  
    p = per(number,p,3,2,1,0) #24  
                                
    return sorted(p)
            
if __name__ == '__main__':
    
    from sys import argv
    
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genprimes.genPrimes(number+1)
    flag = False
    for n in prime:
        if n < 1487:
            continue
        strn = str(n)
        lenn = len(strn)
        if lenn > 4:
            print "increase primes"
            break
        elif lenn < 4:
            continue
        posibilities = permut(strn)
        #print posibilities
        if len(posibilities) < 3:
            continue
        for p in range(0,len(posibilities)-2):
            try:
                #print "%d : %d %d %d" % (n,posibilities[p],posibilities[p+1],posibilities[p+2])
                if posibilities[p+1]-posibilities[p] == posibilities[p+2]-posibilities[p+1]:
                    print "for %d : %d %d %d" % (n,posibilities[p],posibilities[p+1],posibilities[p+2])
                    if not flag:
                        flag = True
                    else:
                        sys.exit(0)
            except TypeError:
                print "error:" 
                print n
                print posibilities[p]
                print posibilities[p+1]
                print posibilities[p+2]
                                 
    
