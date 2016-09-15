import os
import sys

"""
Double-base palindromes
"""
def digit_to_char(digit):
    if digit < 10: 
        return chr(ord('0') + digit)
    else: 
        return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
        if d:
            return str_base(d,base) + digit_to_char(m)
        else:
            return digit_to_char(m)
            
def check(s):
    if s[-1] == '0':
        return False
    for i in range(0,len(s)/2): 
        if s[i] != s[len(s)-1-i]:
            return False
    return True
                        
if __name__ == '__main__':
    from sys import argv
    
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    counter = 0
    palindromes = []
    for i in range(1,number+1):
        str10 = str_base(i,10)
        if check(str10):
            str2 = str_base(i,2)
            if check(str2):
                #palindromes.append((str10,str2))
                counter += i
    print counter
    #for p in palindromes:
    #    print p
            
      
        
