# loop for each element in list
# loop stop when item is reached
data = ['ADD', 'BEQ', '', 'LDRL', '']
size_of_data = len(data)
inList = False
if "BEQ" in data:
    inList = True
    print("data reached")
if not inList:
    print("data missing")
