# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
# его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
from time import sleep
class Auto():
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight
    def move(self):
        print("move")
    def stop(self):
        print("stop")
    def birthday(self):
        return self.age + 1
class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load
    def move(self):
        print("attention")
    def load(self):
        sleep(1)
        print("load")
        sleep(1)
class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed
    def move(self):
        print("Max speed is " + str(self.max_speed))


auto1 = Car('BMW', 3, "electro", 250)
auto2 = Truck('Mercedes', 6,"expert", 20, 'blue', 3000)
print((auto1.brand), (auto1.age), (auto1.mark), (auto1.max_speed), (auto1.color), (auto1.weight))
auto1.move()
auto2.move()
auto2.load()
print((auto2.brand), (auto2.age), (auto2.mark), (auto2.max_load), (auto2.color), (auto2.weight))
print("*"*60)
print("birthday 1: ", auto1.birthday())
print("birthday 2: ", auto2.birthday())
