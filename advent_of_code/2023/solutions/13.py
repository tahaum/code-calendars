from utils import *

path = "../data/13.txt"
data = read_text_file_standard(path)

def parse(data: list) -> list:
    pattern, patterns = list(), list()
    for i, line in enumerate(data):
        if len(line) > 0 and i != (len(data) - 1):
            pattern.append(list(line))
        else:
            patterns.append(pattern)
            pattern = list()
    return patterns

def transpose(pattern: list) -> list:
    return list(map(list, zip(*pattern)))

def is_mirrored_across_row(pattern: list, i: int) -> bool:
    i_min, min_len = min(
        enumerate([len(pattern[:i+1]), len(pattern[i+1:])]),
        key=lambda x: x[1]
    )
    if i_min == 0:
        return pattern[:i+1] == list(reversed(pattern[i+1:i+1+min_len]))
    else:
        return pattern[i+1-min_len:i+1] == list(reversed(pattern[i+1:]))

# Part 1
sum_ = 0
for pattern in parse(data):
    for t in [False, True]:
        if t:
            multiplier = 1
            pattern = transpose(pattern)
        else:
            multiplier = 100
        for i in range(len(pattern)-1):
            if is_mirrored_across_row(pattern, i):
                sum_ += multiplier * (i + 1)
                break
print("p1:", sum_)

