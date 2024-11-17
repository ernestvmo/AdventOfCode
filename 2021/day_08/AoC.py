from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        # data = Puzzle(2021, 8).example_data.splitlines()
        with open("./2021/day_08/test.txt") as file:
            data = file.readlines()
    else:
        data = Puzzle(2021, 8).input_data.splitlines()

    signals = []
    for line in data:
        line = line.rstrip("\n")
        patterns, output = line.split(" | ")
        signals.append([patterns.split(" "), output.split(" ")])
    return signals

def decypher_signal(signal: list):
    letters = {'a': None, 
               'b': None, 
               'c': None,
               'd': None,
               'e': None,
               'f': None,
               'g': None}
    
    one = [''.join(sorted(pattern)) for pattern in signal if len(pattern) == 2][0]
    seven = [''.join(sorted(pattern)) for pattern in signal if len(pattern) == 3][0]
    four = [''.join(sorted(pattern)) for pattern in signal if len(pattern) == 4][0]
    eight = [''.join(sorted(pattern)) for pattern in signal if len(pattern) == 7][0]

    two_three_five = [''.join(pattern) for pattern in signal if len(pattern) == 5]

    letters['a'] = [c for c in seven if c not in one][0]

    three = [three for three in two_three_five if one[0] in three and one[1] in three][0]
    d_g = three.replace(one[0], "").replace(one[1], "").replace(letters['a'], "")
    letters['d'] = [c for c in d_g if c in four][0]
    letters['g'] = d_g.replace(letters['d'], "")
    letters['b'] = four.replace(letters['d'], '').replace(one[0], '').replace(one[1], '')

    five = [num for num in two_three_five if letters['b'] in num][0]
    letters['f'] = five.replace(letters['a'], '').replace(letters['b'], '').replace(letters['d'], '').replace(letters['g'], '')
    letters['c'] = one.replace(letters['f'], '')
    letters['e'] = eight.replace(letters['a'], '').replace(letters['b'], '').replace(letters['c'], '').replace(letters['d'], '').replace(letters['f'], '').replace(letters['g'], '')

    # print("zero", zero)
    # print("one", one)
    # # print("two", two)
    # # print("three", three)
    # print("four", four)
    # # print("five", five)
    # print("six", six)
    # print("seven", seven)
    # print("eight", eight)
    # print("nine", nine)

    return letters

def display_digit(output: str, letters: dict):
    print(output, letters)
    for digit in output:
        print(" "+('a'*4 if letters['a'] in digit else ' '*4))
        print(('b' if letters['b'] in digit else ' ')+' '*4+('c' if letters['c'] in digit else ' '))
        print(('b' if letters['b'] in digit else ' ')+' '*4+('c' if letters['c'] in digit else ' '))
        print(" "+('d'*4 if letters['d'] in digit else ' '*4))
        print(('e' if letters['e'] in digit else ' ')+' '*4+('f' if letters['f'] in digit else ' '))
        print(('e' if letters['e'] in digit else ' ')+' '*4+('f' if letters['f'] in digit else ' '))
        print(" "+('g'*4 if letters['g'] in digit else ' '*4) + "\n")

def decypher_output(output: str, letters: dict):
    output_value = ''
    for digit in output:
        if len(digit) == 2:
            output_value += '1'
        elif len(digit) == 3:
            output_value += '7'
        elif len(digit) == 4:
            output_value += '4'
        elif len(digit) == 7:
            output_value += '8'
        elif len(digit) == 5:
            if letters['c'] in digit and letters['f'] in digit:
                output_value += '3'
            elif letters['c'] in digit and letters['e'] in digit:
                output_value += '2'
            else:
                output_value += '5'
        else:
            if letters['d'] not in digit:
                output_value += '0'
            else:
                if letters['e'] in digit:
                    output_value += '6'
                else:
                    output_value += '9'

    return int(output_value)


def count_digits(signals: list):
    count = 0
    for _, output in signals:
        for digit in output:
            if len(digit) != 5 and len(digit) != 6:
                count += 1
    return count

def sum_digits(signals: list):
    total = 0
    for signal, output in signals:
        letters = decypher_signal(signal)
        output_val = decypher_output(output, letters)
        total += output_val
    return total

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    signals = load_data(args.mode)
    total = count_digits(signals)
    print(total)

    total = sum_digits(signals)
    print(total)