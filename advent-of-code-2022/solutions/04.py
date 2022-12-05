from utils import *

def main():
    path = '../data/04-1.txt'
    data = read_text_file_standard(path)
    
    overlaps_part = 0
    overlaps_comp = 0
    for s in data:
        a, b = s.split(',')
        al, au = (int(i) for i in a.split('-'))
        bl, bu = (int(i) for i in b.split('-'))
        if (al <= bl <= au) or (al <= bu <= au) or (bl <= al <= bu) or (bl <= au <= bu):
            overlaps_part += 1
            if (al <= bl and au >= bu) or (bl <= al and bu >= au):
                overlaps_comp += 1
            
    # Part 1
    print(overlaps_comp)
    
    # Part 2
    print(overlaps_part)
    
if __name__ == '__main__':
    main()