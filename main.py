from mainGame import Game
from menu import Menu

if __name__ == "__main__":
    menu = Menu()
    mainGame = Game()
    while True:
        menu.run()
        mainGame.run()
