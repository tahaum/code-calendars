from utils import *

# Part 1
path = "../data/05.txt"
data = read_text_file_standard(path)
n_lines = len(data)
ds, ss, rs = list(), list(), list()
for line_idx, line in enumerate(data):
    if line_idx == 0:
        seeds = [int(i) for i in line.split(":")[1].split()]
    if ":" not in line and len(line) > 0:
        d, s, r = (int(i) for i in line.split())
        ds.append(d)
        ss.append(s)
        rs.append(r)
    if (len(line) == 0 and line_idx > 1) or (line_idx == (n_lines - 1)):
        for seed_idx, seed in enumerate(seeds):
            for d, s, r in zip(ds, ss, rs):
                if seed >= s and (seed <= (s + r - 1)):
                    diff = seed - s
                    seeds[seed_idx] = d + diff
                    break
        ds, ss, rs = list(), list(), list()

print("p1:", min(seeds))

# Part 2 - inverse binary search
path = "../data/05.txt"
data = read_text_file_standard(path)
