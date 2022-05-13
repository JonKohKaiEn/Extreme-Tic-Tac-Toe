from ETTTenv_test import Board
import os
import json
import time
from random import choice
from math import inf

board = Board()

print(board)
while not board.done:

    move = choice(board.valid_moves)
    print(move)
    board.mark(move)
    print(board)
    print(board.macro_board)