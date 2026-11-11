# import csv
import datetime
# 1
# with open('student.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Age", "city"])
#     writer.writerow(["nurislam", "16", "bishkek"])

# 2
# with open('bootcamp_48.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     name = input('Atyndy jaz: ')
#     age = int(input('jashundy jaz: '))
#     city = input('shaaryndy jaz: ')
#     writer.writerow([name, age, city])

# count = 0
# with open('bootcamp_48.csv', 'r') as f:
#     reader = csv.reader(f)
#     for i in reader:
        # if i['name'] == 'Nurislam':
        #     count += 1
# print(f'Okuuchunun sany: {count})



import math, random
from datetime import date,time
# 1
# def greeting(name):
#     print("Hello world")
# greeting('')

# 2
# def square(number:int)->int:
#     return number ** 2
# print(square(5))

# 3
# def __getattr__(name: str) -> str:
#     return name
# print('Privet Nurislam!')

# 4
# f = lambda i: i * 4
#
# print(f(2))

# 5
# number = lambda x, y: x if x > y else y
#
# print(number(5, 10))

# 6
# try:
#     num = int(input('Сан жаз: '))
#     print(num)
# except:
#     print('ката чыкты')

# 7
# try:
#     num = input("eki san jaz: ")
#     print(num / 0)
# except:
#     print('ката')

# 8
# print(math.sqrt(27))

# 9
# print(random.randint(1,1000))

# 10
# def add(a, b):
#     return a + b

# 11
# today = datetime.date.today()
# print(today)

# 12
# t = date.today()
# print(f'{t.day}-{t.month}-{t.year}')

# 13
# t = time(13, 45, 10)
# print(t)

# 14
