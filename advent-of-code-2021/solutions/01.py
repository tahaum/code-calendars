import input_utils as iu

def main():
    path = '../data/01-1.txt'
    data = iu.read_text_file_standard(path)
    data = [int(val) for val in data]
    depth_sum = 0
    for i in range(1, len(data)):
        prev, curr = data[i-1], data[i]
        if curr > prev:
            depth_sum += 1
    print('Part 1:', depth_sum)
    
    depth_sum = 0
    for i in range(1, len(data) - 2):
        sum_prev = sum(data[i-1:i+2])
        sum_curr = sum(data[i:i+3])
        if sum_curr > sum_prev:
            depth_sum += 1
    print('Part 2:', depth_sum)
            
if __name__ == '__main__':
    main()