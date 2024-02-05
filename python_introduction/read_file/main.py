data_from_dict = 'data.txt'

with open(data_from_dict, 'r') as source_file:
    data = source_file.readline()
    for i in range(0, len(data)):
        data[i] = data[i].rstrip()
        print(data)
source_file.close()
