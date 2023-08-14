# def city_country(city, country):
#     return f'{city}, {country}'
#
#
# print(city_country('Dnepr', 'Ukraine'))
# print(city_country('Kabul', 'Afghanistan'))
# print(city_country('Buenos Aires', 'Argentina'))
# print()
#
#
# def make_album(artist, album, track=None):
#     if track:
#         dict = {artist: {album: track}}
#     else:
#         dict = {artist: album}
#     return dict
#
#
# print(make_album('Tatu', '200 Po Vstrechnoy', 12))
# print(make_album('Tatu', 'Dangerous and Moving'))
# print(make_album('Tatu', '200 km/h in the Wrong Lane'))
# check = True
# while check:
#     result = make_album(input('Enter artist '), input('Enter his album '), input('Enter number of tracks (optional)
#     '))
#     check = input('Continue typing? y/n ')
#     if check == 'n':
#         check = False
#         print(result)
#     elif check == 'y':
#         print(result)
#         continue
#     else:
#         print('Enter y or n')

# def show_massages(msg):
#     for i in msg:
#         print(i)
# show_massages(msg)
# msg = ['hi','bb','hello']
# sent_massages = []
#
#
# def send_massages(msg, sent_massages):
#     while msg:
#         print_msg = msg.pop()
#         print(print_msg)
#         sent_massages.append(print_msg)

# send_massages(msg[:],sent_massages)
# print(msg)
# print(sent_massages[::-1])
# send_massages(msg,sent_massages)
# print(msg)
# print(sent_massages[::-1])

# def print_sandwich_components(*components):
#     print(components)
# print_sandwich_components('sausage', 'cheese', 'salad')
# print_sandwich_components('sausage', 'cheese')
# print_sandwich_components('sausage')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# print(build_profile('Igor', 'Kalinichenko', hobby='sleep', job='manager'))
#
#
# def build_car(title, type, **car):
#     car['title'] = title.title()
#     car['type'] = type
#     return car
#
#
# print(build_car('audi', 'outback', color='red'))
from printing_functions import print_models

unprinted_designs = ['tank', 'mobile']
complete_models = []
print_models(unprinted_designs, complete_models)
print('Напечатаные модели:')
for model in complete_models:
    print(f'\t{model}')