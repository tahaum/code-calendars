from utils import *
from collections import defaultdict

# Part 1
path = "../data/04.txt"
data = read_text_file_standard(path)
sum_ = 0
for line in data:
    w, c = line.split("|")
    _, w = w.split(":")
    winning_cards = [int(x) for x in w.split()]
    cards = [int(x) for x in c.split()]
    n_wins = len(set(winning_cards).intersection(set(cards)))
    if n_wins > 0:
        p = 2**(n_wins - 1)
        sum_ += p

print("p1:", sum_)

# Part 2
path = "../data/04.txt"
data = read_text_file_standard(path)
sum_ = 0
sc = defaultdict(int)
for line in data:
    w, c = line.split("|")
    cn, w = w.split(":")
    cn = int(cn.split()[1])
    winning_cards = set([int(x) for x in w.split()])
    cards = set([int(x) for x in c.split()])
    n_wins = len(winning_cards.intersection(cards))
    print(winning_cards, cards, n_wins)
    sc[cn] += 1
    if n_wins > 0:
        for i in range(cn+1, cn+n_wins+1):
            sc[i] += sc[cn]

print("p2:", sc, sum(sc.values()))