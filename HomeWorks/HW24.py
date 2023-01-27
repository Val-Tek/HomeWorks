# # Создать свой класс String на базе стандартного класса str.
# # В нём необходимо:
# # переопределить стандартный метод отвечающий за сложение
# # написать отсутствующий в классе str метод отвечающий за вычитание

class HW_string(str):
    def __add__(self, other):
        return HW_string(str(self) + str(other))

    def __sub__(self, other):
        self_str = str(self)
        other_str = str(other)
        if other_str in self_str:
            return HW_string(self_str.replace(other_str, "",1))
        else:
            return self


a = HW_string(777736454783)
b = HW_string(7)
print(type(a - b))
print(a - b)
