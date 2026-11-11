def math_utils_py(a, b):
    return a + b

def math_utils1(a, b):
    return a - b

def math_utils2(a, b):
    return a * b

def math_utils3(a, b):
    return a / b


# name = input('Atyndy jaz: ')
# print('salam')


def numbers_py(a):
     if a % 2 == 0:
         return 'jup san: '

print(numbers_py(4))


def text_utils_py(name):
    return len(name)
print(text_utils_py('Nurislam'))

def calculator_py(num1, num2):
    return num1 / num2

def calculator_py2(a, b):
    return a / b

def student_info(name, city, age):
    return name, city, age
print(student_info('Nurislam', 'Bishkek', '16'))

def get_max(* nums):
    return (max(nums))
print(get_max(1, 2, 3, 4, 5, 6, 7))

def get_min(* nums):
    return (min(nums))
print(get_min(1, 2, 3, 4, 5, 6, 7))




