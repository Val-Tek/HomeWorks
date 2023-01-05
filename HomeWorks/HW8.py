# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число, а значение - сколько раз оно встречается).
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.
list_num = [4, 3, 6, 2, 6, 4, 1, 9, 11, 45, 29, 29, 5, 27, 1, 4, 3, 7, 2, 4, 1, 8, 5, 3, 7, 45, 3]

def func_count(list_num):
    counts = {}
    for num in list_num:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

def func_count2(lst):
    counts = {}
    for num in lst:
        if num not in counts:
            counts[num]=len([x for x in lst if x==num])
    return counts

print(func_count(list_num))
print(func_count2(list_num))

