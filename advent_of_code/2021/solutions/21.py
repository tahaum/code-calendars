import input_utils as iu
import functools
from collections import deque

def main():
    path = '../data/21-1.txt'
    p1, p2 = load_data(path)
    boards = initialize_boards(p1, p2)
    scores, rolls = play_det(boards)
    print('Part 1:', min(scores.values()) * rolls)
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    return [int(line.split(': ')[-1]) for line in data]

def initialize_boards(p1, p2):
    boards = {1: deque(range(1, 11)), 2: deque(range(1, 11))}
    for p, pos in zip([1, 2], [p1, p2]):
        boards[p].rotate(-(pos - 1))
    return boards
        
def move_and_get_new_pos(board, roll_sum):
    board.rotate(-roll_sum)
    return board[0]
    
def play_det(boards):
    scores = {1: 0, 2: 0}
    dice = init_det_dice()
    rolls = 0
    finished = False
    while not finished:
        for p in [1, 2]:
            roll_sum = 0
            for _ in range(3):
                rolls += 1
                roll = roll_det_dice(dice)
                roll_sum += roll
            scores[p] += move_and_get_new_pos(boards[p], roll_sum)
            if max([score for score in scores.values()]) >= 1000:
                finished = True
                break
    return scores, rolls
               
def init_det_dice():
    return deque(range(1, 101))
            
def roll_det_dice(dice):
    roll = dice[0]
    dice.rotate(-1)
    return roll

@functools.lru_cache
def solve_quant(wins, p1, p2, s1, s2):
    pass
    
if __name__ == '__main__':
    main()