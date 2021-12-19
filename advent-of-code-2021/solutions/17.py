import input_utils as iu

def main():
    path = '../data/17-1.txt'
    x_min, x_max, y_min, y_max = load_data(path)
    max_try = 200
    max_y = 0
    valid_ys = list()
    for vx_init in range(max_try):
        for vy_init in range(max_try):
            x, y = 0, 0
            temp_xs, temp_ys = list(), list()
            valid = False
            vx, vy = vx_init, vy_init
            while (y >= y_min) and not valid:
                if in_zone(x, y, x_min, x_max, y_min, y_max):
                    valid = True
                x, y, vx, vy = do_step(x, y, vx, vy)
                temp_xs.append(x)
                temp_ys.append(y)
            if valid:
                valid_ys += temp_ys
                # if max(temp_ys) > max_y:
                #     print(f'Currently highest valid y coordinate achieved, inital velocities: {vx_init}, {vy_init}')
                #     max_y = max(temp_ys)
                #     print(temp_xs, temp_ys)
    print('Part 1:', max(valid_ys))
    
    # ex_sol = iu.read_text_file_standard('../data/17-2-solution.txt')
    # ex_sol_set = set()
    # for line in ex_sol:
    #     for pair in line.split():
    #         x, y = [int(i) for i in pair.split(',')]
    #         ex_sol_set.add((x, y))
    
    min_try, max_try = -200, 400
    valid_inits = set()
    for vx_init in range(max_try):
        for vy_init in range(min_try, max_try):
            x, y = 0, 0
            valid = False
            vx, vy = vx_init, vy_init
            while (y >= y_min) and not valid:
                if in_zone(x, y, x_min, x_max, y_min, y_max):
                    valid = True
                x, y, vx, vy = do_step(x, y, vx, vy)
            if valid:
                valid_inits.add((vx_init, vy_init))
    print('Part 2:', len(valid_inits))
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    target_str = data[0]
    x, y = target_str.split(',')
    x_split, y_split = x.split('..'), y.split('..')
    x_min, x_max = int(x_split[0].split('=')[-1]), int(x_split[-1])  
    y_min, y_max = int(y_split[0].split('=')[-1]), int(y_split[-1])
    return x_min, x_max, y_min, y_max

def do_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy

def in_zone(x, y, x_min, x_max, y_min, y_max):
    if (x_min <= x <= x_max) and (y_min <= y <= y_max):
        return True
    else:
        return False
    
def print_trajectory(xs, ys, x_min, x_max, y_min, y_max):
    pass
        
if __name__ == '__main__':
    main()