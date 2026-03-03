class Player:

    def __init__(self, color, player=1):
        self.color = color
        self.turn = False
        self.name, y = ('player', 1) if player == 1 else ('player', 8)
        self.king = King(color, (5, y))  # todo : implement `King`
        self.pawns = [Pawn(color, (x, (2 if player == 1 else 7))) for x in range(1, 9)]  # todo : implement `Pawn`
        self.pieces = [
                          Rook(color, (1, y)), Rook(color, (8, y)),
                          Knight(color, (2, y)), Knight(color, (7, y)),
                          Bishop(color, (3, y)), Bishop(color, (6, y)),
                          Queen(color, (4, y)), self.king
                      ] + self.pawns  # todo : implement `Rook`, `Knight`, `Bishop` & `Queen`


class Computer(Player):
    pass
