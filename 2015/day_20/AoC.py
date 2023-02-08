from aocd.models import Puzzle
from argparse import ArgumentParser
import math

def load_data(mode: str):
    if mode == "test":
        data = ['130']
    else:
        data = Puzzle(2015, 20).input_data.splitlines()

    return int(data[0]) 

def number_of_presents(house, multiplier, stop_delivery=math.inf):
    c = 0
    for n in range(1, int(math.sqrt(house)) + 1):
        if house % n == 0:
            nn = house // n
            if nn <= stop_delivery:
                c += n
            if nn > n and n <= stop_delivery:
                c += nn
    return c * multiplier

def find_house(target_presents, multiplier, stop_delivery=math.inf):
    house = 1
    while number_of_presents(house, multiplier, stop_delivery) < target_presents:
        house += 1
    return house


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    n = load_data(args.mode)
    house_n = find_house(n, 10)
    print(house_n)

    house_n = find_house(n, 11, 50)
    print(house_n)