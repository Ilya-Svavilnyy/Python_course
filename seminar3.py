# Задача17. Дан список чисел. Определите, сколько в нем встречается различных чисел. Input: [1,1,2,0,-1,3,4,4] Output: 6

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_1)))

# Задача 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Введите к: "))
# k = len(list_1)-k

# list_2 = []
# for i in list_1[k:len(list_1)]:
#     list_2.append(i)
# for i in list_1[0:k]:
#     list_2.append(i)

# print(list_2)

# Второй вариант.

# list_1 = [1, 2, 3, 4, 5]
# k = int(input("Введите к: "))

# for i in range(k):
#     list_1.insert(0, list_1.pop())
# print(list_1)

# Задача 21. Напишите программу для печати всех уникальных значений в словаре. Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# start_dict = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"}, {"VI":"S005"}, {"VII":" S005 "}, {"V":"S009 "}, {"VIII":"S007"}]
# result_st = set()

# for mini_dict in start_dict:
#     result_st = result_st.union(set(mini_dict.values()))

# print(result_st)

# Задача 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

# my_list = [0, -1, 5, 2, 3]
# count = 0

# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i-1]:
#         count+=1

# print(count)