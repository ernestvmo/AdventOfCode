import itertools
import os.path
import re

from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = [d.rstrip() for d in file.readlines()]
    else:
        data = Puzzle(2024, 7).input_data.splitlines()
    data = [
        [int(n[0]), list(map(int, n[1:]))] for n in [re.findall("\d+", d) for d in data]
    ]
    return data


def evaluate_valid_equations(equations: dict[int, list[int]], part_2: bool = False):
    totals = 0
    operators = ["*", "+"] if not part_2 else ["*", "+", "||"]
    for test_value, parameters in equations:
        for test in itertools.product(operators, repeat=len(parameters) - 1):
            equation_total = parameters[0]
            for i, j in zip(range(1, len(parameters)), test):
                if j == "*":
                    equation_total *= parameters[i]
                elif j == "+":
                    equation_total += parameters[i]
                elif j == "||":
                    equation_total = int(str(equation_total) + str(parameters[i]))
                # print(equation_total)
                if equation_total > test_value:
                    break
            if test_value == equation_total:
                totals += test_value
                break
    return totals


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = load_data(args.mode)
    res = evaluate_valid_equations(data)
    print(f"part 1: {res}")
    res = evaluate_valid_equations(data, True)
    print(f"part 2: {res}")
