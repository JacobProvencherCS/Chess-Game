
from itertools import batched

# todo : work on keyboard shortcuts setup
# todo : go from decimal_number to binary number represent as check board

"""
hex = 0x400012AD001
dec = 4_398_066_094_081

decimal_to_binary(number: int) -> str

Ouput:

0000 0000
0000 0000
0000 0000
0000 0000
0100 0000
0001 0010
1010 1101
0000 0000
0001

0b 1000 0000 0000 0000 0010 0101 0101 1010 0000 0000 0010 0000 0000 0000 0000 0000 0000 0000 0000

 100 0000
0001 0010
1010 1101
0000 0000
0001

0b 1000 0000 0000 0000 0010 0101 0101 1010 0000 0000 001

"""


decimal_number = 4_398_066_094_081
num = bin(decimal_number)[2:][::-1]

def convert_integer_to_board_representation(number: int) -> str:
    return bin(number)

print(convert_integer_to_board_representation(decimal_number))







