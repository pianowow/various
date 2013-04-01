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

import urllib.request
import pickle

req = 'http://www.pythonchallenge.com/pc/def/banner.p'
##t = urllib.request.urlopen(req).read().decode("utf-8")
t = urllib.request.urlopen(req).read()
##print(t)
s = pickle.loads(t)
##print(s)

for line in s:
    l = ''
    for char in line:
        l += char[0]*char[1]
    print (l)