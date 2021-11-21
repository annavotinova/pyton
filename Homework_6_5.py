class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Начать отрисовку")

class Pen(Stationery):
    def draw(self):
        print(f"Начать отрисовку ручка {self.title}")
class Pencil(Stationery):
    def draw(self):
        print(f"Начать отрисовку карандашом {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Начать отрисовку маркером {self.title}")

pen = Pen("X")
pencil = Pencil("Y")
handle = Handle("Z")

for i in (pen, pencil, handle):
    i.draw()
