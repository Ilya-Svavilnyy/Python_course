#Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n. Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# test_list = ("a a a b c a a d c d d").split()
# print(test_list)
# dictionary = {}
# result = None
# for i in test_list:
#     if i in dictionary:
#         print(f"{i}_{dictionary[i]}")
#         dictionary[i] += 1
#     else:
#         print(f"{i}")
#         dictionary[i] = 1
# print(i)

# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте. Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea
# shells on the sea shore I'm sure that the shells are sea shore shells Output: 13

# input_text = """She sells sea shells on the sea shore The shells that
# she sells are sea shells I'm sure So if she sells sea shells on the sea
# shore I'm sure that the shells are sea shore shells"""

# print(set(input_text.lower().split()))

# Задача 29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# num = int(input("Введите число: "))
# max_num = num
# while num != 0:
#     num = int(input("Введите число: "))
#     if num > max_num:
#         max_num = num
# print(max_num)

# Variant2
# maxx = -1
# while (number:=int(input("Введите число: "))) != 0:
# if number > maxx:
# maxx = number

# print(maxx)