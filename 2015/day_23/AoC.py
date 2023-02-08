from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_23/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 23).input_data.splitlines()

    instructions = []
    for line in data:
        if ',' in line:
            line, jump = line.split(',')
            jump = int(jump.strip()[1:]) if jump.strip()[0] == '+' else int(jump.strip()[1:])*-1
            instruction, register = line.split()
            instructions.append([instruction, register, jump])
        else:
            instruction, register = line.split()
            instructions.append([instruction, register])
    return instructions

def find_value_of_register(instructions: list[list], registers={'a': 0, 'b': 0}, goal: str = 'b'):
    i = 0
    while i < len(instructions):
        instruction, register, *increment = instructions[i]
        if instruction == 'inc':
            registers[register] += 1
        elif instruction == 'tpl':
            registers[register] *= 3
        elif instruction == 'hlf':
            registers[register] //= 2
        elif instruction == 'jmp':
            i += (int(register)-1)
        elif instruction == 'jie' and registers[register] % 2 == 0:
            i += (increment[0]-1)
        elif instruction == 'jio' and registers[register] == 1:
            i += (increment[0]-1)
        i += 1
    return registers[goal]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    total = find_value_of_register(instructions, goal='b')
    print(total)

    total = find_value_of_register(instructions, goal='b', registers={'a': 1, 'b': 0})
    print(total)
