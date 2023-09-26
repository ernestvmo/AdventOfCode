from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 11).example_data.splitlines()
        with open("./2017/day_11/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 11).input_data.splitlines()

    return data[0].split(",")

def handle_directions(directions: list[str]):
    q, r, s = 0, 0, 0
    max_reached = 0

    for d in directions:
        if d == 'n':
            r -= 1
            s += 1
        elif d == 's':
            r += 1
            s -= 1
        elif d == 'nw':
            q -= 1
            s += 1 
        elif d == 'ne':
            q += 1
            r -= 1
        elif d == 'sw':
            q -= 1
            r += 1
        elif d == 'se':
            q += 1
            s -= 1
        max_reached = max(max_reached, max(abs(q), abs(s), abs(r)))
    return max(abs(q), abs(s), abs(r)), max_reached


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    directions = load_data(args.mode)
    distance, max_reached = handle_directions(directions)
    print(distance)
    print(max_reached)
    