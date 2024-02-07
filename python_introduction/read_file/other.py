data_from_dict = 'data.txt'

with open(data_from_dict, 'r') as source_file:
    data = source_file.readlines()
    data = [i for i in data if i != ' ']
    data = [i.upper() for i in data]
    data = [i.split() for i in data if i != ' ']
    print(data)
source_file.close()
