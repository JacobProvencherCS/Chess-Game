
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
for i in range(8, 16):
    white_pawns |= 1 << i

black_occupancy = black_pawns | black_rooks | black_knights | black_bishops | black_queen | black_king
white_occupancy = white_pawns | white_rooks | white_knights | white_bishops | white_queen | white_king

all_occupancy = black_occupancy |white_occupancy

pieces = [black_pawns, black_rooks, black_knights, black_bishops, black_queen, black_king,
          white_pawns, white_rooks, white_knights, white_bishops, white_queen, white_king,
          black_occupancy, white_occupancy,
          all_occupancy]

def req_binaire_formate(n: int) -> str:
    n = f"{n:064b}"
    return "\n".join((n[8*m:8*m+8] for m in range(8)))

print(req_binaire_formate(pieces[WQ]))
print()

# print(req_binaire_formate(pieces[WQ] << 1)) # move one left
# print(req_binaire_formate(pieces[WQ] >> 1)) # move one right
# print(req_binaire_formate(pieces[WQ] << 8)) # move one up
# print(req_binaire_formate(pieces[WQ] << 8 << 1)) # move one up-left
print(req_binaire_formate(pieces[WQ] << 8 >> 1)) # move one up-right

# todo : how to move just one pawn (not all of them) ?
# todo : how to know if move is results in out-of-bound position ?






