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
        data = Puzzle(2025, 4).input_data.splitlines()

    return data


def preprocess(toilet_paper_map: list[str]):
    return [list(tp.rstrip()) for tp in toilet_paper_map]


def count_removable(tp: list[list[str]]):
    tps = []
    for r, row in enumerate(tp):
        for c, col in enumerate(row):
            if tp[r][c] == "@" and find_neighbours(tp, r, c):
                tps.append((r, c))
    return tps


def find_neighbours(tp_map: list[list[str]], r: int, c: int):
    neighbours = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            if (
                0 <= r + i < len(tp_map)
                and 0 <= c + j < len(tp_map[0])
                and tp_map[r + i][c + j] == "@"
            ):
                neighbours += 1
    return neighbours < 4


def remove_all_removables(tp: list[list[str]]):
    def remove(removables: list[tuple[int]]):
        for r, c in removables:
            tp[r][c] = "."

    count = 0
    while True:
        removable_tp = count_removable(tp)
        if len(removable_tp) != 0:
            count += len(removable_tp)
            remove(removable_tp)
        else:
            return count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = preprocess(load_data(args.mode))
    _1 = len(count_removable(data))
    print(_1)
    _2 = remove_all_removables(data)
    print(_2)
