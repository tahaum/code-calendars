from utils import *

def main():
    path = '../data/02-1.txt'
    data = read_text_file_standard(path)
    
    play_win = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
    play_even = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    play_scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    
    # Part 1
    tot_score = 0
    for match in data:
        opp, you = match[0], match[-1]
        if you == play_win[opp]:
            score = 6
        elif you == play_even[opp]:
            score = 3
        else:
            score = 0
        score += play_scores[you]
        tot_score += score
    print(tot_score)
    
        
    # Part 2
    play_lose = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
    def find_score_p2(opp, ins):
        if ins == 'X':
            score = play_scores[play_lose[opp]]
        elif ins == 'Y':
            score = 3 + play_scores[play_even[opp]]
        else:
            score = 6 + play_scores[play_win[opp]]
        return score
        
    tot_score = 0
    for match in data:
        opp, ins = match[0], match[-1]
        tot_score += find_score_p2(opp, ins)
    print(tot_score)
    
if __name__ == '__main__':
    main()