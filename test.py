# ------------------------------------1-----------------------------------

# class Mathematics:
#     @staticmethod
#     def qoshish(a, b):
#         return a + b
#
#     @staticmethod
#     def ayrish(a, b):
#         return a - b
#
#     @staticmethod
#     def  kopaytirish(a, b):
#         return a * b
#
#     @staticmethod
#     def bolish(a, b):
#         return a / b
#
# print(Mathematics.qoshish(4,5))
# print(Mathematics.ayrish(69,48))
# print(Mathematics.kopaytirish(6,8))
# print(Mathematics.bolish(126,3))

# ------------------------------------2-----------------------------------

from abc import ABC, abstractmethod
import csv


class User(ABC):

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @abstractmethod
    def get_name(self):
        return self.name

    @abstractmethod
    def get_phone(self):
        return self.phone_number


class Employee(User):
    def __init__(self, name, phone_number, ish_haqi):
        super().__init__(name, phone_number)
        self.ish_haqi = ish_haqi

        def get_name(self):
            return f"Employee: {self.name}"

        def get_phone(self):
            return self.phone_number

        def get_salary(self):
            return self.ish_haqi

        def write(self):
            with open("users.csv", mode='w') as file:
                writer = csv.writer(file)
                writer.writerow(
                    [self.get_name, self.get_phone, self.get_salary]
                )


user1 = User("Tohir", "+9987648123").write()
# user2 = User("Jalol", "+9984516874")

# employe1 = Employee("Rustam", "+998911230313", 600).write()
# employe2 = Employee("Sobir", "+998901456874", 300).write()
