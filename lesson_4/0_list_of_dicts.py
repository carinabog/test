workers = [
    {'name': 'Alex', 'salary': 10000, "sex": "m"},
    {'name': 'Diana', 'salary': 12000, "sex": "f"},
    {'name': 'Dmitry', 'salary': 3000, "sex": "b"}
]

for worker in workers:
	# print('for ' + worker['name'] + ' salary is ' + str(worker['salary']) + 'and sex is ' + )
    # print("worker %s salary is %s and sex is %s" % (worker['name'], worker['salary'], worker['sex']))
    print("worker %s" % worker["name"])

# Вот так можно узнать длинну списка
print(len(workers))

# Вывести все имена сотрудников
# Вывести всех сотрудников и их зарплаты, больше и равные 10000
# Придумать кортеж и добавить к нему элемент
# Придумать словарь списков
