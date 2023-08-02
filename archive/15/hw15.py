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
