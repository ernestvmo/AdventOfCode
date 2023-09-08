from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 5).example_data.splitlines()
        # with open("./2017/day_05/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2017, 5).input_data.splitlines()

    return [int(elem) for elem in data]

def handle_instructions_1(instructions: list[int]):
    curr = count = 0
    while True:
        next = curr + instructions[curr]
        instructions[curr] += 1
        count += 1

        if next >= len(instructions): 
            break
        else: 
            curr = next
    return count

def handle_instructions_2(instructions: list[int]):
    curr = count = 0
    while True:
        next = curr + instructions[curr]
        if instructions[curr] >= 3:
            instructions[curr] -= 1
        else:
            instructions[curr] += 1
        count += 1

        if next >= len(instructions): 
            break
        else: 
            curr = next
    return count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    count = handle_instructions_1(instructions[:])
    print(count)

    count = handle_instructions_2(instructions[:])
    print(count)