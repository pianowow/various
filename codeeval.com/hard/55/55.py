#https://www.codeeval.com/open_challenges/55/

from string import ascii_lowercase
from argparse import ArgumentParser

teach = '''Mary had a little lamb its fleece was white as snow;
And everywhere that Mary went, the lamb was sure to go.
It followed her to school one day, which was against the rule;
It made the children laugh and play, to see a lamb at school.
And so the teacher turned it out, but still it lingered near,
And waited patiently about till Mary did appear.
"Why does the lamb love Mary so?" the eager children cry; "Why,
Mary loves the lamb, you know" the teacher did reply."'''
#teach = teach.lower()
cleanteach = ""
for l in teach:
    if l.isalnum():
        cleanteach+=l
    else:
        if l in ' \n' and cleanteach[-1] != ' ':
            cleanteach += ' '
wordlist = cleanteach.split(' ')

parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
f = open(args.string)

def ngrams(n, words):
    n = int(n)
    #input = list(map(str.strip,words.lower().split(' ')))
    input = list(map(str.strip,words.split(' ')))
    hist = dict()
    for i in range(len(wordlist)):
        if input == wordlist[i:i+n-1]:
            nxt = wordlist[i+n-1]
            if nxt in hist:
                hist[nxt] += 1
            else:
                hist[nxt] = 1
    outlst = []
    for key in hist.keys():
        outlst.append([key,hist[key]])
    outlst.sort(key=lambda x:(-x[1],x[0]))

    for e in outlst[:-1]:
        print(e[0],',','%1.3f' % (int(e[1])/sum(hist.values())) ,';',sep='',end='')
    if len(outlst) > 0:
        print(outlst[-1][0],',','%1.3f' % (int(outlst[-1][1])/sum(hist.values())),sep='',end='')
    print('')

for line in f:
    n,words = line.split(',')
    #print('%50s' % (line[:-1]),end=' : ')
    ngrams(n,words)

f.close()
