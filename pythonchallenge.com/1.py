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
import string

s = "map"
t = ""
alphafrom = ""
alphato = ""
for x in range(97,123):
    alphafrom += chr(x)

print(alphafrom)

for x in range(99,125):
    alphato += chr(x)

alphato = alphato.replace(chr(123),chr(97))
alphato = alphato.replace(chr(124),chr(98))

alphadict = dict()

for i,c in enumerate(alphafrom):
    alphadict[c] = alphato[i]

print(alphato)

for c in s:
    if c in string.ascii_lowercase:
        t+=alphadict[c]
    else:
        t+=c

print(t)