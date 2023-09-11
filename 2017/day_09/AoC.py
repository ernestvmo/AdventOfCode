from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 9).example_data.splitlines()
        with open("./2017/day_09/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 9).input_data.splitlines()

    return data[0]

def preprocess_data(data: str):
    while "!" in data:
        i = data.index("!")
        data = data[:i] + data[i+2:]
    return data

def treat(data: str):
    opened_group = []
    group_count = 0
    garbage_mode = False
    garbage_count = 0
    for i in range(len(data)):
        if garbage_mode:
            if data[i] == ">":
                garbage_mode = False
            else:
                garbage_count += 1
        if not garbage_mode:
            if data[i] == "<":
                garbage_mode = True
            if data[i] == "{":
                opened_group.append(i)
            if data[i] == "}":
                opened_group.pop()
                group_count += 1 + len(opened_group)
    return group_count, garbage_count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    data = preprocess_data(data)
    q1, q2 = treat(data)
    print(q1)
    print(q2)