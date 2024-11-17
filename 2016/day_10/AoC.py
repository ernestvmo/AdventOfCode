from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2016, 10).example_data.splitlines()
        # with open("./2016/day_09/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2016, 10).input_data.splitlines()

    bots = {}
    outputs = {}
    for line in data:
        if line.startswith("value"):
            _, chip_num, *_, bot_num = line.split()
            if bot_num not in bots.keys():
                bots[bot_num] = {'chips': [int(chip_num)], 'low': None, 'high': None}
            else:
                bots[bot_num]['chips'].append(int(chip_num))
        else:
            _, bot_num, _, _, _, low_to, low_to_bot_num, *_, high_to, high_to_bot_num = line.split()
            if bot_num not in bots.keys():
                bots[bot_num] = {'chips': [], 'low': (low_to, low_to_bot_num), 'high': (high_to, high_to_bot_num)}
            else:
                bots[bot_num]['low'] = (low_to, low_to_bot_num)
                bots[bot_num]['high'] = (high_to, high_to_bot_num)
            if low_to == 'output':
                outputs[low_to_bot_num] = []
            if high_to == 'output':
                outputs[high_to_bot_num] = []
    return bots, outputs

def extract_bots(bots: dict):
    return [bot_num for bot_num in bots.keys() if len(bots[bot_num]['chips']) >= 2]

def find_bot_in_charge(bots: dict, outputs: dict, microchips=[5, 2], part=1):
    two_chips_bots = extract_bots(bots)

    while len(two_chips_bots) > 0:
        for bot in two_chips_bots:
            if part == 1 and sorted(bots[bot]['chips']) == sorted(microchips):
                return bot
                
            if bots[bot]['low'][0] == 'bot':
                bots[bots[bot]['low'][1]]['chips'].append(min(bots[bot]['chips']))
            else:
                outputs[bots[bot]['low'][1]].append(min(bots[bot]['chips']))
            
            if bots[bot]['high'][0] == 'bot':
                bots[bots[bot]['high'][1]]['chips'].append(max(bots[bot]['chips']))
            else:
                outputs[bots[bot]['high'][1]].append(max(bots[bot]['chips']))

            bots[bot]['chips'] = []
        two_chips_bots = extract_bots(bots)
    
    return outputs['0'][0]*outputs['1'][0]*outputs['2'][0]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    bots, outputs = load_data(args.mode)
    total = find_bot_in_charge(bots, outputs, microchips=[61, 17])
    print(total)

    total = find_bot_in_charge(bots, outputs, microchips=[61, 17], part=2)
    print(total)