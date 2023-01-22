"""
Прочитать сохранённый json-файл из задания №18 и записать данные на диск в csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
"""
import csv
import json
import random

with open('json_file.json') as f:
    data_for_csv = json.load(f)
print('data_for_csv: ', data_for_csv)

name_of_fields = ['id', 'Name', 'Age', 'Phone']
print('name_of_fields: ', name_of_fields)

ids = list(data_for_csv.keys())
print('ids: ', ids)

person = list(data_for_csv.values())
print('person: ', person)

first_num = ['097-', '098-', '066-', '068-', '050-', '099-', '079-']
num_list = []
while len(num_list) < len(person):
    num1 = random.choice(first_num) + str(random.randint(10, 99)) \
           + '-' + str(random.randint(10, 99))
    num = random.choice([num1, 'no number', 'no number', 'no number'])
    if not num in num_list:
        num_list.append(num)

print('phone numbers: ', num_list)

index = 0
while index < len(person):
    person[index].insert(0, ids[index])
    person[index].insert(4, num_list[index])
    index += 1
print('final: ', person)
with open('file_csv1.csv', mode='w', encoding='utf-8', newline='') as f:
    file_writer = csv.writer(f)
    file_writer.writerow(name_of_fields)
    for item in person:
        file_writer.writerow(item)


