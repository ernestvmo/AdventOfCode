from aocd.models import Puzzle
from argparse import ArgumentParser
import re

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2023, 3).example_data.splitlines()
        with open("./2023/day_03/test.txt") as file:
            data = file.readlines()
            data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 3).input_data.splitlines()

    return data

def extract_digits_and_special_chars(data: list):
    numbers_dict = {}
    special_chars = {}
    for i in range(len(data)):
        last = 0
        digit = {}
        numbers = re.findall(r"\d+", data[i])
        for n in numbers:
            last = data[i].index(n, last)
            digit[(last, last+len(n)-1)] = n
            numbers_dict[i] = digit
            last += len(n)
        special_chars[i] = {j: n for j, n in enumerate(data[i]) if n.isalnum() is False and n != "."}
        if special_chars[i] == {}:
            special_chars.pop(i)
    return numbers_dict, special_chars

def compute_sum(digits: dict, special_chars: dict):
    nums = []
    for line, v in special_chars.items():
        for s_index in special_chars[line]:
            for i in [-1, 0, 1]:
                if line+i in digits.keys():
                    for d_values_index, d in digits[line+i].items():
                        if abs(d_values_index[0] - s_index) <= 1 or abs(d_values_index[1] - s_index) <= 1:
                            nums.append(int(d))
    return sum(nums)

def compute_gear_ratio(digits: dict, special_chars: dict):
    nums = 0
    for line in special_chars.keys():
        for s_index, v in special_chars[line].items():
            nums_char = []
            if v == "*":
                for i in [-1, 0, 1]:
                    if line+i in digits.keys():
                        for d_values_index, d in digits[line+i].items():
                            if abs(d_values_index[0] - s_index) <= 1 or abs(d_values_index[1] - s_index) <= 1:
                                nums_char.append(int(d))
            if len(nums_char) == 2:
                nums += nums_char[0]*nums_char[1]
    return nums


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    numbers_dict, special_chars = extract_digits_and_special_chars(data)
    sum = compute_sum(numbers_dict.copy(), special_chars.copy())
    print(sum)
    
    ratio = compute_gear_ratio(numbers_dict.copy(), special_chars.copy())
    print(ratio)