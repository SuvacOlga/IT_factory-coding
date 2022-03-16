class Salary:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 12) // 4.9545


class SalarySenior:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 24) // 4.9545


class Employee:
    def __init__(self, pay, bonus):
        self._bonus = bonus
        self._pay = pay

    def annual_salary(self):
        return f'Total salary is: {self._pay.get_total() + self._bonus}'


emp_middle = Employee(Salary(10000), 500)
emp_senior = Employee(SalarySenior(10000), 600)

print(emp_middle.annual_salary())
