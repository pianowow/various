#https://www.codeeval.com/open_challenges/47/

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
f = open(args.string)

def ispalindrome(num):
    n = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    return rev == n

def countpalindromes(start,length):
    tot = 0
    for x in range(start,start+length):
        if ispalindrome(x):
            tot += 1
    return tot

def interestingsubs(low,high):
    tot = 0
    for length in range(1,high-low+2):
        for start in range(low,high-length+2):
            if countpalindromes(start,length) %2 == 0:
                tot += 1
    return tot

for line in f:
    x,y = map(int,line.split(' '))
    print(interestingsubs(x,y))

f.close()