from aocd.models import Puzzle
from argparse import ArgumentParser
import re

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2023, 1).example_data.splitlines()
        with open("./2023/day_01/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2023, 1).input_data.splitlines()
    
    return data

def digit_extract(data: list):
    digits = []
    for line in data:
        nums = re.findall(r"\d{1}", line)
        digits.append(int(nums[0]+nums[-1]))
    return digits

def number_read(data: list):
    num_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    digits = []

    for line in data:
        while len([n for n in num_dict.keys() if n in line]) > 0:
            for n in [n for n in num_dict.keys() if n in line]:
                line = line.replace(n, num_dict[n])
        nums = re.findall(r"\d{1}", line)
        digits.append(int(nums[0]+nums[-1]))
    return sum(digits)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    n = digit_extract(data)
    print(n)

    n = number_read(data)
    print(n)