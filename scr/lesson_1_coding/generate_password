import random


def generate_pwd(length, lower_case=None, upper_case=None, special=None, numbers=None):
    characters = list()
    # upper_case = True
    # special = False
    # numbers = False

    if lower_case:
        characters.extend('abcdefghijklmnopqrstuvwxyz')

    if upper_case:
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if special:
        characters.extend('!@#$%^&*()_')

    if numbers:
        characters.extend('1234567890')

    # length = 15
    pwd = ''

    for i in range(length):
        pwd += random.choice(characters)

    return pwd


# print(generate_pwd(20))
print(generate_pwd(20, numbers=True, lower_case=True))
print(generate_pwd(20, upper_case=True, numbers=True))
print(generate_pwd(20, True, True, True))
