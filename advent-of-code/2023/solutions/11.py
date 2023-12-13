from utils import *
from collections import defaultdict

path = "../data/11.txt"
data = read_text_file_standard(path)


def manhattan_dist(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve(expansion_factor: int = 2) -> int:
    empty_rows = list()
    empty_cols = list(range(len(data[0])))
    for i, line in enumerate(data):
        if "#" not in line:
            empty_rows.append(i)
        else:
            line_g_cols = [pos for pos, char in enumerate(line) if char == "#"]
            for col in line_g_cols:
                if col in empty_cols:
                    empty_cols.remove(col)

    gs = list()
    for i, line in enumerate(data):
        if "#" in line:
            for c, char in enumerate(line):
                if char == "#":
                    gs.append((i, c))
                    

    visited_routes = defaultdict(list)
    calculated_dists = list()
    for i in range(len(gs)):
        for i_ in range(i + 1, len(gs)):
            g, g_ = gs[i], gs[i_]
            if g not in visited_routes[g_]:
                dist = manhattan_dist(g, g_)
                for er in empty_rows:
                    if min(g[0], g_[0]) <= er <= max(g[0], g_[0]):
                        dist += expansion_factor - 1
                for ec in empty_cols:
                    if min(g[1], g_[1]) <= ec <= max(g[1], g_[1]):
                        dist += expansion_factor - 1
                calculated_dists.append(dist)
                visited_routes[g].append(g_)
                visited_routes[g_].append(g)
    return sum(calculated_dists)


print("p1:", solve(2))
print("p2:", solve(10**6))