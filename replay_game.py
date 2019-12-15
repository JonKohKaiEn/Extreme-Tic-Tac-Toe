from ETTTenv import extreme_TTT
import os
import json

env = extreme_TTT()
env.reset()

os.chdir('C:\\Users\Jonathan Koh\Desktop\extreme_tictactoe')
file_name = '17__1576377021'
file_name += '.txt'
with open(f'replay/{file_name}', 'r') as f:
    replay_list = json.loads(f.readline())

print(replay_list)
env.print_board()
for move in replay_list:
    move = tuple(move)
    env.move(move)
    env.print_board()
    