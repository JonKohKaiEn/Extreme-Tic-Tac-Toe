# ETTT-mcts

Extreme Tic Tac Toe with Monte Carlo Tree Search(MCTS) AI.

RULES OF ETTT:
1) 1st move: can place anywhere
2) The cell that subsequent moves can be played on is determined by the position subcell of the previous move
3) If the cell of the current move is already won, any subcell from any cell can be played
4) Player wins if the entire board is won

Positions of each cell are as follows:

0  1  2\
3  4  5\
6  7  8

Positions of the larger cells follow the same numbering

Requirements:\
python 3.7.4\
mcts
