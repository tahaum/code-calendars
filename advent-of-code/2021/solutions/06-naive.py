import input_utils as iu
import numpy as np

def main():
    path = '../data/06-1.txt'
    state = load_data(path)
    days = 80
    state = simulate_fish_growth(state, days)
    print('Part 1:', len(state))
    
    state = load_data(path)
    days = 256
    state = simulate_fish_growth(state, days)
    print('Part 2:', len(state))
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    state = np.array([int(val) for val in data[0].split(',')])
    return state

def simulate_fish_growth(state, days):
    for _ in range(days):
        if any_zeros:
            state = spawn_and_reset(state)
        state = subtract_from_timers(state)
    return state    
    
def subtract_from_timers(state):
    return state - 1

def any_zeros(state):
    if (state == 0).any():
        return True

def spawn_and_reset(state):
    spawn_count = count_zeros(state)
    state = spawn_fish(state, spawn_count)
    state = reset_timers(state)
    return state
 
def count_zeros(state):
    return len(state[state == 0])

def spawn_fish(state, count):
    return np.append(state, [9]*count)

def reset_timers(state):
    state[state == 0] = 7
    return state

if __name__ == '__main__':
    main()