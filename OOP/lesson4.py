from abc import ABC, abstractmethod
# 1
# class Animal:
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print('ит урду')
#
# class Cat(Animal):
#     def sound(self):
#         print('мышык мяу деди')
#
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()

# 2
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         print('Транспорт журот')
#
# class Car(Transport):
#     def move(self):
#         print('Машина журот')
#
# class Bike(Transport):
#     def move(self):
#         print('Велосипед журот')
#
# c = Car()
# b = Bike()
# c.move()
# b.move()

# 3
# class Phone(ABC):
#     @abstractmethod
#     def call(self):
#         pass
#
# class Iphone(Phone):
#     def call(self):
#         print('Айфон 17 про')
#
# class Samsung(Phone):
#     def call(self):
#         print('Samsung Galaxy S26 Ultra')
#
# i = Iphone()
# s = Samsung()
# i.call()
# s.call()

# 4
# class Employee(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Teacher(Employee):
#     def work(self):
#         print("Мугалим сабак берет")
#
# class Programmer(Employee):
#     def work(self):
#         print('Айтишник прграмма жасайт')
#
# t = Teacher()
# p = Programmer()
# t.work()
# p.work()

# 5
# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
#
# class Cash(Payment):
#     def pay(self):
#         print("Cash pay")
#
# class Card(Payment):
#     def pay(self):
#         print("Card pay")
#
# cash = Cash()
# cash.pay()
# card = Card()
# card.pay()

# 6
# class Education(ABC):
#     @abstractmethod
#     def study(self):
#         pass
#
# class School(Education):
#     def study(self):
#         print("школа №94")
#
# class University(Education):
#     def study(self):
#         print('МГУ университет')
#
# s = School()
# s.study()
# u = University()
# u.study()

# 7
# class Food(ABC):
#     @abstractmethod
#     def cook(self):
#         pass
#
# class Pizza(Food):
#     def cook(self):
#         print("Pizza cooking")
#
# class Burger(Food):
#     def cook(self):
#         print("Burgers cooking")
#
# pizza = Pizza()
# burger = Burger()
# burger.cook()
# pizza.cook()

# 8
# class Computer(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#
# class Laptop(Computer):
#     def start(self):
#         print("Laptop")
#
# class Desktop(Computer):
#     def start(self):
#         print("Desktop")
#
# l = Laptop()
# l.start()
# desktop = Desktop()
# desktop.start()

# 9
# class Player(ABC):
#     @abstractmethod
#     def play(self):
#         pass
#
# class FootballPlayer(Player):
#     def play(self):
#         print("You are playing football?")
#
# class BasketballPlayer(Player):
#     def play(self):
#         print("You are playing basketball?")
#
# f = FootballPlayer()
# b = BasketballPlayer()
# f.play()
# b.play()


# 1
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# info = Student('Nurislam', 16)
# print(info.name)
# print(info.age)

# 2
# class Phone:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
# info = Phone('Poco', 'X')
# print(info.brand)
# print(info.model)

# 3
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         pass
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         print('Ит урду')
#
# info = Dog('Rex')
# print(info.name)


# 4
# class Car:
#     def move(self):
#         print('Машина журуп жатат')
# c = Car()
# c.move()
#
# class Bike:
#     def move(self):
#         print('Велосипед журуп жатат')
# b = Bike()
# b.move()

# 5
# class Bank:
#     def __init__(self, _balance):
#         self._balance =_balance
#
# deposit = Bank(2500)
# get_balan

