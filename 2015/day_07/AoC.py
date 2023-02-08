from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2015, 7).example_data.splitlines()
    else:
        data = Puzzle(2015, 7).input_data.splitlines()

    instructions = []
    for instruction in data:
        left, target = instruction.rstrip("\n").split(" -> ")
        parts = left.split()
        instructions.append([parts, target])
    return instructions

def build_circuit(instructions: list, key='a', value_b=None):
    wires = {}
    buffer = []

    while len(instructions) > 0 or len(buffer) > 0:
        if len(instructions) > 0:
            left, target = instructions.pop(0)
        else:
            left, target = buffer.pop(0)

        if value_b is not None and target == 'b':
            left = [str(value_b)]

        if len(left) == 1:
            if not left[0].isdigit():
                if left[0] not in wires.keys():
                    buffer.append([left, target])
                    continue
                else:
                    wires[target] = wires[left[0]]
            else:
                wires[target] = int(left[0])
        
        if len(left) == 2:
            if not left[1].isdigit():
                if left[1] not in wires.keys():
                    buffer.append([left, target])
                    continue
                else:
                    wires[target] = wires[left[1]]^65535
            else:
                wires[target] = int(left[1])^65535
        
        if len(left) == 3:
            if not left[0].isdigit():
                if left[0] not in wires.keys():
                    buffer.append([left, target])
                    continue
                else:
                    if "OR" not in left and "AND" not in left:
                        if left[1] == "LSHIFT":
                            wires[target] = wires[left[0]] << int(left[2])
                        elif left[1] == "RSHIFT":
                            wires[target] = wires[left[0]] >> int(left[2])
                    else:
                        if not left[2].isdigit():
                            if left[2] not in wires.keys():
                                buffer.append([left, target])
                                continue
                            else:
                                if left[1] == "OR":
                                    wires[target] = wires[left[0]] | wires[left[2]]
                                elif left[1] == "AND":
                                    wires[target] = wires[left[0]] & wires[left[2]]
                        else:
                            if left[1] == "OR":
                                wires[target] = wires[left[0]] | int(left[2])
                            elif left[1] == "AND":
                                wires[target] = wires[left[0]] & int(left[2])
            else:
                if not left[2].isdigit():
                    if left[2] not in wires.keys():
                        buffer.append([left, target])
                        continue
                    else:
                        if left[1] == "OR":
                            wires[target] = int(left[0]) | wires[left[2]]
                        elif left[1] == "AND":
                            wires[target] = int(left[0]) & wires[left[2]]
                else:
                    if left[1] == "OR":
                        wires[target] = int(left[0]) | int(left[2])
                    elif left[1] == "AND":
                        wires[target] = int(left[0]) & int(left[2])
        
    return wires[key]

def is_root(left: list[str]):
    if len(left) == 1:
        return left[0].isdigit()
    elif len(left) == 2:
        return left[1].isdigit()
    else:
        if "AND" in left or "OR" in left:
            return left[0].isdigit(), left[2].isdigit()
        else:
            return left[0].isdigit()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    instructions = load_data(args.mode)
    a_value = build_circuit(instructions[:])
    print(a_value)

    a_value_bis = build_circuit(instructions[:], value_b=a_value)
    print(a_value_bis)

    