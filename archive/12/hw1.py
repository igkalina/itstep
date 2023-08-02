sec = int(input('Количество секунд '))
h = sec / 60 // 60
m = (sec - (h * 60 * 60)) // 60
s = sec - (h * 60 * 60 + m * 60)
print(int(h), 'часов', int(m), 'минут', int(s), 'секунд')