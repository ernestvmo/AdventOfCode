from aocd.models import Puzzle
from argparse import ArgumentParser
import itertools

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 13).example_data.splitlines()
        # with open("./2017/day_13/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2017, 13).input_data.splitlines()

    return {int(line.split(": ")[0]): int(line.split(": ")[1]) for line in data}

# def move(layers: list[list], q: int = 1) -> list[list]:
#     pos = None
#     caught = []
#     for _ in range(len(layers)):
#         pos = pos + 1 if pos is not None else 0
#         if is_caught(pos, layers):
#             caught.append(pos*len(layers[pos][0]))
#             if q == 2:
#                 return False
#         # print_layers(pos, layers)
#         for layer in layers:
#             if isinstance(layer, list):
#                 i = layer[0].index('S')
#                 layer[0][i] = ""
#                 if layer[1]: 
#                     if i == len(layer[0]) - 1:
#                         layer[1] = False
#                         i -= 1
#                     else:
#                         i += 1
#                 else:
#                     if i == 0:
#                         layer[1] = True
#                         i += 1
#                     else:
#                         i -= 1

#                 layer[0][i] = "S"
#         # print_layers(pos, layers)
#     return sum(caught)

# def move_packets(layers: list[list], delay: int):
#     for _ in range(delay):
#         for layer in layers:
#             if isinstance(layer, list):
#                 i = layer[0].index('S')
#                 layer[0][i] = ""
#                 if layer[1]: 
#                     if i == len(layer[0]) - 1:
#                         layer[1] = False
#                         i -= 1
#                     else:
#                         i += 1
#                 else:
#                     if i == 0:
#                         layer[1] = True
#                         i += 1
#                     else:
#                         i -= 1

#                 layer[0][i] = "S"
#     return layers[:]

# def find_correct_delay(layers: list[list]):
#     for j in range(10000, 15000):
#         delayed_layers = move_packets(deepcopy(layers), j)
#         if not isinstance(move(delayed_layers, q=2), bool):
#             return j


# def is_caught(pos: int, layers: list[list] )-> bool:
#     if isinstance(layers[pos], list):
#         if layers[pos][0].index("S") == 0:
#             return True
#         else:
#             return False
#     else:
#         return False

# def print_layers(pos: int, layers: list[list]):
#     for i in range(len(layers)):
#         print(f"  {i}  ", sep=" ", end="")
#     print()
#     max_depth = max([len(layer[0]) for layer in layers if layer is not None])
#     for _ in range(max_depth):
#         for l in range(len(layers)):
#             if l == pos:
#                 p = ("(", ")")
#             else:
#                 p = ("[", "]")
                
#             if layers[l] is not None:
#                 val = layers[l][0][min(_, len(layers[l][0])-1)]
#                 if _ >= len(layers[l][0]):
#                     val = "     "
#                 else:
#                     if val != "": val = f" {p[0]}{val}{p[1]} "
#                     else: val = f" [ ] "
#                 print(val, sep=" ", end="")
#             else:
#                 if _ == 0:
#                     if pos == l: print(f" {p[0]}.{p[1]} ", sep=" ", end="")
#                     else: print(" ... ", sep=" ", end="")
#                 else:
#                     print("     ", sep=" ", end="")
#         print()

def scan(depth: int, time: int):
    offset = time % ((depth - 1) * 2)
    return 2 * (depth - 1) - offset if offset > depth - 1 else offset

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    layers = load_data(args.mode)
    q1 = sum([pos * layers[pos] for pos in layers if scan(layers[pos], pos) == 0])
    print(q1)
    q2 = next(wait for wait in itertools.count() if not any(scan(layers[pos], pos + wait) == 0 for pos in layers))
    print(q2)
    