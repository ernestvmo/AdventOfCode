from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 9).example_data.splitlines()
        with open("./2016/day_09/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 9).input_data.splitlines()

    return data[0]

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def count_length(sequence: str, part=1):
    i = 0
    new_sequence = ''
    # print(f"sequence: {sequence}")
    while i < len(sequence):
        if sequence[i] == '(':
            marker = sequence[i:i+sequence[i:].index(')')+1]
            chars, repeats = marker[1:-1].split('x')
            chars, repeats = int(chars), int(repeats)
            repeat_char = sequence[i+sequence[i:].index(')')+1:i+sequence[i:].index(')')+1+chars]
            # print(marker, repeat_char)
            new_sequence += str(repeat_char)*repeats
            i += sequence[i:].index(')') + 1 + chars
        else:
            # print('normal char', sequence[i])
            new_sequence += sequence[i]
            i += 1
    # print(f"new sequence: {new_sequence}")
    if part==1:
        return len(new_sequence), new_sequence
    else:
        if "(" in new_sequence:
            print(len(new_sequence), new_sequence)
            return count_length(new_sequence, part)
        else:
            return len(new_sequence), new_sequence

def decompress(s, part=True):
    if '(' not in s:
        return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        if part:
            ret += decompress(s[:int(marker[0])]) * int(marker[1])
        else:
            ret += len(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    ret += len(s)
    return ret

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    sequence = load_data(args.mode)
    total, new_sequence = count_length(sequence)
    print(total)

    # total, _ = count_length(new_sequence, 2)
    # print(total)

    total = decompress(new_sequence)
    print(total)