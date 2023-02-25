

class UI:
    def __init__(self, game):
        self.__game = game

    def run(self):
        player_turn = False
        while True:
            print(self.__game.board)
            if player_turn:
                try:
                    x_coordinate = int(input("X: "))
                    y_coordinate = int(input("Y: "))
                    symbol = input("Symbol: ")
                    self.__game.player_move(x_coordinate, y_coordinate, symbol)
                except ValueError:
                    print("Bad move")
                    player_turn = not player_turn
            else:
                self.__game.computer_move()
            win = self.__game.check_win()
            if win is not None:
                print(self.__game.board)
                print(win)
                break
            player_turn = not player_turn


