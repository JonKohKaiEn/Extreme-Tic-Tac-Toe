from ETTTenv import extreme_TTT
import os
import json
import time

os.chdir('C:\\Users\Jonathan Koh\Desktop\extreme_tictactoe')

if not os.path.isdir('replay'):
    print("making replay folder...")
    os.makedirs('replay')
    print("replay folder created!")

def save_move_list():
    save_list = json.dumps(moves_list)
    with open(f"replay/{env.turn}__{int(time.time())}.txt", 'w') as f:
        f.write(save_list)

moves_list = []

env = extreme_TTT()
env.reset()

try:
    while not env.done:
        env.print_board()
        if env.player == 1:
            print(f"Player 1 turn!")
        else:
            print(f"Player 2 turn!")
        # print(env.get_possible_moves())
        
        move_cell = int(input("INPUT MOVE CELL: "))
        move_subcell = int(input("INPUT MOVE SUBCELL: "))
        if (move_cell, move_subcell) not in env.get_possible_moves():
            continue
        else:
            env.move((move_cell, move_subcell))
            moves_list.append((move_cell, move_subcell))

except:
    save_move_list()
    print("An error occurred, saving game...")
    