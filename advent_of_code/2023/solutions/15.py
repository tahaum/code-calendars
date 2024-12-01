from utils import *
from collections import defaultdict

path = "../data/15.txt"
data = read_text_file_standard(path)

steps = data[0].split(",")

def HASH(s: str) -> int:
    v = 0
    for char in s:
        v = ((v + ord(char)) * 17) % 256
    return v

# Part 1
sum_ = 0
for step in steps:
    sum_ += HASH(step)
print("p1:", sum_)

# Part 2
boxes = defaultdict(dict)
for step in steps:
    if "=" in step:
        ins = True
        label, fl = step.split("=")
    else:
        ins = False
        label = step[:-1]
    box_id = HASH(label)
    if ins:
        boxes[box_id].update({label: int(fl)})
    else:
        boxes[box_id].pop(label, None)
        
fp = 0
for box_number, box in boxes.items():
    for i, focal_length in enumerate(box.values()):
        fp += (box_number + 1) * (i + 1) * focal_length
print("p2:", fp)