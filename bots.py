from random import choice
from copy import deepcopy

class randBot:
    def choose_action(self, possible_moves):
        action = possible_moves.choice()
        return action

class minimaxBot:

    def __init__(self, board):
        
        self.current_board = deepcopy(board)

    def choose_action(self, possible_moves):
        pass

    def minimax(self, position, depth, alpha, beta):
        if depth == 0 or 
