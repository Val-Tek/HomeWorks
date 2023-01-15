# Написать программу которая состоит из вечного цикла ожидающего ввод числа или одно из значений:
# "выход", "exit", "quit", "e" или "q" в любом регистре.
# При вводе одного из этих значений происходит выход из вечного цикла.
# При любом другом вводе вызывается отдельная функция которая умеет распознавать введённые числа.
# Сама функция ничего не распечатывает, она возвращает строку, типа: "Вы ввели отрицательное дробное число: -6.7" или
# "Вы ввели не корректное число: Erdf"
# Затем в цикле выводится это сообщение и цикл начинается заново ожидая следующего ввода.
# Функция на вход принимает строку из ввода из вечного цикла. Анализирует её исключительно методом .isdigit()
# и другими методами строк, без доп.библиотек и переводит строку в число, если это возможно.
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же распознаёт десятичные дроби как с точкой,
# так и с запятой.
# Функция возвращает строку в которой описывается какое число введено - отрицательное или положительно,
# целое или дробное и выводит его или же сообщает, что введено не корректное число.
# *Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля

def lera_func(inp):
    clean = inp
    clean = clean.replace("-", "")
    clean = clean.replace(",", "")
    clean = clean.replace(".", "")

    if not clean.isdigit():
        return "You entered invalid input: " + inp
    minus=inp.count('-')
    if minus > 1:
        return "You entered invalid input: " + inp
    indot = inp
    if "," in indot:
        indot = indot.replace(",", ".")
    if "." in indot:
        dotcount = indot.count(".")
        if dotcount > 1:
            return "You entered invalid float: " + inp
        num = float(indot)
        type_num = "float"
    else:
        num = int(indot)
        type_num = "integer"
    if num == 0:
        return "You entered Zero: " + inp
    sign = "?"
    if num > 0:
        sign = "positive"
    if num < 0:
        sign = "negative"
    return (f'You entered a {sign} {type_num} : {inp}.')


while True:
    inp = input("Give us a number or exit: ")
    if inp.lower() in ["выход", "exit", "quit", "e", "q"]:
        break
    print(lera_func(inp))
