import numpy as np

class Board:
    
    def __init__(self):
        self.p1_large_board = np.zeros((9,9), dtype=int)  # Overall game board for player 1
        self.p2_large_board = np.zeros((9,9), dtype=int)  # Overall game board for player 2
        self.p1_small_boards = np.zeros((9,))  # Tracks which small board has been won by player 1
        self.p2_small_boards = np.zeros((9,))  # Tracks which small board has been won by player 2
        self.curr_player = 1
        self.curr_small_board = -1
        self.done = False

    
    def board_array(self, output_cellwise=False, show_valid_moves=True):

        cellwise_combined_board = self.p1_large_board + (self.p2_large_board * -1)

        # check for boards won
        if np.any(self.p1_small_boards):
            cellwise_combined_board[np.where(self.p1_small_boards == 1)] = 1
        if np.any(self.p2_small_boards):
            cellwise_combined_board[np.where(self.p2_small_boards == 1)] = -1

        if show_valid_moves:
            valid_moves = self.get_valid_moves(as_index=True)
            cellwise_combined_board[valid_moves] = 2

        if output_cellwise:
            return cellwise_combined_board

        combined_small_boards = [np.reshape(cellwise_combined_board[i], (3,3)) for i in range(9)]
        combined_board_rows = [np.hstack((combined_small_boards[i], combined_small_boards[i+1], combined_small_boards[i+2])) for i in range(0,7,3)]
        board_arr_out = np.vstack(tuple(combined_board_rows))
        return board_arr_out
    

    def __str__(self):

        def num_to_disp(n):
            if n == 1:
                return "O"
            elif n == -1:
                return "X"
            elif n == 2:  # Valid moves
                return "."
            else:
                return " "
            
        curr_board_arr = self.board_array()
        board_str = "+ - - - + - - - + - - - +\n"
        for row in range(9):
            row_slice = list(curr_board_arr[row])
            row_slice = list(map(num_to_disp, row_slice))
            for i in range(0,7,3):
                board_str += f"| {row_slice[i]} {row_slice[i+1]} {row_slice[i+2]} "
            board_str += "|\n"
            if row in {2, 5, 8}:
                board_str += "+ - - - + - - - + - - - +\n"

        return board_str


    def get_valid_moves(self, as_index=False):

        large_board = self.p1_large_board + self.p2_large_board

        if self.curr_small_board == -1:  # any cell
            available_subcells = np.where(large_board==0)[0]
            available_cells = np.where(large_board==0)[1]
        else:
            curr_small_board_arr = large_board[self.curr_small_board, :]
            available_subcells = np.where(curr_small_board_arr==0)[0]
            available_cells = (np.ones_like(available_subcells) * self.curr_small_board).flatten()
            
        if not as_index:
            return list(zip(available_cells.tolist(),  available_subcells.tolist()))
        else:
            available_cells_idx = (available_cells, available_subcells)
            return available_cells_idx


    def make_move(self, move: tuple):

        if self.curr_player == 1:
            self.p1_large_board[move[0], move[1]] = 1
        else:
            self.p2_large_board[move[0], move[1]] = 1

        self.check_for_win()
        self.curr_player *= -1
        
        # check for any cell
        small_boards = self.p1_small_boards + self.p2_small_boards
        if small_boards[move[1]]:
            self.curr_small_board = -1
        else:
            self.curr_small_board = move[1]


    def check_for_win(self):

        win_checklist = [[0,1,2], [3,4,5], [6,7,8],    # rows
                        [0,3,6], [1,4,7], [2,5,8],     # columns
                        [0,4,8], [2,4,6]]              # diagonals
        
        large_board = self.p1_large_board if self.curr_player == 1 else self.p2_large_board
        small_boards = self.p1_small_boards if self.curr_player == 1 else self.p2_small_boards

        for small_board_idx in range(9):

            # check if small board is already won
            if small_boards[small_board_idx]:  
                continue

            # check each small board whether it is won
            for check_list in win_checklist:
                curr_small_board = large_board[small_board_idx, check_list]
                if np.all(curr_small_board):
                    small_boards[small_board_idx] = 1
                    large_board[small_board_idx, :] = 1

        # check if the game is won
        for check_list in win_checklist:
            if np.all(small_boards[check_list]):
                self.done = self.curr_player
        
        # check if game is drawn
        

        # update game state
        if self.curr_player == 1:
            self.p1_large_board, self.p1_small_boards = large_board, small_boards
        else:
            self.p2_large_board, self.p2_small_boards = large_board, small_boards


if __name__ == '__main__':

    from random import choice

    test_board = Board()
    test_board.make_move((8,3))
    print(test_board)
    