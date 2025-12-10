#!/usr/bin/env python3
#from utils import describe_current_room , solve_puzzle , attempt_open_treasure

from player_actions import move_player , get_input , use_item, take_item , show_inventory
import utils
from constants import COMMANDS


def process_command(game_state, command) :
    if ' ' in command:
        str_command, str_addition = command.split(' ',1)
    else:
        str_command = command
        str_addition = ''
    match str_command :
        case 'look' :
            utils.describe_current_room(game_state)
        case 'solve' :
           result = False
           while (not result ):
            result = utils.solve_puzzle(game_state)
        case 'use':
            use_item(game_state, str_addition)
        case 'go':
             move_player(game_state,str_addition)
        case 'north' :
            move_player(game_state,str_command)
        case 'south' :
            move_player(game_state,str_command)
        case 'west' :
            move_player(game_state,str_command)
        case 'east' :
            move_player(game_state,str_command)
        case 'take':
            take_item(game_state, str_addition)
        case 'inventory':
            show_inventory(game_state)
        case 'Quit':
            return
        case 'open':
            utils.attempt_open_treasure(game_state)
        case 'openIt':
            utils.solve_puzzle(game_state)
        case 'show_help':
            for key, value in COMMANDS.items() :
                print(f"{key} : {value}")
        case _:
            print('Команда не принята, повторите ввод!')


  
def main():
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0, # Количество шагов 
        'life': 100 #Жизнь игрока
        }
    print("Добро пожаловать в Лабиринт!")
    utils.describe_current_room(game_state)
    while not game_state['game_over'] :
        user_command = get_input()
        process_command(game_state, user_command)
        if (user_command in ['Quit', 'Exit']) :
            game_state['game_over'] = True
    print('Игра завершена')
    return 
    


#main()





  