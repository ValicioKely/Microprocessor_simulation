memory = [7, 5, 4, 0, 3, 9, 0, 0]

pointer_0 = memory[0]
pointer_1 = memory[1]
pointer_2 = memory[2]
pointer_3 = memory[3]

source_1 = memory[pointer_1]
source_2 = memory[pointer_2]

sum_res = source_2 + source_1
memory[pointer_0] = sum_res

print(memory, " ", sum_res)