# Class 0: no operand NOP
# Class 1: literal BEQ 3
# Class 2: register INC r1
# Class 3: register,literal LDRL r1,5
# Class 4: register,register, MOV r1,r2
# Class 5: register,register,literal ADDL r1,r2,5
# Class 6: register register register ADD r1 r2 r3 tiny
# Class 6: register,register,register ADD r1,r2,r3
# Class 7: register,[register] LDRI r1,[r2]
import sys  # NEW

op_class = {'NOP': [0], 'STOP': [0], 'END': [0], 'ERR': [0], 'BEQ':
    [1], 'BNE': [1], 'BRA': [1], 'INC': [2], 'DEC': [2], 'NOT': [2], 'CMPL':
                [3], 'LDRL': [3], 'DBNE': [3], 'MOV': [4], 'CMP': [4], 'SUBL': [5], 'ADDL':
                [5], 'ANDL': [5], 'ADD': [6], 'SUB': [6], 'AND': [6], 'OR': [6], 'LDRI':
                [7], 'STRI': [7]}
reg1 = {'r0': 0, 'r1': 1, 'r2': 2, 'r3': 3, 'r4': 4, 'r5': 5, 'r6': 6, 'r7': 7}  # Registers
reg2 = {'[r0]': 0, '[r1]': 1, '[r2]': 2, '[r3]': 3, '[r4]': 4, '[r5]': 5, '[r6]': 6, '[r7]': 7}  # Pointer registers
symTab = {}  # Symbol table
r = [0] * 8  # Register set
m = [0] * 8
prog = [] * 32  # Program memory


def equates():  # Process directives and delete from source
    global symTab, sFile
    for i in range(0, len(sFile)):  # Deal with equates
        temp_line = sFile[i].split()
        if len(temp_line) > 2 and temp_line[1] == 'EQU':
            # If line > 2 tokens and secondEQU
            print('SYMB', sFile[i])
            symTab[temp_line[0]] = temp_line[2]  # Put third eg_destination token EQU  in symbol table
            sFile = [i for i in sFile if i.count('EQU') == 0]  # Remove all lines with 'EQU'
            print('Symbol table ', symTab, '\n')
            return ()


def class_decode(predicate):
    lit, reg_destination, rs_1, rs_2 = '', 0, 0, 0  # Initialize variables
    if op_class in [1]:
        lit = predicate
    if op_class in [2]:
        reg_destination = reg1[predicate]
    if op_class in [3, 4, 5, 6, 7]:
        predicate = predicate.split(',')
        reg_destination = reg1[predicate[0]]
    if op_class in [4, 5, 6]:
        rs_1 = reg1[predicate[1]] \
            # Get source reg 1    for classes 4, 5, and 6
    if op_class in [3, 5]:
        lit = (predicate[-1])  # Get literal    for classes 3 and 5
    if op_class in [6]:
        rs_2 = reg1[predicate[2]]  # Get    source reg 2 for class 6
    if op_class in [7]:
        rs_1 = reg2[predicate[1]]  # Get    source pointer reg for class 7
    return lit, reg_destination, rs_1, rs_2


# Testing input
def test_line(tokens):  # Check there's a valid instruction in this line
    error = 1
    if len(tokens) == 1:
        if tokens[0] in op_class:
            error = 0
        else:
            if (tokens[0] in op_class) or (tokens[1] in op_class): error = 0
        return error


def test_index():  # Test for reg or memory index out of range
    print('reg_destination,rs_1 =', reg_destination, rs_1, 'r[rs_1] =', r[rs_1], 'len(m)', len(m), 'mnemonic =',
          mnemonic)
    if reg_destination > 7 or rs_1 > 7 or rs_1 > 7:
        print('Register number error')
        sys.exit()  # Exit programon register error
    if mnemonic in ['LDRI', 'STRI']:
        if r[rs_1] > len(m) - 1:
            print(' Memory index error')
            sys.exit()  # Exit program on pointer error
    return ()


def get_lit(lit_v):  # Extract a   literal (convert formats)
    if lit_v == '':
        return 0  # Return 0 if literal field empty
    if lit_v in symTab:  # Look in symbol table and get value if there
        lit_v = symTab[lit_v]  # Read the symbol value as a string
        lit = int(lit_v)  # Convertstring to integer
    elif lit_v[0] == '%':
        lit = int(lit_v[1:], 2)  # If % convertbinary to int
    elif lit_v[0:1] == '$':
        lit = int(lit_v[1:], 16)  # If first symbol $ , convert hex to int
    elif lit_v[0] == '-':
        lit = (-int(lit_v[1:])) & 0xFFFF  # Deal with negative values
    elif lit_v.isnumeric():
        lit = int(lit_v)  # Convert decimal string to integer
    else:
        lit = 0  # Default value 0 (if all else fails)
    return lit


