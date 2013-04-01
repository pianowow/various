#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     22/01/2013
# Copyright:   (c) CHRISTOPHER_IRWIN 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

histdict = dict()

f = open("2.txt").read()

for line in f:
    for char in line:
        if char not in histdict:
            histdict[char] = 1
        else:
            histdict[char] += 1


for x in histdict:
    if histdict[x] > 10:
        f = f.replace(x,'')

print(f)
