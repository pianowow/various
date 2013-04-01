#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     22/01/2013
from zipfile import ZipFile
path="C:\\somedirectory"  # insert the path to the directory of interest

z = ZipFile('6.zip')
f = z.open('readme.txt').read().decode('utf-8')
nothing = '90052'
c = ''
while True:
    try:
        f = z.open(nothing+'.txt').read().decode('utf-8')
        c += z.getinfo(nothing+'.txt').comment.decode('utf-8')
    except:
        break
    nothing = f.split()[-1]

print(c)
z.close()