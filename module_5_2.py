class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.num_flor = numbers_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_flor}'

    # def __len__(self):
    #     return self.num_flor
    def __eq__(self, other): # =
        isinstance ( other, int )
        return self.num_flor == other.num_flor
    def __le__(self, other): # <=
        return self.num_flor <= other.num_flor
    def __ne__(self, other): # !=
        return self.num_flor != other.num_flor

    def __ge__(self, other): # >=
        return self.num_flor >= other.num_flor
    def __lt__(self, other): # <
        return self.num_flor < other.num_flor
    def __gt__(self, other): # >
        return self.num_flor > other.num_flor

    def __add__(self, value): # +
        isinstance ( value, House )
        self.num_flor += value
        return self
    def __radd__(self, other):
        isinstance ( other, House )
        return self + other
    def __radd__(self, other):
        isinstance ( other, House )
        return self + other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__