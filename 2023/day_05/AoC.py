from aocd.models import Puzzle
from argparse import ArgumentParser
from re import findall


def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2023, 5).example_data.splitlines()
        # with open("./2023/day_04/test.txt") as file:
        #     data = file.readlines()
        #     data = [n.rstrip() for n in data]
    else:
        data = Puzzle(2023, 5).input_data.splitlines()
    max_ = 2811999519+10 if mode == "input" else 100
    return data, max_

def make_maps(data):
    maps = {}
    mode = None
    seeds = None
    for line in data:
        if line.startswith("seeds"):
            seeds = [int(n) for n in findall(r"\d+", line)]
        elif line.startswith("seed-"):
            mode = "seed_to_soil"
        elif line.startswith("soil-"):
            mode = "soil_to_fertilizer"
        elif line.startswith("fertilizer-"):
            mode = "fertilizer_to_water"
        elif line.startswith("water-"):
            mode = "water_to_light"
        elif line.startswith("light-"):
            mode = "light_to_temperature"
        elif line.startswith("temperature-"):
            mode = "temperature_to_humidity"
        elif line.startswith("humidity-"):
            mode = "humidity_to_location"
        elif line != "":
            if mode not in maps.keys():
                maps[mode] = {}
            n1, n2, n3 = [int(n) for n in findall(r"\d+", line)]
            maps[mode][(n2, n2+n3, n3)] = (n1, n1+n3, n3)
    return seeds, maps

def make_reverse_maps(data):
    maps = {}
    mode = None
    seeds = None
    for line in data:
        if line.startswith("seeds"):
            seeds = [int(n) for n in findall(r"\d+", line)]
        elif line.startswith("seed-"):
            mode = "seed_to_soil"
        elif line.startswith("soil-"):
            mode = "soil_to_fertilizer"
        elif line.startswith("fertilizer-"):
            mode = "fertilizer_to_water"
        elif line.startswith("water-"):
            mode = "water_to_light"
        elif line.startswith("light-"):
            mode = "light_to_temperature"
        elif line.startswith("temperature-"):
            mode = "temperature_to_humidity"
        elif line.startswith("humidity-"):
            mode = "humidity_to_location"
        elif line != "":
            if mode not in maps.keys():
                maps[mode] = {}
            n1, n2, n3 = [int(n) for n in findall(r"\d+", line)]
            maps[mode][(n1, n1+n3, n3)] = (n2, n2+n3, n3)
    return seeds, maps

def find_lowest_in_map(seeds, map: dict, map_levels: list[str]):
    locations = []
    for seed in seeds:
        for map_level in map_levels:
            range = [n for n in map[map_level].keys() if n[0] <= seed <= n[1]]
            if range != []:
                temp = map[map_level][range[0]]
                seed = temp[0] + (seed - range[0][0])
        locations.append(seed)
    return min(locations), locations

def find_lowest_in_map_reversed(seeds, map: dict, map_levels: list[str]):
    location = seeds[0]
    # while True:
    for location in [82]:
        start = location
        for map_level in map_levels:
            range = [n for n in map[map_level].keys() if n[0] <= location <= n[1]]
            print(range)
            if range != []:
                temp = map[map_level][range[0]]
                print(temp)
                location = temp[0] + (location - range[0][0])
                print(location)
            print(location)
        break
        if location in seeds:
            return start
    # print(locations)
    # return min(locations)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    data, max_ = load_data(args.mode)
    seeds, map = make_maps(data)
    order = ["seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water","water_to_light","light_to_temperature","temperature_to_humidity","humidity_to_location"]
    n, seeds = find_lowest_in_map(seeds, map.copy(), order)
    print(n, seeds)

    _, map = make_reverse_maps(data)
    n = find_lowest_in_map_reversed([82], map.copy(), order)
    print(n)