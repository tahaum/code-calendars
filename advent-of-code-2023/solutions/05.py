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
    if (
        (len(line) == 0 and line_idx > 1) 
        or (line_idx == (n_lines - 1))
    ):
        for seed_idx, seed in enumerate(seeds):
            for d, s, r in zip(ds, ss, rs):
                if seed >= s and (seed <= (s + r - 1)):
                    diff = seed - s
                    seeds[seed_idx] = d + diff
                    break
        ds, ss, rs = list(), list(), list()

print("p1:", min(seeds))

# Part 2 - ranges instead of single seeds
path = "../data/05-1-ex.txt"
data = read_text_file_standard(path)

class Range:
    def __init__(self, l: int, u: int):
        assert l < u, "Invalid range bounds!"
        self.l = l # Lower bound, inclusive
        self.u = u # Upper bound, inclusive
        
    def __repr__(self) -> str:
        return f"[{self.l}, {self.u}]"
    
    def overlaps(self, other: "Range") -> bool:
        if (
            (self.u >= other.l and self.u <= other.u) 
            or (self.l >= other.l and self.l <= other.u)
            or (other.u >= self.l and other.u <= self.u) 
            or (other.l >= self.l and other.l <= self.u)
        ):
            return True
        else:
            return False
            
n_lines = len(data)
min_loc = 9999999999999
seed_data = list(map(int, data[0].split(":")[1].split()))
seed_ranges = list()
for i in range(0, len(seed_data), 2):
    start, r = seed_data[i:i+2]
    seed_ranges.append(Range(start, start + r - 1))

s_ranges, d_ranges = list(), list()
for seed_range in seed_ranges:
    print(f"\n\n, {seed_range}")
    for line_idx, line in enumerate(data[2:]):
        if ":" not in line and len(line) > 0:
            d, s, r = (int(i) for i in line.split())
            d_ranges.append(Range(d, d + r - 1))
            s_ranges.append(Range(s, s + r - 1))
        if len(line) == 0 or line_idx == (n_lines - 3):
            for s_range, d_range in zip(s_ranges, d_ranges):
                print("S:", s_range, "D:", d_range)
                if seed_range.overlaps(s_range):
                    # print(seed_range)
                    l_diff = max(seed_range.l - s_range.l, 0)
                    u_diff = max(s_range.u - seed_range.u, 0)
                    # print(l_diff, u_diff)
                    seed_range = Range(d_range.l + l_diff, d_range.u - u_diff)
                    # print(seed_range)
            print(seed_range)
            s_ranges, d_ranges = list(), list()
    if seed_range.l < min_loc:
        min_loc = seed_range.l

print("p2:", min_loc)