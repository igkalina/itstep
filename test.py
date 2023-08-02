"""Обратный порядок
У вас есть список чисел.
Напишите программу, которая принимает этот список и возвращает новый список, содержащий
те же числа, но в обратном порядке. Не используйте встроенную функцию reverse()."""


def reverse_num(number):
    reverse = number[::-1]
    return reverse

number = input('enter numbers: ')
print(reverse_num(number))
