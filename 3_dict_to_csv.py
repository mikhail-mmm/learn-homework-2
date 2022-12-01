"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

people = [
    {'name': 'Евгений', 'age': '33', 'job': 'Engineer'},
    {'name': 'Роман', 'age': '25', 'job': 'Researcher'},
    {'name': 'Василий', 'age': '40', 'job': 'Technician'},
    {'name': 'Николай', 'age': '55', 'job': 'Head of Department'},
    {'name': 'Ярослав', 'age': '30', 'job': 'Programmer'}
]

def main():
    with open('people.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, delimiter = ";", lineterminator="\r", fieldnames=['name', 'age', 'job'])
        writer.writeheader()
        writer.writerows(people)

if __name__ == "__main__":
    main()
