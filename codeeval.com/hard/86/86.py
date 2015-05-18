#https://www.codeeval.com/open_challenges/86/

# 1 #High Card: Highest value card.
# 2 #One Pair: Two cards of the same value.
# 3 #Two Pairs: Two different pairs.
# 4 #Three of a Kind: Three cards of the same value.
# 5 #Straight: All cards are consecutive values.
# 6 #Flush: All cards of the same suit.
# 7 #Full House: Three of a kind and a pair.
# 8 #Four of a Kind: Four cards of the same value.
# 9 #Straight Flush: All cards are consecutive values of same suit.

from argparse import ArgumentParser
from itertools import combinations

parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
f = open(args.string)

def flush(suits,values):
    if len(set(suits)) == 1:
        return(6,sorted(values,reverse=True))
    else:
        return()

def straight(values):
    s = sorted(set(values), reverse=True)
    diff = s[0] - s[-1]
    if diff + 1 == len(s) and len(s) == len(values):
        return(5,s[0])
##    elif diff == 12: #we have an ace and a two
##        vals = [1 if x == 14 else x for x in values]
##        if vals != values:
##            return straight(vals)
##        else: #can happen on second iteration where ace and king have diff of 12
##            return()
    else:
        return()

def straightflush(suits,values):
    fv = flush(suits,values)
    sv = straight(values)
    if fv:
        if sv:
            return(9, sv[1])
        else:
            return(fv)
    else:
        if sv:
            return(sv)
        else:
            return()

def fullhouseorfourofakind(values):
    s = set(values)
    if len(s) == 2:
        minv = min(values)
        maxv = max(values)
        lc = values.count(minv)
        bc = values.count(maxv)
        if abs(lc-bc) == 1:
            return(7,(minv if lc>bc else maxv,minv if lc<bc else maxv))
        else:
            return(8,minv if lc>bc else maxv,minv if lc<bc else maxv)
    return()

def threeofakind(values):
    val = 0
    for x,y,z in combinations(values,3):
        if x == y and y == z:
            val = x
            break
    kickers = [x for x in values if x!=val]
    if val:
        return(4, val, kickers)
    else:
        return()

def twopair(values):
    vals = []
    for a,b,c,d in combinations(values,4):
        s = {a,b,c,d}
        if len(s) == 2:
            vals += [x for x in s]
            break
    kickers = [x for x in values if x not in vals]
    if vals:
        return(3, sorted(vals,reverse=True), kickers)
    else:
        return()

def pair(values):
    val = 0
    for x,y in combinations(values,2):
        if x == y:
            val = x
            break
    kickers = [x for x in values if x!=val]
    if val:
        return(2, val, kickers)
    else:
        return()

def highcard(values):
    kickers = sorted([x for x in values],reverse=True)
    return(1, kickers)

def intvalues(values):
    '''turns the strings for card values to numbers'''
    l = [0,0,'2','3','4','5','6','7','8','9','T','J','Q','K','A']
    vals = [l.index(x) for x in values]
    return sorted([x for x in vals],reverse=True)

def handvalue(hand):
    vals = intvalues([x[0] for x in hand])
    suits = [x[1] for x in hand]

    pv = pair(vals)
    if pv:
        thv = threeofakind(vals)
        if thv:
            fv = fullhouseorfourofakind(vals)
            if fv:
                return fv
            else:
                return thv
        else:
            twv = twopair(vals)
            if twv:
                return twv
            else:
                return pv
    else:
        sv = straightflush(suits, vals)
        if sv:
            return sv
        else:
            return highcard(vals)

def whichwins(left, right):
    lv = handvalue(left)
    rv = handvalue(right)
    if lv > rv:
        print('left')
    elif lv < rv:
        print('right')
    else:
        print('none')

for line in f:
    cards = line[:-1].split(' ')
    whichwins(cards[:5],cards[5:])

f.close()