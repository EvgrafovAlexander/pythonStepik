class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        return v + self.money <= self.capacity

    def add(self, v):
        # положить v монет в копилку
        self.money += v



x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)
print(x.money)