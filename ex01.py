my_file = open('test.txt', 'w')
my_str = input('Your text: ') + '\n'
while True:
    my_file.writelines(my_str)
    my_str = input('Your text: ') + '\n'
    if my_str == '\n':
        break
my_file.close()
