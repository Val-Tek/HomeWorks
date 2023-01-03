# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.
# Использовать цикл for
n = 1
input_n = input('Input natural number: ')
total = 0
for n in range(n, int(input_n) + 1):
    if n % 3 == 0:
        print(n, " is skipped")
        continue
    n_cub = n ** 3
    total += n_cub
    print(n, n_cub, total)
else:
    print("Total:", total)
