"""
Прочитать сохранённый json-файл из задания №18 и записать данные на диск в csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
"""
import csv
import json
import random

with open('../json_file.json') as f:
    data_for_csv = json.load(f)
print('data_for_csv: ', data_for_csv)

name_of_fields = ['', 'Person1', 'Person2', 'Person3', 'Person4', 'Person5']
print('name_of_fields: ', name_of_fields)

ids = list(data_for_csv.keys())
ids.insert(0, 'id')
print('ids: ', ids)

names_age = []
for x in data_for_csv.values():
    for i in x:
        names_age.append(i)

names = names_age[::2]
names.insert(0, 'name')
print('names: ', names)

age = names_age[1::2]
age.insert(0, 'age')
print('age: ', age)

first_num = ['097-', '098-', '066-', '068-', '050-', '099-', '079-']
num_list = []
while len(num_list) < len(names) - 1:
    num1 = random.choice(first_num) + str(random.randint(10, 99)) \
           + '-' + str(random.randint(10, 99))
    num = random.choice([num1, 'no number', 'no number', 'no number'])
    if not num in num_list:
        num_list.append(num)
num_list.insert(0, 'phone')
print('phone numbers: ', num_list)

with open('../file_csv.csv', mode='w', encoding='utf-8', newline='') as f:
    file_writer = csv.writer(f)
    file_writer.writerow(name_of_fields)
    file_writer.writerow(ids)
    file_writer.writerow(names)
    file_writer.writerow(age)
    file_writer.writerow(num_list)



