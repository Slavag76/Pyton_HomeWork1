user_name = input("Введите Ваше имя: ")
user_age = int(input("Сколько Вам лет? "))
print(f"Привет,  {user_name}, ты уже взрослый, аж целых {user_age} лет, сейчас я тебе буду задавать вопросы ")

# ************************************************************

time_second = int(input("Введите количество секунд (от 0 до 86400): "))
time_hour = time_second // 3600
time_minute = (time_second - (3600 * time_hour)) // 60
second = time_second - (3600 * time_hour) - (time_minute * 60)
print(f"Ваше время будет: {time_hour}:{time_minute}:{second}")

# ************************************************************

enter_digit = input("Введите число от 1 до 9: ")
bb = enter_digit + enter_digit
bbb = enter_digit + enter_digit + enter_digit
total_summ = int(enter_digit) + int(bb) + int(bbb)
print(f"Сумма чисел {enter_digit} + {bb} + {bbb} равна: {total_summ}")

# ************************************************************

enter_big = int(input("Введите целое натуральное число (8 разрядов):  "))
num = 0
max = 0
while num <= 8:
    digit_10 = enter_big % 10
    enter_big = enter_big // 10
    if digit_10 >= max:
        max = digit_10
    num += 1
print(f"Максимальная цифра в этом числе:  {max}")

# ************************************************************

value = int(input("Введите значение выручки: "))
expenses = int(input("Введите значение расходной части: "))
amount_personal = int(input("Введите количество сотрудников: "))
profitability = 100 * (value - expenses) / value
personal_profitability = profitability / amount_personal

if profitability >= 0:
    print(f"Рентабельность фирмы = {profitability}%, в расчете на одного сотрудника = {personal_profitability} ")
else:
    print(f"Фирма отработала в убыток {profitability} в расчете на одного сотрудника = {personal_profitability}")
