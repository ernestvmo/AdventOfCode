from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 12).example_data.splitlines()
        with open("./2016/day_12/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 12).input_data.splitlines()

    return [line.rstrip("\n").split() for line in data]

def evaluate_registers(instructions: list, key='a', part=1):
    registers = {'a': 0, 'b': 0, 'c': 0 if part == 1 else 1, 'd': 0}
    i = 0
    while i < len(instructions):
        instruction, *rest = instructions[i]
        if instruction == 'cpy':
            if rest[0].isdigit():
                registers[rest[1]] = int(rest[0])
            else:
                registers[rest[1]] = registers[rest[0]]
        elif instruction == 'inc':
            registers[rest[0]] += 1
        elif instruction == 'dec':
            registers[rest[0]] -= 1
        else:
            if rest[0].isdigit() and rest[0] != '0':
                i += int(rest[1])-1
            elif not rest[0].isdigit() and registers[rest[0]] != 0:
                i += int(rest[1])-1
        i += 1
    return registers[key]

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    total = evaluate_registers(instructions)
    print(total)

    total = evaluate_registers(instructions, part=2)
    print(total)