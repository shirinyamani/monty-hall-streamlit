import random


def monty_hall(switch_door):
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors) #inplace so exit is None
    user_choice = random.choice(range(len(doors)))
    #print(f'user initial choice {user_choice} from doors {doors}')

    doors_reveal = [door for door in range(len(doors)) if door != user_choice and doors[door] != 'car']
    #print(f'remained doors {doors_reveal}')
    door_reveal = random.choice(doors_reveal)
    #print(door_reveal)

    if switch_door:
        final_choice  = [door for door in range(3) if door != user_choice and door != door_reveal][0]
    else:
        final_choice = user_choice
    return doors[final_choice] == 'car'

def simulate(n):
    num_win_no_switch = sum([monty_hall(False) for _ in range(n)])
    num_win_switch = sum([monty_hall(True) for _ in range(n)])
    return num_win_no_switch, num_win_switch



if __name__ =="__main__":
        num_games = 1000
        win_percent_without_switching, win_percent_with_switching = simulate(num_games)