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


