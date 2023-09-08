from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        with open("./2017/day_04/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 4).input_data.splitlines()

    return [line.split() for line in data]

def policy_1(passphrases: list[str]):
    valid_count = 0
    for passphrase in passphrases:
        valid = True
        for word in passphrase:
            if passphrase.count(word) > 1:
                valid = False
        if valid:
            valid_count += 1
    return valid_count

def policy_2(passphrases: list[str]):
    valid_count = 0
    for passphrase in passphrases:
        valid = True
        for w1 in passphrase:
            if passphrase.count(w1) > 1:
                valid = False
            else:
                for w2 in passphrase:
                    if w1 != w2 and sorted(w1) == sorted(w2):
                        valid = False
        if valid:
            valid_count += 1
    return valid_count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    passphrases = load_data(args.mode)
    valid = policy_1(passphrases)
    print(valid)

    valid = policy_2(passphrases)
    print(valid)