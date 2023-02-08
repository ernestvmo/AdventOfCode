from aocd.models import Puzzle
from argparse import ArgumentParser
import itertools
import functools
import operator

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_24/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 24).input_data.splitlines()

    return [int(item.rstrip()) for item in data]

def subgroup(items: list[int], subgroups: int=3):
    group_size = sum(items) // subgroups
    for i in range(len(items)):
        sol = [functools.reduce(operator.mul, c) for c in itertools.combinations(items, i) if sum(c) == group_size]
        if sol:
            return min(sol)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    items = load_data(args.mode)
    total = subgroup(items)
    print(total)

    total = subgroup(items, 4)
    print(total)