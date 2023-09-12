from aocd.models import Puzzle
from argparse import ArgumentParser
from functools import reduce
from operator import xor

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 10).example_data.splitlines()
        with open("./2017/day_10/test.txt") as file:
            data = file.readlines()
        length = 256
    else:
        data = Puzzle(2017, 10).input_data.splitlines()
        length = 256

    return data[0], list(range(length))

def process_data(data: str):
    return [int(n) for n in data.split(",")]

def twist(list_: list, instructions: list):
    pos = skip_size = 0
    for instruction in instructions:
        if pos >= len(list_):
            pos -= len(list_)
        if pos + instruction >= len(list_):
            r_list_ = [elem for elem in reversed(list_[pos:pos+instruction]+list_[0:pos+instruction-len(list_)])]
            # print(r_list_, r_list_[:len(list_[pos:pos+instruction])], r_list_[len(list_[pos:pos+instruction]):])
            list_[pos:pos+instruction] = r_list_[:len(list_[pos:pos+instruction])]
            list_[0:pos+instruction-len(list_)] = r_list_[len(list_[pos:pos+instruction]):]
        else:
            list_[pos:pos+instruction] = reversed(list_[pos:pos+instruction])
        pos += instruction + skip_size
        skip_size += 1
        # print("--", list_)
    return list_[0]*list_[1]

def instructions_to_ascii(data: list, length: int):
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


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data, list = load_data(args.mode)
    instructions = process_data(data)
    n = twist(list[:], instructions)
    print(n)

    instructions_ascii = instructions_to_ascii(data, len(list))
    list_ = twist_q2(list[:], instructions_ascii)
    dense_hash = sparse_to_dense_hash(list_)
    hex_ = hexadicemalize(dense_hash)
    print(hex_)