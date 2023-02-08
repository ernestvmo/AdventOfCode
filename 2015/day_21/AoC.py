from aocd.models import Puzzle
from argparse import ArgumentParser
from itertools import permutations

def load_data(mode: str):
    with open('./2015/day_21/shop_items.txt') as file:
        shop_item = file.readlines()

    if mode == "test":
        with open('./2015/day_21/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 21).input_data.splitlines()

    shop_items = [[], [], []]
    i = 0
    for line in shop_item:
        line = line.rstrip("\n")
        if line == "":
            i += 1
        else:
            shop_items[i].append(line.split())
    W, A, R = shop_items

    weapons = {}
    for w in W[1:]:
        weapons[w[0]] = {W[0][1].lower():int(w[1]), W[0][2].lower():int(w[2]), W[0][3].lower():int(w[3])}

    armors = {}
    for a in A[1:]:
        armors[a[0]] = {A[0][1].lower():int(a[1]), A[0][2].lower():int(a[2]), A[0][3].lower():int(a[3])}
    armors['none'] = {A[0][1].lower(): 0, A[0][2].lower(): 0, A[0][3].lower(): 0}

    rings = {}
    for r in R[1:]:
        rings[r[0] + " " + r[1]] = {R[0][1].lower():int(r[2]), R[0][2].lower():int(r[3]), R[0][3].lower():int(r[4])}
    rings['none'] = {R[0][1].lower(): 0, R[0][2].lower(): 0, R[0][3].lower(): 0}

    enemy = [int([v for v in d.rstrip("\n").split(":")][1]) for d in data]
    enemy = {'HP': enemy[0], 'damage': enemy[1], 'armor': enemy[2]}

    return (weapons, armors, rings), enemy

def setup_permutations(weapons: dict[dict], armors: dict[dict], rings: dict[dict], enemy: dict):
    possibilities = []
    for weapon in weapons.keys():
        for armor in armors.keys():
            for ring_1 in rings.keys():
                for ring_2 in rings.keys():
                    if ring_1 != ring_2:
                        possibilities.append([weapon, armor, ring_1, ring_2])
    return possibilities

def evaluate_winner(player: dict, enemy: dict):
    HP = 100
    enemy_HP = enemy['HP']
    while True:
        # print(f"Health at start: enemy [{enemy_HP}] - player [{HP}]")
        damage = max(player['damage'] - enemy['armor'], 1)
        enemy_HP -= damage
        if enemy_HP <= 0:
            return True
        
        damage = max(enemy['damage'] - player['armor'], 1)
        HP -= damage
        if HP <= 0:
            return False
        # print(f"Health at end: enemy [{enemy_HP}] - player [{HP}]")


def find_best_setup(weapons: dict[dict], armors: dict[dict], rings: dict[dict], enemy: dict):
    setups = setup_permutations(weapons, armors, rings, enemy)
    min_cost = 1000
    winning_setups = []
    for w, a, r_1, r_2 in setups:
        cost = weapons[w]['cost'] + armors[a]['cost'] + rings[r_1]['cost'] + rings[r_2]['cost']
        player = {'damage': weapons[w]['damage'] + rings[r_1]['damage'] + rings[r_2]['damage'], 
        'armor':  armors[a]['armor'] + rings[r_1]['armor'] + rings[r_2]['armor']}
        # player = {'damage': 5, 'armor':  5}
        
        if evaluate_winner(player, enemy):
            winning_setups.append([w, a, r_1, r_2])
            min_cost = min(min_cost, cost)
    
    return min_cost

def find_worst_setup(weapons: dict[dict], armors: dict[dict], rings: dict[dict], enemy: dict):
    setups = setup_permutations(weapons, armors, rings, enemy)
    max_cost = 0
    winning_setups = []
    for w, a, r_1, r_2 in setups:
        cost = weapons[w]['cost'] + armors[a]['cost'] + rings[r_1]['cost'] + rings[r_2]['cost']
        player = {'damage': weapons[w]['damage'] + rings[r_1]['damage'] + rings[r_2]['damage'], 
        'armor':  armors[a]['armor'] + rings[r_1]['armor'] + rings[r_2]['armor']}
        # player = {'damage': 5, 'armor':  5}
        
        if not evaluate_winner(player, enemy):
            winning_setups.append([w, a, r_1, r_2])
            max_cost = max(max_cost, cost)
    
    return max_cost
        

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    (weapons, armors, rings), enemy = load_data(args.mode)
    total = find_best_setup(weapons, armors, rings, enemy)
    print(total)

    total = find_worst_setup(weapons, armors, rings, enemy)
    print(total)