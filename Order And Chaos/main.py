from Game.Game import Game
from UI.UI import UI

if __name__ == '__main__':
    game = Game()
    ui = UI(game)

    ui.run()

