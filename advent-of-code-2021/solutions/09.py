import input_utils as iu
import numpy as np
from collections import deque
from functools import reduce

def main():
    path = '../data/09-1.txt'
    arr = load_data(path)
    lps, lp_indexes = find_low_points(arr)
    risk_levels = [lp + 1 for lp in lps]
    print('Part 1:', sum(risk_levels))
    
    basin_sizes = sorted(find_basin_sizes(lp_indexes, arr))
    ans = reduce(lambda x, y: x * y, basin_sizes[-3:])
    print('Part 2:', ans)
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    for i in range(len(data)):
        data[i] = [int(h) for h in data[i]]
    return np.array(data)

def find_low_points(arr):
    low_points, indexes = list(), list()
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            neighbors = find_neighboring_points(arr, r, c)
            if min(neighbors) > arr[r, c]:
                low_points.append(arr[r, c])
                indexes.append((r, c))
    return low_points, indexes
            
def find_neighboring_points(arr, r, c):
    points = list()
    add = {
        'x': [0, 0, -1, 1],
        'y': [-1, 1, 0, 0]
    }
    for x, y in zip(add['x'], add['y']):
        if ((r + x) >= 0) and ((c + y) >= 0):
            try:
                n = arr[r + x, c + y]
                points.append(n)
            except Exception as e:
                pass
    return points

def find_basin_sizes(lp_indexes, arr):
    basin_sizes = list()
    for lp_r, lp_c in lp_indexes:
        basin_sizes.append(find_low_point_basin_size(lp_r, lp_c, arr))
    return basin_sizes

def find_low_point_basin_size(lp_r, lp_c, arr):
    m, n = arr.shape
    s = 0
    q = deque()
    seen = set()
    q.append((lp_r, lp_c))
    while len(q) > 0:
        r, c = q.popleft()
        prnt = f'{r}, {c}'
        if (r, c) in seen:
            continue
        else:
            s += 1
            seen.add((r, c))
            add = {
                'x': [0, 0, -1, 1],
                'y': [-1, 1, 0, 0]
            }
            for x, y in zip(add['x'], add['y']):
                if 0 <= r + x < m and 0 <= c + y < n and arr[r + x, c + y] != 9:
                    prnt += f' added {r + x}, {c + y}'
                    q.append((r + x, c + y))
    return s

if __name__ == '__main__':
    main()