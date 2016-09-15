import os
import sys

"""
Pandigital multiples
the largest 9 digit number is : 987654321; 
it must be the concatenated product of N and (1,2,..n)
N will begin with 9, or 98, ...
"""
def check(ss):
    if len(ss) != 9:
        return False
    s = list(ss)
    if '1' not in s:
        return False
    s.remove('1')
    if '2' not in s:
        return False
    s.remove('2')
    if '3' not in s:
        return False
    s.remove('3')
    if '4' not in s:
        return False
    s.remove('4')
    if '5' not in s:
        return False
    s.remove('5')
    if '6' not in s:
        return False
    s.remove('6')
    if '7' not in s:
        return False
    s.remove('7')
    if '8' not in s:
        return False
    s.remove('8')
    if s != ['9']:
        return False
    return True
    
if __name__ == '__main__':
    
    MAX = 999999999
    maxn = 1
    for number in range(2,9330): # MAX+1
        tmp = str(number)
        n = 2
        no = number*n
        if no > MAX:
            break
        tmp += str(no)
        while no <= MAX and '0' not in tmp and len(tmp) < 9:
            n += 1
            no = number*n
            tmp += str(no)
        if check(tmp):
            print "Pandigital %s for %d: " % (tmp,number)
            if int(tmp) > maxn:
                maxn = int(tmp)
            
    print maxn            
      
        
