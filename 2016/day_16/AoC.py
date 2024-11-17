from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 16).example_data.splitlines()
        with open("./2016/day_16/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 16).input_data.splitlines()

    return data[0]

def dragon_curve(a: str):
    b = a[::-1]
    b = b.replace('0', '-')
    b = b.replace('1', '0')
    b = b.replace('-', '1')
    return a, b

def generate_checksum(string: str):
    while True:
        checksum = ''
        for c in range(0, len(string), 2):
            if string[c] == string[c+1]:
                checksum += '1'
            else:
                checksum += '0'
        if len(checksum) % 2 != 0:
            return checksum
        else:
            string = checksum

def fill_disk_space(disk_space: int, key: str):
    while True:
        if len(key) < disk_space:
            a, b = (dragon_curve(key))
            key = '0'.join([a, b])
        else:
            key = key[:disk_space]
            checksum = generate_checksum(key)
            return checksum

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    input = load_data(args.mode)
    total = fill_disk_space(272, input)
    print(total)

    total = fill_disk_space(35651584, input)
    print(total)