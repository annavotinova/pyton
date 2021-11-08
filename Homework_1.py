#Задание №1

# number_1 = input('Enter number_1: ')
# number_2 = input('Enter number_2: ')
# print(number_1 + ' и ' + number_2)
#
# sum_nums = int(number_1) + int(number_2)
# multi_nums = int(number_1) * int(number_2)
# compare_nums = int(number_2) > int(number_1) and int(number_2) > 100
#
# print(sum_nums)
# print(multi_nums)
# print(compare_nums)
#
# str_1 = 'Anna'
# str_2 = ' Votinova'
#
# sum_str = str_1 + str_2
# multi_str = str_2 * 3
# print(sum_str)
# print(multi_str)

#Задание №2
# time = int(input('Введите время в секундах: '))
#
# hour = time // 3600
# minute = (time % 3600) // 60
# seconds = (time % 3600) % 60
#
# time_h_m_s = f' Время в формате часы, минуты, секунды: {hour}:{minute}:{seconds}'
#
# print(time_h_m_s)

#Задание №3
# number = input('Введите число: ')
# number_2 = number + number
# number_3 = number + number + number
# sum_number = int(number) + int(number_2) + int(number_3)
# print(sum_number)

#Задание №4
# number = int(input('Введите число: '))
# max_number = 0
# while number % 10 != 0:
#       if number % 10 > max_number:
#           max_number = number % 10
#       number //= 10
#
# print(f'Максимальная цифра числа: {max_number}')

#Задание №5

# proceeds = int(input('Введите данные по выручке: '))
# consump = int(input('Введите данные по издержкам: '))
# profit = proceeds - consump
# effect = profit / proceeds
# if   consump > proceeds:
#      print('Компания работает в убыток')
# else:
#      print('Компания приносит прибыль')
#      print(f'Прибыль состовляет: {profit}')
#      print(f'Рентабельность состовляет: {effect}')
#      quantity_woker = int(input('Введите количество сотрудников: '))
#      prof_one_woker = profit // quantity_woker
#      print(f'Прибыль на одного сотрудника состовляет: {prof_one_woker}')

#Задание №6

first_day_km = int(input('Введите количество км в первый день: '))
end_day_km = int(input('Введите количество км необходимое достичь: '))
quantity_day = 1
while first_day_km < end_day_km:
     first_day_km = first_day_km + first_day_km * 0.1
     quantity_day += 1
print(f'День: {quantity_day}')





