import input_utils as iu
import numpy as np

def main():
    path = '../data/11-1.txt'
    grid = load_data(path)
    simulate(grid, 100)
    print('Part 1:', flash_count)
    
    grid = load_data(path)
    simulate(grid, 1000)
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    data = [[int(val) for val in line] for line in data]
    return np.array(data) 

def simulate(grid, iters):
    rr, cc = grid.shape
    tot = rr * cc
    first_simultaneous = True
    for i in range(iters):
        grid += 1
        for r in range(rr):
            for c in range(cc):
                if grid[r, c] > 9:
                    flash(grid, r, c)
                    
        if len(grid[grid < 0]) == tot and first_simultaneous:
            print('Part 2:', i)
            first_simultaneous = False
        grid[grid < 0] = 0
        
flash_count = 0   
def flash(grid, r, c):
    global flash_count
    flash_count += 1
    rr, cc = grid.shape
    grid[r, c] = -1
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rr and 0 <= nc < cc and grid[nr, nc] != -1:
                grid[nr, nc] += 1
                if grid[nr, nc] > 9:
                    flash(grid, nr, nc)
    
if __name__ == '__main__':
    main()