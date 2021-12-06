import input_utils as iu
from collections import Counter

def main():
    path = '../data/06-1.txt'
    state = load_data(path)
    state = simulate_fish_growth(state, 80)
    print('Part 1:', sum(state.values()))
    
    state = load_data(path)
    state = simulate_fish_growth(state, 256)
    print('Part 2:', sum(state.values()))
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    state = Counter([int(val) for val in data[0].split(',')])
    return state

def simulate_fish_growth(state, days):
    for _ in range(days):
        n_spawn = state[0]
        for v in range(8):
            state[v] = state[v + 1]
        state[8] = n_spawn
        state[6] += n_spawn
    return state    
 
if __name__ == '__main__':
    main()