from math import inf
from typing import Tuple
from copy import deepcopy
from random import choice
from ultimate_ttt.UTTT import Board


def score(board_state: int, player: int):

    score_dict = {player: 1, player*-1: -1, 2: 0}
    return score_dict[board_state]

def make_move(board: Board) -> Tuple:

    best_move, best_score = None, -inf
    player = board.player
    SIMS = 1_000

    for move in board.valid_moves:

        sim_board = deepcopy(board)
        sim_board.mark(move)

        for _ in range(SIMS):
            curr_score = 0
            while not sim_board.done:
                sim_board.mark(choice(sim_board.valid_moves))
            curr_score += score(sim_board.done, player)

        if curr_score > best_score:
            best_score = curr_score
            best_move = move

    return best_move