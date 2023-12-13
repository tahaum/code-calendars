import input_utils as iu
import numpy as np

def main():
    path = '../data/03-1.txt'
    data = iu.read_text_file_standard(path)
    data_list = list()
    for line in data:
        data_list.append([int(val) for val in list(line)])
    arr = np.array(data_list)
    gamma_bits, epsilon_bits = '', ''
    for i in range(len(arr[0])):
        values, counts = np.unique(arr[:, i], return_counts=True)
        gamma_bits += str(values[np.argmax(counts)])
        epsilon_bits += str(values[np.argmin(counts)])
    print('Part 1:', int(gamma_bits, base=2) * int(epsilon_bits, base=2))
    
    bit_results = list()
    for equal_bit in [1, 0]:
        arr = np.array(data_list)
        for i in range(len(arr[0])):
            try:
                values, counts = np.unique(arr[:, i], return_counts=True)
                if counts[0] == counts[1]:
                    keep_bit = equal_bit
                else:
                    if equal_bit == 1:
                        keep_bit = values[np.argmax(counts)]
                    else:
                        keep_bit = values[np.argmin(counts)]
                arr = arr[arr[:, i] == keep_bit]
            except Exception as e:
                print(values, counts, len(arr))
                raise(e)
            if len(arr) == 1:
                break
        bit_results.append(''.join([str(val) for val in arr[0]]))
    print('Part 2:', int(bit_results[0], base=2) * int(bit_results[1], base=2))
        
if __name__ == '__main__':
    main()