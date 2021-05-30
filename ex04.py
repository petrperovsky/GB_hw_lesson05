translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('count.txt', 'r') as old_file:
    my_list = old_file.readlines()
    for line in my_list:
        el = line.split(' ', 1)
        new_file.append(translate[el[0]] + ' ' + el[1])
with open('count_new.txt', 'w') as my_file:
    my_file.writelines(new_file)
