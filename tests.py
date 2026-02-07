
from itertools import batched


decimal_number = 4_398_066_094_081
print(hex(decimal_number))
number = bin(decimal_number)[2:][::-1]

array = list(batched(list(batched(number, 4)), 2))

print(array)

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

"""


