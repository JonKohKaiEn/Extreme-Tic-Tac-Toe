from ultimate_ttt.UTTT import Board
from copy import deepcopy
from math import inf
from typing import Tuple
import time
from random import choice

def score(board: Board, player: int) -> int:

    if board.done == 2:  # draw
        return 0
    if board.done == player:  # won
        #return 100
        return 100 / len(board.move_list)
    else:  # lost
        return -100

def minimax(board: Board, alpha, beta, maximizing: bool, player: int) -> int:
        
    if board.done:
        return score(board, player)
    
    if maximizing:
        best_score = -inf
        for move in board.valid_moves:
            copy_board = deepcopy(board)
            copy_board.mark(move)
            curr_score = minimax(copy_board, alpha, beta, False, player)
            best_score = max(best_score, curr_score)

            alpha = max(alpha, curr_score)
            if beta <= alpha:
                break

        return best_score

    else:
        best_score = inf
        for move in board.valid_moves:
            copy_board = deepcopy(board)
            copy_board.mark(move)
            curr_score = minimax(copy_board, alpha, beta, True, player)
            best_score = min(best_score, curr_score)

            beta = min(beta, curr_score)
            if beta <= alpha:
                break

        return best_score

def make_move(board: Board) -> Tuple:

        start_time = time.perf_counter()

        best_move, best_score = None, -inf
        player = board.player

        if len(board.move_list) < 50:
            return choice(board.valid_moves)
        
        for move in board.valid_moves:
            copy_board = deepcopy(board)
            copy_board.mark(move)
            score = minimax(copy_board, -inf, inf, False, player)
            if score > best_score:
                best_move, best_score = move, score

        end_time = time.perf_counter()

        print(f"time taken: {end_time-start_time}")
        return best_move