from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_03/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 3).input_data.splitlines()
    
    directions = [direction for direction in data[0]]
    return directions

def visit_houses(directions: list):
    visited = 1
    pos = [0,0]
    houses = [pos[:]]

    for d in directions:
        if d == ">":
            pos[0] += 1
        elif d == "<":
            pos[0] -= 1
        elif d == "v":
            pos[1] -= 1
        elif d == "^":
            pos[1] += 1

        if pos not in houses:
            visited += 1
            houses.append(pos[:])
        # print(houses, pos)
    return visited

def visit_houses_robot_santa(directions: list):
    visited = 1
    santa_pos = [0,0]
    robot_santa_pos = [0,0]
    houses = [santa_pos[:]]

    for i in range(0, len(directions), 2):
        if directions[i] == ">":
            santa_pos[0] += 1
        elif directions[i] == "<":
            santa_pos[0] -= 1
        elif directions[i] == "v":
            santa_pos[1] -= 1
        elif directions[i] == "^":
            santa_pos[1] += 1

        if directions[i+1] == ">":
            robot_santa_pos[0] += 1
        elif directions[i+1] == "<":
            robot_santa_pos[0] -= 1
        elif directions[i+1] == "v":
            robot_santa_pos[1] -= 1
        elif directions[i+1] == "^":
            robot_santa_pos[1] += 1

        if santa_pos not in houses:
            visited += 1
            houses.append(santa_pos[:])
        if robot_santa_pos not in houses:
            visited += 1
            houses.append(robot_santa_pos[:])
        # print(houses, santa_pos, robot_santa_pos)
    return visited
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    directions = load_data(args.mode)
    visits = visit_houses(directions)
    print(visits)

    robot_visits = visit_houses_robot_santa(directions)
    print(robot_visits)