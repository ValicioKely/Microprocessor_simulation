opCode = {'add': ('Arith', 0b0001, 3), 'ldr': ('Move', 0b1100, 2), 'nop': ('Miscellaneous', 1111, 0)}
regs = {'r0': 0, 'r1': 1, 'r2': 2, 'r3': 3, 'r4': 4}
symTab = {'start': 0, 'time': 24, 'stackP': 'sp', 'next': 0xF2}  # convert symbol into value
test = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
x_0 = 'add r1,r2,r4'
y_0 = 'beq next'
operation = 'ldr'

x_1 = x_0.split(' ')
x_2 = x_1[1].split(',')
op_code = x_2[0]

if op_code in regs:
    op_code_value = regs.get(op_code)
    print("the value of operation in register ", op_code, "is", op_code_value)

y_1 = y_0.split(' ')
y_2 = y_1[1]
y_3 = symTab.get(y_2)

z = symTab.get(y_0.split(' ')[1])
print("beq", hex(z))

if operation in opCode:
    if operation == 'ldr':
        int_class = opCode.get(operation)[0]
        binary_value = opCode.get(operation)[1]
        operands = opCode.get(operation)[2]
        print('\nFor opCode: ', operation, '\nClass = ', int_class, '\nBinary code = ', bin(binary_value), '\nNumber '
                                                                                                           'of '
                                                                                                           'operands= '
                                                                                                           '', operands)
# print formatted dictionary
for key, value in opCode.items():
    print(key, ':', value)
    print()

# store all keys in the dictionary
for i, j in opCode.items():
    print(i, ':', j)
    print()

keys = opCode.keys()
print("There are the keys in the dictionary", keys)
print()

# operation and adding extra data in the dictionary
print("Operation and adding extra data in the dictionary")
print("test[a] before", test['a'])
print()
test['a'] = test['a'] + 1
print("content of test[a] after adding 1 =", test['a'])
# append extra element in the dictionary
test_1 = {'e': 0, 'f': 0}
print("test before", test)
test.update(test_1)
print("test updated!", test)
