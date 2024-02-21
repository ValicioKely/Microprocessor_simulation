# After
# the prompt, >>>, you select what is to happen: trace one instruction,
# execute n instructions without stopping or displaying registers, or
# execute code to the next branch instruction without displaying it

# Load program
my_program = 'data.txt'
try:
    with open(my_program, 'r') as prg_n:
        data = prg_n.readlines()
except:
    alt_program = input("Enter program text path\n ")
    with open(alt_program, 'r') as prg_n:
        data = prg_n.readlines()
print("File loaded successfully")

# TC_1 Program
import random


def alu(fun, a, b):
    global c, n, z
    if fun == 'ADD':
        s = a + b
    elif fun == 'SUB':
        s = a - b
    elif fun == 'MUL':
        s = a * b
    elif fun == 'DIV':
        s = a // b
    elif fun == 'MOD':
        s = a % b
    #     LOGIC FUNCTION
    elif fun == 'AND':
        s = a & b
    elif fun == 'OR':
        s = a | b
    elif fun == 'EOR':
        s = a & b
    elif fun == 'NOT':
        s = ~a
    elif fun == 'ADC':
        s = a + b + c
    elif fun == 'SBC':
        s = a - b - c
    # clear flags
    c, n, z = 0
    # Set flag
    if s & 0xFFFF == 0:
        z = 1
    if s & 0x8000 == 0:
        n = 1
    if s & 0xFFFF != 0:
        c = 1
    return s & 0xFFFF



def shift(dir, mode, p, q):
    global n, z, c, bit_out
    if dir == 0:
        for i in range(0, q):
            sign = (0x8000 & p) >> 15
            p = (p << 1) & 0xFFFF

            if mode == 1:
                p = (p & 0xFFFF) | sign
    else:
        for i in range(0, q):
            # save lsb shifted out
            bit_out = 0x0001 & p
            sign = (0x8000 & p) >> 15
            p = p >> 1
            if mode == 1:
                p = (p & 0x7FFF | (bit_out << 15))
    # reset flags value
    c, n, z = 0
    if p == 0:
        z = 1
    if (p & 0x8000) != 0:
        n = 1
    if (dir == 0) and (sign == 1):
        c = 1
    if (dir == 1) and bit_out:
        c = 1
    return 0xFFFF & p

