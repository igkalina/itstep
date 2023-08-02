# number = int(input('Введите число: '))
# digits_count = 0
# nullCounter = 0
# a = 0
# while number != 0:
#     a += number % 10
#     if number % 10 == 0:
#         nullCounter += 1
#     number //= 10
#     digits_count += 1
# print('Количество цифр:', digits_count)
# print('Сумма цифр в числе:', a)
# print('Среднее арифм.:', a / digits_count)
# print('Колчество нулей:', nullCounter)

# Задание 1 Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать
# все числа в этом диапазоне по следующему правилу: если число кратно 7, его надо выводить на экран.
user_num1 = int(input('Number 1: '))
user_num2 = int(input('Number 2: '))
if user_num2 < user_num1:
    temp = user_num1
    user_num1 = user_num2
    user_num2 = temp
while user_num1 < user_num2:
    if user_num1 % 7 == 0:
        print(user_num1)
    user_num1 += 1
"""Задание 2
Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
числа в этом диапазоне. Нужно вывести на экран:
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5."""
user_num1 = int(input('Number 1: '))
user_num2 = int(input('Number 2: '))
if user_num2 < user_num1:
    temp = user_num1
    user_num1 = user_num2
    user_num2 = temp
i = user_num1
print('Все числа диапазона: ')
while True:
    if i <= user_num2:
        print(i, end=' | ')
        i += 1
        if i > user_num2:
            break
print('\nВсе числа диапазона в убывающем порядке: ')
i = user_num2
while True:
    if i >= user_num1:
        print(i, end=' | ')
        i -= 1
        if i < user_num1:
            break
print('\nВсе числа, кратные 7: ')
i = user_num1
while i <= user_num2:
    if i % 7 == 0:
        print(i, end=' | ')
    i += 1
print('\nКоличество чисел, кратных 5: ')
i = user_num1
counter = 0
while i <= user_num2:
    if i % 5 == 0:
        counter += 1
    i += 1
print(counter)
"""Задание 3
Пользователь вводит с клавиатуры два числа (начало
и конец диапазона). Требуется проанализировать все числа
в этом диапазоне. Вывод на экран должен проходить по
правилам, указанным ниже.
Если число кратно 3 (делится на 3 без остатка) нужно
вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести
Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число"""
user_num1 = int(input('Number 1: '))
user_num2 = int(input('Number 2: '))
if user_num2 < user_num1:
    temp = user_num1
    user_num1 = user_num2
    user_num2 = temp
i = user_num1
while i <= user_num2:
    if i % 3 == 0:
        print(i, end='-')
        print('Fizz', end='. ')
    i += 1
i = user_num1
print('')
while i <= user_num2:
    if i % 5 == 0:
        print(i, end='-')
        print('Buzz', end='. ')
    i += 1
print('')
i = user_num1
while i <= user_num2:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end='-')
        print('Fizz Buzz', end='. ')
    i += 1
print('')
i = user_num1
while i <= user_num2:
    if i % 3 and i % 5:
        print(i, end=' | ')
    i += 1
# Задание 4 Написать программу – конвертер валют. Реализовать общение с пользователем через меню.
while True:
    currency_user = input('Укажите продаваемую валюту: 1.UAH 2.USD. 3.EUR - ')
    convert_currency = input('Укажите покупаемую валюту: 1.UAH 2.USD. 3.EUR - ')
    user_sum = input('Укажите сумму валютообмена - ')
    result = 0
    if currency_user.isdigit() and convert_currency.isdigit() and user_sum.isdigit():
        currency_user = int(currency_user)
        convert_currency = int(convert_currency)
        user_sum = int(user_sum)
    else:
        print('Не корректный ввод')
        continue
    if currency_user == convert_currency or currency_user > 3 or convert_currency > 3 or currency_user < 1 or \
            convert_currency < 1 or user_sum < 1:
        print('Не корректный ввод')
        continue
    if currency_user == 1 and convert_currency == 2:
        result = 0.02707 * user_sum
    elif currency_user == 1 and convert_currency == 3:
        result = 0.025 * user_sum
    elif currency_user == 2 and convert_currency == 1:
        result = 36.94 * user_sum
    elif currency_user == 2 and convert_currency == 3:
        result = 0.92 * user_sum
    elif currency_user == 3 and convert_currency == 1:
        result = 39.99 * user_sum
    elif currency_user == 3 and convert_currency == 2:
        result = 1.08 * user_sum
    print(f'Результат конвертации {result}')
    repeat = input('Желаете повторить? 1.Да 2.Нет - ')
    if repeat.isdigit():
        repeat = int(repeat)
    else:
        print('Ошибка ввода. Обмен завершён')
        break
    if repeat == 1:
        continue
    else:
        print('Обмен завершён')
        break