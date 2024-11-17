from aocd.models import Puzzle
from argparse import ArgumentParser
from hashlib import md5

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 5).example_data.splitlines()
        with open("./2016/day_05/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 5).input_data.splitlines()
        
    return data[0]

def first_door(secret_key: str):
    password = ''
    for i in range(10**10):
        hex = md5(str(secret_key + str(i)).encode()).hexdigest()
        if hex[:5] == '00000':
            password += str(hex[5])
            if len(password) == 8:
                return password

def second_door(secret_key: str):
    password = [None]*8
    for i in range(10**10):
        hex = md5(str(secret_key + str(i)).encode()).hexdigest()
        if hex[:5] == '00000':
            if hex[5].isdigit() and int(hex[5]) < len(password) and password[int(hex[5])] is None:
                password[int(hex[5])] = hex[6]
            if None not in password:
                return ''.join(password)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    door_id = load_data(args.mode)
    password = first_door(door_id)
    print(password)

    password = second_door(door_id)
    print(password)