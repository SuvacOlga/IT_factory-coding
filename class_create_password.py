import random


class CreatePassword:

    """
    """

    def __init__(self, length):
        self._length = length

    def generate_pwd(self, lower_case=None, upper_case=None, special=None, numbers=None):
        """
        :param lower_case:
        :param upper_case:
        :param special:
        :param numbers:
        :return:
        """
        characters = list()

        if lower_case:
            characters.extend('abcdefghijklmnopqrstuvwxyz')

        if upper_case:
            characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        if special:
            characters.extend('!@#$%^&*()_')

        if numbers:
            characters.extend('1234567890')

        pwd = ''

        for i in range(self._length):
            pwd += random.choice(characters)

        return pwd

    def generate_weak_pwd(self):
        return self.generate_pwd(lower_case=True)

    def generate_strong_pwd(self):
        return self.generate_pwd(lower_case=True, upper_case=True, numbers=True, special=True)


p = CreatePassword(9)
# print(p.generate_pwd(numbers=True, lower_case=True))
# print(p.generate_weak_pwd())
# print(p.generate_strong_pwd())
