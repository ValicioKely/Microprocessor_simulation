# example of iteration over a list
data = ['ADD', 'BEQ', '', 'LDRL','']
size_of_data = len(data)
inList = False
for op_code in range (0, size_of_data):
    if data[op_code] == "SUB":
        print(data[op_code])
        inList = True
if not inList:
    print("data missing")
