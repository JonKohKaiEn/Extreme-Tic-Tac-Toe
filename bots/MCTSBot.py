from math import inf, sqrt, log
from typing import Tuple
from copy import deepcopy
from random import choice
import time
from ultimate_ttt.UTTT import Board


class Node:

    def __init__(self, board: Board) -> None:
        
        self.board = board
        self.children = []
        self.value = 0
        self.visits = 0

    def score(self, board_state: int) -> int:

        score_dict = {self.board.player: 1, self.board.player*-1: -1, 2: 0}
        return score_dict[board_state]

    @property
    def best_child(self) -> 'Node':

        best_child, best_uct = None, -inf
        for child in self.children:

            if child.visits == 0:
                return child

            uct = child.value + sqrt(2 * log(self.visits+1) / child.visits)
            if uct > best_uct:
                best_child = child
                best_uct = uct

        return best_child

    def expand(self) -> None:

        for move in self.board.valid_moves:
            board_copy = deepcopy(self.board)
            board_copy.mark(move)
            self.children.append(Node(board_copy))

    def rollout(self) -> None:

        for _ in range(10):
            sim_board = deepcopy(self.board)
            while not sim_board.done:
                sim_board.mark(choice(sim_board.valid_moves))
            self.value += self.score(sim_board.done)

    def update_value(self) -> None:

        self.value = sum([child.value for child in self.children]) / len(self.children)


def mcts(root: Node) -> None:
        
    if root.children:  # if root node has children

        best_child = root.best_child
        mcts(best_child)
        best_child.visits += 1

    else:
        if root.board.done:
            return
        root.expand()
        best_child = root.best_child
        best_child.rollout()
        root.update_value()
        best_child.visits += 1

DURATION = 0.5

def make_move(board: Board) -> Tuple:

    root = Node(board)

    end_time = time.time() + DURATION

    while time.time() < end_time:
        mcts(root)

    return max(zip(board.valid_moves, root.children), key=lambda x: x[1].visits)[0]