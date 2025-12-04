import os
from argparse import ArgumentParser
from collections import Counter
from operator import mul

from aocd.models import Puzzle

SRC = os.path.dirname(__file__)


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2023, 1).example_data.splitlines()
        with open(f"{SRC}/test.txt") as file:
            data = [l.rstrip() for l in file.readlines()]
    else:
        data = Puzzle(2025, 2).input_data.splitlines()

    return data[0]


def process_id_ranges(raw_data: str):
    return [tuple(map(int, r.split("-"))) for r in raw_data.split(",")]


def find_invalid_ids(ranges: list[tuple[int]], part_2: bool = False):
    sum_ids = 0
    for a, b in ranges:
        sum_ids += sum(find_all_invalid_in_range(a, b, part_2))
    return sum_ids


def find_all_invalid_in_range(lower: int, upper: int, part_2: bool):
    invalids = []
    for n in range(lower, upper + 1):
        n_ = str(n)
        if not part_2 and len(n_) % 2 == 0:
            n_1, n_2 = n_[: len(n_) // 2], n_[len(n_) // 2 :]
            if n_1 == n_2:
                invalids.append(n)
        if part_2:
            v = Counter(n_).values()
            if all(c % 2 == 0 for c in v) or len(set(v)) == 1:
                divs = [
                    i
                    for i in range(1, len(n_) + 1)
                    if len(n_) % i == 0 and i != len(n_)
                ]
                for d in divs:
                    if "".join(n_[:d] * (len(n_) // d)) == n_:
                        invalids.append(n)
                        break
    return invalids


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = load_data(args.mode)
    _1 = find_invalid_ids(process_id_ranges(data))
    print(_1)
    _2 = find_invalid_ids(process_id_ranges(data), True)
    print(_2)
