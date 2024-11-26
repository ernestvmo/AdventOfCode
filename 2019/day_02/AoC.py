import os.path
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1)#.example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = file.read()
    else:
        data = Puzzle(2019, 2).input_data

    return [int(n) for n in data.split(",")]


def process_optcode(intcode_program: list[int]) -> int:
    i = 0
    intcode_program[1] = 12
    intcode_program[2] = 2

    while True:
        if intcode_program[i] == 1:
            intcode_program[intcode_program[i + 3]] = (
                intcode_program[intcode_program[i + 1]]
                + intcode_program[intcode_program[i + 2]]
            )
            i += 4
        elif intcode_program[i] == 2:
            intcode_program[intcode_program[i + 3]] = (
                intcode_program[intcode_program[i + 1]]
                * intcode_program[intcode_program[i + 2]]
            )
            i += 4
        elif intcode_program[i] == 99:
            return intcode_program[0]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    input_ = load_data(args.mode)
    res = process_optcode(input_)
    print(res)
