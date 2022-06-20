# ******************************** 1 **********************************

from sys import argv


def func_salary(t, r, b):
    print(f"Зарплата сотрудника: {int(t) * int(r) + int(b)}")


try:
    name, time, rate, bonus = argv
    func_salary(time, rate, bonus)
except ValueError:
    print("Введите три целых числа через пробел")

# ******************************** 1 **********************************

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
max_pred = [my_list[k] for k in range(1, len(my_list)) if my_list[k] > my_list[k - 1]]
print(max_pred)

