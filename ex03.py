with open('salary.txt', 'r') as my_file:
    poor_person = []
    sal = []
    my_list = my_file.readlines()
    for line in my_list:
        el = line.split()
        if el[1] < '20000':
            poor_person.append(el[0])
        sal.append(el[1])
print(f'Average salary is {sum(map(int, sal)) / len(sal)}, the poorest persons are {poor_person}')
