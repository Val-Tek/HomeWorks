# Прочитать сохранённый json-файл из задания №18 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import csv
import json

with open('HW18.json', 'r') as file:
    dictionary = json.load(file)
    name_of_fields = ['id', 'name', 'age', 'phone']
    if len(dictionary) > 0:
        fields = []
        fields.append(name_of_fields)
        for key, values in dictionary.items():
            values.insert(0, key)
            values.append(",,")
            fields.append(values)
with open('HW19.csv', mode='w', encoding='utf-8') as data_list:
    w_file = csv.writer(data_list)
    for item in fields:
        w_file.writerow(item)