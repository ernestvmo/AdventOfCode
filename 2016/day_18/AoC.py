from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 18).example_data.splitlines()
        with open("./2016/day_18/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 18).input_data.splitlines()

    return data[0]

def predict_next_row(prev_row: str):
    row = [None]*len(prev_row)
    for i in range(len(prev_row)):
        if i == 0:
            left = '.'
        else:
            left = prev_row[i-1]
        
        if i == len(prev_row)-1:
            right = '.'
        else:
            right = prev_row[i+1]
        center = prev_row[i]

        # cond 1
        if left == '^' and center == '^' and right == '.':
            row[i] = '^'
        elif left == '.' and center == '^' and right == '^':
            row[i] = '^'
        elif left == '^' and center == '.' and right == '.':
            row[i] = '^'
        elif left == '.' and center == '.' and right == '^':
            row[i] = '^'
        else:
            row[i] = '.'
    return row

def find_traps(first_row: str, repeats: int = 3):
    room = [first_row]
    prev_row = first_row[:]
    for _ in range(repeats-1):
        new_row = predict_next_row(prev_row)
        room.append(''.join(new_row))
        prev_row = new_row[:]
    return room

def count_safe_tiles(room: list[str]):
    safe = 0
    for row in room:
        for tile in row:
            if tile == '.':
                safe += 1
    return safe

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    first_row = load_data(args.mode)
    room = find_traps(first_row, 40)
    total = count_safe_tiles(room)
    print(total)

    room = find_traps(first_row, 400000)
    total = count_safe_tiles(room)
    print(total)