import os
from argparse import ArgumentParser
from collections import Counter
from operator import mul

from aocd.models import Puzzle

SRC = os.path.dirname(__file__)


def load_data(mode: str):
    if mode == "test":
        with open(f"{SRC}/test.txt") as file:
            data = [l.rstrip() for l in file.readlines()]
    else:
        data = Puzzle(2025, 3).input_data.splitlines()

    return data


def find_max_joltage(bank: str, n_banks: int = 1):
    def find_max(bank_int):
        return max(bank_int)

    banks = ""
    last_index = 0
    for i in range(n_banks - 1, -1, -1):
        if i == 0:
            banks_int = list(map(int, list(bank[last_index:])))
        else:
            banks_int = list(map(int, list(bank[last_index:-i])))
        d = find_max(banks_int)
        banks += str(d)
        last_index += banks_int.index(d) + 1
    return int(banks)


def total_optimal(banks: list[str], n_batteries: int = 2):
    output_joltage = 0
    for bank in banks:
        o = find_max_joltage(bank, n_batteries)
        output_joltage += o
    return output_joltage


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = load_data(args.mode)
    _1 = total_optimal(data)
    print(_1)
    _2 = total_optimal(data, n_batteries=12)
    print(_2)
