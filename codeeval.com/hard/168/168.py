#https://www.codeeval.com/open_challenges/168/
#http://dsp.stackexchange.com/questions/2543/determining-frequency-and-period-of-a-wave

from argparse import ArgumentParser
from numpy import fft
from math import log

parser = ArgumentParser()
parser.add_argument("string",type=str)
args = parser.parse_args()
f = open(args.string)

fs = 20000  #sample frequency of data in file, given by problem

def demean(lst):
    avg = 0
    if len(lst) != 0:
        avg = sum(lst)/len(lst)
    return list(map(lambda x: x-avg, lst))

def frequency(params):
    xn = demean(params)
    Xf = fft.rfft(xn).tolist()
    psd = map(lambda x: log(x.real**2,10),Xf)
    peak = max(psd)
    return peak * fs/len(params)

for line in f:
    line = line[:-1]
    params = list(map(int,line.split(' ')))
    print(frequency(params))

f.close()