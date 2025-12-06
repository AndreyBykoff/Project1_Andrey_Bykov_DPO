# labyrinth_game/player_actions.py
from constants import ROOMS
from utils import describe_current_room 





def show_inventory(game_state):
    avaible_player_inventory = str()
    if (game_state.get('player_inventory') ):
       avaible_player_inventory = ','.join(game_state.get('player_inventory'))
    else:
        avaible_player_inventory = 'Инвентаря нет'
    print(f"Текущий набор инветтаря: {avaible_player_inventory}")

def get_input(prompt="> "):
        try:
            prompt = input(f'Для выхода из игры введите Quit или Exit\nВведите команду {prompt}')
            return prompt
        except (KeyboardInterrupt, EOFError):
            print("\nВыход из игры.")
            return "quit"

def move_player(game_state, direction):
    current_room_check = ROOMS[game_state['current_room']]
    check_way = current_room_check['exits'].get(direction)
    if (check_way):
        new_room = ROOMS[check_way]
        new_room_defenition = new_room['description']
        game_state['current_room'] = check_way
        game_state['steps_taken'] += 1
        describe_current_room(game_state)
    else:
        print('В этом направлении идти нельзя')


def take_item(game_state, item_name):
    check_room = ROOMS[game_state['current_room']]
    check_room_items = check_room['items']

    if (item_name in check_room_items):
        game_state['player_inventory'].append(item_name)
        check_room_items.remove(item_name)
        print(f'Вы подняли: {item_name}')
    else:
        print('Такого предмета здесь нет')

def use_item(game_state, item_name):
    if (item_name in game_state['player_inventory']):
        match item_name:
            case 'torch':
                print('Стало светлее')
            case 'sword':
                print('Я чувствую себя уверенее')
            case 'treasure_key':
                print("Вы применяете ключ, и замок щёлкает. Сундук открыт!\nВ сундуке сокровище! Вы победили!")
                game_state['game_over'] = True
                ROOMS['treasure_room'].get('items').pop('treasure_chest' , None)
            case 'bronze box':
                print('Я открыл шкатулку')
                if ('rusty_key' not in game_state['player_inventory']):
                    game_state['player_inventory'].append('rusty_key')
                else:
                    return
            case _:
                print('Я не знаю что с этим делать')
    else:
        print('У вас нет такого предмета')
    return











