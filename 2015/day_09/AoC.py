from aocd.models import Puzzle
from argparse import ArgumentParser
import itertools

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2015, 9).example_data.splitlines()
    else:
        data = Puzzle(2015, 9).input_data.splitlines()

    paths = {}
    for line in data:
        _, weight = line.split(" = ")
        weight = int(weight)
        city_1, city_2 = _.split(" to ")
        if city_1 not in paths.keys():
            paths[city_1] = {city_2: weight}
        else:
            paths[city_1][city_2] = weight
        if city_2 not in paths.keys():
            paths[city_2] = {city_1: weight}
        else:
            paths[city_2][city_1] = weight

    return paths

def tsp_problem(paths: dict[dict], key=min):
    possibilities = list(itertools.permutations(paths.keys()))
    cost = 10000 if key == min else 0
    for possibility in possibilities:
        trip_cost = 0
        for i in range(0, len(possibility)-1):
            trip_cost += paths[possibility[i]][possibility[i+1]]
        cost = key(cost, trip_cost)
    
    return cost

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    paths = load_data(args.mode)
    total = tsp_problem(paths)
    print(total)

    total = tsp_problem(paths, key=max)
    print(total)   