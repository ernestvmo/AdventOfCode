from aocd.models import Puzzle
from argparse import ArgumentParser
from hashlib import md5
from collections import Counter

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 14).example_data.splitlines()
        # with open("./2016/day_14/test.txt") as file:
        #     data = file.readlines()
        data = ['abc']
    else:
        data = Puzzle(2016, 14).input_data.splitlines()

    return data[0]

def evaluate_potential_key(potential_key: str):
    for i in range(len(potential_key)-2):
        if potential_key[i] == potential_key[i+1] == potential_key[i+2]:
            return True, potential_key[i]
    return False, None

def find_keys(salt: str, keys_required: int = 64):
    keys = set()
    for i in range(100**100):
        potential_key = md5(str(salt + str(i)).encode()).hexdigest()
        valid, repeating = evaluate_potential_key(potential_key)
        if valid:
            for j in range(i+1, i+1001):
                second_condition_key = md5(str(salt + str(j)).encode()).hexdigest()
                if str(repeating)*5 in second_condition_key:
                    keys.add((potential_key))
                    if len(keys) == keys_required:
                        return i

def find_keys_with_key_stretching(salt: str, keys_required: int = 64):
    keys = set()
    for i in range(100**100):
        potential_key = md5(str(salt + str(i)).encode()).hexdigest()
        # print(potential_key)
        for _ in range(2016):
            potential_key = md5(potential_key.encode()).hexdigest()
        # print(potential_key)
        valid, repeating = evaluate_potential_key(potential_key)
        if valid:
            for j in range(i+1, i+1001):
                second_condition_key = md5(str(salt + str(j)).encode()).hexdigest()
                for _ in range(2016):
                    second_condition_key = md5(second_condition_key.encode()).hexdigest()
                if str(repeating)*5 in second_condition_key:
                    # print(i, potential_key, j, second_condition_key)
                    # return
                    keys.add((i, potential_key, j, second_condition_key))
                    if len(keys) == keys_required:
                        return i, sorted(keys)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    salt = load_data(args.mode)
    # total = find_keys(salt)
    # print(total)

    total = find_keys_with_key_stretching(salt)
    print(total)