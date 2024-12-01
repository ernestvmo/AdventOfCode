import os.path
import re
from collections import Counter
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = file.readlines()
    else:
        data = Puzzle(2024, 1).input_data.splitlines()
    processed_data = [re.findall(r"\d+", n.rstrip()) for n in data]
    return [int(n[0]) for n in processed_data], [int(n[1]) for n in processed_data]


def part_1(list_1: list[int], list_2: list[int]) -> int:
    distance = 0
    for i, j in zip(sorted(list_1), sorted(list_2)):
        distance += abs(i - j)
    return distance


def part_2(list_1: list[int], list_2: list[int]) -> int:
    c = Counter(list_2)
    distance = 0
    for i in list_1:
        distance += i * c[i]
    return distance


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    list_1, list_2 = load_data(args.mode)
    res = part_1(list_1=list_1, list_2=list_2)
    print(f"part 1: {res}")
    res = part_2(list_1=list_1, list_2=list_2)
    print(f"part 2: {res}")
