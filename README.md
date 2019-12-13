# ETTT

Extreme Tic Tac Toe with AI(To be added...).

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

Guide to UI:\
0 : untaken cell\
1 or 2: cell taken by player 1 or player 2 respectively\
3: cell is in a draw state\
x: cell is available to be taken on that turn

Requirements:\
python 3.7.4
