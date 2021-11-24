from random import randint

class Matrix:
    def __init__(self,num):
        self.num = num

    def __str__(self):
        x = ""
        for i in range(len(self.num)):
            for k in range(len(self.num[i])):
                x += f'{self.num[i][k]:02} '
            x += "\n"
        return x

    def __add__(self, other):
        num = [
            [self.num[i][k] + other.num[i][k] for k in range(len(self.num[i]))]
                for i in range (len(self.num))]
        return Matrix(num)

a = Matrix ([[randint(0,10) for _ in range(5)] for _ in range(5)])
b = Matrix ([[randint(0,10) for _ in range(5)] for _ in range(5)])
print (a+b)