# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во
# элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input("Введите число N элементов: "))
# num_list_1 = set(map(int, input('Введите num: ').split()))
# print(num_list_1)
# m = int(input("Введите число M элементов: "))
# num_list_2 = set(map(int, input('Введите num: ').split()))
# print(num_list_2)
# n = len(num_list_1)
# m = len(num_list_2)
#
# num_list_3 = num_list_1.intersection(num_list_2)
# print(sorted(num_list_3))


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти
# кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# n = int(input('Введите количество кустов: '))
# a = list(map(int, input('Введите количество ягод: ').split()))
# x = 0
# for i in range(1, n-1):
#     if a[i]+a[i+1]+a[i-1] > x:
#         x = a[i]+a[i+1]+a[i-1]
# print(x)