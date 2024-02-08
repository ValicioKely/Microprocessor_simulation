source_file = ['LDRL r2,1', 'LDRL r0,4', 'NOP', 'STRI r0,[r2]', 'LDRI r3,[r2]', 'INC r3', 'ADDL r3,r3,2', 'NOP',
               'DEC r3',
               'BNE -2', 'DEC r3', 'STOP']
# Class 0: no operand NOP
# Class 1: literal BEQ 3
# Class 2: register INC r1
# Class 3: register,literal LDRL r1,5
# Class 4: register,register, MOV r1,r2
# Class 5: register,register,literal ADDL r1,r2,5
# Class 6: register,register,register ADD r1,r2,r3
# Class 7: register,[register] LDRI r1,[r2
codes = {'NOP': [0], 'STOP': [0], 'BEQ': [1], 'BNE': [1], 'BRA': [1],
         'INC': [2], 'DEC': [2], 'CMPL': [3], 'LDRL': [3], 'MOV': [4],
         'CMP': [4], 'SUBL': [5], 'ADDL': [5], 'ANDL': [5], 'ADD': [6],
         'SUB': [6], 'AND': [6], 'LDRI': [7], 'STRI': [7]}
# Legal register
reg_1 = {'r0': 0, 'r1': 1, 'r2': 2, 'r3': 3}
reg_2 = {'[r0]': 0, '[r1]': 1, '[r2]': 2, '[r3]': 3}
r = [0] * 4
# Preset register for testing
r[0], r[1], r[2], r[3] = 1, 2, 3, 4

# memory
mem = [0] * 8
prog_count = 0
go = 1
z = 0

# main loop
while go == 1:
    current_inst = source_file[prog_count]
    prog_count = prog_count + 1
    old_prog_count = prog_count
    # Remove comma
    temp = current_inst.replace(',', ' ')
    tokens = temp.split(' ')
    mnemonics = tokens[0]
    op_class = codes[mnemonics]
    # Process the current instruction and analyse it
    reg_destination = 0
    reg_destination_value = 0
    reg_source_1 = 0
    reg_value_source_1 = 0
    reg_source_2 = 0
    reg_value_source_2 = 0
    literal = 0
    reg_pointer = 0
    reg_pointer_value = 0

    if op_class in [0]:
        pass
    if op_class in [2, 3, 4, 5, 6, 7, 8]:
        reg_destination = reg_1[tokens[1]]
        reg_destination_value = r[reg_destination]
    if op_class in [4, 5, 6]:
        reg_source_1 = reg_1[tokens[2]]
        reg_value_source_1 = r[reg_source_1]
    if op_class in [6]:
        reg_source_2 = reg_1[tokens[2]]
        reg_value_source_2 = r[reg_source_2]
    if op_class in [1, 3, 5, 8]:
        literal = int(tokens[-1])
    # Indirect addressing
    if op_class in [7]:
        reg_pointer = reg_2[tokens[2]]
        reg_pointer_value = r[reg_pointer]
    if mnemonics == 'STOP':
        go = 0
        print('Program terminated!')
    elif mnemonics == 'NOP':
        pass
    elif mnemonics == 'INC':
        r[reg_destination] = reg_destination_value + 1
    elif mnemonics == 'DEC':
        z = 0
        r[reg_destination] = reg_destination_value - 1
        if z == 0:
            z = 1
    elif mnemonics == 'BRA':
        prog_count = prog_count + literal + 1
    elif mnemonics == 'BEQ':
        if z == 1:
            prog_count = prog_count + literal - 1
    elif mnemonics == 'BNE':
        if z == 0:
            prog_count = prog_count + literal - 1
    elif mnemonics == 'ADD':
        r[reg_destination] = reg_value_source_1 + reg_value_source_2
    elif mnemonics == 'ADDL':
        r[reg_destination] = reg_value_source_1 + literal
    elif mnemonics == 'SUB':
        z = 0
        r[reg_destination] = reg_value_source_1 - reg_value_source_2
        if r[reg_destination] == 0:
            z = 1
    elif mnemonics == 'SUBL':
        z = 0
        r[reg_destination] = reg_value_source_1 - literal
        if r[reg_destination] == 0:
            z = 1
    elif mnemonics == 'CMP':
        z = 0
        diff = reg_value_source_1 - reg_value_source_2
        if diff == 0:
            z = 1
    elif mnemonics == 'CMPL':
        z = 0
        diff = reg_value_source_1 - literal
        if diff == 0:
            z = 1
    elif mnemonics == 'MOV':
        r[reg_destination] = reg_value_source_1
    elif mnemonics == 'LDRL':
        r[reg_destination] = literal
    elif mnemonics == 'LDRI':
        r[reg_destination] = mem[reg_pointer_value]
    elif mnemonics == 'STRI':
        mem[reg_pointer_value] = reg_destination_value
        regs = ''.join('%02x' % b for b in r)
        memory = ''.join('%02x' % b for b in mem)
        print('pc =', '{:<3}'.format(old_prog_count), '{:<14}'.format(current_inst), 'Regs =', regs, 'Mem =', memory,
              'z =', z)
        x = input(' >>> ')
