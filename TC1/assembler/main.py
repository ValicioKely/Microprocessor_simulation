data = './data.txt'
alt_code = ['nop', 'NOP 5', 'add R1,R2', '', 'LDR r1,[r2]', 'ldr r1,[R2]', '\n', 'BEQ test @www', '\n']
source_file = []

# looking for data dict
x = input("press d for disk entry")
if x == 'd':
    with open(data, 'r') as source_0:
        source = source_0.readlines()
        source = [i.replace('\n', '') for i in source]
        print("source code", source)
else:
    source = alt_code

# Process source file in list
for i in range(0, len(source)):
    t_1 = source[i].replace(',', ' ')
    t_2 = t_1.replace('[', ' ')
    t_3 = t_2.replace(']', ' ')
    t_4 = t_3.replace('  ', ' ')
    source_file.append(t_4)
# Remove end of line
source_file = [i for i in source_file if i[-1:] != '\n']
# set all string in uppercase
source_file = [i.upper() for i in source_file]
# remove comment split with @ and take the first result
source_file = [i.split('@')[0] for i in source_file]
source_file = [i.rstrip() for i in source_file]
source_file = [i.lstrip() for i in source_file]
source_file = [i for i in source_file if i != '']
print(source_file)
