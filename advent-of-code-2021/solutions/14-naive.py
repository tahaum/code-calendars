import input_utils as iu
from collections import Counter

def main():
    path = '../data/14-1.txt'
    template, rules = load_data(path)
    steps = 10
    for _ in range(steps):
        template = do_step(template, rules)
    counter = Counter(template)
    value_counts = counter.most_common()
    print(value_counts)
    print('Part 1:', value_counts[0][1] - value_counts[-1][1])

def load_data(path):
    data = iu.read_text_file_standard(path)
    template = data[0]
    rules = dict()
    for i in range(2, len(data)):
        pair, insert = data[i].split(' -> ')
        rules[pair] = insert
    return template, rules

def do_step(template, rules):
    new_template = list(template)
    chars_added = 0
    for i in range(len(template) - 1):
        current_pair = template[i:i+2]
        if current_pair in rules.keys():
            new_template.insert(i+1+chars_added, rules[current_pair])
            chars_added += 1
    new_template = ''.join(new_template)
    return new_template

if __name__ == '__main__':
    main()