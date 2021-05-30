subj = {}
with open('file_06.txt', 'r') as my_file:
    my_list = my_file.readlines()
    for line in my_list:
        data = line.replace('(', ' ').split()
        subj[data[0]] = sum(int(i) for i in data if i.isdigit())
print(subj)

