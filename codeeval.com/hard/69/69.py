#https://www.codeeval.com/open_challenges/69/
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
f = open(args.string)

def countsubseq(seq, subseq):
    l = subseq[0]
    i = seq.find(l)
    tot=0
    while i>=0:
        if len(subseq) < 2:
            tot += 1
        else:
            tot += countsubseq(seq[i+1:],subseq[1:])
        i = seq.find(l,i+1)
    return tot

for line in f:
    line = line[:-1]
    params = line.split(',')
    print(countsubseq(params[0],params[1]))

f.close()