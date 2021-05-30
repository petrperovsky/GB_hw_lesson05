with open('file_5.txt', 'w') as my_file:
    line = input('Enter your number separated by a space:\n')
    my_file.writelines(line)
    numbs = line.split()
print(sum(map(float, numbs)))
