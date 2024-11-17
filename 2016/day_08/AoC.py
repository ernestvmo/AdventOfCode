from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 8).example_data.splitlines()
        with open("./2016/day_08/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 8).input_data.splitlines()

    instructions = []
    for line in data:
        line = line.rstrip("\n")
        parts = line.split()
        if parts[0] == 'rect':
            cols, rows = parts[1].split('x')
            instructions.append([parts[0], int(cols), int(rows)])
        else:
            instructions.append([parts[0], parts[2], int(parts[4])])
    return instructions
    
def display_screen(grid):
    print('-'*len(grid[0]))
    for row in grid:
        for cell in row:
            print(cell, sep='', end='')
        print()
    print('-'*len(grid[0]))

def count_activated_pixels(instructions: list[list]):
    screen = [['.' for _ in range(50)] for _ in range(6)]
    # screen = [['.' for _ in range(7)] for _ in range(3)]

    for instruction, *rest in instructions:
        if instruction == 'rect':
            cols, rows = rest
            for i in range(rows):
                for j in range(cols):
                    screen[i][j] = '#'
        else:
            axis, rotation = rest
            axis = axis.split('=')
            if axis[0] == 'x':
                row = [screen[i][int(axis[1])] for i in range(len(screen))]
                # if rotation >= len(screen):
                #     rotation %= len(screen)
                for _ in range(rotation):
                    row.insert(0, row.pop())
                for i in range(len(screen)):
                    screen[i][int(axis[1])] = row[i]
            else:
                # if rotation >= len(screen[int(axis[2])]):
                #     rotation %= len(screen[int(axis[2])])
                for _ in range(rotation):
                    screen[int(axis[1])].insert(0, screen[int(axis[1])].pop())
    display_screen(screen)
    # total = 0
    # for row in screen:
    #     for cell in row:
    #         if cell == '#':
    #             total += 1
    return np.sum(np.char.count(screen, '#'))



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    total = count_activated_pixels(instructions)
    print(total)