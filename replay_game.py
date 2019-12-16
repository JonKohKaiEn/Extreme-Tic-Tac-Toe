from ETTTenv import extreme_TTT
import os
import json

env = extreme_TTT()
env.reset()

file_name = ''
with open(f'replay/{file_name}.txt', 'r') as f:
    replay_list = json.loads(f.readline())

env.print_board()
for move in replay_list:
    move = tuple(move)
    env.move(move)
    env.print_board()
 
