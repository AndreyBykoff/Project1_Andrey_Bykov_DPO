# labyrinth_game/utils.py
from constants import ROOMS



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
    print(f"Название текущей комнаты: {current_room_print_name}\nОписание комнаты: {current_room_defenition}\nЗаметные предметы: {current_items_list_print}\nДоступные выходы: {current_availe_exits_print}\nСообщение о наличии загадки: {current_puzzle_enable}")

def solve_puzzle(game_state):
    puzzle = ROOMS[game_state['current_room']].get('puzzle')
    if (puzzle):
        print(puzzle[0])
        result = str(input('Ваш ответ:'))
        if (puzzle[1] == result):
            print('Вы ответили правильно')
            ROOMS[game_state['current_room']].pop('puzzle', None)
            return True
        else:
            print('Не верно, попробуйте снова')
            return False    
    else:
        print('Загадок здесь нет')
        return False
    
"""

def attempt_open_treasure(game_state):
    # Еслимы в сокровищнецы
    if ('treasure_chest' in ROOMS[game_state['current_room']].get('items')):
        use_item( game_state, 'treasure_key')
    else:
        print('В комнате нет сундука сокровищ')
    return

"""
