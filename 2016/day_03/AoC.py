from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 3).example_data.splitlines()
        with open("./2016/day_03/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 3).input_data.splitlines()
    
    return [[int(side) for side in line.rstrip("\n").split()] for line in data]

def count_valid_triangles(triangles: list[list[int]]):
    valid_triangles = 0
    for triangle in triangles:
        sorted_triangles = sorted(triangle)
        if sum(sorted_triangles[:2]) > sorted_triangles[2]:
            valid_triangles += 1
    return valid_triangles

def count_valid_triangles_horizontal(triangles: list[list[int]]):
    valid_triangles = 0
    for i in range(0, len(triangles), 3):
        for j in range(len(triangles[i])):
            sorted_triangles = sorted([triangles[i][j], triangles[i+1][j], triangles[i+2][j]])
            if sum(sorted_triangles[:2]) > sorted_triangles[2]:
                valid_triangles += 1
    return valid_triangles


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    triangles = load_data(args.mode)
    total = count_valid_triangles(triangles)
    print(total)

    total = count_valid_triangles_horizontal(triangles)
    print(total)