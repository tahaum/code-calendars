from utils import *
from collections import defaultdict
import re

# Part 1
dx_ = [*[-1, 0, 1]*3]
dy_ = [*[-1]*3, *[0]*3, *[1]*3]
path = "../data/03.txt"
data = read_text_file_standard(path)
nrs = defaultdict(list)
sum_ = 0
summed = list()
for idx_y, line in enumerate(data):
    nrs[idx_y].extend(
        [{int(m.group()): (m.start(), m.end())} for m in re.finditer(r'\d+', line)]
    )
for idx_y, line in enumerate(data):
    for idx_x, ch in enumerate(line):
        if ch != "." and not ch.isdigit():
            for dx, dy in zip(dx_, dy_):
                d = data[idx_y + dy][idx_x + dx]
                if d.isdigit():
                    d = int(d)
                    for idx_nr, nr_info in enumerate(nrs[idx_y + dy]):
                        nr, nr_vals = *list(nr_info.keys()), *list(nr_info.values())
                        if (
                            (idx_x + dx >= min(nr_vals))
                            and (idx_x + dx <= max(nr_vals))
                            and ((idx_y + dy, idx_nr) not in summed)
                        ):
                            sum_ += nr
                            summed.append((idx_y + dy, idx_nr))
print("p1:", sum_)

# Part 2
path = "../data/03.txt"
data = read_text_file_standard(path)
nrs = defaultdict(list)
sum_ = 0
summed = list()
for idx_y, line in enumerate(data):
    nrs[idx_y].extend(
        [{int(m.group()): (m.start(), m.end())} for m in re.finditer(r'\d+', line)]
    )
for idx_y, line in enumerate(data):
    for idx_x, ch in enumerate(line):
        if ch == "*":
            gear_digits = list()
            for dx, dy in zip(dx_, dy_):
                d = data[idx_y + dy][idx_x + dx]
                if d.isdigit():
                    d = int(d)
                    for idx_nr, nr_info in enumerate(nrs[idx_y + dy]):
                        nr, nr_vals = *list(nr_info.keys()), *list(nr_info.values())
                        if (
                            (idx_x + dx >= min(nr_vals))
                            and (idx_x + dx <= max(nr_vals))
                            and ((idx_y + dy, idx_nr) not in summed)
                        ):
                            gear_digits.append(nr)
                            summed.append((idx_y + dy, idx_nr))
            if len(gear_digits) >= 2:
                prod = 1
                for v in gear_digits:
                    prod *= v
                sum_ += prod
                
print("p2:", sum_)
                        
                    