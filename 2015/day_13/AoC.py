from aocd.models import Puzzle
from argparse import ArgumentParser
import itertools

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2015, 13).example_data.splitlines()
    else:
        data = Puzzle(2015, 13).input_data.splitlines()

    happys = {}
    for line in data:
        splits = line.split()
        beneficiary, gain, target = splits[0], -1*int(splits[3]) if splits[2] == "lose" else int(splits[3]), splits[len(splits)-1].removesuffix('.')
        if beneficiary not in happys.keys():
            happys[beneficiary] = {target: gain}
        else:
            happys[beneficiary][target] = gain
    return happys

def find_happiest_table(happys: dict):
    people = list(set(happys.keys()))
    print(people)
    possibilities = list(itertools.permutations(people))
    max_happiness = 0
    for possibility in possibilities:
        table_happiness = 0
        for i in range(len(people)):
            if i < len(people)-1:
                j = i+1
            else:
                j = 0
            table_happiness += happys[possibility[i]][possibility[j]] + happys[possibility[j]][possibility[i]]
        max_happiness = max(max_happiness, table_happiness)
    return max_happiness

def add_self(happys: dict):
    for k in happys.keys():
        happys[k]['self'] = 0
    keys = happys.keys()
    happys['self'] = {k: 0 for k in keys}
    return happys


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    happys = load_data(args.mode)
    total = find_happiest_table(happys)
    print(total)

    total = find_happiest_table(add_self(happys))
    print(total)