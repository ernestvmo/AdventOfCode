from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 12).example_data.splitlines()
        # with open("./2017/day_12/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2017, 12).input_data.splitlines()

    return {int(line.split(" <-> ")[0]): [int(n) for n in line.split(" <-> ")[1].split(',')] for line in data}

def count_programs(programs: dict, searched_id: int = 0):
    nums = 0
    to_check = [searched_id]
    checked = []
    while len(to_check) != 0:
        id = to_check[0]
        for d in programs[id]:
            if d not in checked and d not in to_check:
                to_check.append(d)
        checked.append(id)
        to_check.remove(id)
    return checked

def count_groups(programs: dict):
    groups = []
    for id in programs.keys():
        group = sorted(count_programs(programs, id))
        if group not in groups:
            groups.append(group)
    return len(groups)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    directions = load_data(args.mode)
    group_zero = count_programs(directions)
    print(len(group_zero))

    num_of_groups = count_groups(directions)
    print(num_of_groups)
    