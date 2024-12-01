import input_utils as iu
from collections import Counter

def main():
    path = '../data/07-1.txt'
    crab_seq = load_data(path)
    fuel_use_per_pos = list()
    for pos in range(min(crab_seq), max(crab_seq) + 1):
        fuel_use = sum([abs(pos - crab_pos) for crab_pos in crab_seq])
        fuel_use_per_pos.append(fuel_use)
    cheapest_pos, fuel_used = min(enumerate(fuel_use_per_pos), key=lambda x: x[1])
    print(f'Part 1 - Positon: {cheapest_pos}, fuel used: {fuel_used}')
    
    fuel_use_per_pos = list()
    lookup = generate_fuel_use_part_2_lookup(crab_seq)
    for pos in range(min(crab_seq), max(crab_seq) + 1):
        fuel_use = sum([lookup[abs(pos - crab_pos)] for crab_pos in crab_seq])
        fuel_use_per_pos.append(fuel_use)
    cheapest_pos, fuel_used = min(enumerate(fuel_use_per_pos), key=lambda x: x[1])
    print(f'Part 2 - Positon: {cheapest_pos}, fuel used: {fuel_used}')
    
def load_data(path):
    data = iu.read_text_file_standard(path)
    crab_seq = [int(val) for val in data[0].split(',')]
    return crab_seq
    
def generate_fuel_use_part_2_lookup(crab_seq):
    lookup = [0]
    for pos in range(1, max(crab_seq) + 1):
        lookup.append(pos + lookup[pos - 1])
    return lookup

if __name__ == '__main__':
    main()