from utils import *
from collections import defaultdict

def main():
    path = '../data/03-1.txt'
    data = read_text_file_standard(path)
    
    lc = 'abcdefghijklmnopqrstuvwxyz'
    uc = lc.upper()
    pris = {
        **{c: p for c, p in zip(lc, range(1, 27))},
        **{c: p for c, p in zip(uc, range(27, 53))}
    }
    
    # Part 1
    pri_sum = 0
    for ruck in data:
        h = int(len(ruck) / 2)
        r1, r2 = ruck[:h], ruck[h:]
        both = (set(r1) & set(r2)).pop()
        pri_sum += pris[both]
    print(pri_sum)
    
    # Part 2
    def get_common_type(group):
        s1, s2, s3 = set(group[0]), set(group[1]), set(group[2])
        return (s1 & s2 & s3).pop()
    
    pri_sum = 0
    for idx in range(3, len(data)+1, 3):
        group = data[idx-3: idx]
        badge = get_common_type(group)
        pri_sum += pris[badge]
    print(pri_sum)
    
if __name__ == '__main__':
    main()