"""class My_int(int):
    def __truediv__(self, other):
        res= super().__truediv__(other)
        if res == int(res):
            res = int(res)
        return res   """


class MyClass():
    Total_objects = 0

    def __init__(self, age=0):
        MyClass.Total_objects += 1
        self.age = age

    @classmethod
    def total_objects(cls):
        print("Total objects:", cls.Total_objects)
