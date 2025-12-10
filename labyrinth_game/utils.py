# labyrinth_game/utils.py
from constants import ROOMS
 #from player_actions import *
#from player_actions import use_item
#import constants

import player_actions , math






def describe_current_room(game_state):
    current_items_list_print = str()
    current_availe_exits_print = str()
    current_room = ROOMS[game_state['current_room']]
    current_room_print_name = game_state['current_room'].upper()
    current_room_defenition = current_room['description']
    
    current_items_list = current_room['items']

    for value in current_items_list:
        current_items_list_print += ' ' + value

#    current_availe_exits = list(current_room['exits'].values())
    for key, value in current_room['exits'].items():
        current_availe_exits_print = current_availe_exits_print + ' '+ key + '->' + value 
    if (current_room.get('puzzle')) :  
        current_puzzle_enable = "Кажется, здесь есть загадка (используйте команду solve)."
    else:
        current_puzzle_enable = 'Загадок нет'

    if(game_state['current_room'] == 'treasure_room') :
        print('Вы в сокровищнице, вы можете попытаться открыть сундук (используйте команду open)')
    print(f"Название текущей комнаты: {current_room_print_name}\nОписание комнаты: {current_room_defenition}\nЗаметные предметы: {current_items_list_print}\nДоступные выходы: {current_availe_exits_print}\nСообщение о наличии загадки: {current_puzzle_enable}")

def solve_puzzle(game_state):
    puzzle = ROOMS[game_state['current_room']].get('puzzle')
    if (puzzle):
        print(puzzle[0])
        result = str(input('Ваш ответ:'))
        if (puzzle[1] == result):
            print('Вы ответили правильно')
            ROOMS[game_state['current_room']].pop('puzzle', None)
            if (game_state['current_room'] == 'treasure_room') : 
                print("Вы применяете код, и замок щёлкает. Сундук открыт!\nВ сундуке сокровище! Вы победили!")
                game_state['game_over'] = True
                ROOMS['treasure_room'].get('items').remove('treasure_chest')
            else :
                return True
        else:
            print('Ответ не правильный')
            trigger_trap(game_state)
    else:
        print('Загадок здесь нет')
        return False
    
def attempt_open_treasure(game_state):
    # Если мы в сокровищнецы
    if ('treasure_chest' in ROOMS[game_state['current_room']].get('items')):
        if ('treasure_key' in game_state['player_inventory']):
            player_actions.use_item( game_state, 'treasure_key')
        else:
            print('У вас нет ключа от судука, Но вы можете отгадать загадку. Используйте команду openIt')

    else:
        print('В комнате нет сундука сокровищ')
    return

def pseudo_random(seed, modulo) :
    first_val = (math.sin(seed * 15.98979695)) * 67895.34354657
    second_val = first_val - math.floor(first_val)
    third_val = second_val * modulo 
    result = math.floor(third_val)
    return  result

def trigger_trap(game_state) :
    print('Сработала ловушка!')
    if (game_state['player_inventory']) : 
        index_del = pseudo_random(game_state['steps_taken'], len(game_state['player_inventory']))
        item = game_state['player_inventory'].pop(index_del)
        print(f'Вы потеряли {item}')
    else : 
        life_damage = pseudo_random(game_state['steps_taken'], 100 )
        life_level = game_state['steps_taken'] - life_damage
        if (life_level < 30 ) :
            print('Путник погиб, игра окончена')
            game_state['game_over'] = True
        else :
            print(f'Путник получил ранение и его уровень жизни тепер {life_level}')

def random_event(game_state) : 
    first_val = pseudo_random(game_state['steps_taken'] , 10)
    if (first_val in range( 4, 10 )) : 
        return 
    else : 
        second_val = pseudo_random(game_state['steps_taken'] , 10)
        match second_val :
            case 1 :
                print('Я нашел монетку')
                ROOMS[game_state['current_room']]['items'].append('coin')
            case 2 :
                print('Здесь кто-то есть, я слышу шорохи')
                if ('sword' in  game_state['player_inventory']) : 
                    print('Я достал меч и оно убежало')
                else :
                    return
            case 3 :
                if (game_state['current_room'] == 'trap_room'  ) and ('torch' not in game_state['player_inventory']) :
                    print('Ты в опасности')
                    trigger_trap(game_state)
                else :
                    return
    return 

