# print("Integer Calculator")
# a = input("Integer number 1: ")
# b = input("Integer number 2: ")
# res = "sign input error"
# if a.isdigit() and b.isdigit():
#     a = float(a)
#     b = float(b)
#     print(
#         "Enter 1 for sum numbers\nEnter 2 for defference\nEnter 3 for multiply numbers\nEnter 4 for divide "
#         "numbers\nEnter 5 for calculate the remainder of the division\nEnter 6 for raise numbers to a power\nEnter 7 "
#         "for divide numbers without a remainder"
#     )
#     c = input("Enter sign: ")
#     if b == 0 and c == "4":
#         res = "Error. Divide by 0 is not possible"
#     elif c == "1":
#         res = a + b
#     elif c == "2":
#         res = a - b
#     elif c == "3":
#         res = a * b
#     elif c == "4":
#         res = a / b
#     elif c == "5":
#         res = a % b
#     elif c == "6":
#         res = a**b
#     elif c == "7":
#         res = a // b
# else:
#     res = "number input error"
# print("Resultat: ", res)

# num1 = 1
# num2 = 11
# print('while start')
# while num1 < num2:
#     if num1 % 2 == 0:
#         print(num1, end=' | ')
#     num1 += 1
#     if num1 == 8:
#         break
# else:
#     print('\nwhile finished')

# count = 0
# while True:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count)
#     if count > 10:
#         break

# sum = 0
# while True:
#     num = int(input('enter number: '))
#     sum += num
#     if num == 0:
#         print(sum)
#         break

# count = -1
# sum = 0
# while True:
#     mark = int(input('Оценка: '))
#     sum += mark
#     count+=1
#     if mark == 0:
#         print(sum / count)
#         break
#     #второе решение count += 1 после ветвления с break

# import random
# i=0
# while i<5:
#     print(random.randint(1, 10))
#     i+=1

# import random
# while True:
#     rand_num = random.randint(1, 100)
#     user_num = 0
#     trise = 0
#     while user_num != rand_num:
#         trise += 1
#         user_num = int(input('Введите число '))
#         if user_num < rand_num:
#             print('Число больше', user_num)
#         elif user_num > rand_num:
#             print('Число меньше', user_num)
#     print('Загаданое число', +rand_num, 'отгадано за ', trise, 'попыток')
#     answer = input('Сыграть ещё? 1.Да 2.Нет: ')
#     if answer == '1':
#         print('new game')
#         continue
#     else:
#         print('game over')
#         break

# Пользователь вводит две границы диапазона, вывести на экран все числа из этого диапазона.
# Предусмотреть, чтобы пользователь мог вводить границы диапазона в произвольном порядке.
# вывести все четные числа из диапазона.	вывести все нечетные числа из диапазона.	вывести все числа, кратные семи.
#
# user_numb1 = int(input('number 1: '))
# user_numb2 = int(input('number 2: '))
# temp_user_numb_1 = user_numb1
# reverse_number = user_numb1
# if user_numb2 < user_numb1:
#     user_numb1 = user_numb2
#     user_numb2 = reverse_number
#     temp_user_numb_1 = user_numb1
# print('По порядку: ')
# while True:
#     print(user_numb1, end='|')
#     user_numb1 += 1
#     if user_numb1 == user_numb2:
#         print(user_numb1, end='|')
#         user_numb1 = temp_user_numb_1
#         break
# print('\nЧётные: ')
# while True:
#     if user_numb1 % 2 == 0:
#         print(user_numb1, end='|')
#     user_numb1 += 1
#     if user_numb1 == user_numb2:
#         if user_numb1 % 2 == 0:
#             print(user_numb1, end='|')
#         user_numb1 = temp_user_numb_1
#         break
# print('\nНечётные: ')
# while True:
#     if user_numb1 % 2 != 0:
#         print(user_numb1, end='|')
#     user_numb1 += 1
#     if user_numb1 == user_numb2:
#         if user_numb1 % 2 != 0:
#             print(user_numb1, end='|')
#         user_numb1 = temp_user_numb_1
#         break
# print('\nКратно 7: ')
# while True:
#     if user_numb1 % 7 == 0:
#         print(user_numb1, end='|')
#     user_numb1 += 1
#     if user_numb1 == user_numb2:
#         if user_numb1 % 7 == 0:
#             print(user_numb1, end='|')
#         user_numb1 = temp_user_numb_1
#         break

# Задание 3. Написать программу, которая выводит на экран таблицу умножения на k, где k –номер варианта. Например,
# для 7-го варианта: 7 x 2 = 14 7 x 3 = 21

# user_number = int(input('enter number: '))
# res = 0
# i = 1
# while True:
#     i += 1
#     res = user_number * i
#     print(user_number, 'x', i, '=', res)
#     if i == 10:
#         break

# Задание 4 Пользователь вводит с клавиатуры длину линии. Нужно отобразить на экране горизонтальную линию из *,
# указанной длины.

# user_length = int(input('enter length: '))
# i = 0
# while i < user_length:
#     print('*',end='')
#     i += 1
