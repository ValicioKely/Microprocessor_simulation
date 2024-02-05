
def alu(op, value_1, value_2):
    global z_flag, neg_flag
    z_flag = 0
    neg_flag = 0
    if op == 1:
        res = value_1 + value_2
    if op == 2:
        res = value_1 - value_2
    if res == 0:
        z_flag = 1
    if res & 0xFFFF == 0:
        z_flag = 0
    if res & 0x8000 != 0:
        neg_flag = 1
    return 0xFFFF & res  # return res in 16 bits
