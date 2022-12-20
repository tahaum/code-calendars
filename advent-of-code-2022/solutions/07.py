from utils import *
from collections import defaultdict

def main():
    path = '../data/07-1.txt'
    data = read_text_file_standard(path)
    
    SIZES = defaultdict(int)
    path = []
    for line in data:
        words = line.split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            size = int(words[0])
            for i in range(1, len(path) + 1):
                SIZES['/'.join(path[:i])] += size
                
    p1 = 0
    max_used = 70000000 - 30000000
    tot_used = SIZES['/']
    needed = tot_used - max_used
    p2 = 1e9
    for k, v in SIZES.items():
        if v <= 100000:
            p1 += v
        if v > needed:
            p2 = min(p2, v)
    print(p1)
    print(p2)

if __name__ == '__main__':
    main()