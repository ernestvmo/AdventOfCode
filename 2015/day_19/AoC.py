from aocd.models import Puzzle
from argparse import ArgumentParser
import re
import random as rnd

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_19/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 19).input_data.splitlines()

    molecule = data[-1]
    molecule = re.findall(r'[A-Z][^A-Z]*', molecule)    

    data = data[:-2]

    replacements = {}
    for line in data:
        letter, replacement = line.rstrip("\n").split(" => ")
        if letter in replacements.keys():
            replacements[letter].append(replacement)
        else:
            replacements[letter] = [replacement]

    return molecule, replacements

def find_possible_replacements(molecule: list[str], replacements: dict[list]):
    possibilities = []
    for i in range(len(molecule)):
        if molecule[i] in replacements.keys():
            for replacement in replacements[molecule[i]]:
                possibilities.append(''.join(molecule[:i] + [replacement] + molecule[i+1:]))
    return list(set(possibilities))

def fabricate_molecule(molecule: str, replacements: dict[list]):
    from_to_replacements = []
    for from_ in replacements:
        for to_ in replacements[from_]:
            from_to_replacements.append((from_, to_))

    count = shuffles = 0
    m = molecule
    while len(m) > 1:
        start = m
        for from_, to_ in from_to_replacements:
            while to_ in m:
                count += m.count(to_)
                m = m.replace(to_, from_)

        if start == m:
            rnd.shuffle(from_to_replacements)
            m = molecule
            count = 0
            shuffles += 1
    
    return count, shuffles


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    molecule, replacements = load_data(args.mode)
    total = find_possible_replacements(molecule, replacements)
    print(len(total))

    total, _ = fabricate_molecule("".join(molecule), replacements)
    print(total)