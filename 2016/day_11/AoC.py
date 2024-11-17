from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2016, 11).example_data.splitlines()
        # with open("./2016/day_11/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2016, 11).input_data.splitlines()

    print(data)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    bots = load_data(args.mode)
    total = ...
    print(total)