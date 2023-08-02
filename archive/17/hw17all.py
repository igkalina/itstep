"""Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
1.Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
2.Посчитайте сколько раз цифры встречаются в тексте;
3.Посчитайте сколько раз знаки препинания встречаются в тексте;
4.Посчитайте количество восклицательных знаков в тексте."""
import string

text = input('')
a = text.split('.')
b = [i.capitalize() for i in a]
c = '. '.join(b)
punct = string.punctuation
count_num = 0
count_punct = 0
count_znak = 0
i = 0
while i < len(c):
    if c[i].isdigit():
        count_num += 1
    if c[i] == '!':
        count_znak += 1
    i += 1
x = 0
for m in punct:
    while x < len(c):
        if c[x].count(m):
            count_punct += 1
        x += 1
        if x == len(c):
            x = 0
            break
print(
    f'Количество цифр в тексте {count_num}\nКоличество знаков препинания {count_punct}\nКоличество знаков ! {count_znak}')

"""Задание 2
Пользователь с клавиатуры вводит элементы списка целых чисел и некоторое число.
Необходимо посчитать сколько раз данное число присутствует в списке. Результат
вывести на экран."""

numbs = input('enter numbers: ')
search = input('search: ')
arr_numbs = numbs.split()
count = 0
for num in arr_numbs:
    if num == search:
        count += 1
print(f'Запрашиваемое число встречается {count} раз')

"""Задание 3
Пользователь с клавиатуры вводит элементы списка
целых. Необходимо посчитать сумму всех элементов
и их среднеарифметическое. Результаты вывести на
экран."""

numbs = input('enter numbers: ')
arr_numbers = numbs.split()
i = 0
sum = 0
for numb in arr_numbers:
    sum += int(numb)
    i += 1
print(f'Сумма чисел {sum}\nСреднее арифм. {sum / i}')

"""Задание 5
Есть список, заполненный случайными числами.
На основании данных этого массива нужно:
1 Создать список целых, содержащий только четные числа
2 Создать список целых, содержащий только нечетные числа
3 Создать список целых, содержащий только отрицательные числа
4 Создать список целых, содержащий только положительные числа"""

import random

numbs = []
even = ''
not_even = ''
negative = ''
positive = ''
for i in range(10):
    numbs.append(random.randint(-100, 100))
for i in numbs:
    if i % 2 == 0:
        even += str(i) + ' '
    elif i % 2 != 0:
        not_even += str(i) + ' '
    if i < 0:
        negative += str(i) + ' '
    else:
        positive += str(i) + ' '
print(f'Сгенированный список {numbs}\nЧётные {even.split()}\n'
      f'Не чётные {not_even.split()}\nОтрицательные числа {negative.split()}\n'
      f'Положительные числа {positive.split()}')
