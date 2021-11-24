from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def mater(self):
        pass


class Coat(Clothes):
    def __init__(self, r):
        self.r = r
    @property
    def mater(self):
        return self.r / 6.5 * 0.5
    def sum_mater(self, list_coat):
        a = 0
        for coat in list_coat:
            a+= coat.mater
        return a

class Suit(Clothes):
    def __init__(self, s):
        self.s = s

    @property
    def mater(self):
        return 2*self.s + 0.3

coat = Coat(50)
coat_2 = Coat(52)
costume = Suit (1.66)
list_coat = [coat_2, coat]
print(coat.mater)
print(costume.mater)
print(coat.sum_mater(list_coat))

