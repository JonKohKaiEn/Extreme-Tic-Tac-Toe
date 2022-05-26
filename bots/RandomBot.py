from ultimate_ttt.UTTT import Board
from typing import Tuple
from random import choice

def make_move(board: Board) -> Tuple:

    return choice(board.valid_moves)