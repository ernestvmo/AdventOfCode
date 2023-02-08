from aocd.models import Puzzle
from argparse import ArgumentParser
import itertools

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_17/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 17).input_data.splitlines()

    return [int(container.rstrip("\n")) for container in data]

def fill_containers(containers: list[int], size=150):
    pairs = [(0,pair) for pair in containers]
    combinations = [combo for combo in itertools.product(*pairs) if sum(combo) == size]
    return combinations

def minimum_of_containers(combinations: list[tuple]):
    minimum = len(combinations[0])
    minimums = []
    for combination in combinations:
        minimums.append(min(minimum, len(combination)-combination.count(0)))
    return minimums.count(min(minimums))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    containers = load_data(args.mode)
    combinations = fill_containers(containers)
    print(len(combinations))

    minimum = minimum_of_containers(combinations)
    print(minimum)