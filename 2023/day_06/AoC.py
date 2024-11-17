from aocd.models import Puzzle
from argparse import ArgumentParser
from re import findall


def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2023, 6).example_data.splitlines()
        # with open("./2023/day_06/test.txt") as file:
        #     data = file.readlines()
        #     data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 6).input_data.splitlines()
    data = [(int(a), int(b)) for a, b in zip(findall(r"\d+", data[0]), findall(r"\d+", data[1]))]
    return data

def find_valid_button_press(data: list[tuple[int, int]]):
    total = 1
    for d_ in data:
        valid = 0
        for i in range(1, d_[0]):
            n = (d_[0] - i) * i
            if n > d_[1]: valid += 1
        total *= valid
    return total

def q2_data(data):
    return [(int("".join([str(n[0]) for n in data])), int("".join([str(n[1]) for n in data])))]

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    n = find_valid_button_press(data)
    print(n)
    
    data = q2_data(data)
    n = find_valid_button_press(data)
    print(n)
