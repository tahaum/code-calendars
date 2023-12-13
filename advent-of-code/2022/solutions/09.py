from utils import *
from collections import defaultdict

def main():
    path = '../data/09-1.txt'
    data = read_text_file_standard(path)
    
    def add_to_visited(tr, tc, visited):
        if (tr, tc) not in visited:
            visited.append((tr, tc))
        return visited
    
    def distance_between(p1, p2):
        dx = abs(p1[0] - p2[0])
        dy = abs(p1[1] - p2[1])
        if dx == 1 and dy == 1:
            return 1
        else:
            return dx + dy
        
    def get_max_distance_between_snake_elems(snake):
        dists = [distance_between((snake[i][0], snake[i][1]), (snake[i-1][0], snake[i-1][1]))
                 for i in range(1, len(snake))]
        return max(dists)
    
    def get_step(p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        if dx != 0:
            dx = int(dx/abs(dx))
        if dy != 0:
            dy = int(dy/abs(dy))
        return dx, dy
    
    def move_rest_of_snake_one_step(snake, idx, visited_end):
        prev_r, prev_c = snake[idx-1]
        dc, dr = get_step((prev_c, prev_r), (snake[idx][1], snake[idx][0]))
        dist = distance_between((prev_c, prev_r), (snake[idx][1], snake[idx][0]))
        if dist > 1:
            snake[idx][0] += dr
            snake[idx][1] += dc
            if idx == (len(snake) - 1):
                visited_end = add_to_visited(snake[idx][0], snake[idx][1], visited_end)
            else:
                move_rest_of_snake_one_step(snake, idx + 1, visited_end)
    
    # Part 1
    hr, hc = 0, 0
    tr, tc = 0, 0
    visited = [(0, 0)]
    
    # Part 2
    snake = [[0, 0] for _ in range (10)]
    visited_end = [(0, 0)]
    
    for ins in data:
        d, l = ins.split()
        l = int(l)
        
        if d == 'L':
            hc -= l
            snake[0][1] -= l
        elif d == 'R':
            hc += l
            snake[0][1] += l
        elif d == 'U':
            hr -= l
            snake[0][0] -= l
        else:
            hr += l
            snake[0][0] += l
        
        while distance_between((hc, hr), (tc, tr)) > 1:
            dc, dr = get_step((hc, hr), (tc, tr))
            tr += dr
            tc += dc
            visited = add_to_visited(tr, tc, visited)
        
        while get_max_distance_between_snake_elems(snake) > 1:
            move_rest_of_snake_one_step(snake, 1, visited_end)
    
    print(len(visited)) # Part 1
    print(len(visited_end)) # Part 2
   
if __name__ == '__main__':
    main()