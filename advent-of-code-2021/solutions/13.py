import input_utils as iu
import numpy as np
from PIL import Image

def main():
    path = '../data/13-1.txt'
    coords, fold_instructions = load_data(path)
    marker = generate_marker(coords)
    fold_axis, fold_val = fold_instructions[0]
    fold_result = fold_marker(marker, fold_axis, fold_val)
    print('Part 1:', int(fold_result.sum()))
    
    marker = generate_marker(coords)
    for fold_axis, fold_val in fold_instructions:
        marker = fold_marker(marker, fold_axis, fold_val)
    im = Image.fromarray(marker.astype('uint8')*255)
    im.save('../visualizations/13-2-results.png')
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    coords = list()
    fold_instructions = list()
    for line in data:
        if len(line) != 0:
            if line[:4] == 'fold':
                s, val = line.split('=')
                axis = s[-1]
                if axis == 'x':
                    axis = 1
                else:
                    axis = 0
                fold_instructions.append([axis, int(val)])
            else:
                coords.append([int(val) for val in line.split(',')])
    return np.array(coords), np.array(fold_instructions)

def generate_marker(coords):
    max_x, max_y = coords[:, 0].max(), coords[:, 1].max()
    marker = np.zeros(shape=(max_y + 1, max_x + 1))
    for coord in coords:
        marker[coord[1], coord[0]] = 1
    return marker

def fold_marker(marker, fold_axis, fold_val):
    if fold_axis == 1:
        part_keep = marker[:, :fold_val]
        part_flip = marker[:, fold_val+1:]
    else:
        part_keep = marker[:fold_val, :]
        part_flip = marker[(fold_val+1):, :]
    if part_keep.shape != part_flip.shape:
        diff = part_keep.shape[fold_axis] - part_flip.shape[fold_axis]
        if diff > 0:
            if fold_axis == 1:
                part_flip = np.hstack((part_flip, np.zeros(part_flip.shape[0])[:, None]))
            else:
                part_flip = np.vstack((part_flip, np.zeros(part_flip.shape[1])))
        else:
            raise Exception('Part to be flipped is large than keeping part, unhandled case!')
    part_flip = np.flip(part_flip, fold_axis)
    result = part_keep + part_flip
    result[result > 1] = 1
    
    return result
    
if __name__ == '__main__':
    main()