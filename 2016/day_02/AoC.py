from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 2).example_data.splitlines()
        with open("./2016/day_02/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 2).input_data.splitlines()
    
    return [[c for c in line.rstrip("\n")] for line in data]

def find_digicode(instructions: list[list[str]]):
    keypad = np.arange(1, 10).reshape((3, 3))
    starting = [1,1]
    pos = starting[:]
    digicode = ''
    for instruction in instructions:
        for direction in instruction:
            if direction == 'U':
                pos[0] = max(0, pos[0] - 1)
            elif direction == 'D':
                pos[0] = min(2, pos[0] + 1)
            elif direction == 'L':
                pos[1] = max(0, pos[1] - 1)
            elif direction == 'R':
                pos[1] = min(2, pos[1] + 1)
        digicode = digicode + str(keypad[pos[0]][pos[1]])
    return digicode

def find_complex_digicode(instructions: list[list[str]]):
    keypad =         [['1'], 
                 ['2', '3', '4'], 
            ['5', '6', '7', '8', '9'],
                 ['A', 'B', 'C'],
                      ['D']]
    starting = [2,0]
    pos = starting[:]
    digicode = ''
    for instruction in instructions:
        for direction in instruction:
            if direction == 'U':
                if pos[0] - 1 >= 0:
                    if len(keypad[pos[0]]) < len(keypad[pos[0]-1]):
                        pos[0] -= 1
                        pos[1] += 1
                    else:
                        if pos[1] != 0 and pos[1] <= len(keypad[pos[0]-1]):
                            pos[0] -= 1
                            pos[1] -= 1
                else:
                    pos[0] = 0
            elif direction == 'D':
                if pos[0] + 1 < len(keypad):
                    if len(keypad[pos[0]]) < len(keypad[pos[0]+1]):
                        pos[0] += 1
                        pos[1] += 1
                    else:
                        if pos[1] != 0 and pos[1] <= len(keypad[pos[0]+1]):
                            pos[0] += 1
                            pos[1] -= 1
                else:
                    pos[0] = len(keypad) - 1
                # pos[0] = min(5, pos[0] + 1)
            elif direction == 'L':
                pos[1] = max(0, pos[1] - 1)
            elif direction == 'R':
                pos[1] = min(len(keypad[pos[0]]) - 1, pos[1] + 1)
        digicode = digicode + str(keypad[pos[0]][pos[1]])
    return digicode

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    total = find_digicode(instructions)
    print(total)

    total = find_complex_digicode(instructions)
    print(total)