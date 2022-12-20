from utils import *

def main():
    path = '../data/06-1.txt'
    data = read_text_file_standard(path)[0]
    
    marker_len = 14
    for i in range(len(data) - marker_len):
        char_set = set(data[i:i+marker_len])
        if len(char_set) == marker_len:
            print(i + marker_len, char_set)
            break
    
if __name__ == '__main__':
    main()