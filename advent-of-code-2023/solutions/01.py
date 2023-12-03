from utils import *


# Part 1
path = "../data/01.txt"
data = read_text_file_standard(path)
sum_ = 0
for line in data:
    ints = list()
    for c in line:
        try:
            _ = int(c)
            ints.append(c)
        except ValueError:
            pass
    sum_ += int(''.join([ints[0], ints[-1]]))
print("p1:", sum_)

# Part 2
path = "../data/01.txt"
data = read_text_file_standard(path)
sum_ = 0
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    ints = list()
    for line_idx, c in enumerate(line):
        try:
            _ = int(c)
            ints.append(c)
        except ValueError:
            for digit_idx, d in enumerate(digits):
                if d in line[line_idx:line_idx+len(d)]:
                    ints.append(str(digit_idx+1))
    sum_ += int(''.join([ints[0], ints[-1]]))
print("p2:", sum_)