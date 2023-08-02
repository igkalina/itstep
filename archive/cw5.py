# myStr = "python was created in the late 1980's by Guido van Rossum. Guido"
# print(myStr)
# print(myStr[0])
# print(myStr[-1])
# print(len(myStr))
# print(myStr[len(myStr) - 1])
# print(myStr.upper())
# print(myStr.capitalize())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.lower().find('guido'))
# print(myStr.lower().rfind('guido'))
# print(myStr.lower().index('guido')) #возращает ValueError если не находит вместо 0 как в примере с find
# print('|'.join(myStr))
# print(myStr.split(' '))
# print(myStr.replace('python', 'js'))
# print(myStr.center(74, '#'))
# password = input('enter password ')
# i = 0
# countDegit = 0
# countUpper = 0
# countLower = 0
# while i < len(password):
#     if password[i].isdigit():
#         countDegit += 1
#     elif password[i].islower():
#         countLower += 1
#     elif password[i].isupper():
#         countUpper += 1
#     i += 1
# if countLower == 0 or countUpper == 0 or countDegit == 0 or len(password) < 8:
#     print('weak password!')
# else:
#     print('ok')
# print(myStr[0:8:2])
# import string
# import random
#
# s = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
# password = ''
# i = 0
# a = 0
# while True:
#     password += random.choice(s)
#     i += 1
#     if i == 8:
#         print(password)
#         password = ''
#         i = 0
#         a += 1
#     if a == 3:
#         break
# s = input('enter ')
# a = ''
# i = len(s)-1
# while i >= 0:
#     a += s[i]
#     i -= 1
# print(a)
# print(s[::-1])
#
# s = input('enter ')
# a = 0
# n = 0
# i = 0
# while i < len(s):
#     if s[i].isdigit():
#         n += 1
#     elif s[i].isalpha():
#         a += 1
#     i += 1
# print(f'num - {n}, alp - {a}')
#
# Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке встречается искомый
# символ. Полученное число выведите на экран.
#
# s = input('enter ')
# f = input('simbol ')
# print(s.count(f))
#
# Пользователь вводит с клавиатуры строку и слово для поиска. Посчитайте сколько раз в строке встречается искомое слово.
# Полученное число выведите на экран.
#
# s = input('enter ')
# f = input('simbol ')
# print(s.count(f))
#
# Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены.
# Произведите в строке замену одного слова на другое. Полученную строку отобразите на экране.
#
# s = input('enter ')
# f = input('simbol ')
# r = input('replace ')
# print(s.replace(f, r))

