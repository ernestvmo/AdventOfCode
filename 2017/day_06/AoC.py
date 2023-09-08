from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        with open("./2017/day_06/test.txt") as file:
            data = file.readlines()
            return [int(v) for v in data[0].split(" ")]
    else:
        data = Puzzle(2017, 6).input_data.splitlines()
        return [int(v) for v in data[0].split("\t")]

def distribute_blocks(blocks: list[int]):
    cycle = blocks[:]
    observed_cycles = []
    count = 0
    while True:
        observed_cycles.append(cycle[:])
        i = np.argmax(cycle)
        v = cycle[i]
        cycle[i] = 0
        a = i
        for _ in range(1, v+1):
            a+=1
            if a == len(cycle): a = 0
            cycle[a] += 1
        count+= 1
        if cycle[:] in observed_cycles:
            break
    return count, len(observed_cycles) - observed_cycles.index(cycle[:])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    blocks = load_data(args.mode)
    q1, q2 = distribute_blocks(blocks)
    print(q1)
    print(q2)
