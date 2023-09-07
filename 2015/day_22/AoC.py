from aocd.models import Puzzle
from argparse import ArgumentParser
import math

def load_data(mode: str):
    if mode == "test":
        with open('./2015/day_22/test.txt') as file:
            data = file.readlines()
    else:
        data = Puzzle(2015, 22).input_data.splitlines()

    enemy = [int([v for v in d.rstrip("\n").split(":")][1]) for d in data]
    return {'HP': enemy[0], 'damage': enemy[1]}

def play_turn(player: dict, enemy: dict, effects: dict, mana_used: int, player_turn: bool):
    if effects['shield'] == 0:
        player['armor'] = 0     
    else:
        effects['shield'] -= 1
    
    if effects['poison'] > 0:
        enemy['HP'] -= 3
        if enemy['HP'] <= 0:
            return mana_used   
        effects['poison'] -= 1

    if effects['recharge'] > 0:
        player['mana'] += 101
        effects['recharge'] -= 1
    
    if player_turn:
        best_mana_used = math.inf

        if player['mana'] >= 53:
            mana_used_next = mana_used + 53
            player_next = player.copy()
            enemy_next = enemy.copy()
            effects_next = effects.copy()
            player_next['mana'] -= 53
            enemy_next['HP'] -= 4

            if enemy_next['HP'] <= 0:
                return mana_used_next

            res = play_turn(player_next, enemy_next, effects_next, mana_used_next, False)
            best_mana_used = min(best_mana_used, res)
    
        if player['mana'] >= 73:
            mana_used_next = mana_used + 73
            player_next = player.copy()
            enemy_next = enemy.copy()
            effects_next = effects.copy()
            player_next['mana'] -= 73
            player_next['HP'] += 2
            enemy_next['HP'] -= 2

            if enemy_next['HP'] <= 0:
                return mana_used_next

            res = play_turn(player_next, enemy_next, effects_next, mana_used_next, False)
            best_mana_used = min(best_mana_used, res)

        if player['mana'] >= 113 and effects['shield'] == 0:
            mana_used_next = mana_used + 113
            player_next = player.copy()
            enemy_next = enemy.copy()
            effects_next = effects.copy()
            player_next['mana'] -= 113
            player_next['armor'] += 7
            effects_next['shield'] = 6
            res = play_turn(player_next, enemy_next, effects_next, mana_used_next, False)
            best_mana_used = min(best_mana_used, res)

        if player['mana'] >= 173 and effects['poison'] == 0:
            mana_used_next = mana_used + 173
            player_next = player.copy()
            enemy_next = enemy.copy()
            effects_next = effects.copy()
            player_next['mana'] -= 173
            effects['poison'] = 6
            res = play_turn(player_next, enemy_next, effects_next, mana_used_next, False)
            best_mana_used = min(best_mana_used, res)

        if player['mana'] >= 229 and effects['recharge'] == 0:
            mana_used_next = mana_used + 229
            player_next = player.copy()
            enemy_next = enemy.copy()
            effects_next = effects.copy()
            player_next['mana'] -= 229
            effects_next['recharge'] = 5
            res = play_turn(player_next, enemy_next, effects_next, mana_used_next, False)
            best_mana_used = min(best_mana_used, res)

        return best_mana_used

    else:
        mana_used_next = mana_used
        player_next = player.copy()
        enemy_next = enemy.copy()
        effects_next = effects.copy()

        player_next['HP'] -= max(enemy_next['damage'] - player_next['armor'], 1)
        if player_next['HP'] <= 0:
            return math.inf
        else:
            return play_turn(player_next, enemy_next, effects_next, mana_used_next, True)

def find_min_mana(enemy: dict, player={'HP': 50, 'mana': 500, 'armor': 0}, effects={'shield': 0, 'poison': 0, 'recharge': 0}):
    return play_turn(player, enemy, effects, 0, True)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("mode", choices=['test', 'input'])
    args = parser.parse_args()

    enemy = load_data(args.mode)
    min_mana = find_min_mana(enemy)
    print(min_mana)