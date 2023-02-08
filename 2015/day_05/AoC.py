from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_05/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 5).input_data.splitlines()
    
    return [name.rstrip('\n') for name in data]

def naughty_or_nice(name: str):
    vowel_count = 0    
    for c in name:
        if c in 'aeiou':
            vowel_count += 1
    if vowel_count < 3:
        return False

    is_valid = False
    for i in range(len(name)):
        if i < len(name) - 1:
            if name[i] == name[i + 1]:
                is_valid = True
            if name[i] + name[i+1] in ['ab', 'cd', 'pq', 'xy']:
                return False
    return is_valid

def naughty_or_nice_second(name: str):
    cond_1 = cond_2 = False
    for i in range(len(name)):
        if i < len(name) - 1:
            if name[i] + name[i+1] in name[i+2:]:
                cond_1 = True
        if i < len(name) - 2:
            if name[i] == name[i+2]:
                cond_2 = True
    return cond_1 and cond_2

def count_nice(santa_list: list, part: str):
    nice = 0
    for name in santa_list:
        if part == "1" and  naughty_or_nice(name):
            nice += 1
        elif part == "2" and naughty_or_nice_second(name):
            nice += 1
    return nice


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    santa_list = load_data(args.mode)
    number_of_nice = count_nice(santa_list, part='1')
    print(number_of_nice)

    number_of_nice_second = count_nice(santa_list, part='2')
    print(number_of_nice_second)