from enum import Enum

class Piece(Enum):

    BP = 0
    BR = 1
    BN = 2
    BB = 3
    BQ = 4
    BK = 5

    WP = 6
    WR = 7
    WN = 8
    WB = 9
    WQ = 10
    WK = 11

    BO = 12
    WO = 13

    AO = 14

black_rooks = (1 << 63) | (1 << 56)
black_knights = (1 << 62) | (1 << 57)
black_bishops = (1 << 61) | (1 << 58)
black_queen = (1 << 60)
black_king = (1 << 59)
black_pawns = 0
for i in range(48, 56):
    black_pawns |= 1 << i


white_rooks = (1 << 7) | (1 << 0)
white_knights = (1 << 6) | (1 << 1)
white_bishops = (1 << 5) | (1 << 2)
white_queen = (1 << 4)
white_king = (1 << 3)
white_pawns = 0
for i in range(7, 16):
    white_pawns |= 1 << i

black_occupancy = black_pawns | black_rooks | black_knights | black_bishops | black_queen | black_king
white_occupancy = white_pawns | white_rooks | white_knights | white_bishops | white_queen | white_king

all_occupancy = black_occupancy |white_occupancy

pieces = [
    black_pawns, black_rooks, black_knights, black_bishops, black_queen, black_king,
    white_pawns, white_rooks, white_knights, white_bishops, white_queen, white_king,
    black_occupancy, white_occupancy,
    all_occupancy
]

for piece in Piece:
    print(f"{piece}: {bin(pieces[piece.value])}")


"""
Piece.BP: 0b11111111000000000000000000000000000000000000000000000000
Piece.BR: 0b1000000100000000000000000000000000000000000000000000000000000000
Piece.BN: 0b100001000000000000000000000000000000000000000000000000000000000
Piece.BB: 0b10010000000000000000000000000000000000000000000000000000000000
Piece.BQ: 0b1000000000000000000000000000000000000000000000000000000000000
Piece.BK: 0b100000000000000000000000000000000000000000000000000000000000
Piece.WP: 0b1111111110000000
Piece.WR: 0b10000001
Piece.WN: 0b1000010
Piece.WB: 0b100100
Piece.WQ: 0b10000
Piece.WK: 0b1000
Piece.BO: 0b1111111111111111000000000000000000000000000000000000000000000000
Piece.WO: 0b1111111111111111
Piece.AO: 0b1111111111111111000000000000000000000000000000001111111111111111
"""


