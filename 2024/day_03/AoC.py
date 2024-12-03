import os.path
import re
from collections import Counter
from gc import enable

from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2024, 3).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = file.readlines()
    else:
        data = Puzzle(2024, 3).input_data.splitlines()
    return "".join(data)


def extra_valid_multiplications(data: str, part_2: bool = False):
    if not part_2:
        return re.findall(r"mul\(\d*\,\d*\)", data)
    else:
        operations = re.findall(r"mul\(\d*\,\d*\)|do\(\)|don\'t\(\)", data)
        new_operations = []
        enabled = True
        for operation in operations:
            if operation == "don't()":
                enabled = False
            elif operation == "do()":
                enabled = True
            elif enabled:
                new_operations.append(operation)
        return new_operations


def mul(x, y):
    return x * y


def process_operations(operations: list[str]):
    return sum(eval(o) for o in operations)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    a = load_data(args.mode)
    res = process_operations(extra_valid_multiplications(a))
    print(f"part 1: {res}")
    res = process_operations(extra_valid_multiplications(a, part_2=True))
    print(f"part 1: {res}")
