def pmax(norig):
    n = []
    p1 = p9(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p9(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p9(norig):
    n = []
    p1 = p8(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p8(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p8(norig):
    n = []
    p1 = p7(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p7(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p7(norig):
    n = []
    p1 = p6(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p6(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p6(norig):
    n = []
    p1 = p5(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p5(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p5(norig):
    n = []
    p1 = p4(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p4(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p4(norig):
    n = []
    p1 = p3(norig[1:])
    for t in p1:
        p = [norig[0]]+t
        n.append(p)
    nnext = [norig[1]]
    for p in norig:
        if p != norig[1]:
            nnext.append(p)
    for j in range(1,len(norig)):
        pnext = p3(nnext[1:])
        for t in pnext:
            p = [nnext[0]]+t
            n.append(p)
        if j < len(norig)-1:
            nnext = [norig[j+1]]
            for p in norig:
                if p != norig[j+1]:
                    nnext.append(p)
    return n

def p3(n):
    l = [n]
    temp = [n[0],n[2],n[1]]
    l.append(temp)
    temp = [n[1],n[0],n[2]]
    l.append(temp)
    temp = [n[1],n[2],n[0]]
    l.append(temp)
    temp = [n[2],n[0],n[1]]
    l.append(temp)
    temp = [n[2],n[1],n[0]]
    l.append(temp)
    return l
