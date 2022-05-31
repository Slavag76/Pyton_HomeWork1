user_name = input("Введите Ваше имя: ")
user_age = int(input("Сколько Вам лет? "))
print(f"Привет,  {user_name}, ты уже взрослый, аж целых {user_age} лет, сейчас я тебе буду задавать вопросы ")

time_second = int(input("Введите количество секунд (от 0 до 86400): "))
time_hour = time_second // 3600
time_minute = (time_second - (3600 * time_hour)) // 60
second = time_second - (3600 * time_hour) - (time_minute * 60)
print(f"Ваше время будет: {time_hour}:{time_minute}:{second}")

enter_digit = input("Введите целое натуральное число: ")
bb = enter_digit + enter_digit
bbb = enter_digit + enter_digit + enter_digit
total_summ = int(enter_digit) + int(bb) + int(bbb)
print(f"Сумма чисел {enter_digit} + {bb} + {bbb} равна: {total_summ}")
