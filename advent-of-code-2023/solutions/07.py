from utils import *
import pandas as pd

# Part 1
path = "../data/07.txt"
data = read_text_file_standard(path)
card_strengths = {c: i for i, c in enumerate("23456789TJQKA")}

def get_card_char_strengths(hand: str) -> list:
    return [card_strengths[c] for c in hand]

def get_hand_type(hand: str) -> int:
    hand_set = set(hand)
    if len(hand_set) == 1: # Five of a kind
        return 6
    elif len(hand_set) == 2: # Four of a kind og full house
        for ch in hand_set:
            if hand.count(ch) == 4 or hand.count(ch) == 1: # Four of a kind
                return 5
            else: # Full house
                return 4
    elif len(hand_set) == 3: # Three of a kind or two pairs
        types = list()
        for ch in hand_set:
            if hand.count(ch) == 3:
                types.append(3) # Three of a kind
            else:
                types.append(2) # Two pairs
        return max(types)
    elif len(hand_set) == 4: # One pair
        return 1
    else: # High card
        return 0
    
hands = dict()
for line in data:
    hand, bid = line.split()
    char_strengths = get_card_char_strengths(hand)
    hands[hand] = {"type": get_hand_type(hand), "bid": int(bid), **{f"ch_str_{i}": char_strengths[i] for i in range(5)}}

df = pd.DataFrame.from_dict(hands, orient="index")
df.sort_values(by=["type", "ch_str_0", "ch_str_1", "ch_str_2", "ch_str_3", "ch_str_4"], ascending=True, inplace=True)
df.reset_index(inplace=True)
df["rank"] = df.index + 1
df["winning"] = df["bid"] * df["rank"]

print("p1:", df.winning.sum())

# Part 2
path = "../data/07.txt"
data = read_text_file_standard(path)
card_strengths = {c: i for i, c in enumerate("J23456789TQKA")}

def find_optimal_joker_hand_type(hand: str) -> int:
    n_jokers = hand.count("J")
    cards = set(hand)
    best_type = 0
    for c in cards:
        test_hand = hand.replace("J", c)
        type_ = get_hand_type(test_hand)
        if type_ > best_type:
            best_type = type_
    return best_type

hands = dict()
for line in data:
    hand, bid = line.split()
    char_strengths = get_card_char_strengths(hand)
    if "J" in hand:
        type_ = find_optimal_joker_hand_type(hand)
    else:
        type_ = get_hand_type(hand)
    hands[hand] = {"type": type_, "bid": int(bid), **{f"ch_str_{i}": char_strengths[i] for i in range(5)}}

df = pd.DataFrame.from_dict(hands, orient="index")
df.sort_values(by=["type", "ch_str_0", "ch_str_1", "ch_str_2", "ch_str_3", "ch_str_4"], ascending=True, inplace=True)
df.reset_index(inplace=True)
df["rank"] = df.index + 1
df["winning"] = df["bid"] * df["rank"]

print("p2:", df.winning.sum())