# OOP

# -------------------------------------------------

# class User:
#     name = 'Toxir'
#     lastname = 'Toxirov'
#
#
# user1 = User()
# print(user1.name)
# user1.name = 'Jalil'
# user1.age = 27
#
# print(user1.__dict__)
# print(user1.age)


# -------------------------------------------------
# public, protected, private


# class User:
#     def __init__(self, name, lastname, age):
#         self._name = name
#         self.__lastname = lastname
#         self.__age = age
#
#     def get_info(self):
#         return f"User: {self._name} {self.__lastname} {self.__age}"
#
#
# user = User('Jalil', 'Sobirov', 45)
# print(user._name)
# print(user._User__age)



# ---------------------------------------------------------------------------------------


# Voris (Meros) olish, Abstaction

# from abc import ABC, abstractmethod, abstractproperty
#
# class User(ABC):
#     def __init__(self, name, lastname, age):
#         self.__name = name
#         self.__lastname = lastname
#         self.__age = age
#
#     @abstractmethod
#     def get_info(self):
#         return f"User: {self.__name} {self.__lastname} {self.__age}"
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def lastname(self):
#         return self.__lastname
#
#     @property
#     def age(self):
#         return self.__age
#
#
# class Employee(User):
#     def __init__(self, name, lastname, age, salary):
#         User.__init__(self, name, lastname, age)
#         self.__salary = salary
#
#     def get_info(self):
#         return f"Employee: {self.name} {self.lastname}"
#
#     def get_salary(self):
#         return f"User: {self.name} {self.lastname} salary: {self.__salary}"
#
#
# class Student(User):
#     def __init__(self, name, lastname, age, phone):
#         super().__init__(name, lastname, age)
#         self.phone = phone
#
#     def get_info(self):
#         return f"Student: {self.name} {self.lastname}"
#
#
# class Parent(User):
#     def get_info(self):
#         return f"Parent: {self.name} {self.lastname}"
#
#
# employee1 = Employee('Sobir', 'Sobirov', 45, 400)
# parent1 = Parent('Sobir', 'Sobirov', 45)


# toxir = User('Toxir', 'Toxirov', 27)



# ---------------------------------------------------------------------------------------
# staticmethod


# def add(x, y):
#     return x + y
#
#
# def ayirish(x, y):
#     return abs(x - y)
#
#
# def kopaytirish(x, y):
#     return x * y
#
#
# def bolish(x, y):
#     return x / y
#
#
# class Calculate:
#     add = staticmethod(add)
#     ayirish = staticmethod(ayirish)
#
# print(Calculate.add(4, 10))
# print(Calculate.ayirish(55, 5))



# ---------------------------------------------------------------------------------------

#
# class Calculate:
#
#     @staticmethod
#     def add(x, y):
#         return x + y
#
#     @staticmethod
#     def ayirish(x, y):
#         return abs(x - y)
#
#     @staticmethod
#     def kopaytirish(x, y):
#         return x * y
#
#     @staticmethod
#     def bolish(x, y):
#         return x / y
#
# print(Calculate.add(4, 10))
# print(Calculate.ayirish(55, 5))
# print(Calculate.bolish(192, 4))


# ---------------------------------------------------------------------------------------

# class Calculate:
#     @classmethod
#     def qoshish(cls, *args):
#         return sum(args)
#
#     @classmethod
#     def bolish(cls, x, y):
#         return x / y
#
# print(Calculate.qoshish(4, 5, 6))
# print(Calculate.bolish(8, 2))



# ---------------------------------------------------------------------------------------

# import csv
#
# class User:
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#
#     def writer(self):
#         file = open('user_info.csv', mode='a')
#         writer = csv.writer(file)
#         writer.writerow([self.name, self.lastname, self.age])
#         file.close()



# User('Sobir', 'Sobirov', 45).writer()
# User('Toxir', 'Sobirov', 27).writer()
# User('Sobir', 'Toxirov', 32).writer()


# ---------------------------------------------------------------------------------------

import csv
class User:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def info(self):
        return [self.name, self.lastname, self.age]

users = [
    User('Sobir', 'Sobirov', 45).info(),
    User('Toxir', 'Sobirov', 27).info(),
    User('Sobir', 'Toxirov', 32).info()
]

with open('user_info.csv', mode='w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(
        users
    )