import input_utils as iu
import numpy as np

def main():
    path = '../data/05-1.txt'
    coord_arr = load_data(path)
    marker = create_marker_diagram(coord_arr)
    create_field_map_horizontal(coord_arr, marker)
    print('Part 1:', len(marker[marker >= 2]))
    
    marker = create_marker_diagram(coord_arr)
    marker = create_field_map_horizontal_and_diagonal(coord_arr, marker)
    print('Part 2:', len(marker[marker >= 2]))
                
def load_data(path):
    data = iu.read_text_file_standard(path)
    for i in range(len(data)):
        coords = data[i].split(' -> ')
        coords = [pair.split(',') for pair in coords]
        data[i] = coords
    coord_arr = np.array(data, dtype=int)
    return coord_arr

def create_marker_diagram(arr):
    return np.zeros(shape=(arr.max() + 1, arr.max() + 1))

def create_field_map_horizontal(coords, marker):
    for coord in coords:
        p1, p2 = coord[0], coord[1]
        xs = sorted([p1[0], p2[0]])
        ys = sorted([p1[1], p2[1]])
        if (xs[0] == xs[1]) or (ys[0] == ys[1]):
            marker[ys[0]:(ys[1] + 1), xs[0]:(xs[1]+1)] += 1
    return marker

def create_field_map_horizontal_and_diagonal(coords, marker):
    for coord in coords:
        p1, p2 = coord[0], coord[1]
        xs = [p1[0], p2[0]]
        ys = [p1[1], p2[1]]
        if (xs[0] == xs[1]) or (ys[0] == ys[1]):
            xs, ys = sorted(xs), sorted(ys)
            marker[ys[0]:(ys[1] + 1), xs[0]:(xs[1]+1)] += 1
        else:
            if xs[1] < xs[0]: 
                x_step, x_add = -1, -1
            else: 
                x_step, x_add = 1, 1
            if ys[1] < ys[0]: 
                y_step, y_add = -1, -1
            else: 
                y_step, y_add = 1, 1
            for x, y in zip(range(xs[0], xs[1] + x_add, x_step), range(ys[0], ys[1] + y_add, y_step)):
                marker[y, x] += 1
    return marker
    
if __name__ == '__main__':
    main()