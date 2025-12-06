#!/usr/bin/env python3
from utils import *
from player_actions import *



  
def main():
    game_state = {
        'player_inventory': [], # Инвентарь игрока
        'current_room': 'entrance', # Текущая комната
        'game_over': False, # Значения окончания игры
        'steps_taken': 0 # Количество шагов 
        }
    print("Добро пожаловать в Лабиринт!")
    describe_current_room(game_state)
    cycle = ''
    while cycle not in ['quit' , 'exit']:
        user_command = get_input()
        process_command(game_state, user_command)
        cycle = user_command
    print('Игра завершена')
    return 
    
def process_command(game_state, command) :
    if ' ' in command:
        str_command, str_addition = command.split(' ',1)
    else:
        str_command = command
        str_addition = ''
    match str_command :
        case 'look' :
            describe_current_room(game_state)
        case 'solve' :
           result = False
           while (result == False):
            result = solve_puzzle(game_state)
        case 'use':
            use_item(game_state, str_addition)
        case 'go':
             move_player(game_state,str_addition)
        case 'take':
            take_item(game_state, str_addition)
        case 'inventory':
            show_inventory(game_state)
        case 'quit':
            return
        case 'open':
            attempt_open_treasure(game_state)
        case _:
            print('Команда не принята, повторите ввод!')
    









main()





  