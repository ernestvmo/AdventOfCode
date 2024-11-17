from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np
import re


def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 19).example_data
        # with open("./2017/day_18/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2017, 19).input_data

    available_letters = set(re.findall(r"[A-Z]", data))
    data = data.splitlines()

    return np.array([list(line) for line in data]), (0, data[0].index("|")), available_letters

def next(grid: np.ndarray, curr: tuple, prev: list, letters: set):
    y, x = curr
    print(grid[y][x], y, x)
    if grid[y][x] == '|':
        n = [(y+yi, x) for yi in [-1, 1] if (y+yi, x) not in prev][0]
        if grid[n[0]][n[1]] == "-":
            return (curr[0] + ((n[0] - curr[0]) * 2), curr[1]), letters
        return n, letters
    elif grid[y][x] == '-':
        n = [(y, x+xi) for xi in [-1, 1] if (y, x+xi) not in prev][0]
        if grid[n[0]][n[1]] == "|":
            return (curr[0], curr[1] + ((n[1] - curr[1]) * 2)), letters
        return n, letters
    elif grid[y][x] == '+' or grid[y][x].isalpha():
        if grid[y][x].isalpha():
            letters.remove(grid[y][x])
            if len(letters) == 0: return (-1, -1), letters
        next_dir = []
        for yi in [-1, 1]:
            if 0 < y+yi < len(grid) and grid[y+yi][x] != " " and (y+yi, x) not in prev:
                next_dir.append((y+yi, x))
        for xi in [-1, 1]:
            if 0 < x+xi < len(grid[y]) and grid[y][x+xi] != " " and (y, x+xi) not in prev:
                next_dir.append((y, x+xi))
        return next_dir[0], letters
    else:
        ...


def path(grid: np.ndarray, start: tuple, available_letters: set):
    prev = [start]
    curr = (start[0] + 1, start[1])
    letters = available_letters.copy()
    traveled_letters = ""

    print(letters)

    while True:
        # print(prev, curr)
        next_, available_letters = next(grid, curr, prev, available_letters)
        prev.append(curr)
        curr = next_

        if len(letters) != len(available_letters):
            traveled_letters += f"{list(set(letters).difference(available_letters))[0]}"
            letters = available_letters.copy()
        print(traveled_letters)
        if next_ == (-1, -1): break
    print(traveled_letters)
        


if __name__ == "__main__":
    # parser = ArgumentParser()
    # parser.add_argument("mode", choices=['test', 'input'])
    # args = parser.parse_args()

    data, S, letters = load_data("test")
    path(data, S, letters)