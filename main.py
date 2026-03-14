from itertools import product, chain
from datetime import datetime

class Board:
    """
    Docstrings
    """
    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

    def __str__(self):

        board = [['.' for x in range(8)] for y in range(8)]
        for piece in chain(self.player1.pieces, self.player2.pieces):
            x, y = piece.pos.x, piece.pos.y
            board[8-y][x-1] = piece.pieceType

        return '\n'.join(' '.join(square for square in row) for row in board) + '\n'

class Position:
    """
    Docstrings
    """
    def __init__(self, position=(None, None)):

        self.x, self.y = position
        self.conversion = dict(zip(range(1, 9), 'abcdefgh'))

    def convert(self, coord):
        """
        Docstrings
        """
        return self.conversion[coord[0]] + str(coord[1])

class Piece:
    """
    Docstrings
    """
    def __init__(self, color, coord, pieceType):

        self.color = color
        self.pos = Position(coord)
        self.pieceType = pieceType

class Player:
    """
    Docstrings
    """
    def __init__(self, color):

        self.color = color
        self.pieces = [Piece(color, coord, pieceType) for coord, pieceType in
                      zip(product(range(1, 9), range(1, 3)), 'TPCPFPQPKPFPCPTP')]

    def move(self, pos1, pos2):
        """
        Docstrings
        """
        for piece in self.pieces:
            currentPosition = (piece.pos.x, piece.pos.y)
            if currentPosition == pos1 and self.isLegalMove(pos1, pos2):
                piece.pos.x, piece.pos.y = pos2
                break

    def eat(self, opponent, pos1, pos2):
        """
        Docstrings
        """
        self.move(pos1, pos2)
        opponent.removePiece(pos2)

    def isLegalMove(self, pos1, pos2):
        """
        Docstrings
        """
        return True

    def removePiece(self, position):
        """
        Docstrings
        """
        for i, piece in enumerate(self.pieces):
            if (piece.pos.x, piece.pos.y) == position:
                del self.pieces[i]
                break

class Robot(Player):
    """
    Docstrings
    """
    def __init__(self, color):

        super().__init__(color)
        self.pieces = [Piece(color, coord, pieceType) for coord, pieceType in
                       zip(product(range(1, 9), range(7, 9)), 'ptpcpfpqpkpfpcpt')]

class Game:
    """
    Docstrings
    """
    switchColor = {'white' : 'black', 'black' : 'white'}

    def __init__(self, color='white'):

        self.player1 = Player(color)
        self.player2 = Robot(self.switchColor[color])
        self.board = Board(self.player1, self.player2)

    def mainloop(self):

        n = 0

        while n <= 3:

            print(self.board)

            pos1 = (int(input('x1: ')), int(input('y1: ')))
            pos2 = (int(input('x2: ')), int(input('y2: ')))
            self.player1.move(pos1, pos2)

            n += 1

if __name__ == "__main__":
    game = Game(color='white')
    game.mainloop()
