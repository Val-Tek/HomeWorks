# Написать лямбда-функцию определяющую чётное/нечётное.
# Функция принимает параметр (число) и если чётное, то выдаёт слово “чётное”, если нет - то “не чётное”.
# even, odd

number_op= lambda a: print("even") if (int(a) %2==0) else print("odd")
number_op(15)