#!/usr/bin/env python
""""
Square root convergents
"""
def nextiter(I):
    n = I[0]
    d = I[1]
    return (d,2*d+n)
    
def main():
    from sys import argv
    inter = 1000
    if len(argv) == 2:
        inter = int(argv[1]) 
    sum = 0
    it = (1,2)
    inter -= 1
    while inter > 0:
        it = nextiter(it) # 1/(2+n/d)
        inter -= 1
        result = (it[0]+it[1],it[1])
        N = str(result[0])
        D = str(result[1])
        if len(N)>len(D):
            sum += 1
            print "%d %d" % (len(N),len(D))
    print sum
if __name__ == "__main__":
    main()


