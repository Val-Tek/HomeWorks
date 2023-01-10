# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка:
from datetime import datetime
def time_dekor(t_function):
    def wrapper(*args):
        now = datetime.now()
        result = t_function(*args)
        print("time spending: ", datetime.now() - now)
        return result
    return wrapper

list_num = [4, 3, 6, 2, 6, 4, 1, 9, 11, 45, 29, 29, 5, 27, 1, 4, 3, 7, 2, 4, 1, 8, 5, 3, 7, 45, 3]
# now = datetime.now()
@time_dekor
def func_count(list_num):
    counts = {}
    for num in list_num:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

# print("time spending: ", datetime.now() - now)


@time_dekor
def func_count2(lst):
    counts = {}
    for num in lst:
        if num not in counts:
            counts[num] = len([x for x in lst if x == num])

    return counts


print(func_count(list_num))
print(func_count2(list_num))
