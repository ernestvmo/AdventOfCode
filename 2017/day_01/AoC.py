from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        with open("./2017/day_01/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2017, 1).input_data.splitlines()
    
    return data[0]

def captcha_solve(input: str):
    sum = 0
    for i in range(len(input)):
        if i < len(input)-1:
            if input[i] == input[i+1]:
                sum += int(input[i])
        else:
            if input[i] == input[0]:
                sum += int(input[i])
    return sum

def captcha_solve_middle(input: str):
    sum = 0
    l2 = input[len(input)//2:]+input[:len(input)//2]
    for c1,c2 in zip(input, l2):
        if c1 == c2:
            sum += int(c1)
    return sum
            

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    sequence = load_data(args.mode)
    sum = captcha_solve(sequence)
    print(sum)
    sum = captcha_solve_middle(sequence)
    print(sum)