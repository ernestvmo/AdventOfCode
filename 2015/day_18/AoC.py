from aocd.models import Puzzle
from argparse import ArgumentParser
import numpy as np

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_18/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 18).input_data.splitlines()

    lights = []
    for line in data:
        line = line.rstrip("\n")
        lights.append([l for l in line])
    
    return np.array(lights)

def display_lights(lights: np.ndarray):
    print('-'*len(lights[0]))
    for row in lights:
        for col in row:
            print(col, end='', sep='')
        print()
    print('-'*len(lights[0]))

def light_show(lights: np.ndarray, repeats=100, display=True):
    if display: display_lights(lights)
    for _ in range(repeats):
        turn_offs = []
        turn_ons = []
        for i in range(len(lights)):
            for j in range(len(lights[i])):
                neighbours_on = 0
                for row in range(-1, 2):
                    for col in range(-1, 2):
                        if row == col == 0:
                            continue
                        
                        if i+row == len(lights) or i+row < 0 or j+col == len(lights[i]) or j+col < 0:
                            continue

                        if lights[i+row][j+col] == "#":
                            neighbours_on += 1

                if lights[i][j] == '.':
                    if neighbours_on == 3:
                        turn_ons.append([i,j])
                    else:
                        turn_offs.append([i,j])

                if lights[i][j] == '#':
                    if neighbours_on in [2,3]:
                        turn_ons.append([i,j])
                    else:
                        turn_offs.append([i,j])

        for i,j in turn_offs:
            lights[i][j] = '.'

        for i,j in turn_ons:
            lights[i][j] = '#'

    if display: display_lights(lights)
    return np.sum(np.char.count(lights, '#'))

def light_show_with_corners(lights: np.ndarray, repeats=100, display=True):
    corners = [[0,0], [0, len(lights[0])-1], [len(lights)-1,0], [len(lights)-1, len(lights[0])-1]]
    for i, j in corners:
        lights[i][j] = '#'

    if display: display_lights(lights)
    for _ in range(repeats):
        turn_offs = []
        turn_ons = []
        for i in range(len(lights)):
            for j in range(len(lights[i])):
                neighbours_on = 0
                for row in range(-1, 2):
                    for col in range(-1, 2):
                        if row == col == 0:
                            continue
                        
                        if i+row == len(lights) or i+row < 0 or j+col == len(lights[i]) or j+col < 0:
                            continue

                        if lights[i+row][j+col] == "#":
                            neighbours_on += 1

                if lights[i][j] == '.':
                    if neighbours_on == 3:
                        turn_ons.append([i,j])
                    else:
                        turn_offs.append([i,j])

                if lights[i][j] == '#':
                    if neighbours_on in [2,3]:
                        turn_ons.append([i,j])
                    else:
                        turn_offs.append([i,j])

        for i,j in turn_offs:
            if [i,j] not in corners:
                lights[i][j] = '.'

        for i,j in turn_ons:
            lights[i][j] = '#'

    if display: display_lights(lights)
    return np.sum(np.char.count(lights, '#'))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    lights = load_data(args.mode)
    total = light_show(lights, display=False)
    print(total)

    lights = load_data(args.mode)
    total = light_show_with_corners(lights, display=False)
    print(total)