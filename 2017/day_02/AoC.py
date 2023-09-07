from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 2).example_data.splitlines()
        with open("./2017/day_02/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 2).input_data.splitlines()

    for i in range(len(data)):
        if mode == "test":
            vals = [int(i) for i in data[i].split(" ")]

        else:
            vals = [int(i) for i in data[i].split("\t")]
        data[i] = vals

    return data

def checksum(input: list[str]):
    checksum = 0
    for elem in input:
        checksum += (max(elem) - min(elem))
    return checksum

def checksum_even_distrib(input: list[str]):
    checksum = 0
    for elem in input:
        for v in elem:
            for v_ in elem:
                if v != v_ and v < v_ and v_ % v == 0:
                    checksum += (v_ // v)
    return checksum

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    sequence = load_data(args.mode)
    sum = checksum(sequence)
    print(sum)
    sum = checksum_even_distrib(sequence)
    print(sum)
