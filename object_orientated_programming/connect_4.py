import numpy as np


class ConnectFour:
    ROWS = 6
    COLS = 7


"""__init__(self): This is the constructor method for the ConnectFour class.
 It initializes a 2D numpy array of size 6x7 to represent the game board and sets the initial turn to 1."""


def __init__(self):
    self.board = np.zeros((self.ROWS, self.COLS), dtype=int)
    self.turn = 1


"""drop_piece(self, col): This method takes a column number as input and drops a piece in the given column if it is a valid move. 
It returns the row and column of the dropped piece if successful, otherwise returns None."""


def drop_piece(self, col):
    if self.is_valid_location(col):
        row = self.get_next_open_row(col)
        self.board[row][col] = self.turn
        return row, col
    else:
        return None


"""is_valid_location(self, col): This method takes a column number as input and checks if the given column is a valid 
move by checking if the top row of the column is empty."""


def is_valid_location(self, col):
    return self.board[self.ROWS - 1][col] == 0

"""get_next_open_row(self, col): This method takes a column number as input and returns the row number
 of the next open slot in the given column."""

def get_next_open_row(self, col):
    for r in range(self.ROWS):
        if self.board[r][col] == 0:
            return r

"""winning_move(self): This method checks if the current player has won the game by checking all possible winning combinations horizontally, vertically and diagonally.
 It returns True if there is a winning move, otherwise False."""


def winning_move(self):
    for r in range(self.ROWS):
        for c in range(self.COLS - 3):
            if self.board[r][c] == self.turn and self.board[r][c + 1] == self.turn and self.board[r][
c + 2] == self.turn and self.board[r][c + 3] == self.turn:
                return True

    for r in range(self.ROWS - 3):
        for c in range(self.COLS):
            if self.board[r][c] == self.turn and self.board[r + 1][c] == self.turn and self.board[r + 2][
                c] == self.turn and self.board[r + 3][c] == self.turn:
                return True

    for r in range(self.ROWS - 3):
        for c in range(self.COLS - 3):
            if self.board[r][c] == self.turn and self.board[r + 1][c + 1] == self.turn and self.board[r + 2][
                c + 2] == self.turn and self.board[r + 3][c + 3] == self.turn:
                return True

    for r in range(3, self.ROWS):
        for c in range(self.COLS - 3):
            if self.board[r][c] == self.turn and self.board[r - 1][c + 1] == self.turn and self.board[r - 2][
                c + 2] == self.turn and self.board[r - 3][c + 3] == self.turn:
                return True

    return False

# switch_turn(self): This method switches the turn between players.
def switch_turn(self):
    self.turn = 2 if self.turn == 1 else 1

# is_game_over(self): This method checks if the game is over by
def is_game_over(self):
    return np.all(self.board != 0) or self.winning_move() is not False

#get_board(self): This method returns the current game board.
def get_board(self):
    return self.board

#get_turn(self): This method returns the current turn.
def get_turn(self):
    return self.turn
