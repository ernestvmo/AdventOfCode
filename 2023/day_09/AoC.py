from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2023, 9).example_data.splitlines()
        # with open("./2023/day_09/test.txt") as file:
        #     data = file.readlines()
        #     data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 9).input_data.splitlines()

    data = [[int(d) for d in line.split()] for line in data]

    return data

def find_max_num_sequence(sequences: list[list[int]], forward = True):
    number = 0
    for i, sequence in enumerate(sequences):
        if forward:
            trailing_numbers = []
            while True:
                trailing_numbers.append(sequence[-1])
                distance_in_sequence = [j-i for i,j in zip(sequence[:-1], sequence[1:])]
                # print(sequence)
                if all([d == 0 for d in distance_in_sequence]):
                    # print(trailing_numbers)
                    trailing_numbers = trailing_numbers[::-1]
                    while True:
                        if len(trailing_numbers) > 2:
                            trailing_numbers = [trailing_numbers[0] + trailing_numbers[1]] + trailing_numbers[2:]
                        else:
                            v = sum(trailing_numbers)
                            break
                    number += v
                    # print(v)
                    # input()
                    break
                else:
                    sequence = distance_in_sequence
        else:
            leading_numbers = []
            while True:
                leading_numbers.append(sequence[0])
                distance_in_sequence = [j-i for i, j in zip(sequence[:-1], sequence[1:])]
                # print(sequence)
                if all([d == 0 for d in distance_in_sequence]):
                    leading_numbers=leading_numbers[::-1]
                    while True:
                        # print(leading_numbers)
                        if len(leading_numbers) > 2:
                            leading_numbers = [leading_numbers[1]-leading_numbers[0]] + leading_numbers[2:]
                        else:
                            v = leading_numbers[1] - leading_numbers[0]
                            break
                    number += v
                    # print(v)
                    # input()
                    break
                else:
                    sequence = distance_in_sequence
    return number    

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    x = find_max_num_sequence(data)
    print(x)
    x = find_max_num_sequence(data, False)
    print(x)
