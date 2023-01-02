from aocd.models import Puzzle
from argparse import ArgumentParser

# 2*l*w + 2*w*h + 2*h*l
def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2015, 2).example_data.splitlines()
        with open('./2015/day2/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 2).input_data.splitlines()
    
    measures = []
    for line in data:
        l,w,h = line.split('x')
        measures.append([int(l),int(w),int(h)])
    return measures

def calculate_area(measure: list):
    l, w, h = measure
    s1, s2, s3 = 2*l*w, 2*w*h, 2*h*l
    slack = min(s1, s2, s3) / 2
    return s1 + s2 + s3 + slack

def sum_areas(measures: list):
    areas = []
    for measure in measures:
        area = calculate_area(measure)
        areas.append(area)
    return sum(areas), areas

def calculate_ribbon(measure: list):
    l, w, h = measure
    mins = sorted(measure)[:2]
    wrap = 2*mins[0] + 2*mins[1]
    ribbon = l*w*h
    return wrap + ribbon

def sum_ribbons(measures: list):
    ribbons = []
    for measure in measures:
        ribbon = calculate_ribbon(measure)
        ribbons.append(ribbon)
    return sum(ribbons), ribbons

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input", choices=['test', 'input'])
    args = parser.parse_args()

    measures = load_data(args.input)
    total, areas = sum_areas(measures)
    print(int(total))
    total, ribbons = sum_ribbons(measures)
    print(int(total))