from aocd.models import Puzzle
from argparse import ArgumentParser
import re

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2023, 2).example_data.splitlines()
    else:
        data = Puzzle(2023, 2).input_data.splitlines()

    return data


def extract_games(fata: list):
    games = {}
    for i, line in enumerate(data):
        games[(i+1)] = {
            "red": [int(d.split(" ")[0]) for d in re.findall(r"\d+ red", line)],
            "blue": [int(d.split(" ")[0]) for d in re.findall(r"\d+ blue", line)],
            "green": [int(d.split(" ")[0]) for d in re.findall(r"\d+ green", line)]
        }
    return games

def count_valid_games(games: dict):
    count = 0
    for i in games.keys():
        if not any([n > 12 for n in games[i]["red"]]) and not any([n > 13 for n in games[i]["green"]]) and not any([n > 14 for n in games[i]["blue"]]):
            count += i
    return count

def minimum_boxes(games: dict):
    count = 0
    for i in games.keys():
        count += max(games[i]["red"])*max(games[i]["green"])*max(games[i]["blue"])
    return count

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    games = extract_games(data)
    n = count_valid_games(games)
    print(n)

    n = minimum_boxes(games)
    print(n)