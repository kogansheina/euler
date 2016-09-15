import os
import sys


"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def gen(r,first):
    if first:
        txt = "def pmax(norig):\n    "
    else:
        txt = "def p"+str(r)+"(norig):\n    "
    txt += "n = []\n    "
    txt += "p1 = p"+str(r-1)+"(norig[1:])\n    "   
    txt += "for t in p1:\n    "
    txt += "    p = [norig[0]]+t\n    "
    txt += "    n.append(p)\n    "
    txt += "nnext = [norig[1]]\n    "
    txt += "for p in norig:\n    "
    txt += "    if p != norig[1]:\n    "
    txt += "        nnext.append(p)\n    "
    txt += "for j in range(1,len(norig)):\n    "
    txt += "    pnext = p"+str(r-1)+"(nnext[1:])\n    "
    txt += "    for t in pnext:\n    "
    txt += "        p = [nnext[0]]+t\n    "
    txt += "        n.append(p)\n    "
    txt += "    if j < len(norig)-1:\n    "
    txt += "        nnext = [norig[j+1]]\n    "
    txt += "        for p in norig:\n    "
    txt += "            if p != norig[j+1]:\n    "
    txt += "                nnext.append(p)\n    "
    txt += "return n\n\n"
    
    return txt        
       
if __name__ == '__main__':
    from sys import argv
    
    if len(argv) == 1:
        nlen = 10
    else :
        nlen=int(argv[1])
    n = [] 
    norig = [0]
    for i in range(1,nlen):
        norig.append(i)
        
    if nlen >= 4:
        try:
            if os.path.exists("p24s.py"):
                os.remove("p24s.py")
            fd = open("p24s.py",'w')
            cb = gen(nlen,True)
            fd.write(cb)
            nlen -= 1
            while nlen > 3:
                cb = gen(nlen,False)
                fd.write(cb)
                nlen -= 1
            fd.write("def p3(n):\n")
            fd.write("    l = [n]\n")
            fd.write("    temp = [n[0],n[2],n[1]]\n")
            fd.write("    l.append(temp)\n")
            fd.write("    temp = [n[1],n[0],n[2]]\n")
            fd.write("    l.append(temp)\n")
            fd.write("    temp = [n[1],n[2],n[0]]\n")
            fd.write("    l.append(temp)\n")
            fd.write("    temp = [n[2],n[0],n[1]]\n")
            fd.write("    l.append(temp)\n")
            fd.write("    temp = [n[2],n[1],n[0]]\n")
            fd.write("    l.append(temp)\n")
            fd.write("    return l\n")  
            fd.close()
            import p24s
            n = p24s.pmax(norig)

        except IOError:
            print 'File p24s.py cannot be open'
    
    else:
        n = [norig]
        temp = [norig[0],norig[2],norig[1]]
        n.append(temp)
        temp = [norig[1],norig[0],norig[2]]
        n.append(temp)
        temp = [norig[1],norig[2],norig[0]]
        n.append(temp)
        temp = [norig[2],norig[0],norig[1]]
        n.append(temp)
        temp = [norig[2],norig[1],norig[0]]
        n.append(temp)
    
    #print len(n) 
    if len(n) >= 1000000:
        print n[999999]       
    #for p in n:
    #    print p
