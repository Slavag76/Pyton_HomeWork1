# ******************************** 1 **********************************

from sys import argv


def func_salary(t, r, b):
    print(f"Зарплата сотрудника: {int(t) * int(r) + int(b)}")


try:
    name, time, rate, bonus = argv
    func_salary(time, rate, bonus)
except ValueError:
    print("Введите три целых числа через пробел")

# ******************************** 2 **********************************

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
max_pred = [my_list[k] for k in range(1, len(my_list)) if my_list[k] > my_list[k - 1]]
print(max_pred)

# ******************************** 3 **********************************

list_20_240 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(list_20_240)

# ******************************** 4 **********************************

from random import randint

base_list = [randint(0, 30) for _ in range(50)]
print(base_list)
result_list = []

# result_list = [result_list.append(item) for item in base_list if item not in result_list] - выдает None

for item in base_list:
    if item not in result_list:
        result_list.append(item)

print(result_list)

# ******************************** 5 **********************************

from functools import reduce


def func_resultlist(el1, el2):
    return el1 * el2


base_list2 = [el for el in range(100, 1001, 2)]
print(f"Произведение элементов: {reduce(func_resultlist, base_list2)}")

# ******************************** 6 **********************************

from itertools import count, cycle

my_count = count(10)
my_cycle = cycle("XOL")

for _ in range(8):
    print(next(my_count), next(my_cycle))
