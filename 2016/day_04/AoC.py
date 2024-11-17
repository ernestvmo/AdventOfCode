from aocd.models import Puzzle
from argparse import ArgumentParser
from collections import Counter
from string import ascii_lowercase

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 3).example_data.splitlines()
        with open("./2016/day_04/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 4).input_data.splitlines()
    
    rooms = []
    for line in data:
        line = line.rstrip("\n")
        *encryted_name, rest = line.split('-')
        sector_id, checksum = rest.split('[')
        checksum = checksum[:-1]
        rooms.append([encryted_name, int(sector_id), checksum])
    return rooms

def count_valid_rooms(rooms: list[list]):
    valid_rooms = []
    for room in rooms:
        encrypted_name, _, checksum = room
        tuples = Counter(''.join(encrypted_name)).most_common()
        sorted_tuples = sorted(tuples, key=lambda x:(-x[1], x[0]))
        if checksum == ''.join([letter for letter, _ in sorted_tuples[:5]]):
            valid_rooms.append(room)
    return sum([sector_id for _, sector_id, _ in valid_rooms])

def caesar_cipher(rooms: list[list]):
    for room in rooms:
        encrypted_name, sector_id, _ = room
        key = sector_id % 26
        decrypted_name = []
        for word in encrypted_name:
            encrypted_word = ''
            for letter in word:
                u = ascii_lowercase.index(letter) + key
                if u >= 26:
                    u -= 26
                encrypted_word += str(ascii_lowercase[u])
            decrypted_name.append(encrypted_word)
        if "object".lower() in ' '.join(decrypted_name):
            return sector_id


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    rooms = load_data(args.mode)
    total = count_valid_rooms(rooms)
    print(total)

    total = caesar_cipher(rooms)
    print(total)