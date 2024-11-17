from aocd.models import Puzzle
from argparse import ArgumentParser
from functools import reduce
from operator import xor

def load_data(mode: str):
    if mode == "test":
        with open("./2017/day_14/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 14).input_data.splitlines()

    return data[0]

def instructions_to_ascii(data: list):
    sequence = []
    for c in data:
        sequence.append(ord(c))
    return sequence + [17, 31, 73, 47, 23]

def twist_q2(list_: list, instructions: list):
    pos = skip_size = 0
    for _ in range(64):
        for instruction in instructions:
            temp = []
            for j in range(instruction):
                temp.append(list_[(pos+j) % 256])
            for j in range(instruction):
                list_[(pos+instruction-1-j) % 256] = temp[j]
            pos += skip_size + instruction
            skip_size += 1
    return list_

def sparse_to_dense_hash(list_: list):
    dense = []
    for i in range(0, len(list_), 16):
        dense.append(reduce(xor, list_[i:i + 16]))
    return dense

def hexadicemalize(dense: list):
    hex_ = ""
    for bit in dense:
        hex_ += hex(bit)[2:] if len(hex(bit)[2:]) == 2 else "0"+hex(bit)[2:]
    return hex_

def knot_hash(key: str):
    return hexadicemalize(sparse_to_dense_hash(twist_q2(list(range(256)), instructions_to_ascii(key))))

def hex_to_bin(mkey: str, q: int = 1):
    unseen = []
    count = 0
    for i in range(128):
        key = f"{mkey}-{i}"
        key = "".join(['{0:04b}'.format(int(c, 16)) for c in knot_hash(key)])
        unseen += [(i, j) for j, d in enumerate(key) if d == '1']
    if q == 1: return len(unseen)
    while unseen:
        queued = [unseen[0]]
        while queued:
            x, y = queued.pop()
            if (x, y) in unseen:
                unseen.remove((x, y))
                queued += [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        count += 1
    return count

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    n = hex_to_bin(data, q=1)
    print(n)

    n = hex_to_bin(data, q=2)
    print(n)