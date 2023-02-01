class My_vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def positive(cls, arg):
        return abs(arg)

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x * x + y * y

    @staticmethod
    def div(x, y):
        return abs(x - y)

    def __init__(self, x, y):
        x = self.positive(x)
        y = self.positive(y)
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            self.x = self.y = 0

        print(f"coord: {self.x}, {self.y}")
        print("norm2: ", self.norm2(self.x, self.y))
        print("div: ", self.div(self.x, self.y))

    def get_coords(self):
        return self.x, self.y


v = My_vector(-10, 70)
print(v.get_coords())
