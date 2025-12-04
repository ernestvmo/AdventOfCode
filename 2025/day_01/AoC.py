from aocd.models import Puzzle
from argparse import ArgumentParser
import os

SRC = os.path.dirname(__file__)


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2023, 1).example_data.splitlines()
        with open(f"{SRC}/test.txt") as file:
            data = [l.rstrip() for l in file.readlines()]
    else:
        data = Puzzle(2025, 1).input_data.splitlines()

    return data


def process_rotation(value, direction, turns):
    if direction == "L":
        value -= turns % 100
        if value < 0:
            value = value + 100
    if direction == "R":
        value += turns % 100
        if value > 99:
            value = value - 100

    return value


def process_rotation_with_method(value, direction, turns, count=None):
    old = value
    count += abs(turns // 100)
    if direction == "L":
        value -= turns % 100
        if value < old and value <= 0 < old:
            count += 1
        value = (value + 100) % 100
    elif direction == "R":
        value += turns % 100
        if value > old and value >= 100 > old:
            count += 1
        value = (value - 100) % 100
    return value, count


def find_password(rotations, part_2=False):
    value = 50
    count = 0
    for i, rotation in enumerate(rotations):
        direction, turns = rotation[0], int(rotation[1:])
        if not part_2:
            value = process_rotation(value, direction, turns)
            if value == 0:
                count += 1
        else:
            value, count = process_rotation_with_method(value, direction, turns, count)
    return count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = load_data(args.mode)
    _1 = find_password(data)
    print(_1)
    _2 = find_password(data, True)
    print(_2)
