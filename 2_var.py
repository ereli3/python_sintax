# однострочный комментарий

'''
многострочный
комментарий
'''

"""
это тоже
многострочный 
комментарий
"""

# *** переменные ***
# int - целые числа (1 2 3 4)
# float - дробные числа (1,2 2,3 3,4)
# bool - true/false 
# string - строка ("Nadya", "Apple")

var_1 = 100
number_of_apples = 10

myNumVar = 123

CONST_VAR = 1000

# вызов встроенной функции вывода в терминал
apple = 0
apple = 2
orange = 4

RED = "red"
NADYA = "NADYA"

fruits = apple + orange 

print(fruits, orange, apple)
print(var_1)
print(myNumVar, CONST_VAR)

# встроенная функция ввода из терминала
# in_1 = input('введите число: ')

# print(in_1)

#  небольшой калькулятор
in_1 = input('введите 1 число: ')
in_2 = input('введите 2 число: ')
#  конкатенация строк
# result = in_1 + in_2

# сложение
# перед сложением конвертируем данные
result = int(in_1) + int(in_2)

print(result)
