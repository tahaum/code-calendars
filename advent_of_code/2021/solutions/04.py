import input_utils as iu
import numpy as np

def main():
    path = '../data/04-1.txt'
    seq, boards, markers = load_data(path)
    results = dict()
    for marker_idx, marker in enumerate(markers):
        for n, val in enumerate(seq):
            marker = mark_board(boards[marker_idx], marker, val)
            if is_board_complete(marker):
                results[n] = calcuate_score(boards[marker_idx], marker, val)
                break
    print('Part 1:', results[min(results.keys())])
    print('Part 2:', results[max(results.keys())])
      
def load_data(path):
    data = iu.read_text_file_standard(path)
    seq = data[0].split(',')
    boards = list()
    for i in range(2, len(data), 6):
        board = data[i:i+5]
        board = [line.strip().replace('  ', ' ').split(' ') for line in board]
        boards.append(board)
    boards = np.array(boards)
    markers = np.zeros(boards.shape)
    return seq, boards, markers
          
def mark_board(board, markers, val):
    markers[board == val] = 1
    return markers
        
def is_board_complete(marker):
    row_sums = marker.sum(axis=0)
    col_sums = marker.sum(axis=1)
    sums = np.concatenate((row_sums, col_sums))
    if (sums == 5).any():
        return True
    else: 
        return False
    
def calcuate_score(board, marker, val):
    unmarked_sum = board[marker == 0].astype(int).sum()
    score = unmarked_sum * int(val)
    return score
        
if __name__ == '__main__':
    main()