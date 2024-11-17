from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np
from collections import Counter

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2016, 6).example_data.splitlines()
        # with open("./2016/day_05/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2016, 6).input_data.splitlines()
        
    return data

def find_error_corrected_message(messages: list[str]):
    # flip messages
    messages = np.array(np.array([[letter for letter in message] for message in messages]))
    messages = np.transpose(messages)

    error_corrected_message = ''
    for error_corrupted in messages:
        error_corrected_message += str(Counter(error_corrupted).most_common(1)[0][0])
    return error_corrected_message

def find_error_corrected_message_least(messages: list[str]):
    # flip messages
    messages = np.array(np.array([[letter for letter in message] for message in messages]))
    messages = np.transpose(messages)

    error_corrected_message = ''
    for error_corrupted in messages:
        error_corrected_message += str(Counter(error_corrupted).most_common()[-1][0])
    return error_corrected_message


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    messages = load_data(args.mode)
    total = find_error_corrected_message(messages)
    print(total)

    total = find_error_corrected_message_least(messages)
    print(total)