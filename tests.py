import numpy as np
import sys

"""
board = np.array([
    [2, 4, 3, 5, 6, 4, 3, 2],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [9, 9, 9, 9, 9, 9, 9, 9],
    [10, 11, 12, 13, 14, 12, 11, 10]
])
"""

board = np.zeros((8, 8), dtype=int)

def get_position(num: int) -> tuple[int, int]:

    index = num.bit_length() - 1
    row = 7 - index // 8
    col = 7 - index % 8

    return row, col


piece = 0b1000_1110
mask = 0b1111
# board[piece.position] = piece.info (where piece.position = 1000 and piece.info = 1110)


print(get_position(0b1000)) # (0, 3) -> (7, 4)
print(get_position(0b10_0000_0000_0000)) # (6, 2)
print(get_position(0b1000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000)) # (0, 0)

# pieces
# pieces -> board
# board -> display

# todo : write every piece integer representation in a numpy array (piece array)
# todo : loop through piece array to add them to a board array
# todo : display clean formatted board using board array






















# white_pawn_d2 = int(0b1_0000_0000_0000_1000)
# black_queen_c6 = int(0b0010_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0101)

### Convert binary number to 2D array
# First method
x = 0b1010101010101010101010101010101010101010101010101010101010101010
bits = np.array(list(np.binary_repr(x, width=64)), dtype=int)
matrix = bits.reshape((8, 8))

# Second method (cleaner)
x = np.array([142], dtype=np.uint64)
bits = np.unpackbits(x.view(np.uint8))
matrix = bits.reshape(8, 8)

# One-liner
x = 0b1000_1110
matrix = np.unpackbits(np.array([x], dtype=np.uint64).view(np.uint8)).reshape(8, 8)
