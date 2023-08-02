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
