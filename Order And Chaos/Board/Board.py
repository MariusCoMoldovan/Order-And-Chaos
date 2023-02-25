class Board:

    def __init__(self):
        self.__size = 6
        self.__data = [[" "] * 6 for i in range(6)]

    @property
    def board(self):
        return self.__data


    def move(self, x, y, symbol):
        if self.is_free(x, y) and symbol in ["O", "X"]:
            self.__data[x][y] = symbol
        else:
            raise ValueError()

    def is_free(self, x, y):
        return True if self.__data[x][y] == " " else False

    def __str__(self):
        string = "+---" * 6 + "+\n"
        for row in self.__data:
            for element in row:
                string += f"| {element} "
            string += "|\n" + "+---" * 6 + "+\n"
        return string

    def is_full(self):
        bool = True
        for row in self.board:
            for element in row:
                if element == " ":
                    bool = False

        return bool