from aocd.models import Puzzle
from argparse import ArgumentParser
import re

def load_data(mode: str):
    if mode == "test":
        with open("./2015/day_12/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 12).input_data.splitlines()

    return data[0]

def sum_numbers(input: str):
    numbers = re.findall(r'[-+]?\d+', input)
    numbers = [int(n) for n in numbers]
    return sum(numbers)

def explore_dict(nested_dict):
    if isinstance(nested_dict, dict):
        if "red" in nested_dict.values():
            return 0
        return sum(map(explore_dict, nested_dict.values()))

    if isinstance(nested_dict, list):
        return sum(map(explore_dict, nested_dict))
    
    if isinstance(nested_dict, int):
        return nested_dict

    return 0

def ignore_red(input: str):
    input = eval(input)
    sum_numbers = explore_dict(input)
    return sum_numbers


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    input = load_data(args.mode)
    total = sum_numbers(input)
    print(total)

    total = ignore_red(input)
    print(total)