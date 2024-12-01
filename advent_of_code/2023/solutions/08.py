from utils import *
from math import lcm

path = "../data/08.txt"
data = read_text_file_standard(path)

moves = list(data[0])
move_map = {"L": 0, "R": 1}

nodes = dict()
for line in data[2:]:
    s, d = line.split(" = ")
    d = d.strip("()").split(", ")
    nodes[s] = d

# Part 1
steps = 0
n = "AAA"
while n != "ZZZ":
    for move in moves:
        n = nodes[n][move_map[move]]
        steps += 1

print("p1:", steps)

# Part 2
starting_ns = [k for k in nodes.keys() if k[-1] == "A"]
steps = list()
for n in starting_ns:
    current_steps = 0
    while n[-1] != "Z":
        for move in moves:
            n = nodes[n][move_map[move]]
            current_steps += 1
    steps.append(current_steps)

print("p2:", lcm(*steps))