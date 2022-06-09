# ********************************** 1 **************************************

def my_div(var1, var2):
    try:
        result = round(var1 / var2, 2)
        return result
    except ZeroDivisionError:
        result = "Деление на ноль невозможно"
        return result


result = my_div(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
print(f"Результат деления: {result}")


# ********************************** 2 **************************************

def person_data(**kwargs):
    return kwargs


print(person_data(second_name="Grozny", first_name="Viatcheslav", phone=7916555333, year_birth=1976, city="Moscow",
                  email="myemal@mail.ru"))


# ********************************** 3 **************************************

def func_max(var1, var2, var3):
    sum1 = var1 + var2
    sum2 = var1 + var3
    sum3 = var2 + var3
    iter_obj = [sum1, sum2, sum3]
    return max(iter_obj)


result_func = func_max(-12, 9, 0)
print(f"Максимальное значение суммы: {result_func}")


# ********************************** 4 **************************************

def my_func(var1, var2):
    result = round((1 / var1 ** abs(var2)), 3)
    return result


result = my_func(int(input("Введите первое положительное число: ")), int(input("Введите второе отрицательное число: ")))
print(f"Результат возведения в степень: {result}")
