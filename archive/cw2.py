import math

# a = int(input('Количество отработанных часов: '))
# b = float(input('Цена 1 часа работы: '))
# print(a * b)

# num = 1
# if num == 2:
#     print('test if')
# else:
#     print('else work')

# age = 10
# if 0 < age < 6:
#     print('1')
# elif 6 <= age < 18:
#     print('2')
# elif 18 <= age < 22:
#     print('3')
# else:
#     print('end')

# a = int(input('number: '))
# if a % 2 == 0:
#     print('чётное')
# else:
#     print('не чётное')

# a = int(input('number 1: '))
# b = int(input('number 2: '))
# if a < b:
#     print(a)
# else:
#     print(b)

# a = int(input('number: '))
# if a >= 1:
#     print('положительное')
# elif a < 0:
#     print('отрицательное')
# else:
#     print('ноль')

# a = int(input('number 1: '))
# b = int(input('number 2: '))
# if a == b:
#     print('равны')
# elif a > b:
#     print(b, a)
# else:
#     print(a, b)

# a = int(input('number 1: '))
# b = int(input('number 2: '))
# c = int(input('number 3: '))
# d = int(input('number 4: '))
# e = int(input('number 5: '))
# res = (a + b + c + d + e)/5
# if res >= 4:
#     print('допущен')
# else:
#     print('не допущен, средний балл ', res)

# a = int(input('number 1: '))
# b = int(input('number 2: '))
# c = (input('Enter sign: '))
# res = 'error sign'
# if c == '+':
#     res = a + b
# elif c == '-':
#     res = a - b
# elif c == '*':
#     res = a * b
# elif c == '/':
#     res = a / b
# print(res)

# sec = int(input('Сколько секунд прошло с начала дня: '))
# a = input('Выбирите единицу отображения (sec, min, hour): ')
# text = 'До конца дня осталось: '
# day = 86400
# if a == 'sec' and sec < day:
#     print(text, 86400 - sec, ' sec')
# elif a == 'min' and sec < day:
#     print(text, int((86400 - sec) / 60), ' min')
# elif a == 'hour' and sec < day:
#     print(text, int((86400 - sec) / 60 // 60), ' hour')
# elif a != 'sec' or a != 'min' or a != 'hour':
#     print('Не верная единица отображения времени')

# a = int(input('Введите диаметр окружности: '))
# q = input('Выбирете, что требуется посчитать: Площадь. Перимитр: ')
# if q == 'Площадь':
#     print(a ** 2 / 4 * math.pi)
# elif q == 'Перимитр':
#     print(a * math.pi)

# a = int(input('Стоимость приставки: '))
# x = int(input('Количество: '))
# s = int(input('Укажите скидку: '))
# q = input('1. Посчитать общую сумму заказа. 2. Или стоимость 1-й приставки со скидкой: ')
# if q == '1':
#     print('Сумма: ', int((a * x) - (a * x) * (s / 100)))
# elif q == '2':
#     print('1 приставка со скидкой: ', int(a * (s / 100)))

# a = int(input('hour: '))
# if a < 0 or a > 24:
#     print('error input')
# elif 0 <= a < 6:
#     print('good night')
# elif 6 <= a < 13:
#     print('good morning')
# elif 13 <= a < 17:
#     print('good day')
# elif 17 <= a <= 24:
#     print('good evening')
