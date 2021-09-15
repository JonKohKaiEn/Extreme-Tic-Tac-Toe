from ETTTenv_test import Board
import os
import json
import time
from random import choice
from math import inf

os.chdir('C:\\Users\Jonathan Koh\Desktop\Python Projects\extreme_tictactoe')

""" if not os.path.isdir('replay'):
    print("making replay folder...")
    os.makedirs('replay')
    print("replay folder created!")

def save_move_list(moves_list):
    save_list = json.dumps(moves_list)
    with open(f"replay/{board.turn}_{int(time.time())}.txt", 'w') as f:
        f.write(save_list)

moves_list = [] """


""" # starting from a previous save file
load_file = None
if load_file is not None:
    with open(f'replay/{load_file}.txt', 'r') as f:
        moves_list = json.loads(f.readline())
    for move in moves_list:
        move = tuple(move)
        board.make_move(move)
 """
 
board = Board()

while not board.done:
    print(f"Player {board.curr_player}'s turn")
    print(board)
    available_moves = board.get_valid_moves()
    move = choice(available_moves)
    board.make_move(move)
print(f"Player {board.done} won!" if board.done in [1, -1] else "draw")