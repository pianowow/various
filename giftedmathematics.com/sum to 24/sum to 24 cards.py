#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/01/2013

from itertools import permutations, product, combinations_with_replacement
from time import clock

limit = 10**9
oplist = ['+','-','*','/']
digits = (1,2,3,4,5,6,7,8,9,10,11,12,13)
test = 24
print('using these ops:',oplist)
print('using these digits:',digits)

##def is_rearrangement(lst1,lst2):
##    a = [x for x in lst1 if x not in lst2]
##    b = [x for x in lst2 if x not in lst1]
##    if a == b == []:
##        return True
##    else:
##        return False

##def factorial(n):
##    res = 1
##    for i in range(2, n+1):
##        res *= i
##    return res

##def gcd(a, b):
##    if a < 0:  a = -a
##    if b < 0:  b = -b
##    if a == 0: return b
##    if b == 0: return a
##    while b != 0:
##        (a, b) = (b, a % b)
##    return a


def test_expression(nums,ops,ansset):
    for opnums in permutations(nums+ops):
        if opnums[1] in digits and opnums[0] in digits:
            stack =  []
            for opnum in opnums:
                try:
                    if opnum == '+':
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num1+num2)
                    elif opnum == '-':
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num2-num1)
                    elif opnum == '*':
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num1*num2)
                    elif opnum == '/':
                        num1 = stack.pop()
                        num2 = stack.pop()
                        stack.append(num2/num1)
##                    elif opnum == 'gcd':
##                        num1 = stack.pop()
##                        num2 = stack.pop()
##                        stack.append(gcd(num1,num2))
##                    elif opnum == '!':
##                        num = stack.pop()
##                        stack.append(factorial(num))
                    else: #number
                        stack.append(opnum)
                except:
                    break

            #print (opnums, stack)
            if len(stack) == 1:
                ans = round(stack[0],5)
                if ans%1==0 and ans < limit:
                    ansset.add(ans)
##                    if ans == test:
##                        return
##                            if ans not in ansdict:
##                                ansdict[ans] = []
##                            rearrangement = False
##                            for expr in ansdict[ans]:
##                                if is_rearrangement(opnums,expr):
##                                    rearrangement = True
##                                    break
##                            if not rearrangement:
##                                ansdict[ans].append(opnums)
    return ansset

clock()
good = 0
bad = 0
totanshist = dict()
#for nums in numslist:
for nums in combinations_with_replacement(digits,4):
    #ansdict = dict()
    ansset = set()
    for ops in combinations_with_replacement(oplist,3):
        test_expression(nums,ops,ansset)
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
        if ans in totanshist:
            totanshist[ans] += 1
        else:
            totanshist[ans] = 1
    print (nums, list(ansset))

##    if 24 not in ansset:
##        print(nums,'is insoluable to',test)
##        bad += 1
##    else:
##        good += 1
##    else:
##        print(nums,'comes to', test)

anslist = list(totanshist.keys())
anslist.sort()
for ans in anslist:
    print(str(ans)+','+str(totanshist[ans]))

##print(good,'sets which get to 24')
##print(bad, 'sets which do not get to 24')

print(clock(),'seconds')