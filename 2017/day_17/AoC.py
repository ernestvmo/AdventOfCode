from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        return 3
    else:
        return int(Puzzle(2017, 17).input_data.splitlines()[0])

def spinlock(steps: int, stop=2018):
    buffer = []
    for i in range(stop):
        if len(buffer) == 0:
            buffer.append(i)
        else:
            pos = (buffer.index(i-1) + steps) % len(buffer)
            buffer.insert(pos+1, i)
    if stop == 2018:
        return buffer[buffer.index(2017)+1]
    else:
        return buffer[buffer.index(0) + 1]
    



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    n = spinlock(data)
    print(n)

    n = spinlock(data, 10**7*5)
    print(n)