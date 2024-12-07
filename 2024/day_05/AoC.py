import os.path
import re
from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = list(map(str.rstrip, file.readlines()))
    else:
        data = Puzzle(2024, 5).input_data.splitlines()

    page_ordering, updates = data[: data.index("")], data[data.index("") + 1 :]
    page_ordering_dict = {}
    for o in [re.split(r"\|", o) for o in page_ordering]:
        if int(o[0]) in page_ordering_dict:
            page_ordering_dict[int(o[0])].append(int(o[1]))
        else:
            page_ordering_dict[int(o[0])] = [int(o[1])]
    updates = [list(map(int, u.split(","))) for u in updates]
    return page_ordering_dict, updates


def insertion_sort(ordering: dict[int, int], array: list[int]) -> list[int]:
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        if ordering.get(key):
            while j >= 0 and array[j] in ordering.get(key):
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
    return array


def process_updates(
    ordering: dict[int, list[int]], updates: list[list[int]], part_2: bool = False
) -> int:
    pages_mid_total = 0
    for update in updates:
        sorted_update = insertion_sort(ordering, update[:])
        if update == sorted_update and not part_2:
            pages_mid_total += update[len(update) // 2]
        elif update != sorted_update and part_2:
            pages_mid_total += sorted_update[len(sorted_update) // 2]
    return pages_mid_total


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    ordering, updates = load_data(args.mode)
    res = process_updates(ordering=ordering, updates=updates)
    print(f"part 1: {res}")
    res = process_updates(ordering=ordering, updates=updates, part_2=True)
    print(f"part 2: {res}")
