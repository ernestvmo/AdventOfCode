import os.path
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2024, 4).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = file.readlines()
    else:
        data = Puzzle(2024, 4).input_data.splitlines()

    return [d.rstrip() for d in data]


def find_xmas(word_map: list[list[str]]):
    count = 0
    for row in range(len(word_map)):
        for column in range(len(word_map[row])):
            if word_map[row][column] == "X":
                count += spells_xmas(row, column, word_map)
    return count


def spells_xmas(row: int, col: int, word_map: list[list[str]]) -> int:
    count = 0
    for i, target_letter in zip(range(1, 4), "MAS"):
        if 0 <= col + i < len(word_map[0]):
            if target_letter != word_map[row][col + i]:
                break
            elif target_letter == word_map[row][col + i] == "S":
                count += 1
    for i, target_letter in zip(range(-1, -4, -1), "MAS"):
        if 0 <= col + i < len(word_map[0]):
            if target_letter != word_map[row][col + i]:
                break
            elif target_letter == word_map[row][col + i] == "S":
                count += 1
    for i, target_letter in zip(range(1, 4), "MAS"):
        if 0 <= row + i < len(word_map):
            if target_letter != word_map[row + i][col]:
                break
            elif target_letter == word_map[row + i][col] == "S":
                count += 1
    for i, target_letter in zip(range(-1, -4, -1), "MAS"):
        if 0 <= row + i < len(word_map):
            if target_letter != word_map[row + i][col]:
                break
            elif target_letter == word_map[row + i][col] == "S":
                count += 1
    for i, target_letter in zip(range(1, 4), "MAS"):
        if 0 <= row + i < len(word_map) and 0 <= col + i < len(word_map[0]):
            if target_letter != word_map[row + i][col + i]:
                break
            elif target_letter == word_map[row + i][col + i] == "S":
                count += 1
    for i, target_letter in zip(range(-1, -4, -1), "MAS"):
        if 0 <= row + i < len(word_map) and 0 <= col + i < len(word_map[0]):
            if target_letter != word_map[row + i][col + i]:
                break
            elif target_letter == word_map[row + i][col + i] == "S":
                count += 1
    for i, j, target_letter in zip(range(-1, -4, -1), range(1, 4), "MAS"):
        if 0 <= row + i < len(word_map) and 0 <= col + j < len(word_map[row]):
            if target_letter != word_map[row + i][col + j]:
                break
            elif target_letter == word_map[row + i][col + j] == "S":
                count += 1
    for j, i, target_letter in zip(range(-1, -4, -1), range(1, 4), "MAS"):
        if 0 <= row + i < len(word_map) and 0 <= col + j < len(word_map[row]):
            if target_letter != word_map[row + i][col + j]:
                break
            elif target_letter == word_map[row + i][col + j] == "S":
                count += 1
    return count


def find_x_mas(word_map: list[list[str]]) -> int:
    count = 0
    for row in range(len(word_map)):
        for column in range(len(word_map[row])):
            if word_map[row][column] == "A":
                count += spells_x_mas(row, column, word_map)
    return count


def spells_x_mas(row: int, col: int, word_map: list[list[str]]) -> int:
    if (
        0 <= row - 1
        and 0 <= col - 1
        and row + 1 < len(word_map)
        and col + 1 < len(word_map[0])
    ):
        if (
            word_map[row - 1][col - 1] != word_map[row + 1][col + 1]
            and word_map[row - 1][col - 1] in ["M", "S"]
            and word_map[row + 1][col + 1] in ["M", "S"]
        ):
            if (
                word_map[row - 1][col + 1] != word_map[row + 1][col - 1]
                and word_map[row - 1][col + 1] in ["M", "S"]
                and word_map[row + 1][col - 1] in ["M", "S"]
            ):
                return 1
    return 0


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    script = load_data(args.mode)
    res = find_xmas(script)
    print(f"part 1: {res}")
    res = find_x_mas(script)
    print(f"part 2: {res}")
