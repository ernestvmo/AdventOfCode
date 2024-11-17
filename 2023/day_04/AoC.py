from aocd.models import Puzzle
from argparse import ArgumentParser
from re import findall
from math import floor

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2023, 4).example_data.splitlines()
        # with open("./2023/day_04/test.txt") as file:
        #     data = file.readlines()
        #     data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 4).input_data.splitlines()

    return data

def solve(data, q: str):
    total = 0
    cards = {i: 1 for i in range(len(data))}
    for i, line in enumerate(data):
        _, numbers = line.rstrip().split(":")
        winning_numbers, numbers = numbers.split("|")
        winning_numbers = set([int(n) for n in findall(r"\d+", winning_numbers)])
        numbers = set([int(n) for n in findall(r"\d+", numbers)])
        winnings = len(numbers.intersection(winning_numbers))
        if q == "1":
            total += floor(2**(winnings-1))
        else:
            for j in range(1, winnings+1):
                cards[i+j] += cards[i]
    
    return total if q == "1" else sum(cards.values())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    n = solve(data, "1")
    print(n)

    n = solve(data, "2")
    print(n)