#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     01/04/2015
# Copyright:   (c) CHRISTOPHER_IRWIN 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import random

attempts = 1000000
minionkilled = 0

for x in range(attempts):
    minion = 0
    hero = 0
    for missile in range(4):
       if minion < 2:
           if random() >= .5:
               minion+=1
           else:
               hero+=1
       else:
           hero+=1
    if minion==2:
        minionkilled+=1
print('probability minion dies:',minionkilled/attempts)


