#Написать программу используя функции input() и print().
# Программа запрашивает ввести произвольную строку.
# Затем необходимо создать 2 строковые переменные, первая из которых состоит только из чётных символов введённой строки,
# а вторая состоит из введённой строки написанной в обратной последовательности,
# при этом все буквы должны быть написаны в верхнем регистре.
# В качестве результата вывести введённую строку и 2 получившиеся новые строки, каждую с новой строчки.
a=input()
print(a.upper())
a_even=(a[1::2])
a_rev=(a[::-1])
print(a_even.upper())
print(a_rev.upper())

