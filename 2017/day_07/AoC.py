from aocd.models import Puzzle
from argparse import ArgumentParser
import re
from collections import Counter


class Tower:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight
        self.subtowers = []
        self.parent = None
        self.carrying_weight = 0
    
    def __repr__(self) -> str:
        return f"tower {self.name} ({self.weight}) with {len(self.subtowers)} subtowers."

    def get_subtowers(self):
        return self.subtowers
    
    def add_subtowers(self, subtower):
        self.subtowers.append(subtower)

    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
    

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 7).example_data.splitlines()
    else:
        data = Puzzle(2017, 7).input_data.splitlines()

    return data

def process_list(data: list):
    has_subtowers = []
    towers = {}
    for line in data:
        if "->" in line:
            has_subtowers.append(line)
            line = line.split("->")[0]
        name = re.findall(r"[a-zA-Z]+", line)[0]
        weight = int(re.findall(r"[0-9]+", line)[0])
        towers[name] = Tower(name, weight)

    for line in has_subtowers:
        tower, *subtowers = re.findall(r"[A-Za-z]+", line)
        for subtower in subtowers:
            towers[tower].add_subtowers(towers[subtower])
            towers[subtower].set_parent(towers[tower])
    return towers
        
def find_bottom(towers: dict[Tower]):
    for tower_key in towers:
        if towers[tower_key].get_parent() is None:
            return tower_key

def find_balanced_weight(towers: dict[Tower]):
    bottom = towers[find_bottom(towers)]
    set_carrying_weights(bottom)
    return find_unbalanced(bottom)

def set_carrying_weights(tower: Tower):
    carrying_weight = tower.weight
    for sub in tower.subtowers:
        if sub is not None:
            carrying_weight += set_carrying_weights(sub)
    tower.carrying_weight = carrying_weight
    return tower.carrying_weight

def find_unbalanced(tower: Tower, o_diff = 0):
    c = Counter([sub.carrying_weight for sub in tower.subtowers])
    unbalanced = min(c, key=c.get)
    balanced = max(c, key=c.get)
    diff = balanced - unbalanced

    if len(c) == 1:
        return tower.weight + o_diff
    else:
        for sub in tower.subtowers:
            if c[sub.carrying_weight] == 1:
                return find_unbalanced(sub, diff)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data = load_data(args.mode)
    towers = process_list(data)
    bottom = find_bottom(towers)
    print(bottom)
    
    mass = find_balanced_weight(towers)
    print(mass)