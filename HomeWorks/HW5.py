# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.
# Использовать цикл while
n = 1
input_n = input('Input value: ')
total=0
while n <= int(input_n):
    if n % 3 == 0:
        print(n, " is skipped")
        n += 1
        continue
    n_cub=n**3
    total+=n_cub
    print(n, n_cub, total)
    n += 1
print("Total:",total)