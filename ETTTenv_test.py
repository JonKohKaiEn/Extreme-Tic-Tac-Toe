from typing import List, Tuple


class Board:

    def __init__(self) -> None:
        
        self.board = [[0] * 9 for _ in range(9)]
        self.macro_board = [0] * 9
        self.player = 1
        self.curr_miniboard = -1
        self.move_list = []
        self.done = None

    def is_valid(self, move: Tuple[int]) -> bool:

        if (not self.board[move[0]][move[1]]) and (not self.macro_board[move[0]]):  #if cell is empty and miniboard is not won

            if move[0] == self.curr_miniboard or self.curr_miniboard == -1:  # if it is in current miniboard or if any cell is at play
                return True

        return False
    
    def mark(self, move: Tuple[int]) -> None:
        
        if self.is_valid(move):  # if move is valid
            self.board[move[0]][move[1]] = self.player
            miniboard_status = self.board_status(self.board[move[0]])
            if miniboard_status:
                self.board[move[0]] = [miniboard_status] * 9
            self.macro_board[move[0]] = miniboard_status  # update macro board
            self.move_list.append(move)
            game_state = self.board_status(self.macro_board)

            if  game_state:  # if game is finished
                self.done = game_state  # set done
            else:
                self.curr_miniboard = -1 if self.macro_board[move[1]] else move[1]  # update current miniboard
                self.player *= -1  # update player

        else:
            print(f"Invalid move: {move}")

    def board_status(self, list_to_check: List[int]) -> int:
        
        checklist = [(0,1,2), (3,4,5), (6,7,8),     # rows
                     (0,3,6), (1,4,7), (2,5,8),     # columns
                     (0,4,8), (2,4,6)]              # diagonals

        for check_idx in checklist:

            if list_to_check[check_idx[0]] == list_to_check[check_idx[1]] == list_to_check[check_idx[2]] and list_to_check[check_idx[0]] != 0:
                return 1 if list_to_check[check_idx[0]] == 1 else -1

        if all(list_to_check):
            return 2

        return 0

    @property
    def valid_moves(self) -> List[Tuple]:

        return [(miniboard, cell) for miniboard in range(9) for cell in range(9) if self.is_valid((miniboard, cell))]

    def __str__(self):

        def num_to_disp(n):
            if n == 1:
                return "O"
            elif n == -1:
                return "X"
            elif n == 2:
                return "D"
            else:
                return " "

        disp_board = [[0] * 9 for _ in range(9)]

        for miniboard in range(9):
            for cell in range(9):
                disp_board[miniboard][cell] = "." if self.is_valid((miniboard, cell)) else num_to_disp(self.board[miniboard][cell])

        board_str = "+ - - - + - - - + - - - +\n"

        for miniboard in [0, 3, 6]:  # loop through leftmost miniboards
            for cell in [0, 3, 6]:  # loop through leftmost cell in set
                for i in range(3):  # loop through miniboard idx in set
                    board_str += f"| {disp_board[miniboard+i][cell]} {disp_board[miniboard+i][cell+1]} {disp_board[miniboard+i][cell+2]} "
                board_str += "|\n"
            board_str += "+ - - - + - - - + - - - +\n"

        return board_str[:-1]