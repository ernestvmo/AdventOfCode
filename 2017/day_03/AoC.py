from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 3).example_data.splitlines()
        with open("./2017/day_03/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 3).input_data.splitlines()

    return int(data[0])

def build_traversal(input: int):
    completed_circles = 0
    circle_sequence = ""
    while len(circle_sequence) < input:
        circle_sequence += "RU"+"UU"*completed_circles\
                +"LL"+"LL"*completed_circles\
                +"DD"+"DD"*completed_circles\
                +"RR"+"RR"*completed_circles
        completed_circles += 1
    move_sequence = circle_sequence[:input-1]

    L_c, R_c = move_sequence.count("L"), move_sequence.count("R")
    D_c, U_c = move_sequence.count("D"), move_sequence.count("U")

    steps = (max(L_c, R_c) - min(L_c, R_c)) + (max(U_c, D_c) - min(U_c, D_c))
    return steps, np.zeros((50, 50)), move_sequence

def traversal_squared(map: np.ndarray, move_sequence: str, input: int):
    curr_pos_y, curr_pos_x = len(map)//2, len(map[0])//2
    map[curr_pos_y][curr_pos_x] = 1
    for c in move_sequence:
        if c == "R":
            curr_pos_x += 1
        if c == "L":
            curr_pos_x -= 1
        if c == "D":
            curr_pos_y += 1
        if c == "U":
            curr_pos_y -= 1
        neigh_vals = neighbour_boxes(curr_pos_x, curr_pos_y, map)
        map[curr_pos_y][curr_pos_x] = neigh_vals
        if neigh_vals > input:
            return int(neigh_vals)

def neighbour_boxes(x: int, y: int, map: np.ndarray):
    sum = 0
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if x + r >= 0 and x + r < len(map) and y + c >= 0 and y + c < len(map[0]):
                if not (r == 0 and c == 0):
                    sum += map[y+c][x+r]
    return sum


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    input = load_data(args.mode)
    steps, map, move = build_traversal(input)
    print(steps)
    traversal_val = traversal_squared(map, move, input)
    print(traversal_val)