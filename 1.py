# ----------------------------------------------------------------------------

# Figure = type('Figure', (), {
#     'name': 'Figure',
#     'perimetr': lambda self: None,
#     'area': lambda self: None
# })
#
# Triangle = type('Triangle', (Figure, ), {
#     'name': 'Triangle',
#     'a': None,
#     'b': None,
#     'c': None,
#     'perimetr': lambda self: self.a + self.b + self.c,
#     'area': lambda self: ((self.a + self.b + self.c) / 2)
# })
#
# Square = type('Square', (Figure, ), {
#     'name': 'Square',
#     'a': None,
#     'b': None,
#     'perimetr': lambda self: 2 * (self.a + self. b),
#     'area': lambda self: self.a * self.b
# })
#
# Circle = type('Circle', (Figure, ), {
#     'name': 'Circle',
#     'r': None,
#     'perimetr': lambda self: 2 * 3.14 * self.r,
#     'area': lambda self: 2 * 3.14 * self.r ** 2
# })
#
# triangle = Triangle()
# triangle.a = 3
# triangle.b = 4
# triangle.c = 5
#
# square = Square()
# square.a = 6
# square.b = 8
#
# circle = Circle()
# circle.r = 9
#
# print(f"Name : {triangle.name}: perimetr: {triangle.perimetr()}, area: {triangle.area}")
# print(f"Name : {square.name}: perimetr: {square.perimetr()}, area: {square.area}")
# print(f"Name : {circle.name}: perimetr: {circle.perimetr()}, area: {circle.area}")
# ----------------------------------------------------------------------------

# class Metacar(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['model'] = 'BMV'
#         attrs['color'] = 'Green'
#         attrs['speed'] = '260 km/s'
#         return type(name, bases, attrs)
#
# class Car(metaclass=Metacar):
#     pass
#
# print(Car.model)
# print(Car.color)
# print(Car.speed)

# ----------------------------------------------------------------------------

# class Metatable(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['id'] = 1
#         attrs['name'] = 'Zokir'
#         attrs['phone'] = '+998123456789'
#         attrs['address'] = 'Fargona'
#         return  type(name, bases, attrs)
#
# class Table(metaclass=Metatable):
#     pass
#
# print(Table.id)
# print(Table.name)
# print(Table.phone)
# print(Table.address)

# ----------------------------------------------------------------------------

# class Calculate:
#     @classmethod
#     def qoshish(cls, a, b):
#         return a + b
#
#     @classmethod
#     def ayrish(cls, a, b):
#         return a - b
#
#     @classmethod
#     def kopaytirish(cls, a, b):
#         return a * b
#
#     @classmethod
#     def bolish(cls, a, b):
#         return a / b
#
# print(Calculate.qoshish(4,5))
# print(Calculate.ayrish(8, 6))
# print(Calculate.kopaytirish(4, 7))
# print(Calculate.bolish(26,13))