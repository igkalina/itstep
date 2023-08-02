# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран сумму трёх чисел или произведение трёх чисел.
num_1 = int(input('enter number: '))
num_2 = int(input('enter number: '))
num_3 = int(input('enter number: '))
q = input('Введите 1 если требуется посчитать сумму \nВведите 2 если требуется посчитать произведение: ')
if q < '1' or q > '2':
    print('Error input')
elif q == '1':
    print(num_1 + num_2 + num_3)
elif q == '2':
    print(num_1 * num_2 * num_3)
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
num_1 = int(input('enter number: '))
num_2 = int(input('enter number: '))
num_3 = int(input('enter number: '))
q = input(
    'Введите 1 если требуется вывести максимум из трёх чисел \nВведите 2 если требуется вывести минимум из трёх чисел \nВведите 3 если требуется вывести среднеарифметическое трёх чисел: ')
if q < '1' or q > '3':
    print('Error input')
elif q == '1':
    if num_2 < num_1 > num_3:
        print('Максимальное число: ', num_1)
    elif num_1 < num_2 > num_3:
        print('Максимальное число: ', num_2)
    elif num_2 < num_3 > num_1:
        print('Максимальное число: ', num_3)
elif q == '2':
    if num_2 > num_1 < num_3:
        print('Минимальное число: ', num_1)
    elif num_1 > num_2 < num_3:
        print('Минимальное число: ', num_2)
    elif num_2 > num_3 < num_1:
        print('Минимальное число: ', num_3)
elif q == '3':
    print('Cреднеарифметическое трёх чисел: ', int((num_2 + num_1 + num_3) / 3))
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды.
metr = int(input('enter meters: '))
q = input(
    'Enter 1 if you want to convert meters to miles \nEnter 2 if you want to convert meters to inches\nEnter 3 if you want to convert meters to yards: ')
if q < '1' or q > '3':
    print('Error input')
elif q == '1':
    print('Meters to miles: ', metr * 0.000621371)
elif q == '2':
    print('Meters to inches: ', metr * 39.3701)
elif q == '3':
    print('Meters to yards: ', metr * 1.09361)
# Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на экран названия дня недели. Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.
day = int(input('enter number day: '))
if day < 1 or day > 7:
    print('Error input')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')
# Пользователь вводит с клавиатуры номер месяца (1-12). Необходимо вывести на экран название месяца. Например, если 1, то на экране надпись январь, 2 — февраль и т.д.
day = int(input('enter number month: '))
if day < 1 or day > 12:
    print('Error input')
elif day == 1:
    print('Январь')
elif day == 2:
    print('Февраль')
elif day == 3:
    print('Март')
elif day == 4:
    print('Апрель')
elif day == 5:
    print('Май')
elif day == 6:
    print('Июнь')
elif day == 7:
    print('Июль')
elif day == 8:
    print('Август')
elif day == 9:
    print('Сентябрь')
elif day == 10:
    print('Октябрь')
elif day == 11:
    print('Ноябрь')
elif day == 12:
    print('Декабрь')
# Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести надпись «Number is positive», если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»
num = int(input('enter number: '))
if num > 0:
    print('Number is positive')
elif num < 0:
    print('Number is negative')
else:
    print('Number is equal to zero')
# Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их на экран в порядке возрастания.
num = int(input('enter number: '))
num_2 = int(input('enter number: '))
if num == num_2:
    print('Числа равны')
else:
    if num < num_2:
        print(num, num_2)
    else:
        print(num_2, num)
# Написать программу подсчета стоимости разговора для разных мобильных операторов. Пользователь вводит время разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран
time = float(input('Время звонка: '))
operator = int(input(
    'Нажмите 1 для звонка на оператор "Киевстар" - цена 1.56 минута \nНажмите 2 для звонка на оператор "МТС" - цена 1.43 мниута: '))
if operator == 1:
    print('Стоимость звонка: ', time * 1.56)
elif operator == 2:
    print('Стоимость звонка: ', time * 1.43)
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше 1000 — 8%.
# Пользователь вводит с клавиатуры уровень продаж для трех менеджеров. Определить их зарплату,определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.
maneger_1 = int(input('Продажи первого менеджера: '))
maneger_2 = int(input('Продажи второго менеджера: '))
maneger_3 = int(input('Продажи третьего менеджера: '))
salary = 200
bestMan_1 = 'Нет'
bestMan_2 = 'Нет'
bestMan_3 = 'Нет'
if maneger_1 < 500:
    bonus_1 = maneger_1 * 0.03
    salary_1 = maneger_1 + (maneger_1 * 0.03) + salary
elif 500 < maneger_1 < 1000:
    bonus_1 = maneger_1 * 0.05
    salary_1 = maneger_1 + (maneger_1 * 0.03) + salary
else:
    bonus_1 = maneger_1 * 0.08
    salary_1 = maneger_1 + (maneger_1 * 0.08) + salary
if maneger_2 < 500:
    bonus_2 = maneger_2 * 0.03
    salary_2 = maneger_2 + (maneger_2 * 0.03) + salary
elif 500 < maneger_2 < 1000:
    bonus_2 = maneger_2 * 0.05
    salary_2 = maneger_2 + (maneger_2 * 0.05) + salary
else:
    bonus_2 = maneger_2 * 0.08
    salary_2 = maneger_2 + (maneger_2 * 0.08) + salary
if maneger_3 < 500:
    bonus_3 = maneger_3 * 0.03
    salary_3 = maneger_3 + (maneger_3 * 0.03) + salary
elif 500 < maneger_3 < 1000:
    bonus_3 = maneger_3 * 0.05
    salary_3 = maneger_3 + (maneger_3 * 0.05) + salary
else:
    bonus_3 = maneger_3 * 0.08
    salary_3 = maneger_3 + (maneger_3 * 0.08) + salary
bestBonus_1 = 0
bestBonus_2 = 0
bestBonus_3 = 0
if salary_1 <= salary_2 >= salary_3:
    bestMan_2 = 'Да - надбавка 200.'
    bestBonus_1 += 200
if salary_2 <= salary_1 >= salary_3:
    bestMan_1 = 'Да - надбавка 200.'
    bestBonus_2 += 200
if salary_1 <= salary_3 >= salary_2:
    bestMan_3 = 'Да - надбавка 200.'
    bestBonus_3 += 200
print('\nЗарплата 1го менеджера -', salary_1 + bestBonus_1, '\nИз которых: \n', bonus_1,
      '- бонус к продажам\n', maneger_1, '- продажи\n',
      salary, '- ставка\n', 'Лучший менеджер:', bestMan_1)
print('\nЗарплата 2го менеджера -', salary_2 + bestBonus_2, '\nИз которых: \n', bonus_2,
      '- бонус к продажам\n', maneger_2, '- продажи\n',
      salary, '- ставка\n', 'Лучший менеджер:', bestMan_2)
print('\nЗарплата 3го менеджера -', salary_3 + bestBonus_3, '\nИз которых: \n', bonus_3,
      '- бонус к продажам\n', maneger_3, '- продажи\n',
      salary, '- ставка\n', 'Лучший менеджер:', bestMan_3)
