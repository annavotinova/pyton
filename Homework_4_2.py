my_list = [100, 12, 23, 250, 4, 69, 12, 93]
list_rest = [my_list [elem] for elem in range (1, len(my_list)) if my_list[elem] > my_list[elem-1]]
print (list_rest)