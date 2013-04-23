#https://www.codeeval.com/open_challenges/14/

from argparse import ArgumentParser
from itertools import permutations
parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
#print(args.string)
instr = args.string
l = list()
for p in permutations(instr):
    l.append(''.join(p))
print(','.join(sorted(l)))



