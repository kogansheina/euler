import os
import sys
import genprimes

"""
Digit cancelling fractions
restrictions.
1. the numerator and denominator will have 2 digits
2. they are not mod 10
3. numberator < denominator (fraction < 1)

numerator / denominator
"""
           
if __name__ == '__main__':
    result = []
    for a in range (10,100):
        for b in range(a+1,100):
            if a%10 == 0 and b%10 == 0:
                continue
            stra = str(a)
            strb = str(b)
            newa = newb = 0
            if stra[0] == strb[0]:
                newa = int(stra[1])
                newb = int(strb[1])
            elif stra[0] == strb[1]:
                newa = int(stra[1])
                newb = int(strb[0])
            elif stra[1] == strb[0]:
                newa = int(stra[0])
                newb = int(strb[1])
            elif stra[1] == strb[1]:
                newa = int(stra[0])
                newb = int(strb[0])
            else:
                continue
            if newa != 0 and newb != 0:
                try:
                    y = float(newa)/float(newb)
                    x = float(a)/float(b)
                    if y == x:
                        print "a=%d b=%d newa=%d newb=%d %f == %f" % (a,b,newa,newb,y,x)
                        result.append((a,b))
                except ZeroDivisionError:
                    print "Error a=%d b=%d newa=%d newb=%d" % (a,b,newa,newb)
    factd = 1        
    for r in result: 
        factd *= r[1]
    factn = 1        
    for r in result: 
        factn *= r[0]
    print "factn=%d factd=%d" % (factn,factd)
    prime = genprimes.genPrimes(100)
    tpn = genprimes.foundDividers(factn,prime)
    tpd = genprimes.foundDividers(factd,prime)
    nfact = tpn[0]
    npow = tpn[1]
    dfact = tpd[0]
    dpow = tpd[1]
    print "N"
    print nfact
    print npow
    print "D"
    print dfact
    print dpow
    for c in range(0,len(nfact)):
        if nfact[c] in dfact:
            ind = dfact.index(nfact[c])
            if dpow[ind] <= npow[c]:
                del dfact[ind]
                del dpow[ind]
            else:
                dpow[ind] -= npow[c]
    s = 1
    print "D"
    print dfact
    print dpow
    for c in range(0,len(dfact)):
        s *= dfact[c]**dpow[c]
    print s
            
      
        
