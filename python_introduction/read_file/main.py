data_from_dict = 'read_file/data.txt'

with open(data_from_dict, 'r') as source_file:
    data = source_file.readline()
    print(data)
    for i in range(0, len(data)):
        data[i] = data[i].rstrip()
        print(data)
source_file.close()
