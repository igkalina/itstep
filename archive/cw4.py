# try:
#     amount = int(input('enter the amount of items: '))
#     item_type = input('what the type of products?: ')
#     parts_num = int(input('enter number of parts?: '))
#     parts = amount / parts_num
#     print('add', amount, 'of type', item_type)
# except ValueError:
#     print('Amount should be an integer!')
# except ZeroDivisionError:
#     print('you cannot divide by zero!')
# except (TypeError, NameError):
#     print('')
# else:
#     print('end')
# finally:
#     print('program finished')
#
# try:
#     file = open('text.txt', 'w')
# finally:
#     file.close()


# try:
#     num = int(input('enter amount - '))
#     if num < 0:
#         raise Exception
#     print('you number - ', num)
# except Exception:
#     print('num error')

# try:
#     raise ValueError('igor')
# except ValueError as ex:
#     print('value error')
#     print('good', ex)
# except Exception as ex:
#     print('some error', ex)

# try:
#     side_square = int(input('Enter side of square - '))
#     i_horizontal = 0
#     i_vertical = 0
#     while True:
#         if i_horizontal <= side_square:
#             print('*', end='  ')
#             i_horizontal += 1
#             if i_horizontal == side_square:
#                 print('')
#                 i_horizontal = 0
#                 i_vertical += 1
#                 if i_vertical == side_square:
#                     break
# except ValueError:
#     print('input error')

# try:
#     side_square = int(input('Enter side of square - '))
#     i = 0
#     while i < abs(side_square):
#         print('*  ' * abs(side_square))
#         i += 1
# except ValueError:
#     print('input error')

# try:
#     side_square = int(input('Enter side of square - '))
#     i = 0
#     if side_square<1:
#         raise Exception
#     while i < side_square:
#         print('*  ' * side_square)
#         i += 1
# except ValueError:
#     print('input error')
# except Exception:
#     print('Number need bigger 1')
# try:
#     rectangle_h = int(input('enter the height of the rectangle - '))
#     rectangle_w = int(input('enter the width of the rectangle - '))
#     if rectangle_h < 1 or rectangle_w < 1:
#         raise Exception('number need bigger 1')
#     if rectangle_w < rectangle_h:
#         raise Exception('height > width')
#     if rectangle_w == rectangle_h:
#         raise Exception('height == width')
#     i = 0
#     while i < rectangle_h:
#         print('*  ' * rectangle_w)
#         i += 1
# except ValueError:
#     print('input error')
# except Exception as ex:
#     if rectangle_h < 1 or rectangle_w < 1:
#         print('error: ', ex)
#     if rectangle_w < rectangle_h:
#         print('error: ', ex)
#     if rectangle_w == rectangle_h:
#         print('error: ', ex)

"""Пользователь вводит с клавиатуры размер стороны квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата). Размер стороны равен введённому размеру.
******
*      *
*      *
*      *
*      *
******"""
try:
    side_square = int(input('Enter side of square - '))
    i = 0
    if side_square < 1:
        raise Exception('number need bigger 1')
    while i < side_square:
        if i == 0 or i == side_square - 1:
            print('*  ' * side_square)
        else:
            print('*', '   ' * (side_square - 2), '*')
        i += 1
except ValueError:
    print('input error')
except Exception as ex:
    print('Error -', ex)
