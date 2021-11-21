class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht

    def get_weitgh(self, grav, thick):
        return self._lenght * self._widht * grav * thick / 1000

a = Road(5000, 20)
print(a.get_weitgh(25,5))