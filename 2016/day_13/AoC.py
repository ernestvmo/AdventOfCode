from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np
import heapq

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 13).example_data.splitlines()
        # with open("./2016/day_13/test.txt") as file:
        #     data = file.readlines()
        data = [10]
    else:
        data = Puzzle(2016, 13).input_data.splitlines()

    magic_number = int(data[0])
    grid = np.full((magic_number, magic_number), '-')
    for x in range(magic_number):
        for y in range(magic_number):
            sum = x**2 + 3*x + 2*x*y + y + y**2 + magic_number
            if str(bin(sum))[2:].count('1') % 2 == 0:
                grid[y][x] = '.'
            else:
                grid[y][x] = '#'
    return grid

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

def find_coordinates_in_range(grid: np.ndarray, start: tuple = (1,1), end: tuple = (7,4), part: int = 2, range_: int = 10):
    coords = dijkstra(grid, start, end, part, range_)
    return len(coords)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    grid = load_data(args.mode)
    if args.mode == 'test':
        total = find_minimal_path(grid)
        print(total)

        total = find_coordinates_in_range(grid)
        print(total)
    else:
        total = find_minimal_path(grid, end=(31,39))
        print(total)

        total = find_coordinates_in_range(grid, end=(31,39), range_=50)
        print(total)