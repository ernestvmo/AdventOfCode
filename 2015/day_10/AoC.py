from aocd.models import Puzzle
from argparse import ArgumentParser

def load_data(mode: str):
    if mode == "test":
        data = ['1']
    else:
        data = Puzzle(2015, 10).input_data.splitlines()

    return data[0]
    
def look_and_say(sequence: str, repeat: int):
    for _ in range(repeat):
        new_sequence = ''

        curr_char = sequence[0]
        if len(sequence) == 1:
            new_sequence = "1" + curr_char
            sequence = new_sequence
        else:
            i = 0
            counter = 1
            while i < len(sequence):
                for j in range(i+1, len(sequence), 1):
                    if sequence[i] == sequence[j]:
                        counter += 1
                    else:
                        to_add = str(counter) + sequence[i]
                        new_sequence += to_add
                        counter = 1
                        i = j-1
                        break
                i += 1
            to_add = str(counter) + sequence[i-1]
            new_sequence += to_add
        sequence = new_sequence
    return sequence


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    sequence = load_data(args.mode) 
    sequence_after = look_and_say(sequence, 40)
    print(len(sequence_after))

    sequence_after = look_and_say(sequence, 50)
    print(len(sequence_after))