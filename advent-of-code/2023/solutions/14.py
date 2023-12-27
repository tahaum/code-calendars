from utils import *

path = "../data/14.txt"

def parse(path: str) -> list:
    data = read_text_file_standard(path)
    for idx, line in enumerate(data):
        data[idx] = list(line)
    return data

def tilt_north(data: list) -> list:
    for x in range(len(data[0])):
        for y in range(len(data)):
            char = data[y][x]
            if char == "O":
                new_y = find_stop_above(data, x, y)
                data = move_rock(data, x, y, new_y)
    return data

def find_stop_above(data: list, x: int, y: int) -> int:
    if y > 0:
        for y_ in range(y-1, -1, -1):
            if data[y_][x] != ".":
                return y_ + 1
    return 0

def move_rock(data: list, x: int, y: int, new_y: int) -> list:
    if new_y != y:
        data[new_y][x] = "O"
        data[y][x] = "."
    return data

def calc_load(data: list) -> int:
    sum_ = 0
    for x in range(len(data[0])):
        for y in range(len(data)):
            char = data[y][x]
            if char == "O":
                sum_ += len(data) - y
    return sum_

def cycle(grid: list) -> list:
    for _ in range(4):
        grid = tilt_north(grid)
        grid = rotate_grid_clockwise(grid)
    return grid


def rotate_grid_clockwise(grid: list) -> list:
    return [list(row) for row in zip(*reversed(grid))]


def load_after_n_cycles(grid: list, cycles: int) -> int:
    cycle_hashes, cycle_loads = dict(), dict()

    for cycle_count in range(1, cycles+1):
        grid = cycle(grid)
        grid_hash = hash_grid(grid)

        if grid_hash in cycle_hashes:
            cycle_start = cycle_hashes[grid_hash]
            cycle_size = cycle_count - cycle_start
            extra_cycles = (cycles - cycle_start) % cycle_size
            return cycle_loads[cycle_start + extra_cycles]
        else:
            cycle_hashes[grid_hash] = cycle_count
            cycle_loads[cycle_count] = calc_load(grid)

def hash_grid(grid: list) -> int:
    return hash(frozenset([tuple(row) for row in grid]))

# Part 1
grid = parse(path)
grid = tilt_north(grid)
print("p1:", calc_load(grid))

# Part 2
grid = parse(path)
print("p2:", load_after_n_cycles(grid, 1000000000))