#https://www.codeeval.com/open_challenges/14/

from argparse import ArgumentParser
from itertools import permutations
parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
f = open(args.string)
for line in f:
    l = list()
    for p in permutations(line[:-1]):
        l.append(''.join(p))
    print(','.join(sorted(l)))
f.close()