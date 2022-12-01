from utils import *

def main():
    path = '../data/01-1.txt'
    data = read_text_file_standard(path)
    elves = list()
    elf = 0
    for c in data:
        if c != '':
            elf += int(c)
        else:
            elves.append(int(elf))
            elf = 0
    print(max(elves)) # Part 1
    top_3 = sorted(elves)[-3:]
    print(sum(top_3)) # Part 2
    
    
if __name__ == '__main__':
    main()