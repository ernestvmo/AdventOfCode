from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 19).example_data.splitlines()
        # with open("./2016/day_19/test.txt") as file:
        #     data = file.readlines()
        data = ['3001330']
    else:
        data = Puzzle(2016, 19).input_data.splitlines()

    return int(data[0])

def white_elephant(elfs: int):
    gifts = {n: 1 for n in range(1, elfs+1)}

    i = 1
    while True:
        if i == 6:
            i = 1
        j = i + 1

        if any([gift==elfs for gift in gifts.values()]):
            return [k for k,v in gifts.items() if v == elfs][0]

        if gifts[i] != 0:
            j = i + 1
            if i == elfs:
                j = 1
            while gifts[j] == 0:
                j += 1 
            gifts[i] += gifts[j]
            gifts[j] = 0
        i += 1
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    elfs = load_data(args.mode)
    total = white_elephant(elfs)
    print(total)