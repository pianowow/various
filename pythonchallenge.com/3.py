#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     22/01/2013
import string, re
f = open('3.txt').read()
f = f.replace('\n','')
upper = string.ascii_uppercase
lower = string.ascii_lowercase

length = len(f)
sol = ''
for i,c in enumerate(f):
    found = True
    if i < length - 9:
        test = f[i:i+9]
        if test[4] in lower and test[0] in lower and test[8] in lower:
            for x in test[1:4]+test[5:8]:
                if x not in upper:
                    found = False
            if found:
                sol += test[4]


print(sol)