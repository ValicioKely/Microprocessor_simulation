print("This program test the fetch cycle")
# Set our memory
memory = [0] * 16
program_counter = 0  # initialize counter to 0
memory[0] = 0b011011111010
memory[1] = 0b100011111111
print(memory)


# func catch content of a memory provided and address
def fetch(mem):
    global program_counter
    mem_add_reg = program_counter
    program_counter = program_counter + 1
    # Take the value off address provided
    mem_buff_reg = mem[mem_add_reg]
    # Store all instruction from buffer
    inst_reg = mem_buff_reg
    control_unit = inst_reg >> 8
    addr = inst_reg & 0xFF
    return control_unit, addr


op_code, address = fetch(memory)
print("pc = ", program_counter, "opcode=", op_code, "operand=", address)
print("pc = ", program_counter - 1, "opcode=", op_code, "operand=", address)
