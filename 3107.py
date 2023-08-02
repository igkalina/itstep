class Book:
    def __init__(self, name, year, publisher, author, genre, price):
        self.__name = name
        self.__year = year
        self.__publisher = publisher
        self.__author = author
        self.__genre = genre
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def set_year(self, year):
        self.__year = year

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def get_publisher(self):
        return self.__publisher

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_price(self):
        return self.__price

    def get_info(self):
        print(
            f'Name: {self.get_name()}\nYear: {self.get_year()}\nPublisher: {self.get_publisher()}\nAuthor: {self.get_author()}'
            f'\nGenre: {self.get_genre()}\nPrice: {self.get_price()}\n')


my_book = Book('Мастер и маргарита', 1928, '-', 'Михаил Булгаков', 'роман', '200 грн')
my_book.get_info()
your_book = Book('Идиот', 1868, '-', 'Фёдор Михайлович Достоевский', 'роман', '300 грн')
your_book.get_info()


class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def set_numerator(self, numerator):
        self.__numerator = numerator

    def set_denominator(self, denominator):
        self.__denominator = denominator

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator
    def get_sum(self, sign):
        if sign == '+':
            res = self.get_numerator() + self.get_denominator()
        elif sign == '-':
            res = self.get_numerator() - self.get_denominator()
        elif sign == '*':
            res = self.get_numerator() * self.get_denominator()
        elif sign == '/':
            res = self.get_numerator() / self.get_denominator()
        else:
            res = f'{self.get_numerator()}.{self.get_denominator()}'
        print(res)
    def get_info(self):
        print(f'{self.get_numerator()}.{self.get_denominator()}\n')


my_numb = Fraction(4, 321)
my_numb.get_info()

class Address:
    def __init__(self, street, state, country, zipcode):
        self.__street = street.title()
        self.__state = state.title()
        self.__country = country.title()
        self.__zipcode = zipcode

    def get_street(self):
        return self.__street
    def get_state(self):
        return self.__state
    def get_country(self):
        return self.__country
    def get_zipcode(self):
        return self.__zipcode
    def is_valid_zipcode(self):
        if len(str(self.__zipcode)) == 5:
            return True
        else:
            return False
    def get_full_address(self):
        address = f'street: {self.get_street()}\nstate: {self.get_state()}\ncountry: {self.get_country()}' \
                  f'\nzipcode: {self.get_zipcode()}'
        return address

my_address = Address('Naberezhnaya Pobedyi','Dnepropetrovskaya', 'Ukraine', 49094)
print(my_address.get_full_address())
print(my_address.is_valid_zipcode())