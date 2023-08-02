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
