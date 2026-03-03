from players import Player, Computer
from display import Board
from data import History

from itertools import chain


class Game:

    switchColor = {'white': 'black', 'black' : 'white'}

    def __init__ (self, color='white'):

        self.player1 = Player(color, player=1)
        self.player2 = Computer(self.switchColor[color], player=2)
        self.board = Board(self.player1, self.player2)
        self.gamestate = list(chain(self.player1.pieces, self.player2.pieces))
        self.history = History()

    def mainloop(self): # todo : implement `mainloop`
        pass


if __name__ == "__main__":
    pass

