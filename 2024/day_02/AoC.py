import os.path
import re
from collections import Counter

from aocd.models import Puzzle
from argparse import ArgumentParser


def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2019, 1).example_data.splitlines()
        with open(os.path.join(os.path.dirname(__file__), "test.txt")) as file:
            data = file.readlines()
    else:
        data = Puzzle(2024, 2).input_data.splitlines()
    processed_data = [list(map(int, re.findall(r"\d+", n.rstrip()))) for n in data]
    return processed_data


def is_solution_safe(diff: list[int]) -> bool:
    return all(0 < n <= 3 for n in diff) or all(-3 <= n < 0 for n in diff)


def count_safe_reports(reports: list[list[int]], damper: bool = False) -> int:
    count = 0
    for report in reports:
        differences = [j - i for i, j in zip(report[:-1], report[1:])]
        if is_solution_safe(differences):
            count += 1
        elif damper:
            for e in range(len(report)):
                report_ = report[:e] + report[e + 1 :]
                if is_solution_safe([j - i for i, j in zip(report_[:-1], report_[1:])]):
                    count += 1
                    break
    return count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=["test", "input"])
    args = parser.parse_args()

    a = load_data(args.mode)
    res = count_safe_reports(a)
    print(f"part 1: {res}")
    res = count_safe_reports(a, True)
    print(f"part 2: {res}")
