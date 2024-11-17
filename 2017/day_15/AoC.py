from aocd.models import Puzzle
from argparse import ArgumentParser
import re

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 15).example_data.splitlines()
        with open("./2017/day_15/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 15).input_data.splitlines()

    data = data[0] + data[1]
    n = re.findall(r'\d+', data.strip())
    return int(n[0]), int(n[1])

def find_denominator(A: int, B: int):
    xA = 16807
    xB = 48271
    div = 2147483647
    count = 0

    for _ in range(40*10**6):
        A = (A*xA)%div
        B = (B*xB)%div
        if str(bin(A))[-16:] == str(bin(B))[-16:]:
            count += 1
    return count

def find_denominator_mu(A: int, B: int):
    xA = 16807
    xB = 48271
    div = 2147483647
    count = 0

    for _ in range(5*10**6):
        while True:
            A = (A*xA)%div
            if A % 4 == 0:
                break
        while True:
            B = (B*xB)%div
            if B % 8 == 0:
                break
        if str(bin(A))[-16:] == str(bin(B))[-16:]:
            count += 1
    return count



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    A, B = load_data(args.mode)
    # n = find_denominator(A, B)
    # print(n)
    
    n = find_denominator_mu(A, B)
    print(n)
    