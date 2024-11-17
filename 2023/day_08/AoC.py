from aocd.models import Puzzle
from argparse import ArgumentParser
from re import findall


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2023, 8).example_data.splitlines()
        with open("./2023/day_08/test.txt") as file:
            data = file.readlines()
            data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 8).input_data.splitlines()
    instructions = [c for c in data[0]]
    maps = {}
    for line in data[2:]:
        node, *elements = findall(r"[A-Z]{3}", line)
        maps[node] = elements
    return instructions, maps

def follow_path(instructions, maps):
    curr = "AAA"
    end = "ZZZ"
    i = 0
    steps = []
    while curr != end:
        dir = 0 if instructions[i] == "L" else 1
        curr = maps[curr][dir]
        steps.append(curr)
        i += 1
        if i == len(instructions):
            i = 0
    return len(steps)

def follow_ghost_path(instructions, maps: dict[str, tuple]):
    currs = [n for n in maps.keys() if n.endswith("A")]
    end = "ZZZ"
    i = 0
    steps = []
    while True:
        for j in range(len(currs)):
            dir = 0 if instructions[i] == "L" else 1
            currs[j] = maps[currs[j]][dir]
        steps.append(currs)
        i += 1
        if i == len(instructions):
            i = 0
        if all([n.endswith("Z") for n in currs]):
            return len(steps)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions, maps = load_data(args.mode)
    # n = follow_path(instructions, maps)
    # print(n)

    n = follow_ghost_path(instructions, maps)
    print(n)