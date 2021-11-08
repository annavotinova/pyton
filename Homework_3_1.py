#Задание №1

def divis ():
    num_1 = int(input('Введите число № 1: '))
    num_2 = int(input('Введите число № 2: '))
    if num_2 == 0:
       erorr_div = "Делить на ноль нельзя"
       return erorr_div
    else:
       div_num = num_1 / num_2
       return div_num
divis_numbers = divis ()
print(divis_numbers)


