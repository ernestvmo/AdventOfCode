from aocd.models import Puzzle
from argparse import ArgumentParser
from collections import Counter

card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
card_values_ = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
hands_values = {(1,1,1,1,1): 1, (1,1,1,2): 2, (1,2,2): 3, (1,1,3): 4, (2,3): 5, (1,4): 6, (5,): 7,}

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2023, 7).example_data.splitlines()
    else:
        data = Puzzle(2023, 7).input_data.splitlines()
    data = {line.split(" ")[0]: int(line.split(" ")[1]) for line in data}
    return data

def get_highest_card(hand: dict):
    return max([card_values[n] for n in hand.keys() if hand[n]  == 1])

def hand_to_value(hand: str, q=1):
    if q == 1:
        return [card_values[c] for c in hand]
    else:
        return [card_values_[c] for c in hand]

def value_to_hand(values: list[int], q=1):
    if q ==1: value_cards = {v: k for k, v in card_values.items()}
    else: value_cards = {v: k for k, v in card_values_.items()}
    return "".join(value_cards[n] for n in values)

def count_hands(player_hands: list[tuple[str, int]]):
    hands_sorted = {k: [] for k in hands_values.keys()}
    for hand in player_hands:
        c = Counter(hand)
        k = tuple(sorted(Counter(hand).values()))
        hands_sorted[k].append(hand_to_value(hand))
        hands_sorted[k].sort()
    sorted_list = []
    for values in hands_sorted.values():
        for value in values:
            sorted_list.append(player_hands[value_to_hand(value)])
    return sum([(i+1)*v for i, v in enumerate(sorted_list)])

def count_hands_q2(player_hands: dict[str, int]):
    hands_sorted = {k: [] for k in hands_values.keys()}
    for hand in player_hands:
        if "J" in hand:
            c = Counter(hand.replace("J", ""))
            if hand == "J"*5:
                hand_no_jokers = "AAAAA"
            else:
                J_replace = sorted(c, key=c.get)[::-1][0]
                hand_no_jokers = hand.replace("J", J_replace)
            k = tuple(sorted(Counter(hand_no_jokers).values()))
        else:
            c = Counter(hand)
            k = tuple(sorted(c.values()))
        hands_sorted[k].append(hand_to_value(hand, 2))
        hands_sorted[k].sort()
    sorted_list = []
    for values in hands_sorted.values():
        for value in values:
            sorted_list.append(player_hands[value_to_hand(value, 2)])
            # sorted_list.append(value_to_hand(value, 2))
    return sum([(i+1)*v for i, v in enumerate(sorted_list)])

        



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    n = count_hands(data)
    print(n)

    n = count_hands_q2(data)
    print(n)