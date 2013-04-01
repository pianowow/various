#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/01/2013

from itertools import permutations, combinations_with_replacement, count
from time import clock

##Sum to 24
##
##a) 4 5 6 7
##
##b) 5 5 5 5
##
##c) 3 3 8 8
limit = 10**9
oplist = ['+','-','/','*']
digits = (1,2)
digitcount = 6

clock()
totansset = set()
#for nums in numslist:
for nums in combinations_with_replacement(digits,digitcount):
    ansset = set()
    for ops in combinations_with_replacement(oplist,digitcount-1):
        for opnums in permutations(ops+nums):
            if opnums[1] in digits and opnums[0] in digits:
                stack = []
                for opnum in opnums:
                    try:
                        if opnum == '+':
                            sm = stack.pop() + stack.pop()
                            stack.append(sm)
                        elif opnum == '-':
                            num2 = stack.pop()
                            num1 = stack.pop()
                            stack.append(num1-num2)
                        elif opnum == '*':
                            prd = stack.pop() * stack.pop()
                            stack.append(prd)
                        elif opnum == '/':
                            num2 = stack.pop()
                            num1 = stack.pop()
                            stack.append(num1/num2)
##                        elif opnum == '%':
##                            num1 = stack.pop()
##                            num2 = stack.pop()
##                            stack.append(num2%num1)
##                        elif opnum == '^':
##                            num1 = stack.pop()
##                            num2 = stack.pop()
##                            if num1 > 30 or num2 > limit:  #2**30 > limit
##                                break
##                            stack.append(num2**num1)
##                        elif opnum == 'r':
##                            num1 = stack.pop()
##                            num2 = stack.pop()
##                            stack.append(num2**(1/num1))
                        else: #number
                            stack.append(opnum)
                    except:
                        break
                else:
                    #print (opnums, stack)
                    if len(stack) == 1:
                        try:
                            ans = round(stack[0],1)
                        except:
                            pass #complex solution, i.e., multiple of i, (-1)**(1/2)
                        else:
                            if 0 < ans < limit and ans%1 == 0:
                                ansset.add(ans)


##    uniques = [x for x in ansdict if len(ansdict[x])==1]
##    if 24 in uniques:
##        print (nums,'has unique solution',ansdict[24])
##    elif 24 in ansdict:
##        print (nums,'has many solutions',ansdict[24])
##    else:
##        sollst = []
##        anslst = []
##        mindiff = 100
##        for ans in ansdict.keys():
##            diff = abs(24-ans)
##            if diff < mindiff:
##                anslst = [ans]
##                sollst = ansdict[ans]
##                mindiff = diff
##            elif diff == mindiff:
##                anslst += [ans]
##                sollst += ansdict[ans]
##        print (nums,'has no solutions, closest:',anslst,sollst)
    for ans in ansset:
        totansset.add(ans)
    print (nums, ansset,clock(),'secs')

for x in count(1):
    if x not in totansset:
        print(x,'cannot be made.')
        break

print(clock(),'seconds')