prgN = 'NewIdeas_1.txt'  # prgN =program name: test file
sFile = []  # sFile source data
with open(prgN, 'r') as prgN:  # Open it and read it
    prgN = prgN.readlines()
    for i in range(0, len(prgN)):  # First level of text-processing
        prgN[i] = prgN[i].replace('\n', '')  # Remove newline code in source
        prgN[i] = ' '.join(prgN[i].split())  # Remove multiple spaces
        prgN[i] = prgN[i].strip()  # First strip spaces
        prgN = [i.split('@')[0] for i in prgN]  # Remove comment fields

    while '' in prgN:
        prgN.remove('')  # Remove blank lines

    for i in range(0, len(prgN)):  # Copy source to sFile: stop on END
        sFile.append(prgN[i])  # Build new source text file sFile
        if 'END' in sFile[i]: break  # Leave on 'END' and ignore any more source text ignore any more source text

    for i in range(0, len(sFile)):
        print(sFile[i])
        print()
        equates()

    for i in range(0, len(sFile)):
        print(sFile[i])
    print()
    for i in range(0, len(sFile)):  # We need to compile a list of labels
        label = ''  # Give each line a default empty label
        predicate = ''  # Create default predicate (label+ mnemonic + predicate)
        tokens = sFile[i].split(' ')  # Split into separate groups
        error = test_line(tokens)  # Test for an invalid instruction
        if error == 1:  # If error found
            print('Illegal instruction', tokens, 'at', i)
            sys.exit()  # Exit program

        numTokens = len(tokens)  # Process this line
        if numTokens == 1: mnemonic = tokens[0]
        if numTokens > 1:
            if tokens[0][-1] == ':':
                symTab.update({tokens[0][0:-1]: i})  # Insert new value and line number
                label = tokens[0][0:-1]
                mnemonic = tokens[1]
            else:
                mnemonic = tokens[0]
                predicate = tokens[-1]
                op_class = op_class.get(mnemonic)[0]  # Use the mnemonic to read opClass from codes dictionary
                thisLine = list((i, label, mnemonic, predicate, op_class))
                prog.append(thisLine)  # Program line + label + mnemonic+ predicate + opClass
                print('Symbol table ', symTab, '\n')  # Display symbol table for equates and line labels

# Instruction execution
run = 1
z = 0
pc = 0
while run == 1:
    thisOp = prog[pc]
    if thisOp[2] in ['STOP', 'END']:
        run = 0  # Terminate on STOP or END
    pcOld = pc
    pc = pc + 1
    mnemonic = thisOp[2]
    predicate = thisOp[3]
    op_class = thisOp[4]
    lit, reg_destination, rs_1, rS2 = class_decode(predicate)
    lit = get_lit(lit)
    if mnemonic == 'NOP':
        pass
    elif mnemonic == 'BRA':
        pc = lit
    elif mnemonic == 'BEQ':
        if z == 1:
            pc = lit
    elif mnemonic == 'BNE':
        if z == 0:
            pc = lit
    elif mnemonic == 'INC':
        r[reg_destination] = r[reg_destination] + 1
    elif mnemonic == 'DEC':
        z = 0
        r[reg_destination] = r[reg_destination] - 1
        if r[reg_destination] == 0:
            z = 1
    elif mnemonic == 'NOT':
        r[reg_destination] = (~r[reg_destination]) & 0xFFFF  # Logical NOT
    elif mnemonic == 'CMPL':
        z = 0
        diff = r[reg_destination] - lit
        if diff == 0:
            z = 1
    elif mnemonic == 'LDRL':
        r[reg_destination] = lit
    elif mnemonic == 'DBNE':
        r[reg_destination] = r[reg_destination] - 1
        if r[reg_destination] != 0:
            pc = lit
    elif mnemonic == 'MOV':
        r[reg_destination] = r[rs_1]
    elif mnemonic == 'CMP':
        z = 0
        diff = r[reg_destination] - r[rs_1]
        if diff == 0: z = 1
    elif mnemonic == 'ADDL':
        r[reg_destination] = r[rs_1] + lit
    elif mnemonic == 'SUBL':
        r[reg_destination] = r[rs_1] - lit
    elif mnemonic == 'ADD':
        r[reg_destination] = r[rs_1] + r[rS2]
    elif mnemonic == 'SUB':
        r[reg_destination] = r[rs_1] - r[rS2]
    elif mnemonic == 'AND':
        r[reg_destination] = r[rs_1] & r[rS2]
    elif mnemonic == 'OR':
        r[reg_destination] = r[rs_1] | r[rS2]
    elif mnemonic == 'LDRI':
        test_index()
        r[reg_destination] = m[r[rs_1]]
    elif mnemonic == 'STRI':
        test_index()
        m[r[rs_1]] = r[reg_destination]
        regs = ' '.join('%04x' % b for b in r)  # Format memory location's hex
        mem = ' '.join('%04x' % b for b in m)  # Format register's hex
        print('pc =', '{:<3}'.format(pcOld), '{:<18}'.format(sFile[pcOld]), 'regs =', regs, 'Mem=', mem, 'z =', z)
