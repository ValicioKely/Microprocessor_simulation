op_code = [('NOP', 'misc', 0), ('BEQ', 'flow', 1), ('LDR', 'move', 2), ('ADD', 'arith', 3)]

for instruction in op_code:
    operation = instruction[0]
    group = instruction[1]
    params = instruction[2]
    if operation == "BEQ":
        print("operation type: ", operation, "\n", "group : ", group, "\n", "params : ", params)
