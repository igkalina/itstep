#Задание 1 Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит значение x в степени y.
try:
    user_num_x = int(input('enter number x - '))
    user_num_y = int(input('enter number y - '))
    if user_num_y == 0:
        raise Exception('error. y=0')
    if user_num_x == 0:
        raise Exception('error. x=0')
    print(user_num_x ** user_num_y)
except ValueError:
    print('input error')
except Exception as ex:
    print(ex)
# Задание 2 Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и вывести обратно на экран.
try:
    num = int(input('num '))
    result = ''
    result_end = ''
    check = False
    if num < 0:
        num = abs(num)
        check = True
    while result_end == '':
        a = num % 10
        if a != 3 and a != 6:
            result += str(a)
        num = num // 10
        if num == 0 or num == -1:
            if result == '':
                check = False
                result_end = 'num is not def'
                break
            b = int(result)
            while True:
                result_temp = b % 10
                result_end += str(result_temp)
                b //= 10
                if b == 0:
                    break
    while check:
        result_end = '-' + result_end
        check = False
    print(result_end)
except ValueError:
    print('error! enter number!')
#Второй вариант с использованием среза [::-1] - обратный порядок. [индекс с которого начинать::шаг]
try:
    num = int(input('num '))
    result = ''
    check = False
    if num < 0:
        num = abs(num)
        check = True
    while True:
        a = num % 10
        if a != 3 and a != 6:
            result += str(a)
        num = num // 10
        if num == 0:
            break
    while check:
        result = result + '-'
        check = False
    print(result[::-1])
except ValueError:
    print('error! enter number!')
"""Задание 3
Пользователь вводит с клавиатуры целое шестизначное число. Написать программу, которая определяет,
является ли введенное число — счастливым (Счастливым считается шестизначное число, у которого сумма
первых 3 цифр равна сумме вторых трех цифр).
Например, 123321 — счастливое число, так как 1+2+3 = 3+2+1.
С другой стороны 378423 несчастливое число, так как 3+7+8 != 4+2+3.
Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке."""
try:
    user_number = int(input('enter your 6 numbers '))
    i = 0
    res_1 = 0
    res_2 = 0
    if len(str(user_number)) != 6:
        raise Exception('error! your number not 6')
    if user_number<0:
        raise Exception('error! your number is under 0')
    while i < 3:
        res_1 += user_number % 10
        i += 1
        user_number //= 10
        if i == 3:
            while i < 6:
                res_2 += user_number % 10
                i += 1
                user_number //= 10
    if res_1 == res_2:
        print('lucky numb!')
    else:
        print('not lucky')
except ValueError:
    print('error! enter only number')
except Exception as ex:
    print(ex)
"""Задание 4
Пользователь вводит с клавиатуры номер месяца (от 1
до 12). В зависимости от полученного номера месяца программа выводит на экран надпись: Winter (если введено
значение 1,2 или 12), Spring (если введено значение от 3 до 5), Summer (если введено значение от 6 до 8), Autumn
(если введено значение от 9 до 11).
Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке."""
try:
    user_number = int(input('enter your number '))
    if user_number > 12 or user_number < 1:
        raise Exception('need a number for 1 to 12')
    if user_number == 12 or user_number == 1 or user_number == 2:
        print('winter')
    elif 2 < user_number <= 5:
        print('spring')
    elif 5 < user_number <= 8:
        print('summer')
    else:
        print('autumn')
except ValueError:
    print('error! enter only number')
except Exception as ex:
    print(ex)
"""Задание 5
Пользователь вводит с клавиатуры длину и ширину
прямоугольника. Требуется отобразить на экран незаполненный прямоугольник (отображаются только границы прямоугольника). Размер длины и ширины равен
введенным данным."""
try:
    rectangle_h = int(input('Enter h rectangle - '))
    rectangle_w = int(input('Enter w rectangle - '))
    i = 0
    if rectangle_h < 1 or rectangle_w < 1:
        raise Exception('number need bigger 1')
    if rectangle_h == rectangle_w:
        raise Exception('you enter the sides of the square')
    while i < rectangle_h:
        if i == 0 or i == rectangle_h - 1:
            print('*  ' * rectangle_w)
        else:
            print('*', '   ' * (rectangle_w - 2), '*')
        i += 1
except ValueError:
    print('input error')
except Exception as ex:
    print('Error -', ex)