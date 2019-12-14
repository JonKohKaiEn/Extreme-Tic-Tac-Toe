'''
RULES OF ETTT:
1) 1st move: can place anywhere
2) The cell that subsequent moves can be played on is determined by the position subcell of the previous move
3) If the cell of the current move is already won, any subcell from any cell can be played
4) Player wins if the board is won

'''

class extreme_TTT:

    def __init__(self):

        # defines what postitions to check for winner
        self.win_check_list = [(0,1,2), (3,4,5), (6,7,8),     # rows
                               (0,3,6), (1,4,7), (2,5,8),     # columns
                               (0,4,8), (2,4,6)]              # diagonals

    # returns a list of all possible next moves
    def get_possible_moves(self):

        # initialise list variable
        possible_moves = []

        # if it is the first turn, all spots are available
        if self.turn == 1:
            for cell in range(0,9):
                for cell_pos in range(0,9):
                    possible_moves.append((cell, cell_pos))

            # disable 'any subcell from any cell'
            self.any_cell = False

        # if not first turn, get index of previous cell. if subcell is 0, the subcell is available
        else:
            if self.any_cell:
                for cell_idx in range(0,9):
                    if self.macro_board[cell_idx] == 0:
                        for subcell_idx in range(0,9):
                            if self.board[cell_idx][subcell_idx] == 0:
                                possible_moves.append((cell_idx, subcell_idx))

            else:
                for cell_pos in range(0,9):
                    if self.board[self.last_move[1]][cell_pos] == 0:
                        possible_moves.append((self.last_move[1], cell_pos))

        return possible_moves
    
    # updates board with updated state, accepts tuple as move
    def move(self, position):

        self.print_board()

        # parse position into cell and subcell
        move_cell, move_subcell = position

        if self.macro_board[move_cell] != 0:
            self.any_cell = True

        # check if subcell is available
        if position not in self.get_possible_moves():
            print("Invalid move! Please re-enter your move.")

        else:
            # update postition with player number
            if self.player == 1:
                self.board[move_cell][move_subcell] = 1
            else:
                self.board[move_cell][move_subcell] = 2

        self.win_state()
        self.turn += 1
        self.last_move = position
        print(self.last_move)
        
        # changes the player when turn ends
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
    
    # detects whether a player wins and prints out the winner
    def win_state(self):

        # variables that keep track of whether a player has won a cell
        p1_win = False
        p2_win = False
        cell_won = 0

        # check if a player has won a cell or a cell ends up in a draw
        for cell_idx, cell in enumerate(self.board):

            if min(cell) != 0:
                self.macro_board[cell_idx] = 3
                for idx in range(0,9):
                    self.board[cell_idx][idx] = 3

            for test_idx_1, test_idx_2, test_idx_3 in self.win_check_list:

                if cell[test_idx_1] == cell[test_idx_2] == cell[test_idx_3] and cell[test_idx_1] == 1 and self.macro_board[cell_idx] == 0:
                    p1_win = True
                    cell_won = cell_idx
                    self.macro_board[cell_idx] = 1
                    for idx in range(0,9):
                        self.board[cell_idx][idx] = 1

                elif cell[test_idx_1] == cell[test_idx_2] == cell[test_idx_3] and cell[test_idx_1] == 2 and self.macro_board[cell_idx] == 0:
                    p2_win = True
                    cell_won = cell_idx
                    self.macro_board[cell_idx] = 2
                    for idx in range(0,9):
                        self.board[cell_idx][idx] = 2

                else:
                    pass

        # prints if a player has won a cell
        if p1_win:
            print(f"Player 1 wins cell {cell_won}!")
        elif p2_win:
            print(f"Player 2 wins cell {cell_won}!")
        else:
            pass

        # checks if a player has won the game
        for test_idx_1, test_idx_2, test_idx_3 in self.win_check_list:

                if self.macro_board[test_idx_1] == self.macro_board[test_idx_2] == self.macro_board[test_idx_3] and self.macro_board[test_idx_1] == 1:
                    print(f"Player 1 wins!")
                    self.done = True

                elif self.macro_board[test_idx_1] == self.macro_board[test_idx_2] == self.macro_board[test_idx_3] and self.macro_board[test_idx_1] == 2:
                    print(f"Player 2 wins!")
                    self.done = True
    
    # resets the board and game variables
    def reset(self):
        # initialise the board
        self.board = []
        for _ in range(0,9):
            cell = []
            for _ in range(0,9):
                cell.append(0)
            self.board.append(cell)

        self.macro_board = []
        for _ in range(0,9):
            self.macro_board.append(0)

        # keeps track of the turn number
        self.turn = 1                                        

        # keeps track of which player's turn it is
        self.player = 1

        # variable for last move
        self.last_move = None

        # variable that keeps track of whether every cell that isn't won is available
        self.any_cell = True

        # variable that keeps track of whether the game has been won
        self.done = False

    # prints the board
    def print_board(self):

        replaced_list = []
        for cell, subcell in self.get_possible_moves():
            self.board[cell][subcell] = 'x'
            replaced_list.append((cell, subcell))

        print("-" * 25)
        i = 0
        for _ in range(0,3):
            j = 0
            for _ in range(0,3):
                row_str = ["|"]
                for cell_row in range(i,i+3):
                    for subcell_row in range(j,j+3):
                        row_str += str(self.board[cell_row][subcell_row])
                    row_str += "|"
                print(" ".join(row_str))
                j += 3
            print("-" * 25)
            i += 3

        if self.turn != 1:
            print("TURN COMPLETE!")

        for cell, subcell in replaced_list:
            self.board[cell][subcell] = 0

# for testing
if __name__ == "__main__":
    pass
