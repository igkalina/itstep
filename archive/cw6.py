# nums = [12345, 14532, 17523, 23421, 21345, 32124, 36214, 34214, 31245, 30123, 29313, 20235]
# sum = 0
# max = 0
# min = nums[0]
# for i in nums:
#     sum += i
#     if i>max:
#         max = i
#     if i<min:
#         min = i
# print(sum / 12)
# print(f'min {min}, max {max}')
# print(nums)
# print(nums[-3])
# myList = ['igor', 3, 2.3, True, [1, 2, 3]]
# print(myList)
# for i in myList:
#     print(i, end = '|')
# for i in range(10):
#     print(i)
# o = [1,2,3,4,5]
# numbers = [i for i in range(10)]
# numbers.insert(0, 1)
# numbers.pop()
# print(numbers)
import random

numbs = []
sum_N = 0
c = 0
sum_C = 0
sum_nC = 0
b=0
a=0
for i in range(10):
    numbs.append(random.randint(-100, 100))
for i in numbs:
    if i < 0:
        sum_N += i
    if i % 2 == 0:
        sum_C += i
    elif i % 2 != 0:
        sum_nC += i
    if i>0:
        c+=i
a=min(numbs)*max(numbs)
for i in numbs[::3]:
    b+=i
print(numbs)
print(f'Сумма всех отрицательных: {sum_N}\nКратные 2: {sum_C}\nНе кратные 2: {sum_nC}\nСумма чиссел каждого 3го индексаа: {b}'
      f'\nПроизведение элементов между минимальным и максимальным элементом {a}\n'
      f'Сумму элементов, находящихся между первым и последним положительными элементами: {c}')
