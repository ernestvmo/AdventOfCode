from aocd.models import Puzzle
from argparse import ArgumentParser
import heapq
import numpy as np


import pprint

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2023, 10).example_data.splitlines()
        with open("./2023/day_10/test.txt") as file:
            data = file.readlines()
            data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 10).input_data.splitlines()

    map = np.array([list(line) for line in data])

    S = np.where(map == "S")
    if np.array(S).shape[1] > 0:
        S = (S[0][0], S[1][0])
    else: S = (1, 1)

    return map, S

def get_neighbours(grid: np.ndarray, y: int, x: int):
    # print(grid[y][x], y, x)
    if grid[y][x] == "|":
        # north and south
        return [
            (y - 1, x), # north
            (y + 1, x), # south
        ]
    elif grid[y][x] == "-":
        # east and west
        return [
            (y, x - 1), # west
            (y, x + 1), # east
        ]
    elif grid[y][x] == "L":
        # north and east
        return [
            (y - 1, x), # north
            (y, x + 1), # west
        ]
    elif grid[y][x] == "J":
        # north and west
        return [
            (y - 1, x), # north
            (y, x - 1), # west
        ]
    elif grid[y][x] == "7":
        # south and west
        return [
            (y + 1, x), # south
            (y, x - 1), # west
        ]
    elif grid[y][x] == "F":
        # east and south
        return [
            (y, x + 1), # east
            (y + 1, x), # south
        ]
    elif grid[y][x] == "S":
        neighbours = []
        for xi in [-1, 1]:
            if 0 <= x+xi < len(grid[y]) and grid[y][x+xi] != ".":
                neighbours.append((y, x+xi))
        for yi in [-1, 1]:
            if 0 <= y+yi < len(grid) and grid[y+yi][x] != ".":
                neighbours.append((y+yi, x))
        # print(neighbours)
        return neighbours

def dijkstra(grid: np.ndarray, start: tuple):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {}
    previous = {}

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            distances[(i, j)] = float('inf')
            previous[(i, j)] = None
    distances[start] = 0
    results = set()

    while queue:
        curr_distance, curr = heapq.heappop(queue)
        
        # print("-", curr, get_neighbours(grid, curr[0], curr[1]))

        for n in get_neighbours(grid, curr[0], curr[1]):
            tentative_distance = distances[curr] + 1
            if tentative_distance < distances[n]:
                distances[n] = tentative_distance
                previous[n] = curr
                heapq.heappush(queue, (tentative_distance, n))
    
    return max([v for k, v in distances.items() if v != float('inf')])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data, S = load_data(args.mode)

    res = dijkstra(data, S)
    print(res)
