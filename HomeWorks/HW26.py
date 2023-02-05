# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.


class MyOperationException(Exception):
    pass


def start_calculator():
    print("Welcome to calculator!")
    while True:
        s = input("Enter the first number (or q to quit) : ")
        if s == "q":
            print("Thank you for using my calculator")
            break
        try:
            x = float(s)
        except ValueError:
            print("That was no valid number.  Try again...")
            continue
        operation = input("Enter the operation: + , - , * , / , ** , s : ")
        if operation not in ["+", "-", "*", "/", "**", "s"]:
            print("Operation not allowed")
            continue
        if operation == 's':
            try:
                res = calculator(x, 0, operation)
                print(f"{x} {operation}  = {res} ")
            except MyOperationException as exc:
                print(exc)
        else:
            y = float(input("Enter the second number: "))
            try:
                res = calculator(x, y, operation)
                print(f"{x} {operation} {y} = {res} ")
            except MyOperationException as exc:
                print(exc)


def calculator(x, y, operation):
    res = None
    if operation == "+":
        res = x + y
    elif operation == "-":
        res = x - y
    elif operation == "*":
        res = x * y
    elif operation == "/":
        if y == 0:
            raise MyOperationException("Division by zero ")
        res = x / y
    elif operation == "**":
        res = x ** y
    elif operation == "s":
        if x < 0:
            raise MyOperationException("Squareroot of a negative number is not real ")
        res = x ** 0.5
    else:
        raise MyOperationException("This operation is not recognized ")
    return res


start_calculator()
