#!/usr/bin/env python

""""
Lychrel numbers
"""
def is_palindromic(n):
    strn = str(n)
    strr = strn[::-1]
    if strn == strr:
        return True
    return False
    
def reverse(n):
    strn = str(n)
    strr = strn[::-1]
    return int(strr)
        
def main():
    n = 1
    N = 10000
    while n <= 10000:
        iterations = 1
        nn = n+reverse(n)
        if is_palindromic(nn):
            N -= 1
            print "nn=%d n=%d interations=%d" % (nn, n,iterations)
            n += 1
            continue
        while iterations < 50:
            nn = nn+reverse(nn)
            if is_palindromic(nn):
                N -= 1
                print "nn=%d n=%d interations=%d" % (nn, n,iterations)
                break
            iterations += 1
        n += 1
    print N
           
if __name__ == "__main__":
    from sys import argv
    
    main()


