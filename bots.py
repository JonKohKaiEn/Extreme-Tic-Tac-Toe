from typing import Tuple
from ETTTenv_test import Board
from random import choice
from copy import deepcopy
import time
from functools import cache
from math import inf


class RandomBot:

    def __init__(self, board: Board) -> None:

        self.board = board

    def make_move(self) -> Tuple:

        return choice(self.board.valid_moves)


class MinimaxBot:

    def __init__(self, board: Board):
        
        self.board = board
        self.player = self.board.player
        self.leaves_searched = 0

    def score(self, board: Board):

        if board.done == 2:  # draw
            return 0
        if board.done == self.player:  # won
            #return 100
            return 100 / len(board.move_list)
        else:  # lost
            return -100

    @cache
    def minimax(self, board: Board, alpha, beta, maximizing: bool, return_move: bool = False) -> int:
        
        if board.done:
            self.leaves_searched += 1
            if self.leaves_searched % 100 == 0:
                print(f"Leaves searched: {self.leaves_searched}")
            return self.score(board)
        
        if maximizing:
            best_score = -inf
            for move in board.valid_moves:
                copy_board = deepcopy(board)
                copy_board.mark(move)
                score = self.minimax(copy_board, alpha, beta, False)
                best_score = max(best_score, score)

                alpha = max(alpha, score)
                if beta <= alpha:
                    break

            return best_score

        else:
            best_score = inf
            for move in board.valid_moves:
                copy_board = deepcopy(board)
                copy_board.mark(move)
                score = self.minimax(copy_board, alpha, beta, True)
                best_score = min(best_score, score)

                beta = min(beta, score)
                if beta <= alpha:
                    break

            return best_score

    def make_move(self) -> Tuple:

        start_time = time.time()

        best_move, best_score = None, -inf

        if len(self.board.move_list) < 50:
            return choice(self.board.valid_moves)
        
        for move in self.board.valid_moves:
            copy_board = deepcopy(self.board)
            copy_board.mark(move)
            score = self.minimax(copy_board, -inf, inf, maximizing=False, return_move=True)
            if score > best_score:
                best_move, best_score = move, score

        end_time = time.time()

        print(f"leaves searched: {self.leaves_searched} \t time taken: {end_time-start_time}")
        return best_move