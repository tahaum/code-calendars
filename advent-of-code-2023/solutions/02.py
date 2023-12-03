from utils import *


# Part 1
path = "../data/02.txt"
data = read_text_file_standard(path)
max_ = {"red": 12, "green": 13, "blue": 14}
sum_ = 0
for line in data:
    valid = True
    id_, sets = line.split(":")
    for set_ in sets.split(";"):
        for subset_ in set_.split(", "):
            n, color = subset_.strip().split()
            if int(n) > max_[color]:
                valid = False
    if valid:
        sum_ += int(id_.split()[1])
                
print("p1:", sum_)            

# Part 2
path = "../data/02.txt"
data = read_text_file_standard(path)
sum_ = 0
for line in data:
    max_ = {c: m for c, m in zip(["red", "green", "blue"], [0] * 3)}
    _, sets = line.split(":")
    for set_ in sets.split(";"):
        for subset_ in set_.split(", "):
            n, color = subset_.strip().split()
            if int(n) > max_[color]:
                max_.update({color: int(n)})
    prod = 1
    for v in max_.values():
        prod *= v
    sum_ += prod
                
print("p2:", sum_)            