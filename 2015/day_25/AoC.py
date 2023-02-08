from aocd.models import Puzzle
from argparse import ArgumentParser
from re import findall
import numpy as np

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_25/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 25).input_data.splitlines()

    row, column = findall(r'\d+', data[0])
    return (int(row), int(column))

def infinite_grid(row: int, column: int):
    grid = np.zeros((max(row, column)*2-1, max(row, column)*2-1), dtype=int)

    # traverse grid
    i = j = 0
    last_row = 0
    last_value = 20151125
    grid[i][j] = last_value

    while True:
        if i != 0 or j != 0:
            grid[i][j] = (last_value * 252533) % 33554393
        
        if i == row-1 and j == column-1:
            return last_value

        if i == 0:
            j = 0
            i += last_row + 1
            last_row += 1
        else:
            i -= 1
            j += 1

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    row, column = load_data(args.mode)
    total = infinite_grid(row, column)
    print(total)