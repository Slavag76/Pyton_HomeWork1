# ******************************** 1 **********************************

from sys import argv


def func_salary(t, r, b):
    print(f"Зарплата сотрудника: {int(t) * int(r) + int(b)}")


try:
    name, time, rate, bonus = argv
    func_salary(time, rate, bonus)
except ValueError:
    print("Введите три целых числа через пробел")

