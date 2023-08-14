# class Cat:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_color(self):
#         return self.__color
#
#     def get_info(self):
#         print(f'name: {self.get_name()}\nage: {self.get_age()}\ncolor: {self.get_color()}')
#
#
# class Dog:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_color(self):
#         return self.__color
#
#     def get_info(self):
#         print(f'name: {self.get_name()}\nage: {self.get_age()}\ncolor: {self.get_color()}')
#
#
# class Cow:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_color(self):
#         return self.__color
#
#     def get_info(self):
#         print(f'name: {self.get_name()}\nage: {self.get_age()}\ncolor: {self.get_color()}')


# class Animal:
#     def __init__(self, name, age, color):
#         self.__name = name
#         self.__age = age
#         self.__color = color
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def get_color(self):
#         return self.__color
#
#     def get_info(self):
#         print(f'name: {self.get_name()}\nage: {self.get_age()}\ncolor: {self.get_color()}')
#
# class Cat(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age, color)
#         self.__count_life = 9
#     def get_info(self):
#         super().get_info()
#         print(self.__count_life)
# my_cat = Cat('sara', 6, 'red')
# my_cat.get_info()

# class Passport:
#     def __init__(self, number, name, date):
#         self.number = number
#         self.name = name
#         self.date = date
#     def get_info(self):
#         print(f'number = {self.number}, name = {self.name}, date = {self.date}')
#
# class ForeignPassport(Passport):
#     def __init__(self, number, name, date, visa):
#         super().__init__(number, name, date)
#         self.visa = visa
#     def get_info(self):
#         super().get_info()
#         print(f'visa = {self.visa}')
#
# my_passport = Passport(44423, 'Igor', '27/05/1990')
# my_passport.get_info()
#
# my_f_passport = ForeignPassport(44423, 'Igor', '27/05/1990', 'France')
# my_f_passport.get_info()

# class Dates:
#     def __init__(self, date):
#         self.date = date
#
#     def get_date(self):
#         return self.date
#
#     @staticmethod
#     def to_dash_date(date):
#         return date.replace('/', '-')
#
# my_date = Dates("31/07/2023")
# new_date = Dates.to_dash_date(my_date.date)
# print(new_date)

''''Задания'''


# К уже реализованному классу «Дробь» добавьте статический метод, который при вызове возвращает количество созданных объектов класса «Дробь».
# class Fraction:
#     count = 0
#
#     def __init__(self, numerator, denominator):
#         self.__numerator = numerator
#         self.__denominator = denominator
#         Fraction.count += 1
#
#     def set_numerator(self, numerator):
#         self.__numerator = numerator
#
#     def set_denominator(self, denominator):
#         self.__denominator = denominator
#
#     def get_numerator(self):
#         return self.__numerator
#
#     def get_denominator(self):
#         return self.__denominator
#
#     def get_sum(self, sign):
#         if sign == '+':
#             res = self.get_numerator() + self.get_denominator()
#         elif sign == '-':
#             res = self.get_numerator() - self.get_denominator()
#         elif sign == '*':
#             res = self.get_numerator() * self.get_denominator()
#         elif sign == '/':
#             res = self.get_numerator() / self.get_denominator()
#         else:
#             res = f'{self.get_numerator()}.{self.get_denominator()}'
#         print(res)
#
#     def get_info(self):
#         print(f'{self.get_numerator()}.{self.get_denominator()}\n')
#
#     @staticmethod
#     def count_class():
#         return f'Количсество объектов созданных на основе класса = {Fraction.count}'
#
#
# class Сelsius_fahrenheit:
#     count = 0
#
#     def __init__(self, c, f):
#         self.c = c
#         self.f = f
#         Сelsius_fahrenheit.count += 1
#     # def get_c(self):
#     #     return self.__c
#     # def get_f(self):
#     #     return self.__f
#
#     @staticmethod
#     def count_class():
#         return f'Количсество объектов созданных на основе класса = {Сelsius_fahrenheit.count}'
#     @staticmethod
#     def convert_c_to_f(c):
#         form = (c*9/5)+32
#         print(form)
#
#     @staticmethod
#     def convert_f_to_c(f):
#         form = (f-32)*5/9
#         print(form)
#
# my_class = Сelsius_fahrenheit(0,44)
# my_class_1 = Сelsius_fahrenheit(0,22)
# my_class.convert_c_to_f(44)
# my_class.convert_f_to_c(334)
#
# print(my_class.count_class())

# class Device:
#     def __init__(self, power, color, weight):
#         self.power = power
#         self.color = color
#         self.weight = weight
#
#     def get_info(self):
#         print(f'Мощьность: {self.power}\nЦвет: {self.color}\nВес: {self.weight} кг')
#
#
# class CoffeeMachine(Device):
#     def __init__(self, power, color, weight, max_cups):
#         super().__init__(power, color, weight)
#         self.__cups = max_cups
#     def get_cups(self):
#         return self.__cups
#
#     def clean_coffe_machine(self):
#         print('Произведена очистка фильтров')
#     def make_coffe(self, user_cups_coffee):
#         Coffee_machine_max = CoffeeMachine.get_cups(self)
#         if user_cups_coffee > Coffee_machine_max:
#             print('Данная кофемашина не поддерживает столько чашек кофе')
#         else:
#             cups = user_cups_coffee
#             i = 0
#             while i <= cups:
#                 i += 1
#                 print(f'\tСделана {i} чашка кофе')
#
#                 if 0 == i % 5:
#                     CoffeeMachine.clean_coffe_machine(self)
#
#
#     def get_info(self):
#         super().get_info()
#         print(f'Максимальное количество чашек кофе: {self.get_cups()}')
#
# class Blender(Device):
#     def __init__(self, power, color, weight, max_speed):
#         super().__init__(power, color, weight)
#         self.__speed = max_speed
#     def get_max_speed(self):
#         return self.__speed
#     def mixer(self, user_speed):
#         speed = Blender.get_max_speed(self)
#         if user_speed < speed:
#             print(f'Блендер включён на {user_speed} скорости')
#         else:
#             print(f'Не верно выбрана скорость, максимальная скорость у данного блендера {Blender.get_max_speed(self)}, выбрана скорость {user_speed}')
#
#
# my_coffe = CoffeeMachine(220, "red", 1, 19)
# my_coffe.get_info()
# my_coffe.make_coffe(16)
# my_mixer = Blender(500, 'white', 0.5, 3)
# my_mixer.mixer(2)
