miles_1 = input('Введите целую часть числа: ')
miles_2 = input('Введите дробную часть числа: ')
miles_res = float(miles_1 + '.' + miles_2)
km_res = miles_res * 1.61
print(f'{miles_res} miles = {km_res:.2f} kilometers')
#Ввод:
#Введите целую часть числа: 15
#Введите дробную часть числа: 7
#Вывод:
#15.7 miles = 25.28 kilometers