from abc import ABC, abstractmethod


# class Student:
#     __slots__ = ('name', 'age')
#
#
# class Trainee(Student):
#     __slots__ = ('enployer',)
#
#     def __init__(self):
#         self.enployer = 'director'
#
#
# stud = Student()
# trainee = Trainee()
# stud.age = 20
# stud.name = 'Igor'
# stud.marks = []
# print(stud.name)
# print(stud.age)
# print(trainee.__dict__)
# print(trainee.__slots__)
# print(stud.__slots__)
#
#
# class Abstarct_method(ABC):
#     @abstractmethod
#     def show_info(self):
#         pass


# obj = Abstarct_method()
# obj.show_info()
# class TestAbc(Abstarct_method):
#     pass
#
#
# obj = TestAbc()
# # obj.show_info()

# class AbstractBasePlayer:
#     def __init__(self, name, race):
#         self.__name = name
#         self.race = race
#     def get_name(self):
#         return self.__name
#     @abstractmethod
#     def show_info(self):
#         pass
#     @abstractmethod
#     def atack(self):
#         pass
# class Human(AbstractBasePlayer):
#     def __init__(self, name, race, age):
#         super().__init__(name, race)
#         self.age = age
#     def show_info(self):
#         print(f'Name: {self.get_name()}\nRace: {self.race}\nAge: {self.age}')
#     def atack(self):
#         print(f'I human. Attack with sword!')
# class Elf(AbstractBasePlayer):
#     def __init__(self, name, race, age):
#         super().__init__(name, race)
#         self.age = age
#     def show_info(self):
#         print(f'Name: {self.get_name()}\nRace: {self.race}\nAge: {self.age}')
#     def atack(self):
#         print(f'I elf. Attack with bow!')
#
# player_1 = Human('Artur', 'human', 18)
# player_1.show_info()
# player_2 = Elf('Joy', 'elf', 44)
# player_2.show_info()
#
# class Game:
#     def __init__(self):
#         self.players = []
#     def add_player(self, new_player):
#         if isinstance(new_player, (Human, Elf)):
#             self.players.append(new_player)
#         else:
#             print('Error type player')
#     def show_players(self):
#         for player in self.players:
#             player.show_info()
#
# my_game = Game()
# my_game.add_player(player_1)
# my_game.add_player(player_2)
# my_game.show_players()
# class AbstractBaseA(ABC):
#     __slots__ = ()
# class BaseA(AbstractBaseA):
#     __slots__ = ('a',)
#
# class AbstractBaseB(ABC):
#     __slots__ = ()
# class BaseB(AbstractBaseB):
#     __slots__ = ('b',)
#
#
# class Child(BaseA, BaseB):
#     pass
#
# obj = Child()
# total = 0
# #ваш код должен быть здесь
# count = 0
# while count <5:
#     age = int(input())
#     count +=1
#     if age<=3:
#         continue
#     else:
#         total +=100
# print (total)

# class AbstarctClass(ABC):
#     @abstractmethod
#     def sq(self):
#         pass
#
#
# class Square(AbstarctClass):
#     def __init__(self, a):
#         self.a = a
#
#     def sq(self):
#         square = self.a ** 2
#         return square
#
#
# square = Square(10)
# #
# print(square.sq())
#
#
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @abstractmethod
#     def show(self):
#         pass
#
#
# class Cat(Animal):
#     def __init__(self, name, age, voice, cat_type):
#         super().__init__(name, age)
#         self.voice = voice
#         self.cat_type = cat_type
#
#     def say_hi(self):
#         print(f'{self.voice}')
#
#     def show(self):
#         print(f'hello, my name {self.name}')
#
#     def type(self):
#         print(f'my type {self.cat_type}')
#
#     def show_info(self):
#         print(f'{self.name}\n{self.age}\n{self.cat_type}')
#
#
# my_cat = Cat('vasia', 12, 'miau', 'perc')
# my_cat.show()

# class Employer(ABC):
#     @abstractmethod
#     def print(self):
#         pass
# class President(Employer):
#     def print(self):
#         print(f'hello, i am resident')
# class Manager(Employer):
#     def print(self):
#         print(f'hello, i am manager')
# class Worker(Employer):
#     def print(self):
#         print(f'hello, i am worker')
#
# worer = Worker()
# manager = Manager()
# president = President()
# worer.print()
# manager.print()
# president.print()
#
#
# class FootballTeam:
#     __slots__ = ("name", "country", "head_coach")
#     def __init__(self, name, country, head_coach):
#         self.name = name
#         self.country = country
#         self.head_coach = head_coach
#
#     def show_info(self):
#         print(f'{self.name}\n{self.country}\n{self.head_coach}')
#
# team_1 = FootballTeam('Dinamo', 'Ukraine', 'Popov')
# # team_1.age = 12
# team_1.show_info()
# # print(team_1.age)

