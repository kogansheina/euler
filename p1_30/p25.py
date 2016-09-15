import os
import sys


"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
def fibonacci(n):
    nlen = len(n)-2
    if nlen < 0:
        return None
    n.append(n[nlen]+n[nlen+1])
    
    return n
    
if __name__ == '__main__':
    n = [1,1]
    ind = 2
    while len(str(n[-1])) <= 1000:
        # uses only the last 2 numbers to calculate the next
            n = fibonacci(n[-2:])
            ind += 1
            #print n
            #print ind
            #print "%d %d %d" % (len(str(n[-2])),len(str(n[-1])),len(str(n[0])))
    if len(str(n[-2])) == 1000 and len(str(n[-1])) > 1000:
        print "final=%d" % (ind)
    else:
        print "ind=%d len of nlen=%d len of prev=%d" % (ind,len(str(n[-1])),len(str(n[-2])))
        
        
