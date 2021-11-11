
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_rest = [elem for elem in my_list if my_list.count (elem) == 1]
print (list_rest)