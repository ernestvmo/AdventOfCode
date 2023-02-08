from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        with open("./2015/day_08/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 8).input_data.splitlines()

    return [item.rstrip("\n") for item in data]

def literal_vs_string(santa_list: list[str]):
    literal = 0
    string = 0

    for item in santa_list:
        literal += len(str(eval(item)))
        string += len(item)
    
    return string - literal

def string_encoded(santa_list: list[str]):
    string = 0
    encoded = 0

    for item in santa_list:
        string += len(item)
        if "\\" in item:
            item = item.replace("\\", "\\\\")
        if "\"" in item:
            item = item.replace("\"", "\\\"")
        encoded += len(item) + 2
    return encoded - string

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    santa_list = load_data(args.mode)
    total = literal_vs_string(santa_list)
    print(total)

    encoded_total = string_encoded(santa_list)
    print(encoded_total)

    