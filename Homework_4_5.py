from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
def mul_nums (x,y):
    mul = x * y
    return mul
print(reduce(mul_nums, my_list))