from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np
import pprint

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 1).example_data.splitlines()
        with open("./2016/day_01/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 1).input_data.splitlines()
    
    return [d.strip() for d in data[0].split(',')]

def turn(facing: str, turning: str):
    right = ['N', 'E', 'S', 'W']
    left = ['N', 'W', 'S', 'E']

    if turning == 'L':
        if left.index(facing) + 1 == len(right):
            return left[0]
        else:
            return left[left.index(facing) + 1]
    else:
        # return right[0]
        if right.index(facing) + 1 == len(right):
            return right[0]
        else:
            return right[right.index(facing) + 1]

def display(grid):
    print('-'*100)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[j][i], sep='', end='')
        print()
    print('-'*100)

def move_on_grid(instructions: list[str]):
    facing = 'N'
    pos, start = [0,0], [0,0]
    for instruction in instructions:
        # print('start', facing, pos)
        direction, distance = instruction[0], instruction[1:]
        # print(direction, distance)
        facing = turn(facing, direction)
        if facing == 'E':
            pos[0] += int(distance)
        elif facing == 'W':
            pos[0] -= int(distance)
        elif facing == 'N':
            pos[1] += int(distance)
        elif facing == 'S':
            pos[1] -= int(distance)
        # print('end', facing, pos)
    print(pos)
    return sum(pos)
    # return abs(sum(pos))-1 if 0 not in pos else abs(sum(pos))

 

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    total = move_on_grid(instructions)
    print(total)