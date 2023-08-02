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
