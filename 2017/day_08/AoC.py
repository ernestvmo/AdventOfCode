from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 8).example_data.splitlines()
        # with open("./2017/day_08/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2017, 8).input_data.splitlines()

    data = [line.split(" if ") for line in data]
    registers = {line[0].split(" ")[0]: 0 for line in data}
    conditions = [line[1].replace(line[1].split(" ")[0], f'registers[\'{line[1].split(" ")[0]}\']') for line in data]
    operations = [line[0].split(" ") for line in data]
    operations = [[a, b, int(c)] for a, b, c in operations]

    return registers, operations, conditions

def handle_operations(registers: dict, operations: list, conditions: list):
    max_held = 0
    for operation, condition in zip(operations, conditions):
        if eval(condition):
            if operation[1] == "inc":
                registers[operation[0]] += operation[2]
            if operation[1] == "dec":
                registers[operation[0]] -= operation[2]
            max_held = max(max_held, registers[operation[0]])
    return registers, max_held


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    registers, operations, conditions = load_data(args.mode)
    handled_registers, max_held = handle_operations(registers, operations, conditions)
    print(max(handled_registers.values()))
    print(max_held)