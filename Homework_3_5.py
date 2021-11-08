def sum_numbers(str, stop):
    list = str.split(' ')
    sum_nums_str = 0
    for i in list:
        if i == stop:
            break
        sum_nums_str += int(i)

    return sum_nums_str


stop_symbol = '+'
end = False
sum_str = 0

while not end:
    str_of_numb = input("Введите строку чисел: ")
    sum_str += sum_numbers(str_of_numb, stop_symbol)
    end = stop_symbol in str_of_numb
    print(f'Сумма чисел в строке = {sum_str}')