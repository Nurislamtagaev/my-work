# Инкапсуляция
# задача 1
# 1
# class Student:
#     def __init__(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
# s = Student('Nurislam')
# print(s.get_name())

# 2
# class Phone:
#     def __init__(self, brand):
#         self.__brand = brand
#
#     def get_brand(self):
#         return self.__brand
#
# p = Phone('iphone15')
# print(p.get_brand())

# 3
# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#
#     def get_age(self):
#         return self.__age
#
# p = Person(20)
# print(p.get_age())

# 4
# class Car:
#     def __init__(self, speed):
#         self.__speed = speed
#
#
#     def get_speed(self):
#         return self.__speed
#
# c = Car(195)
# print(c.get_speed())

# 5
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
# b = BankAccount('1000k')
# print(b.get_balance())

# 6
# class Computer:
#     def __init__(self, price):
#         self.__price = price
#
#
#     def get_price(self):
#         return self.__price
#
# c = Computer('56000som')
# print(c.get_price())

# 7
# class School:
#     def __init__(self, name):
#         self.__name = name
#
#
#     def get_name(self):
#         return self.__name
#
# s = School('94_mektep')
# print(s.get_name())

# 8
# class Book:
#     def __init__(self, title):
#         self.__title = title
#
#
#     def get_title(self):
#         return self.__title
#
# b = Book('piraty')
# print(str(b.get_title()))

# 9
# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
# e = Employee('70000 min som')
# print(e.get_salary())

# 10
# class Player:
#     def __init__(self, level):
#         self.__level = level
#
#
#     def get_level(self):
#         return self.__level
#
# p = Player('99 lv')
# print(p.get_level())

# задача 2

# 1
# class Animal:
#     def __init__(self, name):
#         self._name = name
#
#     def sound(self):
#         return f"{self._name} Жаныбар ун чыгарды: "
#
# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self._breed = breed
#
#     def sound(self):
#         super().sound()
#         print(f'{self._name} Myshyk myau dedi')

# a = Animal('myshyk')
# print(a.sound())


# 2
# class Phone:
#     def __init__(self, brand):
#         self.__brand = brand
#
#     def brand(self):
#         return f'brand:{self.__brand}'
#
# class Smartphone(Phone):
#     def __init__(self, brand):
#         super().__init__(brand)
#
# s = Smartphone('LG')
# print(s.brand())

# 3
# class Person:
#     def __init__(self, name):
#         self._name = name
#
# class Student(Person):
#     def __init__(self, name):
#         super().__init__(name)
#
# s = Student("Nurislam")
# print(s._name)

# 4
# class Car:
#     def __init__(self, _color):
#         self._color = _color
#
# class BMW(Car):
#     def __init__(self, _color):
#         super().__init__(_color)
#
# b = BMW('blue')
# print(b._color)

# 5
# class Employee:
#     def __init__(self, _salary):
#         self.salary = _salary
#
# class Teacher(Employee):
#     def __init__(self, _salary):
#         super().__init__(_salary)
#
# t = Teacher('65000som')
# print(t.salary)


