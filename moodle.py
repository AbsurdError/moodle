#//////////////_1-задача_//////////////////////
# def all_divisors(number):
#     n = [1, number]
#     for i in range(2, 1 + int(number ** 0.5)):
#         if number % i == 0:
#             n.extend({number // i, i})
#     return sorted(n)
# print(all_divisors(int(input('Введите число:  '))))

#//////////////_2-задача_//////////////////////

# def three_args(var1, var2, var3):
#     args_var = locals()
#     return 'Переданы аргументы:', *(f'{key} = {value}' for key, value in args_var.items() if value)
# print(*three_args(int(input('Введите первый аргумент:  ')), int(input('Введите второй аргумент:  ')), int(input('Введите третий аргумент:  '))))

#//////////////_3-задача_//////////////////////

# def palindrome(word): # вводим слово
#   n = word[::-1] # берём и отражаем его
#   if word == n: # проверка на совпадение
#     return ('Да, это палиндром')
#   else:
#     return ('Нет, это не палиндром')
# print(palindrome(str(input('Введите палиндром:  '))))

#//////////////_4-задача_//////////////////////

# import collections
# def text_search(text):
# #text = 'lorem ipsum dolor sit amet amet amet'
#     words = text.split()
#     counter = collections.Counter(words)
#     most_common, occurrences = counter.most_common()[0]
#     longest = max(words, key=len)
#     return f'Наиболее часто встречающееся:  {most_common}/ Самое длинное:   {longest}'
# print(text_search(input('Введите текст:  ')))

#//////////////_5-задача_//////////////////////(отредактировать)
#
# lines = int(input("Введите количество строк: "))
# column = int(input("Введите количество столбцов: "))
#
# matrix = [[0] * column for _ in range(lines)]
# y = 0
# m_y = lines - 1
# x = 0
# m_x = column - 1
# num = 1
# while num <= lines * column:
#     for i in range(x, m_x + 1):
#         matrix[y][i] = num
#         num += 1
#     y += 1
#
#     if lines * column < num:
#         break
#
#     for i in range(y, m_y + 1):
#         matrix[i][m_x] = num
#         num += 1
#     m_x -= 1
#
#     if num > lines * column:
#         break
#
#     for i in range(m_x, x - 1, -1):
#         matrix[m_y][i] = num
#         num += 1
#     m_y -= 1
#
#     if num > lines * column:
#         break
#
#     for i in range(m_y, y - 1, -1):
#         matrix[i][x] = num
#         num += 1
#     x += 1
#
# for result in matrix:
#     print(*result)

#//////////////_6-задача_//////////////////////
#
# def magic_square(matrix):
#     n = len(matrix)
#     amount = sum(matrix[0])
#
#     if n != len(matrix[0]):
#         return False
#
#     for column in matrix:
#         if sum(column) != amount:
#             return False
#
#     for i in range(n):
#         column_sum = sum(column[i] for column in matrix)
#         if column_sum != amount:
#             return False
#
#     diagonal_sum = sum(matrix[i][i] for i in range(n))
#     if diagonal_sum != amount:
#         return False
#
#     diagonal_sum = sum(matrix[i][n-i-1] for i in range(n))
#     if diagonal_sum != amount:
#         return False
#
#     return True
#
# n = int(input("Введите количество строк в квадратной матрице: "))
# matrix = []
# for i in range(n):
#     column = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
#     matrix.append(column)
#
# if magic_square(matrix):
#     print("Матрица является магическим квадратом")
# else:
#     print("Матрица не является магическим квадратом")



