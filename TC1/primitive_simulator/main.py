# put this program into a text file .. 
prog = ['LDRL r0 0', 'LDRL r1 0', 'ADDL r1 r1 1', 'ADD r0 r0 r1', 'CMPL r1 10', 'BNE 2', 'STOP']
reg = [0] * 8
z = 0
prog_counter = 0
run = True

while run:
    inst = prog[prog_counter]
    old_prog_counter = prog_counter
    prog_counter = prog_counter + 1
    inst = inst.split(' ')
    if inst[0] == 'ADD':
        rd = int(inst[1][1])
        r_s_1 = int(inst[2][1])  # rs1 = inst[2] -> rs1 = rs1[1]
        r_s_2 = int(inst[3][1])
        reg[rd] = reg[r_s_1] + reg[r_s_2]
    elif inst[0] == 'ADDL':
        rd = int(inst[1][1])
        r_s_1 = int(inst[2][1])
        literal = int(inst[3])
        reg[rd] = reg[r_s_1] + literal
    elif inst[0] == 'BNE':
        if z == 0:
            prog_counter = int(inst[1])
    elif inst[0] == 'CMPL':
        z = 0
        reg_value = reg[int(inst[1][1])]
        int_value = int(inst[2])
        if reg_value == int_value:
            z = 1
    elif inst[0] == 'LDRL':
        rd = int(inst[1][1])
        literal = int(inst[2])
        reg[rd] = literal
    elif inst[0] == 'STOP':
        run = False
        print("Program ended")
    else:
        run = False
        print("Error: illegal instruction", inst)

    print("program counter =", old_prog_counter, "r0=", reg[0], "r1= ", reg[1], "z= ", z)
