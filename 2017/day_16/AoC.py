from aocd.models import Puzzle
from argparse import ArgumentParser

from string import ascii_lowercase

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2017, 16).example_data.splitlines()
        with open("./2017/day_16/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 16).input_data.splitlines()

    letters = ascii_lowercase[:16] if mode == "input" else ascii_lowercase[:5]

    return [l for l in letters], data[0].split(",")

def dance(letters: list[str], moves: list[str]):
    for move in moves:
        if move.startswith("s"):
            letters = spin(int(move[1:]), letters)
        elif move.startswith("x"):
            letters = exchange(move[1:].split("/"), letters)
        else:
            letters = partner(move[1:].split("/"), letters)
    return letters

def spin(move: int, letters: list[str]):
    return letters[-move:] + letters[:-move]

def exchange(move: str, letters):
    A, B = move
    A, B = int(A), int(B)
    t = letters[A]
    letters[A] = letters[B]
    letters[B] = t
    return letters

def partner(move: int, letters):
    A, B = move
    A, B = letters.index(A), letters.index(B)
    t = letters[A]
    letters[A] = letters[B]
    letters[B] = t
    return letters

def dance_one_billion(letters, moves):
    seen = []
    for _ in range(10**9):
        h = tuple(letters)
        if h in seen:
            return ''.join(seen[10**9 % len(seen)])
        seen += [h]
        letters = dance(letters, moves)
    return letters


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    letters, moves = load_data(args.mode)
    answer = dance(letters.copy(), moves)
    print(''.join(answer))

    answer_2 = dance_one_billion(letters.copy(), moves)
    print(''.join(answer_2))