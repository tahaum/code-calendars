import input_utils as iu

def main():
    path = '../data/02-1.txt'
    data = iu.read_text_file_standard(path)
    pos_keeper = {
        'forward': 0,
        'up': 0,
        'down': 0
    }
    for line in data:
        try:
            d, a = line.split(' ')
            pos_keeper[d] += int(a)
        except Exception as e:
            raise(e)
    print('Part 1:', pos_keeper['forward'] * (pos_keeper['down'] - pos_keeper['up']))
    
    pos_keeper = {
        'aim': 0,
        'depth': 0,
        'forward': 0 
    }
    for line in data:
        try:
            d, a = line.split(' ')
            a = int(a)
            if d == 'up':
                pos_keeper['aim'] -= a
            elif d == 'down':
                pos_keeper['aim'] += a
            else:
                pos_keeper['forward'] += a
                pos_keeper['depth'] += (a * pos_keeper['aim'])
        except Exception as e:
            raise(e)
    print('Part 2:', pos_keeper['forward'] * pos_keeper['depth']) 
    
if __name__ == '__main__':
    main()