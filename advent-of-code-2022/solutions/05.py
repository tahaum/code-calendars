from utils import *
from copy import deepcopy
import re

def main():
    path = '../data/05-1.txt'
    
    with open(path) as f:
        cargo = {
            int(c[0]): [*filter(str.isalpha, c)]
            for c in zip(*[*iter(f.readline, '\n')][::-1])
            if c[0].isdigit()
        }
        ins = [[int(i) for i in re.findall('\d+', j)] for j in f.readlines()]
    
    carg2 = deepcopy(cargo)
    for i in ins:
        n, f, t = i
        m1, m2 = list(), list()
        for _ in range(n):
            m1 += cargo[f].pop()
            m2 += carg2[f].pop()
        cargo[t].extend(m1)
        carg2[t].extend(list(reversed(m2)))
        
    print(''.join([v[-1] for v in cargo.values()])) # Part 1
    print(''.join([v[-1] for v in carg2.values()])) # Part 2
    
if __name__ == '__main__':
    main()