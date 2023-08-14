import random
import datetime


# class Person:
#     hobby = 'cooking'
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = age
#         self.__person_id = random.randint(1, 100)
#
#     def __show_id(self):
#         print(f'id: {self.__person_id}')
#
#     def get_info(self):
#         self.__show_id()
#         return f'Person name: {self.first_name} {self.last_name}\nAge: {self._age}\nHobby: {self.hobby}\n'
#
#     def say_hi(self, sms):
#         print(self.get_info())
#         return f'{sms}! A am {self.first_name}'
#
#     @classmethod
#     def set_hobby(cls):
#         cls.hobby = 'sleep'
#
#     @classmethod
#     def based_on_year(cls, first_name, last_name, year):
#         person_age = datetime.date.today().year - year
#         return cls(first_name, last_name, person_age)
#
#     @classmethod
#     def based_on_str(cls, str_info):
#         first_name, last_name, age = str_info.split(' ')
#         return cls(first_name, last_name, age)
#
#
# my_person = Person('Igor', 'Kalinichenko', 33)
# print(my_person.get_info())
# my_person.set_hobby()
# my_person1 = Person('Anna', 'Kalinichenko', 32)
# print(my_person1.get_info())
#
# my_person2 = Person.based_on_year('Maxim', 'Kalinichenko', 2019)
# print(my_person2.get_info())
# my_person3 = Person.based_on_str('Alex Primachenko 34')
# print(my_person3.get_info())
#
#
# class Developer(Person):
#     def __init__(self, first_name, last_name, age, jop_title):
#         super().__init__(first_name, last_name, age)
#         self.job_title = jop_title
#         self.__salary = 0
#
#     def set_basic_salary(self):
#         if self.__rung == 'junior':
#             self.__salary = 500
#         elif self.__rung == 'middle':
#             self.__salary = 1500
#         elif self.__rung == 'senior':
#             self.__salary = 3000
#
#     def percent_salary(self, percent):
#         self.__salary = self.__salary + ((self.__salary * percent) / 100)
#         return self.__salary
#
#     @classmethod
#     def set_rung(cls, rung_name):
#         cls.__rung = rung_name
#
#     def get_info(self):
#         return super().get_info() + f'Job title: {self.job_title}\nrung: {self.__rung}\nsalary: {self.__salary}'
#
#
# Developer.set_rung('senior')
# jun1 = Developer('Igor', 'Kalinichenko', 33, 'Python developer')
# jun1.set_basic_salary()
# jun1.percent_salary(50)
# print(jun1.get_info())

# class my_book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def show_book(self):
#         print('Title: ', self.title)
#         print('Author: ', self.author)
#         print('Pages: ', self.pages)
#
#
# class my_file:
#     def __init__(self, file_size, src):
#         self.file_size = file_size
#         self.src = src
#
#     def show_file_props(self):
#         print('File size: ', self.file_size)
#         print('src: ', self.src)
#
#
# class My_ebook(my_book, my_file):
#     def __init__(self, title, author, pages, file_size, src):
#         my_book.__init__(self, title, author, pages)
#         my_file.__init__(self, file_size, src)
#
#
# new_book = My_ebook('Python', 'Gvidov', 400, 33, 'd://books')
# new_book.show_book()
# new_book.show_file_props()


# class Doors:
#     def __init__(self, quantity_doors):
#         self.quantity_doors = quantity_doors
#
#     def open_doors(self, check):
#         if check == 'open':
#             print(f'Двери открыты')
#             return False
#         elif check == 'close':
#             print('Двери закрыты')
#             return True
#
#
# class Wheels:
#     def __init__(self, quantity_wheels):
#         self.quantity_wheels = quantity_wheels
#
#
# class Engine:
#     def __init__(self, power, volume):
#         self.power = power
#         self.volume = volume
#
#     def start_engine(self, examination):
#         if examination == True:
#             print('Двигатель заведён')
#         elif examination == False:
#             print('Двигатель не заведён - закройте двери')
#
#
# class Car(Doors, Wheels, Engine):
#     def __init__(self, quantity_doors, quantity_wheels, power, volume, name):
#         Doors.__init__(self, quantity_doors)
#         Wheels.__init__(self, quantity_wheels)
#         Engine.__init__(self, power, volume)
#         self.name = name
#     def get_info(self):
#         print(f'name: {self.name}\ndoors: {self.quantity_doors}\nwheels: {self.quantity_wheels}\nengine power: {self.power}, '
#               f'engine volume: {self.volume}')
#
# my_car = Car(4,4,200,1.4,"lanos")
# my_car.get_info()
# my_car.start_engine(my_car.open_doors("open"))

# class BankAccount:
#     balance = []
#     def __init__(self,acc_num, balance):
#         self.acc_num = acc_num
#         self.balance = balance
#         self.__class__.balance.append([acc_num, balance])
#     def get_info(self):
#         print(f'acc number: {self.acc_num}\nbalance: {self.balance}')
#     @staticmethod
#     def total_balance():
#         res = 0
#         for acc in BankAccount.balance:
#                 res +=acc[1]
#         return res
#
# my_bank_acc_1 = BankAccount(4749629344085584,-33000)
# my_bank_acc_2 = BankAccount(5363542060160836,10)
# my_bank_acc_3 = BankAccount(5375414128449757,0)
# print(BankAccount.total_balance())

# class Film:
#     films = []
#     counter = 0
#     def __init__(self, name, grade):
#         Film.counter+=1
#         self.name = name
#         self.grade = grade
#         self.__class__.films.append([name, grade])
#     def get_info(self):
#         print(f'Название фильма: {self.name}, оценка: {self.grade}')
#     @classmethod
#     def get_all_info(cls):
#         for film in Film.films:
#             print(f'Название фильма: {film[0]}, оценка: {film[1]}')
#     @classmethod
#     def avg_grade(cls):
#         grade = 0
#         for film in Film.films:
#             grade += film[1]
#         return f'Средняя оценка всех фильмов ({Film.counter} фильма/ов): {grade/Film.counter}'
#
# film_1 = Film('Итальянцы в россии', 7.5)
# film_2 = Film('Очень страшное кино', 5.6)
# print(Film.avg_grade())
# Film.get_all_info()
# film_1.get_info()

class Brain:
    def __init__(self, iq):
        self.iq = iq

    def get_iq(self):
        print(f'Iq = {self.iq}')


class Heart:
    def __init__(self, strokes):
        self.strokes = strokes

    def get_strokes(self):
        print(f'strokes = {self.strokes}')

    def set_strokes(self, stroke):
        self.strokes += stroke


class Legs:
    def running_or_walking(self, user_inp):
        if user_inp == 'running':
            print('Вы бежите')
            Heart.set_strokes(self, 50)
        else:
            print('Вы идёте')


class Human(Brain, Heart, Legs):
    def __init__(self, iq, strokes):
        Brain.__init__(self, iq)
        Heart.__init__(self, strokes)

    def get_info(self):
        print(f'iq {self.iq}, strokes {self.strokes}')


my_human = Human(110, 60)
my_human.get_info()
my_human.get_strokes()
my_human.running_or_walking('running')
my_human.get_strokes()
my_human.get_info()
