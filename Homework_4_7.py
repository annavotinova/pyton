def factorial (n):
    x = 1
    for i in range(1, n+1):
        x *= i
        yield x

number = 7
for elem in factorial(number):
    print (f'{elem}')