import input_utils as iu
import numpy as np

def main():
    path = '../data/20-1.txt'
    algo, img = load_data(path)
    print(algo)
    print(img)
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    algo = data[0]
    rows = list()
    for i in range(2, len(data)):
        rows.append([p for p in data[i]])
    return algo, np.array(rows)
    
if __name__ == '__main__':
    main()