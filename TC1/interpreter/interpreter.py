# Memory
mem = [4, 6, 1, 2, 7, 8, 4, 4, 5]
# Register
reg = [0, 0, 0, 0, 0, 0, 0, 0]
# IR
inst = 'add reg[4],mem[3],mem[4]'

inst_1 = inst.replace(' ', ',')
inst_2 = inst_1.split(',')
token_0 = inst_2[0]
token_1 = inst_2[1]
token_2 = inst_2[2]
token_3 = inst_2[3]

reg_value = int(token_1[4])
mem_value_1 = int(token_2[4])
mem_value_2 = int(token_3[4])

# ALU
if token_0 == 'add':
    reg[reg_value] = mem[mem_value_1] + mem[mem_value_2]

print("Register r =", reg)
