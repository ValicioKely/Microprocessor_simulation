# Teaching Computer 1
 ## Crafting component 
 ## Program structure
        prog=['LDRL r0 0','LDRL r1 0','ADDL r1 r1 1','ADD r0 r0 r1', \
        'CMPL r1 10','BNE 2','STOP']
        Define and initialize variables (PC, registers, memory)
        while run == True:
            read instruction from prog
            point to next instruction (increment program counter)
            split instruction into fields (opcode plus operands)
            if first field = op-code1 get operands and execute
            elif first field = op-code2 get operands and execute
            elif first field = op code3
            elif first field = op-code3 . . .
            . . .
            else declare an error if no instruction matches.