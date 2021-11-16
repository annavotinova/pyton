import random

with open('sum_nums.txt', 'w') as file:
    for _ in range(10):
        file.write(f'{random.randint(0, 5)} ')

with open('sum_nums.txt') as file:
    str = file.read().split()
    sum = 0
    for i in str:
        sum += int(i)
print(sum)