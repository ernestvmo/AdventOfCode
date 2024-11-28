import os.path
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = file.read()
    else:
        data = Puzzle(2019, 2).input_data

    return [int(n) for n in data.split(",")]


def process_optcode(intcode_program: list[int], noun: int, verb: int) -> int:
    i = 0
    intcode_program[1] = noun
    intcode_program[2] = verb

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


def intcode(intcode_program: list[int]) -> (int, int):
    for noun in range(100):
        for verb in range(100):
            if process_optcode(intcode_program[:], noun, verb) == 19690720:
                return 100 * noun + verb


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    input_ = load_data(args.mode)
    res = process_optcode(input_[:], 12, 2)
    print(res)
    res = intcode(input_[:])
    print(res)
