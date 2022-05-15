from ETTTenv_test import Board
from bots import RandomBot
from copy import deepcopy

def play(agent1, agent2):

    board = Board()

    while not board.done:
        print("Agent 1 turn")
        print(board.valid_moves)
        board.mark(agent1(board).make_move())
        print(board)
        print(board.macro_board)
        print("\n")
        print("Agent 2 turn")
        print(board.valid_moves)
        board.mark(agent2(board).make_move())
        print(board)
        print(board.macro_board)
        print("\n")

    print("Draw!" if board.done == 2 else f"Player {board.done} won!")
    print(board.move_list)

play(RandomBot, RandomBot)