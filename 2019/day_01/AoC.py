import os.path
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1)#.example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = [n.rstrip() for n in file.readlines()]
    else:
        data = Puzzle(2019, 1).input_data.splitlines()

    return data


def counter_upper(aoc_input: list[str]) -> int:
    return sum((int(n) // 3) - 2 for n in aoc_input)


def counter_rudder_recursion(num: int, list_: list) -> list[int]:
    a = (int(num) // 3) - 2
    if a <= 0:
        return list_
    else:
        list_.append(a)
        return counter_rudder_recursion(a, list_)


def part_2(aoc_input: list[str]) -> int:
    return sum([sum(counter_rudder_recursion(int(n), [])) for n in aoc_input])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    input_ = load_data(args.mode)
    res = counter_upper(input_)
    print(res)
    res = part_2(input_)
    print(res)
