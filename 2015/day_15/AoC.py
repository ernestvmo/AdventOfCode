from aocd.models import Puzzle
from argparse import ArgumentParser
import itertools

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2015, 15).example_data.splitlines()
    else:
        data = Puzzle(2015, 15).input_data.splitlines()

    cookies = {}
    for line in data:
        line = line.split()
        name, capacity, durability, flavor, texture, calories = line[0].removesuffix(':'), int(line[2].removesuffix(',')), int(line[4].removesuffix(',')), int(line[6].removesuffix(',')), int(line[8].removesuffix(',')), int(line[10])
        cookies[name] = {'capacity':capacity, 'durability':durability, 'flavor':flavor, 'texture':texture, 'calories':calories}
    
    return cookies

def best_combination(cookies: dict[dict], part=1):
    pairs = [range(1,101)]*len(cookies.keys())
    permutations = [combo for combo in itertools.product(*pairs) if sum(combo) == 100]
    best = 0
    for permutation in permutations:
        capacity = durability = flavor = texture = calories = 0
        for p, c in zip(permutation, cookies.keys()):
            capacity += cookies[c]['capacity']*p
            durability += cookies[c]['durability']*p
            flavor += cookies[c]['flavor']*p
            texture += cookies[c]['texture']*p
            calories += cookies[c]['calories']*p
        if capacity <= 0 or durability <= 0 or flavor <= 0 or texture <= 0: 
            continue
        else:
            if part==2 and calories != 500:
                continue
            else:
                best = max(best, capacity*durability*flavor*texture)

    return best


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    cookies = load_data(args.mode)
    total = best_combination(cookies)
    print(total)

    total = best_combination(cookies, part=2)
    print(total)