# Set our memory
memory = [0] * 12  # 12 memory location
program_counter = 0  # initialize counter to 0
memory[0] = 0b000100001100
memory[1] = 0b001000000111
memory[2] = 0b111100000000
memory[7] = 8
print(memory)


# fetch function
def fetch(mem):
    global program_counter
    inst_reg = mem[program_counter]
    program_counter = program_counter + 1
    return inst_reg >> 8, inst_reg & 0xFF

run = 1
while run == 1:
    op_code, addr = fetch(memory)
    if op_code == 0b1111:
        run = 0
    if op_code == 0b0001:
        r_0 = addr
    elif op_code == 0b0010:
        mem_addr_reg = addr
        mem_buff_reg = memory[mem_addr_reg]
        r_0 = mem_buff_reg + r_0
    print("pc =", program_counter - 1, "opCode=", op_code, "Register r0=", r_0)
