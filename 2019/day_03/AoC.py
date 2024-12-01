import os.path

import numpy as np

from aocd.models import Puzzle
from argparse import ArgumentParser

from scipy.spatial.distance import cityblock
from skspatial.objects import LineSegment


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1)#.example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = [n.rstrip() for n in file.readlines()]
    else:
        data = Puzzle(2019, 3).input_data.splitlines()

    return [n.split(",") for n in data]


def instruction_as_points(instruction: list[str]):
    pos = [0, 0]
    points = []
    for i in instruction:
        next_pos = None
        if i[0] == "R":
            next_pos = [pos[0] + int(i[1:]), pos[1]]
        if i[0] == "L":
            next_pos = [pos[0] - int(i[1:]), pos[1]]
        if i[0] == "U":
            next_pos = [pos[0], pos[1] + int(i[1:])]
        if i[0] == "D":
            next_pos = [pos[0], pos[1] - int(i[1:])]
        points.append([pos, next_pos])
        pos = next_pos
    return points


def find_segments_intersections(instructions_as_points: list[list[list[int]]]):
    a_, b_ = instructions_as_points[0], instructions_as_points[1]
    min_distance = float("inf")
    for a in a_:
        for b in b_:
            try:
                l1 = LineSegment(a[0], a[1])
                l2 = LineSegment(b[0], b[1])
                intersect = l1.intersect_line_segment(l2)
                if not np.array_equal(intersect, np.array([0, 0])):
                    min_distance = min(min_distance, cityblock(intersect, [0, 0]))
            except ValueError:
                pass
    return int(min_distance)


def minimize_delay(instruction: list[str]):
    pos = [0, 0]
    points = []
    for step in instruction:
        if step[0] == "R":
            points += [[pos[0] + n, pos[1]] for n in range(1, int(step[1:]) + 1)]
            pos = [pos[0] + int(step[1:]), pos[1]]
        if step[0] == "L":
            points += [
                [pos[0] + n, pos[1]] for n in range(-1, -(int(step[1:]) + 1), -1)
            ]
            pos = [pos[0] - int(step[1:]), pos[1]]
        if step[0] == "U":
            points += [[pos[0], pos[1] + n] for n in range(1, int(step[1:]) + 1)]
            pos = [pos[0], pos[1] + int(step[1:])]
        if step[0] == "D":
            points += [
                [pos[0], pos[1] + n] for n in range(-1, -(int(step[1:]) + 1), -1)
            ]
            pos = [pos[0], pos[1] - int(step[1:])]
    return points


def part_2(instructions: list[list[str]]):
    points = [minimize_delay(instruction) for instruction in instructions]
    instruction_1, instruction_2 = points[0], points[1]
    intersections = []
    min_lasso_1, min_lasso_2 = float("inf"), float("inf")
    for a in instruction_1:
        for b in instruction_2:
            if a[0] == b[0] and a[1] == b[1]:
                min_lasso_1 = min(
                    min_lasso_1, instruction_1.index(a) + 1 + instruction_2.index(b) + 1
                )
                continue
    for b in instruction_2:
        for a in instruction_1:
            if a[0] == b[0] and a[1] == b[1]:
                min_lasso_2 = min(
                    min_lasso_2, instruction_1.index(a) + 1 + instruction_2.index(b) + 1
                )
                continue
    return min(min_lasso_1, min_lasso_2)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    res = find_segments_intersections([instruction_as_points(n) for n in instructions])
    print(f"part 1: {res}")
    res = part_2(instructions)
    print(f"part 2: {res}")
