from typing import Tuple
from ETTTenv_test import Board
from random import choice
from copy import deepcopy
import time


class RandomBot:

    def __init__(self, board: Board) -> None:

        self.board = board

    def make_move(self) -> Tuple:

        return choice(self.board.valid_moves)


class minimaxBot:

    def __init__(self, board: Board):
        
        self.board = board
        self.player = self.board.player
        self.leaves_searched = 0

    def score(self, board: Board):

        if board.done == 2:  # draw
            return 0
        if board.done == self.player:  # won
            return 100
            #return 100 / len(board.move_list)
        else:  # lost
            return -100

    def minimax(self, board: Board, maximizing: bool, return_move: bool) -> int:
        
        if board.done:
            self.leaves_searched += 1
            return self.score(board)
        
        best_score = -999999 if maximizing else 999999
        for move in board.valid_moves:
            copy_board = deepcopy(board)
            copy_board.mark(move)
            score = self.minimax(copy_board, not maximizing)
            best_score = max(best_score, score) if maximizing else min(best_score, score)

    def make_move(self) -> Tuple:

        start_time = time.time()

        best_move, best_score = None, -999999

        for move in self.board.valid_moves:
            copy_board = deepcopy(self.board)
            copy_board.mark(move)
            score = self.minimax(copy_board, False)
            if score > best_score:
                best_move, best_score = move, score

        end_time = time.time()

        print(f"leaves searched: {self.leaves_searched} \t time taken: {end_time-start_time}")
        return best_move