from utils import *
from collections import defaultdict

path = "../data/16.txt"
grid = read_text_file_standard(path)

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

def energize(pos: tuple, dir: tuple) -> dict:
    queue = [(pos, dir)]
    grid_visited = defaultdict(list)
    while queue:
        pos, dir = queue.pop()
        in_grid = check_if_in_grid(pos)
        if in_grid:
            if dir in grid_visited[pos]:
                continue
            grid_visited[pos].append(dir)
        else:
            continue
        c = grid[pos[1]][pos[0]]
        if c == "|":
            if dir == E or dir == W:
                queue.append((move(pos, S), S))
                queue.append((move(pos, N), N))
            else:
                queue.append((move(pos, dir), dir))
        elif c == "-":
            if dir == N or dir == S:
                queue.append((move(pos, E), E))
                queue.append((move(pos, W), W))
            else:
                queue.append((move(pos, dir), dir))
        elif c == "/":
            if dir == N:
                queue.append((move(pos, E), E))
            elif dir == S:
                queue.append((move(pos, W), W))
            elif dir == E:
                queue.append((move(pos, N), N))
            elif dir == W:
                queue.append((move(pos, S), S))
        elif c == "\\":
            if dir == N:
                queue.append((move(pos, W), W))
            elif dir == S:
                queue.append((move(pos, E), E))
            elif dir == E:
                queue.append((move(pos, S), S))
            elif dir == W:
                queue.append((move(pos, N), N))
        else:
            queue.append((move(pos, dir), dir))
    return grid_visited

def check_if_in_grid(pos: tuple) -> bool:
    return pos[0] >= 0 and pos[0] < len(grid[0]) and pos[1] >= 0 and pos[1] < len(grid)

def move(pos: tuple, dir: tuple) -> tuple:
    return (pos[0] + dir[0], pos[1] + dir[1])

def max_energize(grid: list) -> int:
    max_e = 0
    max_x, max_y = len(grid[0]), len(grid)
    for i in range(max_x):
        e = len(energize((i, 0), S))
        if e > max_e:
            max_e = e
        
        e = len(energize((i, max_y-1), N))
        if e > max_e:
            max_e = e
    
    for i in range(max_y):
        e = len(energize((0, i), E))
        if e > max_e:
            max_e = e
        
        e = len(energize((max_x-1, i), W))
        if e > max_e:
            max_e = e
    return max_e
        

print("p1:", len(energize((0, 0), E)))
print("p2:", max_energize(grid))