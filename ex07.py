from json import dumps

results = [{}, {}]
count = 0
try:
    with open('file_07.txt', 'r', encoding='utf-8') as my_file:
        lines = my_file.readlines()

    for line in lines:
        name, title, proceeds, costs = line.split()
        results[0][name] = int(proceeds) - int(costs)
        if int(proceeds) - int(costs) > 0:
            count += 1

    results[1]['average_profit'] = round(
        sum(profit for name, profit in results[0].items() if profit > 0) / count, 2)

    with open('file_07.json', 'w', encoding='utf-8') as their_file:
        their_file.writelines(dumps(results))
except:
    print("Некорректные данные")
