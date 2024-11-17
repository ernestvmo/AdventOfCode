from aocd.models import Puzzle
from argparse import ArgumentParser
import re

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2016, 7).example_data.splitlines()
        with open("./2016/day_07/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2016, 7).input_data.splitlines()

    ipv7s = []
    for line in data:
        line = line.rstrip("\n")
        ipv7 = []
        for center in re.findall(r'\[[a-z]+\]', line):
            if ']' not in line[:line.find(center)]:
                left = line[:line.find(center)]
            else:
                left = line[line[:line.find(center)].rfind(']')+1:line.find(center)]

            if ']' not in line[line.find(center) + len(center):]:
                right = line[line.find(center) + len(center):]
            else:
                right = line[line.find(center) + len(center):][:line[line.find(center) + len(center):].find('[')]
            ipv7.append([left, center[1:-1], right])
        ipv7s.append(ipv7)
    return ipv7s

def check_ABBA(block: str):
    for i in range(0, len(block)-3):
        # print(block[i], block[i+1], block[i+2], block[i+3])
        if block[i] == block[i+3] and block[i+1] == block[i+2] and block[i] != block[i+1]:
            return True
    return False

def count_valid_ips_ABBA(ipv7s: list):
    valid_ips = 0
    for ipv7 in ipv7s:
        ip_valid = False
        for IP in ipv7:
            left, center, right = IP

            if check_ABBA(center):
                ip_valid = False
                break

            if not check_ABBA(center) and (check_ABBA(left) or check_ABBA(right)):
                ip_valid = True

        if ip_valid:
            valid_ips += 1
    return valid_ips

def check_ABA_BAB(block: str, centers: list[str]):
    ABA = []
    for i in range(0, len(block)-2):
        if block[i] == block[i+2] and block[i] != block[i+1]:
            ABA.append(block[i:i+3])

    for group in ABA:
        reverse_group = group[1] + group[0] + group[1]
        for center in centers:
            if reverse_group in center:
                return True
    return False

def count_valid_ips_ABA_BAB(ipv7s: list):
    valid_ips = 0
    for ipv7 in ipv7s:
        ip_valid = False
        centers = [center for left, center, right in ipv7]
        for IP in ipv7:
            left, _, right = IP

            if check_ABA_BAB(left, centers) or check_ABA_BAB(right, centers):
                ip_valid = True

        if ip_valid:
            valid_ips += 1
    return valid_ips


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    ipv7s = load_data(args.mode)
    total = count_valid_ips_ABBA(ipv7s)
    print(total)

    total = count_valid_ips_ABA_BAB(ipv7s)
    print(total)