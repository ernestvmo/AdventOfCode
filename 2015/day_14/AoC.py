from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str, part=1):
    if mode == "test":
        with open("./2015/day_14/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 14).input_data.splitlines()

    reindeers = {}
    for line in data:
        line = line.rstrip("\n")
        line = line.split()
        reindeer = {'speed':int(line[3]), 'endurance':int(line[6]), 'rest': int(line[13]), 'distance':0, 'flag':[]}
        if part==2:
            reindeer['points'] = 0
        reindeers[line[0]] = reindeer
    
    return reindeers
    
def lead_after_x(reindeers: dict, x: int):
    for i in range(x):
        for k in reindeers.keys():
            if reindeers[k]['flag'] == []:
                reindeers[k]['flag'] = ['flying', i+reindeers[k]['endurance']]
            
            if reindeers[k]['flag'][0] == 'resting':
                if reindeers[k]['flag'][1] == i:
                    reindeers[k]['flag'] = ['flying', i+reindeers[k]['endurance']]

            if reindeers[k]['flag'][0] == 'flying':
                if reindeers[k]['flag'][1] == i:
                    reindeers[k]['flag'] = ['resting', i+reindeers[k]['rest']]
                else:
                    reindeers[k]['distance'] += reindeers[k]['speed']

    return max([reindeers[k]['distance'] for k in reindeers.keys()])
    
def points_after_x(reindeers: dict, x: int):
    for i in range(x):
        lead = 0
        for k in reindeers.keys():
            if reindeers[k]['flag'] == []:
                reindeers[k]['flag'] = ['flying', i+reindeers[k]['endurance']]
            
            if reindeers[k]['flag'][0] == 'resting':
                if reindeers[k]['flag'][1] == i:
                    reindeers[k]['flag'] = ['flying', i+reindeers[k]['endurance']]

            if reindeers[k]['flag'][0] == 'flying':
                if reindeers[k]['flag'][1] == i:
                    reindeers[k]['flag'] = ['resting', i+reindeers[k]['rest']]
                else:
                    reindeers[k]['distance'] += reindeers[k]['speed']
            
            lead = max(lead, reindeers[k]['distance'])

        for k in reindeers.keys():
            if reindeers[k]['distance'] == lead:
                reindeers[k]['points'] += 1

    return max([reindeers[k]['points'] for k in reindeers.keys()])

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    reindeers = load_data(args.mode)
    total = lead_after_x(reindeers, 2503)
    print(total)

    reindeers = load_data(args.mode, part=2)
    total = points_after_x(reindeers, 2503)
    print(total)