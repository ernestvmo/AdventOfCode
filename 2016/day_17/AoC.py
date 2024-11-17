from aocd.models import Puzzle
from argparse import ArgumentParser
from hashlib import md5
import numpy as np
import heapq

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 17).example_data.splitlines()
        with open("./2016/day_17/test.txt") as file:
            data = file.readlines()
    else:
        data = ['hijkl']

    return data[0]

def get_neighbours(grid: np.ndarray, cell: tuple):
    x, y = cell
    neighbours = []
    if y < len(grid) - 1:
        if grid[y+1][x] == '.':
            neighbours.append((x, y+1))
    if y > 0:
        if grid[y-1][x] == '.':
            neighbours.append((x, y-1))
    if x < len(grid[0]) - 1:
        if grid[y][x+1] == '.':
            neighbours.append((x+1, y))
    if x > 0:
        if grid[y][x-1] == '.':
            neighbours.append((x-1, y))
    return neighbours

def extract_path(previous: dict, end: tuple):
    path = [end]
    curr = end
    while curr in previous:
        curr = previous[curr]
        if curr:
            path.append(curr)
    return path[::-1]

def dijkstra(grid: np.ndarray, start: tuple, end: tuple, part: int, range_: int):
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
        if part == 1 and curr == end:
            return extract_path(previous, end)
        
        if part == 2 and curr_distance <= range_:
            results.add(curr)
        
        if part == 2 and curr_distance > range_:
            break

        for n in get_neighbours(grid, curr):
            tentative_distance = distances[curr] + 1
            if tentative_distance < distances[n]:
                distances[n] = tentative_distance
                previous[n] = curr
                heapq.heappush(queue, (tentative_distance, n))
    return results

def find_minimal_path(grid: np.ndarray, start: tuple = (1,1), end: tuple = (7,4), part: int = 1):
    path = dijkstra(grid, start, end, part, None)
    return len(path)-1


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    input = load_data(args.mode)
    total = ...
    print(total)