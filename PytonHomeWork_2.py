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

for i in range (1, len(result_list_2), 2):
    result_list_2[i-1], result_list_2[i] = result_list_2[i], result_list_2[i-1]

print(f"Ваш список после замены: {result_list_2}")