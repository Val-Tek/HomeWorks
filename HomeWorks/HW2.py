# 1. Создать 3 переменные одного и тоже типа с одинаковыми данными и с одинаковым id.
# 2. Создать 2 переменные одного и тоже типа с одинаковыми данными и с разными id.
# 3*. Поменять их типы так, чтобы у 1-х трёх стали разные id, но при этом остались одинаковые данные (и одинаковый тип), а у 2-х последних стали одинаковые id и остались одинаковые данные (и одинаковый тип).

# 1
print(" Ex.1")
a = (1, 2, 3)
a1 = (1, 2, 3)
a2 = (1, 2, 3)
print(a == a1 == a2)
print(a is a1 is a2)
# 2
print(' Ex.2')
<<<<<<< HEAD
b1 = ['peace', 'love']
b2 = ['peace', 'love']
print(b1 == b2)
print(b1 is b2)

=======

b1 = ['peace', 'love']
b2 = ['peace', 'love']
print(b1)
print(b1 == b2)
print(b1 is b2)


>>>>>>> bb6dcd8 (Initial commit)
# 3
print(' Ex.3')
a=list(a)
a1=list(a1)
a2=list(a2)
print(a == a1 == a2)
print(a is a1 is a2)
<<<<<<< HEAD
b1=str(b1)
b2=b1
=======

b1=str(b1)
b2=str(b2)
b1=b2



print(id(b1))
print(id(b2))


>>>>>>> bb6dcd8 (Initial commit)
print(b1 == b2)
print(b1 is b2)
