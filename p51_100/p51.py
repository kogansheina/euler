import os
import sys
import genprimes

prime = []
"""
Prime digit replacements

from problem analyse (Internet !!!) the numbers will 6-digit long and the group to be replaced
will be 3-digit long
"""
                  
def is_prime(n):
    if n == 1:
        return False
    elif n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def number_to_list(number):
    strn = str(number)
    return list(strn)
        
def list_to_number(l):
    strn = ''.join(l)
    return int(strn)
    
if __name__ == '__main__':
    
    from sys import argv
    
    R = ['0','1','2','3','4','5','6','7','8','9']
    result = []
    firstindex = 0
    #the greatest 6-digit number is 999999
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genprimes.genPrimes(number)
    for first in range(0,len(prime)):
        if prime[first] >= 100000:
            firstindex = first
            break
    doit = True
    for i in prime[firstindex:]:
        if not doit:
            break
        result = [i]
        #choose digit to be the replacement
        for replacement in R:
            if not doit:
                break
            newstr = number_to_list(i)
            #choose the first index to be replaced - leading 0 are not considered
            if replacement == '0':
                ind1 = 1
            else:
                ind1 = 0
            while ind1 < 4 and newstr[ind1] != replacement:
                if not doit:
                    break
                #choose the first index to be replaced
                ind2 = ind1+1
                while ind2 < 5 and newstr[ind2] != replacement:
                    if not doit:
                        break
                    #choose the first index to be replaced
                    ind3 = ind2+1
                    while ind3 < 6 and newstr[ind3] != replacement:
                        if not doit:
                            break
                        #print "replace=%s ind1=%d ind2=%d ind3=%d" % (replacement,ind1,ind2,ind3) 
                        try:
                            newstr[ind1]=replacement
                            newstr[ind2]=replacement
                            newstr[ind3]=replacement
                            newnumber = list_to_number(newstr)
                            if is_prime(newnumber):
                                result.append(newnumber)
                                print "Result: n=%s ind1=%d ind2=%d ind3=%d" % (replacement,ind1,ind2,ind3) 
                                print result
                                if len(result) == 8:
                                    doit = False
                                    break
                        except IndexError:
                            print "error: n=%s ind1=%d ind2=%d ind3=%d" % (newstr,ind1,ind2,ind3) 
                        ind3 += 1  
                    ind2 += 1 
                    #print "increment ind2" 
                ind1 += 1  
                #print "increment ind1" 
    print  result        
    
                                 
    
