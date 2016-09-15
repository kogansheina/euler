import os
import sys

"""
Poker hands
Spades (black), Hearts (red), Diamonds (yellow),Clubs (green),
second letter H,S,C,D is the suit.
first letter is the number of the card : 2-9,T,J,Q,K,A
"""

debug = False #True
debug1 = False #True
SPADE           = 10
HEART           = SPADE-1
CLUB            = SPADE-2
DIAMOND         = SPADE-3

ROYAL_FLUSH     = 100
STRAIGHT_FLUSH  = ROYAL_FLUSH-1 # 99
FOUR_KIND       = ROYAL_FLUSH-2 # 98
FULL_HOUSE      = ROYAL_FLUSH-3 # 97
FLUSH           = ROYAL_FLUSH-4 # 96
STRAIGHT        = ROYAL_FLUSH-5 # 95
THREE_KIND      = ROYAL_FLUSH-6 # 94
TWO_PAIR        = ROYAL_FLUSH-7 # 93
ONE_PAIR        = ROYAL_FLUSH-8 # 92

def samesuit(s):
    vals = set(s)
    #print s, vals
    if len(vals) == 1:
        return (True,list(vals))  
    return (False,[])
          
def is_consecutive(s): 
    n0 = s[0]
    for n in s[1:]:
        if n != n0-1:
            return False   # not consecutive
        else:
            n0 = n
    return True
    
def splitcards(player):
    suits = []
    numbers = []
    for card in player:
        if card[1] == 'S':
            suits.append(SPADE)
        elif card[1] == 'H':
            suits.append(HEART)
        elif card[1] == 'D':
            suits.append(DIAMOND)
        else:
            suits.append(CLUB)
        if card[0]=='T':
            numbers.append(10)
        elif card[0]=='J':
            numbers.append(11)
        elif card[0]=='Q':
            numbers.append(12)
        elif card[0]=='K':
            numbers.append(13)
        elif card[0]=='A':
            numbers.append(14)
        else:
            numbers.append(ord(card[0])-ord('0'))
    return (suits,numbers)
                   
def winner(suits,numbers):
    tp = samesuit(suits)
    if tp[0]: # possible rank 10,9 or 6
        if is_consecutive(numbers):
            if 'T' in numbers: # Royal Flush
                return (ROYAL_FLUSH,tp[1])
            else:
                return (STRAIGHT_FLUSH,tp[1]) # Straight Flush
        else:
            return (FLUSH,tp[1]) # Flush
    elif is_consecutive(numbers):
        return (STRAIGHT,numbers[0]) # Straight - greatest
    else:
        tp = one_pair(numbers)
        weigth = tp[0]
        nr = tp[1]
        if 4 in weigth:
            i = weigth.index(4)
            return (FOUR_KIND,nr[i],nr[1-i])
        elif 3 in weigth: # may be full_house or 3 of a kind
            i = weigth.index(3)
            if 2 in weigth:
                return (FULL_HOUSE,nr[i],nr[1-i])
            else:
                return (THREE_KIND,nr[i])
        elif 2 in weigth:
            i = weigth.index(2)
            if 2 in weigth[i+1:]: # 2 pairs
                j = weigth[i+1:].index(2)
                return (TWO_PAIR,nr[i],nr[i+j])
            else:
                return (ONE_PAIR,nr[i])
        return (-1,numbers)
        
def one_pair(l):
    weight = []
    numbers = []
    for i in range(0,len(l)):
        if l[i] in numbers:
            continue
        countv = 1
        for j in range(0,len(l)):
            if i == j:
                continue
            if l[j] == l[i]:
                countv += 1
        numbers.append(l[i])        
        weight.append(countv)
    return (weight,numbers)
                            
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        debug = argv[1] 
    filename = "p054_poker.txt"
    #filename = "t.txt"
    win1_counter = 0
    win2_counter = 0
    try:
        fd = open(filename,'r')
        linenumber = 0
        for line in fd:
            debug1 = False
            if debug:
                debug1 = True
            if line.startswith('#'):
                continue
            player = []
            if len(line) < 30:
                continue
            linenumber += 1
            a = line.split()
            for i in range(0,5):
                player.append(a[i])
            tp = splitcards(player)
            suits1 = tp[0]
            suits1.sort(reverse=True)
            numbers1 = tp[1]
            numbers1.sort(reverse=True) 
            win1 = winner(suits1,numbers1)
            player = []
            for i in range(5,10):
                player.append(a[i])
            tp = splitcards(player)
            suits2 = tp[0]
            suits2.sort(reverse=True)
            numbers2 = tp[1]
            numbers2.sort(reverse=True) 
            win2 = winner(suits2,numbers2)
            if win1[0] > win2[0]:
                win1_counter += 1
            elif win1[0] < win2[0]:
                win2_counter += 1
            else: # same first rank; check the second one
                if win1[0]==-1:
                    # look for highest card into numbers
                    for h in range(0,len(win1)):
                        if win1[h] > win2[h]:
                            win1_counter += 1
                            break
                        elif win1[h] < win2[h]:
                            win2_counter += 1
                            break
                else:
                    if win1[1] > win2[1]:    
                        win1_counter += 1
                    elif win1[1] < win2[1]:
                        win2_counter += 1
                    else:
                       # look for highest card 
                       if win1[0] == TWO_PAIR:
                           if win1[1] > win2[1]:    
                               win1_counter += 1
                           elif win1[1] < win2[1]:
                               win2_counter += 1
                           else:
                               if win1[2] > win2[2]:    
                                   win1_counter += 1
                               elif win1[2] < win2[2]:
                                   win2_counter += 1
                               else:
                                   numbers1.remove(win1[1])
                                   numbers1.remove(win1[1])
                                   numbers1.remove(win1[2])
                                   numbers1.remove(win1[2])
                                   numbers2.remove(win1[1])
                                   numbers2.remove(win1[1])
                                   numbers2.remove(win1[2])
                                   numbers2.remove(win1[2])
                                   if numbers1[0] > numbers2[0]:
                                       win1_counter += 1
                                   else:
                                       win2_counter += 1
                       elif win1[0] == FULL_HOUSE:
                           print "FULL_HOUSE !!!!!!!!!!!!"
                       elif win1[0] == ONE_PAIR:
                           if win1[1] > win2[1]:    
                               win1_counter += 1
                           elif win1[1] < win2[1]:
                               win2_counter += 1
                           else: # see higest
                               numbers1.remove(win1[1])
                               numbers1.remove(win1[1])
                               numbers1.sort(reverse=True)
                               numbers2.remove(win1[1])
                               numbers2.remove(win1[1])
                               numbers2.sort(reverse=True)
                               if numbers1[0] > numbers2[0]:
                                   win1_counter += 1
                               elif numbers1[0] < numbers2[0]:
                                   win2_counter += 1
                               else: 
                                   if numbers1[1] > numbers2[1]:
                                       win1_counter += 1
                                   elif numbers1[1] < numbers2[1]:
                                       win2_counter += 1
                                   else: 
                                       if numbers1[2] > numbers2[2]:
                                           win1_counter += 1
                                       else:
                                           win2_counter += 1
                       else:
                           for h in range(0,len(win1)):
                               if win1[h] > win2[h]:
                                   win1_counter += 1
                                   break
                               elif win1[h] < win2[h]:
                                   win2_counter += 1
                                   break
        fd.close()
        print "final player1=%d player2=%d" % (win1_counter,win2_counter)
    except IOError:
        print 'File '+filename+' cannot be open'
