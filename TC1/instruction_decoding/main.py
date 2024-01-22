memory = [0] * 32
reg = [0] * 16
# put assembly code in a text file and convert it into binary code
bin_code = 0b10000000010100110000000000000000

bin_op = bin_code >> 25
reg_dest = bin_code >> 22 & 0b111  # extract register destination and mask it to 3 bit i-e 101
r_s_1 = bin_code >> 19 & 0b111
r_s_2 = bin_code >> 16 & 0b111
literal = bin_code & 0xFFF  # extract 16 bits of literal

# value of each element in the register
value_dest = reg[reg_dest]
value_1 = reg[r_s_1]
value_2 = reg[r_s_2]
