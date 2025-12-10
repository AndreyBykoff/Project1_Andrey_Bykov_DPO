# labyrinth_game/player_actions.py
from constants import ROOMS
import utils


def show_inventory(game_state):
    avaible_player_inventory = str()
    if (game_state.get('player_inventory') ):
       avaible_player_inventory = ','.join(game_state.get('player_inventory'))
    else:
        avaible_player_inventory = 'Инвентаря нет'
    print(f"Текущий набор инветтаря: {avaible_player_inventory}")

def get_input(prompt="> "):
        try:
            prompt = input(f'Для выхода из игры введите Quit \nВведите команду {prompt}')
            return prompt
        except (KeyboardInterrupt, EOFError):
            print("\nВыход из игры.")
            return "quit"

def move_player(game_state, direction):
    if (not direction) :
        print("Укажите направление")
        return 
    else :
        current_room_check = ROOMS[game_state['current_room']]
        check_way = current_room_check['exits'].get(direction)
        if (check_way):
            if ('treasure_room' == check_way ) :
             if ('rusty_key' in game_state['player_inventory']) : 
                print("Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
             else :
                print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
                return
            utils.random_event(game_state)
#            new_room = ROOMS[check_way]
#            new_room_defenition = new_room['description']
            game_state['current_room'] = check_way
            game_state['steps_taken'] += 1
            utils.describe_current_room(game_state)
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
                game_state['player_inventory'].remove(item_name)
            case 'sword':
                print('Я чувствую себя уверенее')
                game_state['player_inventory'].remove(item_name)
            case 'treasure_key':
                if (item_name not in game_state['player_inventory'] ) :
                    print('У вас нет ключа от судука, Но вы можете отгадать загадку. Используйте команду openIt')
                else:
                    print("Вы применяете ключ, и замок щёлкает. Сундук открыт!\nВ сундуке сокровище! Вы победили!")
                    game_state['game_over'] = True
                    ROOMS['treasure_room'].get('items').remove('treasure_chest')
            case 'bronze box':
                print('Я открыл шкатулку')
                game_state['player_inventory'].remove(item_name)
                if ('rusty_key' not in game_state['player_inventory']):
                    game_state['player_inventory'].append('rusty_key')
                else:
                    return
            case 'rusty_key':
                print('Что бы применить Ржавый ключ, нужна бронзовая коробочка')
            case _:
                print('Я не знаю что с этим делать')
    else:
        print('У вас нет такого предмета')
    return











