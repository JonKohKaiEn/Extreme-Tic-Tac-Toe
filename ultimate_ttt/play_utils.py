from ultimate_ttt.UTTT import Board
from typing import List
from itertools import cycle

def play(agent_list: List):

    agent_gen = cycle(agent_list)
    board = Board()

    while not board.done:

        print(f"Player {board.player} turn!")
        agent = next(agent_gen)
        move = agent.make_move(board)
        print(f"Player {board.player} makes move {move}")
        board.mark(move)
        print(board)
        print("\n")

    print("Draw!" if board.done == 2 else f"Player {board.done} won!")
    print(board.move_list)


def play_trials(agent_list: List, trials: int = 100):

    trial_results = [0, 0, 0]  # win / loss / draw

    for trial in range(1, trials+1):

        agent_gen = cycle(agent_list)
        board = Board()

        while not board.done:

            agent = next(agent_gen)
            move = agent.make_move(board)
            board.mark(move)

        if board.done == 1:
            trial_results[0] += 1
        elif board.done == -1:
            trial_results[1] += 1
        elif board.done == 2:
            trial_results[2] += 1

        if trial % 10 == 0:
            print(f"Completed {trial} trials! \t Agent 1 wins: {trial_results[0]} \t Agent 1 losses: {trial_results[1]} \t Draws: {trial_results[2]}")

    print(f"Win rate of agent 1: {(trial_results[0] / trials)*100:.2f}%")