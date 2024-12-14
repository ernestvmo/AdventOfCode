import os.path
import re
from collections import Counter
from itertools import combinations

import numpy as np
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = [d.rstrip() for d in file.readlines()]
    else:
        data = Puzzle(2024, 8).input_data.splitlines()

    return np.array([list(d) for d in data], dtype=str)


def is_valid_antinode(antinode: np.ndarray[int], map: np.ndarray[str]):
    if 0 <= antinode[0] < len(map) and 0 <= antinode[1] < len(map[0]):
        return True
    else:
        return False


def calculate_antinodes(data: np.ndarray[str]):
    unique_signals = np.unique(data)[np.where(np.unique(data) != ".")]
    antinodes = []
    for signal in unique_signals:
        signals = np.argwhere(data == signal)
        for combination in combinations(signals, 2):
            antinode_1 = combination[0] + (combination[0] - combination[1])
            if is_valid_antinode(antinode_1, data):
                antinodes.append(antinode_1)
            antinode_2 = combination[1] - (combination[0] - combination[1])
            if is_valid_antinode(antinode_2, data):
                antinodes.append(antinode_2)
    return len([list(x) for x in set(tuple(x) for x in antinodes)])


def calculate_antinodes_resonants(data: np.ndarray[str]):
    print(data)
    unique_signals = np.unique(data)[np.where(np.unique(data) != ".")]
    for signal in unique_signals:
        signals = np.argwhere(data == signal)
        for combination in combinations(signals, 2):
            a_1 = combination[0]
            a_2 = combination[1]
            count = 1
            while True:
                a_3 = a_2 - count * (a_1 - a_2)
                if is_valid_antinode(a_3, data):
                    count += 1
                    if data[a_3[0]][a_3[1]] == ".":
                        data[a_3[0]][a_3[1]] = data[combination[0][0]][
                            combination[0][1]
                        ]
                else:
                    break
            count = 1
            while True:
                a_3 = a_1 - count * (a_2 - a_1)
                if is_valid_antinode(a_3, data):
                    count += 1
                    if data[a_3[0]][a_3[1]] == ".":
                        data[a_3[0]][a_3[1]] = data[combination[0][0]][
                            combination[0][1]
                        ]
                else:
                    break
    return np.sum(data != ".")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = load_data(args.mode)
    res = calculate_antinodes(data[:])
    print(f"part 1: {res}")
    res = calculate_antinodes_resonants(data[:])
    print(np.savetxt("input.res.text", data, fmt="%s"))
    print(f"part 2: {res}")
