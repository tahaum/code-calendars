import input_utils as iu

def main():
    path = '../data/08-1.txt'
    data = iu.read_text_file_standard(path)
    ans = 0
    for line in data:
        before, after = line.split('|')
        before = before.split()
        after = after.split()
        for digit in after:
            if len(digit) in [2, 3, 4, 7]:
                ans += 1
    print('Part 1:', ans)
    
if __name__ == '__main__':
    main()