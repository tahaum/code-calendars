from utils import *

def main():
    path = '../data/08-1.txt'
    grid = read_text_file_standard(path)
    grid_t = list(zip(*[*grid]))
    
    # Part 1
    visible = 0
    for ri, r in enumerate(grid):
        r = [int(v) for v in r]
        for ci, c in enumerate(r):
            r_t = grid_t[ci]
            r_t =  [int(v) for v in r_t]
            if ri == 0 or ci == 0 or ri == (len(r_t) - 1) or ci == (len(r) - 1):
                visible += 1
            else:
                left, right = r[:ci], r[ci+1:]
                up, down = r_t[:ri], r_t[ri+1:]
                for line in [left, right, up, down]:
                    if c > max(line):
                        visible += 1
                        break
    print(visible)
    
    # Part 2
    max_score = 0
    for ri, r in enumerate(grid):
        r = [int(v) for v in r]
        for ci, c in enumerate(r):
            current_score = 1
            r_t = grid_t[ci]
            r_t =  [int(v) for v in r_t]
            if ri == 0 or ci == 0 or ri == (len(r_t) - 1) or ci == (len(r) - 1):
                current_score = 0
            else:
                left, right = r[:ci], r[ci+1:]
                up, down = r_t[:ri], r_t[ri+1:]
                for line, dir in zip([left, right, up, down],
                                     ['l', 'r', 'u', 'd']):
                    los = 0
                    if dir in ('l', 'u'):
                        line = list(reversed(line))
                    for v in line:
                        los += 1
                        if v >= c:
                            break
                    current_score *= los
            max_score = max(max_score, current_score)
    print(max_score)
    
if __name__ == '__main__':
    main()