#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     22/01/2013
import urllib.request

req = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'

for x in range(401):
    t = urllib.request.urlopen(req+nothing).read().decode("utf-8")
    print(t)
    nextnothing = t.split()[-1]
    try:
        i = int(nextnothing)
    except:
        if t == 'Yes. Divide by two and keep going.':
            nextnothing = str(int(nothing)/2)
        else:
            break
    nothing = nextnothing