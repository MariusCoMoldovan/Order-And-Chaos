import random

from Board.Board import Board


class Game:

    def __init__(self):
        self.__board = Board()

    @property
    def board(self):
        return self.__board

    def player_move(self, x, y, symbol):
        if x < 0 or y < 0 or x > 5 or y > 5:
            raise ValueError()
        self.__board.move(x, y, symbol)

    def computer_move(self):
        move = self.find_winning_move()

        if move is not None:
            self.__board.move(move[0], move[1], move[2])
        else:
            max_neighbours = 0
            initial_coordinates = [0, 0]
            most_occurences = self.find_most_occurences()
            for i in range(6):
                for j in range(6):
                    neighbours = self.check_neighbours(i, j, most_occurences)
                    if neighbours > max_neighbours:
                        initial_coordinates = [i, j]
                        max_neighbours = neighbours
            self.board.move(initial_coordinates[0], initial_coordinates[1], most_occurences)

    def check_neighbours(self, x, y, symbol):
        if self.__board.board[x][y] != " ":
            return 0
        neighbours = 0
        try:
            if self.__board.board[x + 1][y - 1] == symbol and y - 1 >= 0:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x + 1][y] == symbol:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x + 1][y + 1] == symbol:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x][y - 1] == symbol and y - 1 >= 0:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x][y + 1] == symbol:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x - 1][y - 1] == symbol and y - 1 >= 0 and x - 1 >= 0:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x - 1][y] == symbol and x - 1 >= 0:
                neighbours += 1
        except IndexError:
            pass

        try:
            if self.__board.board[x - 1][y + 1] == symbol and x - 1 >= 0:
                neighbours += 1
        except IndexError:
            pass

        return neighbours

    def find_winning_move(self):
        transposed_board = Board()
        for i in range(6):
            for j in range(6):
                transposed_board.board[j][i] = self.__board.board[i][j]
        for i in range(len(self.__board.board)):
            row = self.check_winning_row(self.__board.board[i][:-1])
            if row is not None:
                return i, row[0], row[1]
            row = self.check_winning_row(self.__board.board[i][1:])
            if row is not None:
                return i, row[0] - 1, row[1]
        for i in range(len(transposed_board.board)):
            column = self.check_winning_row(transposed_board.board[i][:-1])
            if column is not None:
                return column[0], i, column[1]
            column = self.check_winning_row(transposed_board.board[i][1:])
            if column is not None:
                return column[0] - 1, i, column[1]
        diagonal = [self.__board.board[i][i] for i in range(6)]
        diagonal_1 = self.check_winning_row(diagonal[:-1])
        if diagonal_1 is not None:
            return diagonal_1[0], diagonal_1[0], diagonal_1[1]
        diagonal_1 = self.check_winning_row(diagonal[1:])
        if diagonal_1 is not None:
            return diagonal_1[0] - 1, diagonal_1[0] - 1, diagonal_1[1]

        diagonal = [self.__board.board[i][i-1] for i in range(1, 6)]
        diagonal = self.check_winning_row(diagonal)
        if diagonal is not None:
            return diagonal[0] + 1, diagonal[0], diagonal[1]

        diagonal = [self.__board.board[i-1][i] for i in range(1, 6)]
        diagonal = self.check_winning_row(diagonal)
        if diagonal is not None:
            return diagonal[0], diagonal[0] + 1, diagonal[1]


    def check_winning_row(self, row):
        winning_rows_x = [[" ", "X", "X", "X", "X"], ["X", " ", "X", "X", "X"], ["X", "X", " ", "X", "X"],
                          ["X", "X", "X", " ", "X"], ["X", "X", "X", "X", " "]]
        winning_rows_o = [[" ", "O", "O", "O", "O"],
                          ["O", " ", "O", "O", "O"], ["O", "O", " ", "O", "O"], ["O", "O", "O", " ", "O"],
                          ["O", "O", "O", "O", " "]]
        for i in range(len(winning_rows_o)):
            if row == winning_rows_x[i]:
                return i, "X"
            elif row == winning_rows_o[i]:
                return i, "O"

    def find_most_occurences(self):
        symbols = {"O": 0, "X": 0}
        for row in self.__board.board:
            for element in row:
                if element != " ":
                    symbols[element] += 1
        values = list(symbols.values())
        return "O" if max(values) == values[0] else "X"

    def check_win(self):
        """
        The function checks if either the player or the computer won

        The function checks every row, column and diagonal(of length 5) by turning it into a set
        (so we only keep the unique values), and if there is only one unique value, that is not
        an empty space, that means that the computer won. Alternatively, if the board is full
        and this has not happened, the player wins

        :return: a string saying who won
        """
        for row in self.__board.board:
            rset = set(row[:-1])
            if len(rset) == 1 and " " not in rset:
                return "Computer wins"
            rset = set(row[1:])
            if len(rset) == 1 and " " not in rset:
                return "Computer wins"

        transposed_board = Board()
        for i in range(6):
            for j in range(6):
                transposed_board.board[j][i] = self.__board.board[i][j]

        for row in transposed_board.board:
            rset = set(row[:-1])
            if len(rset) == 1 and " " not in rset:
                return "Computer wins"
            rset = set(row[1:])
            if len(rset) == 1 and " " not in rset:
                return "Computer wins"

        diagonal = [self.__board.board[i][i] for i in range(6)]

        dset = set(diagonal[:-1])
        if len(dset) == 1 and " " not in dset:
            return "Computer wins"

        dset = set(diagonal[1:])
        if len(dset) == 1 and " " not in dset:
            return "Computer wins"

        diagonal = [self.__board.board[i][i - 1] for i in range(1, 6)]
        dset = set(diagonal)
        if len(dset) == 1 and " " not in dset:
            return "Computer wins"

        diagonal = [self.__board.board[i-1][i] for i in range(1, 6)]
        dset = set(diagonal)
        if len(dset) == 1 and " " not in dset:
            return "Computer wins"

        if self.__board.is_full():
            return "Player wins"
