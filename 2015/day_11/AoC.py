from aocd.models import Puzzle
from argparse import ArgumentParser
from string import ascii_lowercase

def load_data(mode: str):
    if mode == "test":
        data = ['ghijklmn']
    else:
        data = Puzzle(2015, 11).input_data.splitlines()

    return data[0]

def next_password(password: str):
    password = password[::-1]
    new_password = ''
    amount_to_increase = 1
    for i in range(len(password)):
        if amount_to_increase != 0:
            if ascii_lowercase.index(password[i])+1 != len(ascii_lowercase):
                new_password += ascii_lowercase[ascii_lowercase.index(password[i])+amount_to_increase] + password[i+1:]
                amount_to_increase = 0
            else:
                new_password += 'a'
    return new_password[::-1]

def is_valid(pwd: str):
    valid = False
    for i in range(len(pwd) - 2):
        if ascii_lowercase.index(pwd[i]) + 1 == ascii_lowercase.index(pwd[i+1]) and ascii_lowercase.index(pwd[i]) + 2 == ascii_lowercase.index(pwd[i+2]):
            valid = True
    if not valid: return valid

    if 'o' in pwd or 'i' in pwd or 'l' in pwd: return False

    valid = False
    pairs = []
    for i in range(len(pwd) - 1):
        if pwd[i] == pwd[i+1] and (i not in pairs and i+1 not in pairs):
            pairs.append(i)
            pairs.append(i+1)
        if len(pairs) == 4:
            valid = True
            break
    return valid

def find_next_password(current_password: str):
    while True:
        next_pwd = next_password(current_password)
        if is_valid(next_pwd): return next_pwd
        else: current_password = next_pwd

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    password = load_data(args.mode)
    new_password = find_next_password(password)
    print(new_password)

    new_password = find_next_password(new_password)
    print(new_password)
