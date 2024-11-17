from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        data = Puzzle(2017, 18).example_data.splitlines()
        # with open("./2017/day_18/test.txt") as file:
        #     data = file.readlines()
    else:
        data = Puzzle(2017, 18).input_data.splitlines()

    registers = {}
    instructions = []
    for line in data:
        c, r, *r_ = line.split()
        if r not in registers.keys():
            registers[r] = 0
        if r_ != []:
            r_ = r_[0]
            if r_[0] == "-" or r_.isnumeric():
                r_ = int(r_)
            elif r_ not in registers.keys():
                registers[r_] = 0
            instructions.append([c, r, r_])
        else:    
            instructions.append([c, r])
    
    return registers, instructions

def execute(registers: dict, instructions: list, q="1"):
    last_played = None
    i = 0
    if q == "2": registers["p"] = 1
    send = send_ = 0
    while i < len(instructions):
        if instructions[i][0] == "snd":
            last_played = registers[instructions[i][1]]
            send += 1
            send_ += 1
        elif instructions[i][0] == "set":
            if isinstance(instructions[i][2], int):
                registers[instructions[i][1]] = instructions[i][2]
            else:
                registers[instructions[i][1]] = registers[instructions[i][2]]
        elif instructions[i][0] == "add":
            if isinstance(instructions[i][2], int):
                registers[instructions[i][1]] += instructions[i][2]
            else:
                registers[instructions[i][1]] += registers[instructions[i][2]]
        elif instructions[i][0] == "mul":
            if isinstance(instructions[i][2], str):
                registers[instructions[i][1]] *= registers[instructions[i][2]]
            else:
                registers[instructions[i][1]] *= instructions[i][2]
        elif instructions[i][0] == "mod":
            if isinstance(instructions[i][2], str):
                registers[instructions[i][1]] %= registers[instructions[i][2]]
            else:
                registers[instructions[i][1]] %= instructions[i][2]
        elif instructions[i][0] == "rcv":
            if registers[instructions[i][1]] != 0:
                registers[instructions[i][1]] = last_played
                if q == "1": return last_played
                send_ -= 1
                if q == "2" and send_ == -1: return send
        elif instructions[i][0] == "jgz":
            if registers[instructions[i][1]] > 0:
                if instructions[i][2] > 0:
                    i += instructions[i][2]
                else:
                    i += (instructions[i][2]-1)
        i += 1

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    registers, instructions = load_data(args.mode)
    n = execute(registers.copy(), instructions, "1")
    print(n)

    n = execute(registers.copy(), instructions, "2")
    print(n)


# from aocd.models import Puzzle
# from argparse import ArgumentParser

# def load_data(mode: str):
#     if mode == "test":
#         data = Puzzle(2017, 18).example_data.splitlines()
#         # with open("./2017/day_18/test.txt") as file:
#         #     data = file.readlines()
#     else:
#         data = Puzzle(2017, 18).input_data.splitlines()

#     registers = {}
#     instructions = []
#     for line in data:
#         c, r, *r_ = line.split()
#         if r not in registers.keys():
#             registers[r] = 0
#         if r_ != []:
#             r_ = r_[0]
#             if r_[0] == "-" or r_.isnumeric():
#                 r_ = int(r_)
#             elif r_ not in registers.keys():
#                 registers[r_] = 0
#             instructions.append([c, r, r_])
#         else:    
#             instructions.append([c, r])
    
#     return registers, instructions

# def execute(registers: dict, instructions: list, q="1"):
#     last_played, i = None, 0
#     if q == "2": registers["p"] = 1
#     send = send_ = 0
#     while i < len(instructions):
#         if instructions[i][0] == "snd":
#             last_played = registers[instructions[i][1]]
#             send += 1
#             send_ += 1
#         elif instructions[i][0] == "set":
#             value = instructions[i][2] if isinstance(instructions[i][2], int) else registers[instructions[i][2]]
#             registers[instructions[i][1]] = value
#         elif instructions[i][0] == "add":
#             adder = instructions[i][2] if isinstance(instructions[i][2], int) else registers[instructions[i][2]]
#             registers[instructions[i][1]] += adder
#         elif instructions[i][0] == "mul":
#             multiplier = instructions[i][2] if isinstance(instructions[i][2], int) else registers[instructions[i][2]]
#             registers[instructions[i][1]] *= multiplier
#         elif instructions[i][0] == "mod":
#             moduler = instructions[i][2] if isinstance(instructions[i][2], int) else registers[instructions[i][2]]
#             registers[instructions[i][1]] %= moduler
#         elif instructions[i][0] == "rcv":
#             if registers[instructions[i][1]] != 0:
#                 registers[instructions[i][1]] = last_played
#                 if q == "1": return last_played
#                 send_ -= 1
#                 if q == "2" and send_ == -1: return send
#         elif instructions[i][0] == "jgz":
#             if registers[instructions[i][1]] > 0:
#                 offset = instructions[i][2] if isinstance(instructions[i][2], int) else registers[instructions[i][2]]
#                 if offset > 0:
#                     offset = offset-1
#                 i += offset
#         i += 1

# if __name__ == "__main__":
#     parser = ArgumentParser()
#     parser.add_argument("mode", choices=['test', 'input'])
#     args = parser.parse_args()

#     registers, instructions = load_data(args.mode)
#     n = execute(registers.copy(), instructions, "1")
#     print(n)

#     n = execute(registers.copy(), instructions, "2")
#     print(n)