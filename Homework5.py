# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# def multiplication(number, degree):
#     if degree == 1:
#         return number
#     if degree != 1:
#         return number * multiplication(number, degree - 1)


# num = int(input("Введите число: "))
# deg = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", multiplication(num, deg))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def summa(a, b):
#     if a == 0:
#         return b
#     return summa(a - 1, b + 1)

# print(summa(2, 2))