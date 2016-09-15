import os
import sys

"""
Digit fifth powers
any number of 1 digit is not a sum, therefore it is not considered
the maximum number on power of 5, pow(9,5) has 5 digits = 59,049
the sum will have , at least 5 digits, therefore the maximum number will be 59,049 * 5 = 295,245
"""
if __name__ == '__main__':
    mylist = []
    number = 5 #4 
    maxnumber = number*pow(9,number)
    for i in range(10,maxnumber):
        stri = str(i)
        sum = 0
        for j in stri:
            sum += pow(int(j),number)
        if sum == i:
            mylist.append(i)
    s = mylist[0]
    for i in mylist[1:]:
        s += i
    print mylist
    print s
            
    
                    
        
            
        
        
