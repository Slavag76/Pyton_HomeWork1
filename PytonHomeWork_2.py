# ************************************ 1 ************************************

result_list = [22, 'Viatcheslav', 87.0, None, True, [1, 2, 3, 4], (1, 2, 3, 4), {1, 2, 3, 4},
               {"key1": 100, "key2": False}]
for i in result_list:
    print(type(i))

# ************************************ 2 ************************************

print("Заполните список 10 элементами")
result_list_2 = []
num = 1
while num <= 10:
    print(f"введите {num} элемент: ")
    result_list_2.append(input())
    num += 1
print(f"Ваш список: {result_list_2}")

for i in range(1, len(result_list_2), 2):
    result_list_2[i - 1], result_list_2[i] = result_list_2[i], result_list_2[i - 1]

print(f"Ваш список после замены: {result_list_2}")

# ************************************ 3 ************************************

dict12 = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь",
          10: "октябрь", 11: "ноябрь", 12: "декабрь"}

number_month = int(input("Введите номер месяца от 1 до 12: "))

if number_month in [12, 1, 2]:
    period = "зима"
elif number_month in [3, 4, 5]:
    period = "весна"
elif number_month in [6, 7, 8]:
    period = "лето"
elif number_month in [9, 10, 11]:
    period = "осень"
else: print("Вы ввели некорректное значение")

print(f"веденный Вами месяц:  {dict12.get(number_month)} относится к {period}")
