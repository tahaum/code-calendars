import input_utils as iu
import numpy as np

def main():
    path = '../data/11-1.txt'
    grid = load_data(path)
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    data = [[int(val) for val in line] for line in data]
    return np.array(data) 

def simulate(grid, iters):
    for i in range(iters):
        grid += 1
        if (grid == 9).any():
            pass
            
def add_to_neighbors():
    pass
    
if __name__ == '__main__':
    main()