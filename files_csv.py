import csv
users_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Иван', 'age': 23, 'job': 'Student'},
        {'name': 'Сергей', 'age': 50, 'job': 'Worker'},
        {'name': 'Мария', 'age': 34, 'job': 'Teacher'},
    ]
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in users_list:
        writer.writerow(user)
    print('Список записан в файл.')