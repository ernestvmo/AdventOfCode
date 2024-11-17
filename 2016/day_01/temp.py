#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def main():
    with open('./2016/day_01/test.txt') as input_file:
        content = input_file.read().replace('\n', '').split(', ')

    position = 0 + 0j
    direction = 0 + 1j
    grid = np.ndarray((2000,2000))

    grid[0, 0] = 1

    result_2 = None

    for step in content:
        if step[0] == 'L':
            direction *= 1j
        else:
            direction *= -1j

        step_len = int(step[1:])

        for i in range(0, step_len):
            position += direction
            grid[int(position.real)][int(position.imag)] += 1
            if grid[int(position.real)][int(position.imag)] >= 2 and result_2 is None:
                result_2 = int(abs(position.real) + abs(position.imag))

    # with open('./2016/day_01/output.txt', 'w+') as output_file:
    print(str(int(abs(position.real) + abs(position.imag))) + "\n")
        # output_file.write(str(result_2))


if __name__ == '__main__':
    main()