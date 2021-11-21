class Car:
    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = police

    def go(self):
        print("едет")
    def stop(self):
        print('стоит')
    def turn(self,direct):
        print(f'повернулась на {direct}')
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Скорость превышена')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Скорость превышена')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar (70, 'white', 'Town')
sport = SportCar (150, 'yellow', "Sport")
work = WorkCar (50, "black", "Work")
police = PoliceCar (90, "blue", "Police")

town.show_speed()
work.show_speed()
work.speed = 20
work.show_speed()

police.turn("Right")
