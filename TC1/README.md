# Teaching Computer 1
 ## Crafting component 
 ## Step to do:
 - Designing a minimal computer with one instruction
    
    ######  Memory
        mem = [4, 6, 1, 2, 7, 8, 4, 4, 5]
    ######  Registers
          reg = [0,0,0,0,0,0,0,0] # reg = [0] * 8
    
   - Designing a simple simulator that can decode and execute several
instructions

          
 - The instruction set of a general-purpose computer called TC1

    ######  Instruction
           ADD reg[4], mem[3] , mem[4] # This mean reg[4] = 2 + 7
 - Handing bits in Python (Boolean operations)

            if token_0 == 'add':
 - Decoding an instruction in binary form into its component parts

            inst_1 = inst.replace(' ', ',')
            inst_2 = inst_1.split(',')
            token_0 = inst_2[0]
            token_1 = inst_2[1]
            token_2 = inst_2[2]
            token_3 = inst_2[3]
 - Executing an instruction after it has been decoded
 - Arithmetic operations in a computer

           reg[reg_value] = mem[mem_value_1] + mem[mem_value_2]

 - Designing functions in Python
 - Branch and flow control instructions in computer instruction sets
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
  ## Encoding operation 
  ###### Example
consider the following bin operation
   #### 10 00000 001 010 011 0000000000000000
        10 : Arithmetic and logic data-processing operations Group
        00000 : operation type ADD
        001 : register destination 
        010 : source 1
        011 : source 2
        0000000000000000 :  literal
        assembly code ADD rd, r1, r2
