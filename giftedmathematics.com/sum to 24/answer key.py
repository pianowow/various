
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/01/2013

from itertools import permutations, combinations_with_replacement

goal = 24
oplist = ['+','-','*','/']
digits = (1,2,3,4,5,6,7,8,9)
digitcount = 4

def is_rearrangement(lst1,lst2): #to determine if one expression is equivalent to another
    a = [x for x in lst1 if x not in lst2] #lst1-lst2
    b = [x for x in lst2 if x not in lst1] #lst2-lst1
    if a == b == []:
        return True
    else:
        return False

def test_expression(nums,ops,ansdict):  #put all solutions with these numbers and operators in the ansdict
    for opnums in permutations(nums+ops): #combine numbers and operators every way possible
        if opnums[1] in digits and opnums[0] in digits: #you need two digits to start
            stack = [] #holds intermediate values as the evaluation progressions from start to finish
            for opnum in opnums: #many of these opnums will be invalid expressions, hence the try/catch
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
                    else: #number
                        stack.append(opnum)
                except:
                    break #exit this for loop and go to the next opnums
            if len(stack) == 1:
                ans = round(stack[0],5)  #needed because sometimes the computer confuses 5 with 4.999999...
                if ans not in ansdict:
                    ansdict[ans] = []
                rearrangement = False
                for expr in ansdict[ans]: #check all already-found solutions against this one
                    if is_rearrangement(opnums,expr):
                        rearrangement = True
                        break #no need to continue checking if one rearrangement is found
                if not rearrangement:
                    ansdict[ans].append(opnums) #save found solution if not a rearrangement of previous found solutions

#Program starts here
for nums in combinations_with_replacement(digits,digitcount):
    ansdict = dict() #dictionary (key/value pairs): key is goal, value is list of expressions... so that ansdict[goal] = [list of expressions that evaluate to goal]
    for ops in combinations_with_replacement(oplist,digitcount-1):
        test_expression(nums,ops,ansdict) #put all solutions with these numbers and operators in the ansdict
    uniques = [x for x in ansdict if len(ansdict[x])==1]
    if goal in uniques:
        print (nums,'has unique solution',ansdict[goal])
    elif goal in ansdict:
        print (nums,'has many solutions',ansdict[goal])
    else:  #no solution, search for closest
        sollst = [] #list of expressions found to be closest
        anslst = [] #list of answers found to be closest
        mindiff = 100
        for ans in ansdict.keys():
            diff = abs(goal-ans)
            if diff < mindiff:
                anslst = [ans]
                sollst = ansdict[ans]
                mindiff = diff
            elif diff == mindiff:
                anslst += [ans]
                sollst += ansdict[ans]
        print (nums,'has no solutions, closest:',anslst,sollst)
