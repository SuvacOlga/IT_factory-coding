"""
Inheritance
"""
from src.part_1_coding.lessons.class_create_password import CreatePassword


class StrongPassword(CreatePassword):

    # def set_pwd(self):
    def generate_strong_pwd(self):
        if self._length < 10:
            return "Your password is too short"
        else:
            return self.generate_pwd(lower_case=True, upper_case=True, numbers=True, special=True)

    @staticmethod
    def generate_strong_pass_for_andrei():
        return 'jabgiuaebgubeg'


p1 = StrongPassword(9)
print(p1.generate_strong_pwd())
print(p1.generate_strong_pass_for_andrei())
