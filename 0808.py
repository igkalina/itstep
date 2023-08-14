# class Film:
#     def __init__(self, title, director, genre):
#         self.title = title
#         self.director = director
#         self.genre = genre
#     def show_info(self):
#         print(f'{self.title}\n{self.director}\n{self.genre}')
# film_1 = Film('Matrix', 'The Wachowskis', 'Science fiction, Action film')
# film_2 = Film('The Matrix Revisited', 'The Wachowskis', 'Documentary')
# film_1.show_info()
# print()
# film_2.show_info()
# print()
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def show_info(self):
#         print(f'{self.title}\n{self.author}\n{self.pages}')
#
# book_1 = Book('The Witcher', 'Andrzej Sapkowski', 235)
# book_1.show_info()
# for item in (film_1, book_1):
#     item.show_info()
#     print()

''''Задания'''
# Создайте класс Дробь. Используя перегрузку операторов реализуйте
# для него арифметические операции для работы с дробями (операции +, -, *, /).
# Также операторы составного присваивания и методы преобразования (int,float,str)
import math


class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        Fraction.count += 1

    def set_numerator(self, numerator):
        self.__numerator = numerator

    def set_denominator(self, denominator):
        self.__denominator = denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def get_info(self):
        print(f'{self.get_numerator()}.{self.get_denominator()}')

    def __str__(self):
        return f'{self.__numerator}.{self.__denominator}'

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.__numerator + other.__numerator, self.__denominator + other.__denominator)
        else:
            try:
                if float(other):
                    num = float(f'{self.__numerator}.{self.__denominator}') + other
                    return float("{0:.2f}".format(num))
            except ValueError:
                return f'Не верное значение'

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.__numerator - other.__numerator, self.__denominator - other.__denominator)
        else:
            try:
                if float(other):
                    num = float(f'{self.__numerator}.{self.__denominator}')
                    return "{0:.2f}".format(num - other)
            except ValueError:
                return f'Не верное значение'

    def __mul__(self, other):
        if isinstance(other, Fraction):
            num = float(f'{self.__numerator}.{self.__denominator}') * float(
                f'{other.__numerator}.{other.__denominator}')
            return float("{0:.2f}".format(num))
        else:
            try:
                if float(other):
                    num = float(f'{self.__numerator}.{self.__denominator}') * other
                    return float("{0:.2f}".format(num))
            except ValueError:
                return f'Не верное значение'

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            num = float(f'{self.__numerator}.{self.__denominator}') / float(
                f'{other.__numerator}.{other.__denominator}')
            return "{0:.2f}".format(num)
        else:
            try:
                if float(other):
                    num = float(f'{self.__numerator}.{self.__denominator}') / other
                    return float("{0:.2f}".format(num))
            except ValueError:
                return f'Не верное значение'

    def __iadd__(self, other):
        try:
            if isinstance(other, Fraction):
                self.__numerator += other.__numerator
                self.__denominator += other.__denominator
                return self
            elif float(other):
                num = float(f'{self.__numerator}.{self.__denominator}') + other
                return float("{0:.2f}".format(num))
        except ValueError:
            return f'Не верное значение'

    @staticmethod
    def count_class():
        return f'Количсество объектов созданных на основе класса = {Fraction.count}'


# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
#  Проверка на равенство типов самолетов (операция ==);
#  Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
#  Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).

class Airplane:
    def __init__(self, type, max_pas, pas):
        self.type = type
        self.max_pas = max_pas
        self.pas = pas

    def __str__(self):
        return f'Type: {self.type}\nMaximum pas: {self.max_pas}\nPas: {self.pas}'

    def __eq__(self, other):
        if self.type == other.type:
            return True
        else:
            return False

    def __le__(self, other):
        if self.max_pas <= other.max_pas:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.max_pas >= other.max_pas:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.max_pas < other.max_pas:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.max_pas > other.max_pas:
            return True
        else:
            return False

    def __add__(self, other):
        if self.pas + other <= self.max_pas:
            self.pas += other
            print(f'{other} пассажиров зашли в самолёт. Пассажиров в самолёте {self.pas}.')
        else:
            return f'Привышено максимальное количество пассажиров ({self.max_pas})'

    def __sub__(self, other):
        if self.pas - other > 0:
            temp = self.pas
            self.pas -= other
            print(f'Высажено {other} пассажиров из {temp}. Пассажиров в самолёте {self.pas}.')
        else:
            print('В самолёте нет столько пассажиров.')

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __isub__(self, other):
        self.__sub__(other)
        return self

    def get_info(self):
        return f'Type: {self.type}\nMaximum pas: {self.max_pas}\nPas: {self.pas}'


# my_air_1 = Airplane('Boeing 747-400', 624, 434)
# my_air_2 = Airplane('Boeing 747-400', 724, 434)
# print(my_air_1 == my_air_2)
# my_air_1 + 50
# my_air_1 += 1
# my_air_1 -= 32
# my_air_1 - 50
# print(my_air_1 <= my_air_2)
# print(my_air_1.get_info())

# Создать класс Flat (квартира). Реализовать перегруженные операторы:
#  Проверка на равенство площадей квартир (операция ==);
#  Проверка на неравенство площадей квартир (операция !=);
#  Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, sq, price):
        self.sq = sq
        self.price = price

    def __eq__(self, other):
        if self.sq == other.sq:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.sq != other.sq:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False


my_flat_1 = Flat(33, 23300)
my_flat_2 = Flat(33, 30000)
print(my_flat_1 > my_flat_2)
print(my_flat_1 == my_flat_2)
