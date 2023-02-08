from aocd.models import Puzzle
from argparse import ArgumentParser
import re
import numpy as np

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_06/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 6).input_data.splitlines()
    
    return [['toggle' if "toggle" in instruction else " ".join(instruction.rstrip('\n').split()[0:2]), [int(d) for d in re.findall(r'\d+', instruction.rstrip("\n"))]] for instruction in data]

def handle_lights(instructions: list):
    lights = np.zeros((1000, 1000), dtype=int)

    for instruction, coords in instructions:
        for i in range(coords[0], coords[2] + 1, 1):
            for j in range(coords[1], coords[3] + 1, 1):
                if instruction == "toggle":
                    # toggle
                    if lights[i][j] == 0:
                        lights[i][j] = 1
                    else:
                        lights[i][j] = 0
                elif instruction == "turn on":
                    # turn on
                    if lights[i][j] == 0:
                        lights[i][j] = 1
                else:
                    # turn off
                    if lights[i][j] == 1:
                        lights[i][j] = 0

    return np.sum(lights.flatten())


def handle_nordic_lights(instructions: list):
    lights = np.zeros((1000, 1000), dtype=int)

    for instruction, coords in instructions:
        for i in range(coords[0], coords[2] + 1, 1):
            for j in range(coords[1], coords[3] + 1, 1):
                if instruction == "toggle":
                    lights[i][j] += 2
                elif instruction == "turn on":
                    lights[i][j] += 1
                else:
                    # turn off
                    if lights[i][j] > 0:
                        lights[i][j] -= 1

    return np.sum(lights.flatten())


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    lights_on = handle_lights(instructions)
    print(lights_on)

    nordic_lights_on = handle_nordic_lights(instructions)
    print(nordic_lights_on)
    