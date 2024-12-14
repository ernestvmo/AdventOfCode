import os.path
from collections import Counter
from itertools import chain

from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = [d.rstrip() for d in file.readlines()]
    else:
        data = Puzzle(2024, 9).input_data.splitlines()

    return list(map(int, data[0]))


def file_compact(diskmap: list[int], part_2: bool = False) -> int:
    counter = 0
    pre_compact = []
    for i, n in enumerate(diskmap):
        if i % 2 == 0:
            pre_compact += [counter] * n
            counter += 1
        else:
            pre_compact += ["."] * n
    if not part_2:
        c = Counter(pre_compact)["."]
        nums = [n for n in pre_compact if n != "."][-c:][::-1]
        for n in nums:
            pre_compact[pre_compact.index(".")] = n
        pre_compact = pre_compact[:-c]
    else:
        curr = [pre_compact[0]]
        test = []
        for i in range(1, len(pre_compact)):
            if pre_compact[i] == pre_compact[i - 1]:
                curr.append(pre_compact[i])
            else:
                test.append(curr)
                curr = [pre_compact[i]]
        test.append(curr)
        for i, group in enumerate(test[::-1]):
            if "." not in group:
                moved = [d for d in test if "." in d and len(d) >= len(group)]
                if len(moved) > 0:
                    j = test.index(moved[0])
                    test[j] = group
                    test.reverse()
                    a = test.index(group)
                    test.reverse()
                    test[len(test) - 1 - a] = ["."] * len(group)
                    if len(moved[0]) - len(group) > 0:
                        test.insert(j + 1, moved[0][: len(moved[0]) - len(group)])
        pre_compact = list(chain.from_iterable(test))
    return sum(i * int(n) for i, n in enumerate(pre_compact) if n != ".")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    data = load_data(args.mode)
    res = file_compact(data)
    print(f"part 1: {res}")
    res = file_compact(data, True)
    print(f"part 2: {res}")
