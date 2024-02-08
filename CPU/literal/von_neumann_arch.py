# We load the literal 9 into r0, subtract the contents of memory location 7
# (which contains 9), and then branch to location 6 if the result was 0
memory = [0] * 12

prog_count = 0
z = 0
run = 1
memory[0] = 0b000100001001
memory[1] = 0b001100000111
memory[2] = 0b010000000110
memory[3] = 0b111100000000
memory[6] = 0b111100000000  # Stop instruction
memory[7] = 9


def fetch(mem):
    global prog_count
    inst_reg = mem[prog_count]
    prog_count = prog_count + 1
    return inst_reg >> 8, inst_reg & 0xFF


# Main loop to do operation
while run == 1:
    old_prog_count = prog_count
    op_code, address = fetch(memory)
    if op_code == 0b1111:   # STOP
        run = 0
    elif op_code == 0b0001:  # LDRL r0, 9
        r_0 = address
    elif op_code == 0b0010:  # SUB r0, 7
        r_0 = r_0 + memory[address]
    elif op_code == 0b0011:
        r_0 = r_0 - memory[address]
        if r_0 == 0:
            z = 1
        else:
            z = 0
    elif op_code == 0b0100:
        if z == 1:  # BEQ 6
            prog_count = address
    print("pc =", old_prog_count, "operation code =", op_code, "\tRegister r_0 =", r_0, "Z= ", z)
