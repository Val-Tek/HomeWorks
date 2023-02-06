# Создать генератор геометрической прогрессии


def Geo_generater(b, q, t):
    """
    Calculates geometric sequence
    :param b: first number
    :param q: ratio
    :param t: number of operations
    :return: yields
    """
    if (b != 0) and (q != 0):
        count = 0
        while count <= t:
            count += 1
            yield b * q ** (count - 1)
    else:
        raise ArithmeticError("Geometric progression needs nonzero arguments")


a = Geo_generater(3, 9, 9)
print(a)
for item in a:
    print(item)
