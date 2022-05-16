from ETTTenv_test import Board
from bots import RandomBot, MinimaxBot
from typing import List
from itertools import cycle
from tqdm import tqdm

def play(agent_list: List):

    agent_gen = cycle(agent_list)
    board = Board()

    while not board.done:

        print(f"Player {board.player} turn!")
        agent = next(agent_gen)
        move = agent(board).make_move()
        print(f"Player {board.player} makes move {move}")
        board.mark(move)
        print(board)
        print("\n")

    print("Draw!" if board.done == 2 else f"Player {board.done} won!")
    print(board.move_list)


def play_trials(agent_list: List, trials: int = 1000):

    avg_game_len = 0

    for trial in tqdm(range(trials)):

        agent_gen = cycle(agent_list)
        board = Board()

        while not board.done:

            agent = next(agent_gen)
            move = agent(board).make_move()
            board.mark(move)

        avg_game_len += len(board.move_list)

    print(f"Average game length: {int(avg_game_len / trials)}")

play([MinimaxBot, RandomBot])