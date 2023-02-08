from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    tape = Puzzle(2015, 16).example_data.splitlines()
    if mode == "test":
        with open('./2015/day_16/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 16).input_data.splitlines()

    ticker_tape = {}
    for item in tape:
        attribute, value = item.split(":")
        ticker_tape[attribute] = int(value)

    Sues = {}
    for line in data:
        line = line.rstrip("\n")
        name, line = line[:line.index(":")], line[line.index(":"):].replace(":", "").split(",")
        Sue = {}
        for elem in line:
            attribute, value = elem.strip().split()
            Sue[attribute] = int(value)
        Sues[name] = Sue
    
    return ticker_tape, Sues

def find_aunt(ticker_tape: dict, Sues: dict[dict]):
    potential_aunts = []
    for Sue in Sues:
        valid = True
        for attribute, value in Sues[Sue].items():
            if ticker_tape[attribute] != value:
                valid = False
        if valid:
            potential_aunts.append(Sue)

    if len(potential_aunts) == 1:
        return potential_aunts[0]
    else:
        raise ValueError("More than one aunt found")

def find_aunt_retroencabulator(ticker_tape: dict, Sues: dict[dict]):
    potential_aunts = []
    for Sue in Sues:
        valid = True
        for attribute, value in Sues[Sue].items():
            if attribute == "cats" or attribute == "trees":
                if ticker_tape[attribute] >= value:
                    valid = False
            elif attribute == "pomeranians" or attribute == "goldfish":
                if ticker_tape[attribute] <= value:
                    valid = False
            else:
                if ticker_tape[attribute] != value:
                    valid = False
        if valid:
            potential_aunts.append(Sue)

    if len(potential_aunts) == 1:
        return potential_aunts[0]
    else:
        print(potential_aunts)
        raise ValueError("More than one aunt found")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    ticker_tape, Sues = load_data(args.mode)
    aunt = find_aunt(ticker_tape, Sues)
    print(aunt)

    aunt = find_aunt_retroencabulator(ticker_tape, Sues)
    print(aunt)